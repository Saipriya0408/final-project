package com.simats.symptocareappfrontend;

import android.app.AlarmManager;
import android.app.PendingIntent;
import android.app.TimePickerDialog;
import android.content.ContentValues;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.database.sqlite.SQLiteDatabase;
import android.graphics.Color;
import android.os.Bundle;
import android.text.TextUtils;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;
import android.widget.ToggleButton;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;

import com.google.android.material.bottomsheet.BottomSheetDialogFragment;
import com.google.android.material.chip.Chip;
import com.google.android.material.chip.ChipGroup;

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;
import java.util.List;
import java.util.Locale;

public class AddTaskBottomSheet extends BottomSheetDialogFragment {

    private ToggleButton btnTypeTablet, btnTypeTopical, btnTypeExercise, btnTypeMonitor;
    private String selectedType = "Tablet / Med";
    
    private EditText etTaskName, etDuration;
    private ChipGroup cgReminders;
    private Button btnSaveTask;
    private Chip chipAddCustomTime;

    private List<String> selectedTimes = new ArrayList<>();

    @NonNull
    @Override
    public android.app.Dialog onCreateDialog(@Nullable Bundle savedInstanceState) {
        com.google.android.material.bottomsheet.BottomSheetDialog dialog = (com.google.android.material.bottomsheet.BottomSheetDialog) super.onCreateDialog(savedInstanceState);
        dialog.setOnShowListener(dialogInterface -> {
            com.google.android.material.bottomsheet.BottomSheetDialog d = (com.google.android.material.bottomsheet.BottomSheetDialog) dialogInterface;
            View bottomSheetInternal = d.findViewById(com.google.android.material.R.id.design_bottom_sheet);
            if (bottomSheetInternal != null) {
                com.google.android.material.bottomsheet.BottomSheetBehavior.from(bottomSheetInternal).setState(com.google.android.material.bottomsheet.BottomSheetBehavior.STATE_EXPANDED);
            }
        });
        return dialog;
    }

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.bottom_sheet_add_task, container, false);
        
        btnTypeTablet = view.findViewById(R.id.btnTypeTablet);
        btnTypeTopical = view.findViewById(R.id.btnTypeTopical);
        btnTypeExercise = view.findViewById(R.id.btnTypeExercise);
        btnTypeMonitor = view.findViewById(R.id.btnTypeMonitor);
        
        etTaskName = view.findViewById(R.id.etTaskName);
        etDuration = view.findViewById(R.id.etDuration);
        cgReminders = view.findViewById(R.id.cgReminders);
        btnSaveTask = view.findViewById(R.id.btnSaveTask);
        chipAddCustomTime = view.findViewById(R.id.chipAddCustomTime);

        setupTypeToggles();
        setupChips();

        btnSaveTask.setOnClickListener(v -> saveTask());

        return view;
    }

    private void setupTypeToggles() {
        btnTypeTablet.setChecked(true);
        updateToggleStyles();

        View.OnClickListener toggleListener = v -> {
            btnTypeTablet.setChecked(v.getId() == R.id.btnTypeTablet);
            btnTypeTopical.setChecked(v.getId() == R.id.btnTypeTopical);
            btnTypeExercise.setChecked(v.getId() == R.id.btnTypeExercise);
            btnTypeMonitor.setChecked(v.getId() == R.id.btnTypeMonitor);
            
            if (v.getId() == R.id.btnTypeTablet) selectedType = "Tablet / Med";
            else if (v.getId() == R.id.btnTypeTopical) selectedType = "Topical / Apply";
            else if (v.getId() == R.id.btnTypeExercise) selectedType = "Exercise / Cardio";
            else if (v.getId() == R.id.btnTypeMonitor) selectedType = "Check / Monitor";
            
            updateToggleStyles();
        };

        btnTypeTablet.setOnClickListener(toggleListener);
        btnTypeTopical.setOnClickListener(toggleListener);
        btnTypeExercise.setOnClickListener(toggleListener);
        btnTypeMonitor.setOnClickListener(toggleListener);
    }

    private void updateToggleStyles() {
        ToggleButton[] btns = {btnTypeTablet, btnTypeTopical, btnTypeExercise, btnTypeMonitor};
        for (ToggleButton btn : btns) {
            if (btn.isChecked()) {
                btn.setBackgroundColor(Color.parseColor("#3FBAF1")); // primary_blue
                btn.setTextColor(Color.WHITE);
            } else {
                btn.setBackgroundColor(Color.parseColor("#E2E8F0")); // divider
                btn.setTextColor(Color.parseColor("#032A44")); // text_title
            }
        }
    }

    private void setupChips() {
        for (int i = 0; i < cgReminders.getChildCount(); i++) {
            View child = cgReminders.getChildAt(i);
            if (child instanceof Chip && child.getId() != R.id.chipAddCustomTime) {
                Chip chip = (Chip) child;
                chip.setOnCheckedChangeListener((buttonView, isChecked) -> {
                    String time = chip.getText().toString();
                    if (isChecked) {
                        if (!selectedTimes.contains(time)) selectedTimes.add(time);
                    } else {
                        selectedTimes.remove(time);
                    }
                });
            }
        }

        chipAddCustomTime.setOnClickListener(v -> {
            Calendar c = Calendar.getInstance();
            new TimePickerDialog(getContext(), (view, hourOfDay, minute) -> {
                Calendar time = Calendar.getInstance();
                time.set(Calendar.HOUR_OF_DAY, hourOfDay);
                time.set(Calendar.MINUTE, minute);
                
                String timeStr = new SimpleDateFormat("h:mm a", Locale.US).format(time.getTime());
                
                Chip customChip = new Chip(getContext());
                customChip.setText(timeStr);
                customChip.setCheckable(true);
                customChip.setChecked(true);
                customChip.setOnCheckedChangeListener((buttonView, isChecked) -> {
                    if (isChecked) {
                        if (!selectedTimes.contains(timeStr)) selectedTimes.add(timeStr);
                    } else {
                        selectedTimes.remove(timeStr);
                    }
                });
                
                selectedTimes.add(timeStr);
                cgReminders.addView(customChip, cgReminders.getChildCount() - 1);
            }, c.get(Calendar.HOUR_OF_DAY), c.get(Calendar.MINUTE), false).show();
        });
    }

    private void saveTask() {
        String name = etTaskName.getText().toString().trim();
        String durationStr = etDuration.getText().toString().trim();

        if (TextUtils.isEmpty(name)) {
            Toast.makeText(getContext(), "Please enter a task name", Toast.LENGTH_SHORT).show();
            return;
        }

        if (selectedTimes.isEmpty()) {
            Toast.makeText(getContext(), "Please select at least one reminder time", Toast.LENGTH_SHORT).show();
            return;
        }

        int duration = 1;
        if (!TextUtils.isEmpty(durationStr)) {
            duration = Integer.parseInt(durationStr);
        }

        SharedPreferences prefs = getContext().getSharedPreferences("SymptoCarePrefs", Context.MODE_PRIVATE);
        long userId = prefs.getLong("active_user_id", -1);
        
        if (userId == -1) return;

        String timesCsv = TextUtils.join(", ", selectedTimes);
        String today = new SimpleDateFormat("yyyy-MM-dd", Locale.getDefault()).format(new Date());

        DatabaseHelper dbHelper = new DatabaseHelper(getContext());
        SQLiteDatabase db = dbHelper.getWritableDatabase();

        ContentValues cv = new ContentValues();
        cv.put(DatabaseHelper.COL_RT_USER_ID, userId);
        cv.put(DatabaseHelper.COL_RT_TASK_NAME, name);
        cv.put(DatabaseHelper.COL_RT_TASK_TYPE, selectedType);
        cv.put(DatabaseHelper.COL_RT_REMINDER_TIMES, timesCsv);
        cv.put(DatabaseHelper.COL_RT_DURATION_DAYS, duration);
        cv.put(DatabaseHelper.COL_RT_CREATED_DATE, today);
        cv.put(DatabaseHelper.COL_RT_IS_COMPLETED, 0);

        long id = db.insert(DatabaseHelper.TABLE_RECOVERY_TASKS, null, cv);
        db.close();

        if (id != -1) {
            scheduleAlarms((int)id, name, duration);
            Toast.makeText(getContext(), "Task saved", Toast.LENGTH_SHORT).show();
            if (getActivity() instanceof RecoveryTasksActivity) {
                ((RecoveryTasksActivity) getActivity()).loadTasks();
            }
            dismiss();
        } else {
            Toast.makeText(getContext(), "Error saving task", Toast.LENGTH_SHORT).show();
        }
    }

    private void scheduleAlarms(int taskId, String taskName, int durationDays) {
        AlarmManager alarmManager = (AlarmManager) getContext().getSystemService(Context.ALARM_SERVICE);
        if (alarmManager == null) return;

        SimpleDateFormat sdf = new SimpleDateFormat("h:mm a", Locale.US);
        
        for (int i = 0; i < selectedTimes.size(); i++) {
            String timeStr = selectedTimes.get(i);
            try {
                Date d = sdf.parse(timeStr);
                Calendar alarmCal = Calendar.getInstance();
                Calendar parsedCal = Calendar.getInstance();
                parsedCal.setTime(d);
                
                alarmCal.set(Calendar.HOUR_OF_DAY, parsedCal.get(Calendar.HOUR_OF_DAY));
                alarmCal.set(Calendar.MINUTE, parsedCal.get(Calendar.MINUTE));
                alarmCal.set(Calendar.SECOND, 0);

                if (alarmCal.before(Calendar.getInstance())) {
                    alarmCal.add(Calendar.DATE, 1); // If time has passed, schedule for tomorrow
                }

                Intent intent = new Intent(getContext(), TaskAlarmReceiver.class);
                intent.putExtra("task_id", taskId);
                intent.putExtra("task_name", taskName);
                intent.putExtra("reminder_time", timeStr);
                
                int requestCode = taskId * 100 + i; // Unique request code per task per time
                intent.putExtra("request_code", requestCode);

                PendingIntent pendingIntent = PendingIntent.getBroadcast(getContext(), requestCode, intent, PendingIntent.FLAG_UPDATE_CURRENT | PendingIntent.FLAG_IMMUTABLE);

                try {
                    if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.M) {
                        alarmManager.setExactAndAllowWhileIdle(AlarmManager.RTC_WAKEUP, alarmCal.getTimeInMillis(), pendingIntent);
                    } else if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.KITKAT) {
                        alarmManager.setExact(AlarmManager.RTC_WAKEUP, alarmCal.getTimeInMillis(), pendingIntent);
                    } else {
                        alarmManager.set(AlarmManager.RTC_WAKEUP, alarmCal.getTimeInMillis(), pendingIntent);
                    }
                } catch (SecurityException se) {
                    alarmManager.set(AlarmManager.RTC_WAKEUP, alarmCal.getTimeInMillis(), pendingIntent);
                }

            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
}
