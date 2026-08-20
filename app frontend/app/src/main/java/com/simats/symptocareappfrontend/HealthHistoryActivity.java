package com.simats.symptocareappfrontend;

import android.content.Context;
import android.content.SharedPreferences;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.simats.symptocareappfrontend.adapters.HealthHistoryAdapter;

import java.util.ArrayList;
import java.util.List;

public class HealthHistoryActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_health_history);

        findViewById(R.id.btnBack).setOnClickListener(v -> finish());

        RecyclerView rvHealthHistory = findViewById(R.id.rvHealthHistory);
        TextView tvEmptyState = findViewById(R.id.tvEmptyState);
        rvHealthHistory.setLayoutManager(new LinearLayoutManager(this));

        List<HealthHistoryAdapter.HealthRecord> records = new ArrayList<>();

        SharedPreferences prefs = getSharedPreferences("SymptoCarePrefs", Context.MODE_PRIVATE);
        long userId = prefs.getLong("active_user_id", -1);

        if (userId != -1) {
            DatabaseHelper dbHelper = new DatabaseHelper(this);
            SQLiteDatabase db = dbHelper.getReadableDatabase();

            Cursor cursor = db.query(DatabaseHelper.TABLE_HEALTH_HISTORY,
                    new String[]{DatabaseHelper.COL_HIST_SYMPTOMS, DatabaseHelper.COL_HIST_PREDICTION, DatabaseHelper.COL_HIST_TIMESTAMP},
                    DatabaseHelper.COL_HIST_USER_ID + "=?", new String[]{String.valueOf(userId)}, null, null, DatabaseHelper.COL_HIST_ID + " DESC");

            if (cursor != null) {
                while (cursor.moveToNext()) {
                    records.add(new HealthHistoryAdapter.HealthRecord(
                            cursor.getString(0),
                            cursor.getString(1),
                            cursor.getString(2)
                    ));
                }
                cursor.close();
            }
        }

        if (records.isEmpty()) {
            tvEmptyState.setVisibility(View.VISIBLE);
            rvHealthHistory.setVisibility(View.GONE);
        } else {
            tvEmptyState.setVisibility(View.GONE);
            rvHealthHistory.setVisibility(View.VISIBLE);
            rvHealthHistory.setAdapter(new HealthHistoryAdapter(records));
        }
    }
}
