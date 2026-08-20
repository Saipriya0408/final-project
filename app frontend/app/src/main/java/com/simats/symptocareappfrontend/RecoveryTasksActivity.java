package com.simats.symptocareappfrontend;

import android.content.Context;
import android.content.SharedPreferences;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ProgressBar;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.simats.symptocareappfrontend.adapters.RecoveryTaskAdapter;
import com.simats.symptocareappfrontend.models.RecoveryTask;

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.Locale;

public class RecoveryTasksActivity extends AppCompatActivity implements RecoveryTaskAdapter.OnTaskStatusChangedListener {

    private RecyclerView rvTasks;
    private TextView tvNoTasks;
    private TextView tvProgressLabel;
    private ProgressBar progressTasks;
    private Button btnAddTask;

    private DatabaseHelper dbHelper;
    private long activeUserId;
    private RecoveryTaskAdapter adapter;
    private List<RecoveryTask> taskList = new ArrayList<>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_recovery_tasks);

        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);
        if (getSupportActionBar() != null) {
            getSupportActionBar().setDisplayHomeAsUpEnabled(true);
            getSupportActionBar().setDisplayShowHomeEnabled(true);
        }
        toolbar.setNavigationOnClickListener(v -> finish());

        rvTasks = findViewById(R.id.rvTasks);
        tvNoTasks = findViewById(R.id.tvNoTasks);
        tvProgressLabel = findViewById(R.id.tvProgressLabel);
        progressTasks = findViewById(R.id.progressTasks);
        btnAddTask = findViewById(R.id.btnAddTask);

        dbHelper = new DatabaseHelper(this);
        SharedPreferences prefs = getSharedPreferences("SymptoCarePrefs", Context.MODE_PRIVATE);
        activeUserId = prefs.getLong("active_user_id", -1);

        rvTasks.setLayoutManager(new LinearLayoutManager(this));
        adapter = new RecoveryTaskAdapter(taskList, dbHelper, this);
        rvTasks.setAdapter(adapter);

        btnAddTask.setOnClickListener(v -> {
            AddTaskBottomSheet bottomSheet = new AddTaskBottomSheet();
            bottomSheet.show(getSupportFragmentManager(), "AddTaskBottomSheet");
        });

        checkAndRequestNotificationPermission();
        loadTasks();
    }

    public void loadTasks() {
        if (activeUserId == -1) return;
        taskList.clear();
        String today = new SimpleDateFormat("yyyy-MM-dd", Locale.getDefault()).format(new Date());

        SQLiteDatabase db = dbHelper.getReadableDatabase();
        Cursor c = db.rawQuery("SELECT * FROM " + DatabaseHelper.TABLE_RECOVERY_TASKS + " WHERE " + DatabaseHelper.COL_RT_USER_ID + "=? AND " + DatabaseHelper.COL_RT_CREATED_DATE + "=?", new String[]{String.valueOf(activeUserId), today});

        if (c != null && c.moveToFirst()) {
            do {
                RecoveryTask task = new RecoveryTask();
                task.id = c.getInt(c.getColumnIndexOrThrow(DatabaseHelper.COL_RT_ID));
                task.userId = c.getLong(c.getColumnIndexOrThrow(DatabaseHelper.COL_RT_USER_ID));
                task.taskName = c.getString(c.getColumnIndexOrThrow(DatabaseHelper.COL_RT_TASK_NAME));
                task.taskType = c.getString(c.getColumnIndexOrThrow(DatabaseHelper.COL_RT_TASK_TYPE));
                task.reminderTimes = c.getString(c.getColumnIndexOrThrow(DatabaseHelper.COL_RT_REMINDER_TIMES));
                task.durationDays = c.getInt(c.getColumnIndexOrThrow(DatabaseHelper.COL_RT_DURATION_DAYS));
                task.createdDate = c.getString(c.getColumnIndexOrThrow(DatabaseHelper.COL_RT_CREATED_DATE));
                task.isCompleted = c.getInt(c.getColumnIndexOrThrow(DatabaseHelper.COL_RT_IS_COMPLETED)) == 1;

                taskList.add(task);
            } while (c.moveToNext());
            c.close();
        }

        adapter.updateTasks(taskList);

        if (taskList.isEmpty()) {
            rvTasks.setVisibility(View.GONE);
            tvNoTasks.setVisibility(View.VISIBLE);
        } else {
            rvTasks.setVisibility(View.VISIBLE);
            tvNoTasks.setVisibility(View.GONE);
        }

        updateProgress();
    }

    private void updateProgress() {
        int total = taskList.size();
        int completed = 0;
        for (RecoveryTask t : taskList) {
            if (t.isCompleted) completed++;
        }

        if (total > 0) {
            int percentage = (int) (((float) completed / total) * 100);
            progressTasks.setProgress(percentage);
        } else {
            progressTasks.setProgress(0);
        }
        
        tvProgressLabel.setText(completed + " of " + total + " done");
    }

    @Override
    public void onStatusChanged() {
        updateProgress();
    }

    private void checkAndRequestNotificationPermission() {
        if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.TIRAMISU) {
            if (androidx.core.content.ContextCompat.checkSelfPermission(this, android.Manifest.permission.POST_NOTIFICATIONS) != android.content.pm.PackageManager.PERMISSION_GRANTED) {
                androidx.core.app.ActivityCompat.requestPermissions(
                    this,
                    new String[]{android.Manifest.permission.POST_NOTIFICATIONS},
                    101
                );
            }
        }
    }

    @Override
    public void onRequestPermissionsResult(int requestCode, String[] permissions, int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
        if (requestCode == 101) {
            if (grantResults.length > 0 && grantResults[0] == android.content.pm.PackageManager.PERMISSION_GRANTED) {
                android.widget.Toast.makeText(this, "Notification permission granted. You will receive recovery reminders.", android.widget.Toast.LENGTH_SHORT).show();
            } else {
                android.widget.Toast.makeText(this, "Notification permission denied. Reminders will not show in the notification panel.", android.widget.Toast.LENGTH_LONG).show();
            }
        }
    }

    private final android.content.BroadcastReceiver refreshReceiver = new android.content.BroadcastReceiver() {
        @Override
        public void onReceive(Context context, android.content.Intent intent) {
            loadTasks();
        }
    };

    @Override
    protected void onStart() {
        super.onStart();
        if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.TIRAMISU) {
            registerReceiver(refreshReceiver, new android.content.IntentFilter("com.simats.symptocare.REFRESH_TASKS"), Context.RECEIVER_NOT_EXPORTED);
        } else {
            registerReceiver(refreshReceiver, new android.content.IntentFilter("com.simats.symptocare.REFRESH_TASKS"));
        }
    }

    @Override
    protected void onStop() {
        super.onStop();
        unregisterReceiver(refreshReceiver);
    }
}
