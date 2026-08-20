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

import com.simats.symptocareappfrontend.adapters.AppointmentAdapter;

import java.util.ArrayList;
import java.util.List;

public class AppointmentsActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_appointments);

        findViewById(R.id.btnBack).setOnClickListener(v -> finish());

        RecyclerView rvAppointments = findViewById(R.id.rvAppointments);
        TextView tvEmptyState = findViewById(R.id.tvEmptyState);
        rvAppointments.setLayoutManager(new LinearLayoutManager(this));

        List<AppointmentAdapter.Appointment> appointments = new ArrayList<>();

        SharedPreferences prefs = getSharedPreferences("SymptoCarePrefs", Context.MODE_PRIVATE);
        long userId = prefs.getLong("active_user_id", -1);

        if (userId != -1) {
            DatabaseHelper dbHelper = new DatabaseHelper(this);
            SQLiteDatabase db = dbHelper.getReadableDatabase();

            Cursor cursor = db.query(DatabaseHelper.TABLE_APPOINTMENTS,
                    new String[]{DatabaseHelper.COL_APP_DOC_NAME, DatabaseHelper.COL_APP_SPECIALITY, DatabaseHelper.COL_APP_DATETIME},
                    DatabaseHelper.COL_APP_USER_ID + "=?", new String[]{String.valueOf(userId)}, null, null, DatabaseHelper.COL_APP_ID + " DESC");

            if (cursor != null) {
                while (cursor.moveToNext()) {
                    appointments.add(new AppointmentAdapter.Appointment(
                            cursor.getString(0),
                            cursor.getString(1),
                            cursor.getString(2)
                    ));
                }
                cursor.close();
            }
        }

        if (appointments.isEmpty()) {
            tvEmptyState.setVisibility(View.VISIBLE);
            rvAppointments.setVisibility(View.GONE);
        } else {
            tvEmptyState.setVisibility(View.GONE);
            rvAppointments.setVisibility(View.VISIBLE);
            rvAppointments.setAdapter(new AppointmentAdapter(appointments));
        }
    }
}
