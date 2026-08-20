package com.simats.symptocareappfrontend;

import android.content.ContentValues;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;

public class DoctorProfileActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_doctor_profile);

        Intent intent = getIntent();
        String name = intent.getStringExtra("doc_name");
        String speciality = intent.getStringExtra("doc_speciality");
        String exp = intent.getStringExtra("doc_exp");
        String fee = intent.getStringExtra("doc_fee");
        String initials = intent.getStringExtra("doc_initials");
        String distance = intent.getStringExtra("doc_distance");
        Double lat = intent.getDoubleExtra("doc_lat", 0);
        Double lng = intent.getDoubleExtra("doc_lng", 0);

        TextView tvName = findViewById(R.id.tvDoctorName);
        TextView tvSpeciality = findViewById(R.id.tvDoctorSpeciality);
        TextView tvExp = findViewById(R.id.tvDoctorExp);
        TextView tvFee = findViewById(R.id.tvDoctorFee);
        TextView tvInitials = findViewById(R.id.ivDoctorAvatar);
        TextView tvDistance = findViewById(R.id.tvDoctorDistance);

        if (name != null) tvName.setText(name);
        if (speciality != null) tvSpeciality.setText(speciality);
        if (exp != null) tvExp.setText("Experience: " + exp);
        if (fee != null) tvFee.setText("Consultation Fee: " + fee);
        if (initials != null) tvInitials.setText(initials);
        
        if (distance != null) {
            tvDistance.setText("Distance: " + distance);
            tvDistance.setVisibility(View.VISIBLE);
        } else {
            tvDistance.setVisibility(View.GONE);
        }

        findViewById(R.id.btnBack).setOnClickListener(v -> finish());
        
        View btnNavigate = findViewById(R.id.btnNavigateDoctor);
        if (btnNavigate != null) {
            btnNavigate.setOnClickListener(v -> {
                android.net.Uri gmmIntentUri = android.net.Uri.parse("google.navigation:q=" + lat + "," + lng);
                android.content.Intent mapIntent = new android.content.Intent(android.content.Intent.ACTION_VIEW, gmmIntentUri);
                mapIntent.setPackage("com.google.android.apps.maps");
                try {
                    startActivity(mapIntent);
                } catch (android.content.ActivityNotFoundException e) {
                    Toast.makeText(this, "Google Maps is not installed", Toast.LENGTH_SHORT).show();
                }
            });
        }

        findViewById(R.id.btnSaveDoctor).setOnClickListener(v -> {
            SharedPreferences prefs = getSharedPreferences("SymptoCarePrefs", Context.MODE_PRIVATE);
            long userId = prefs.getLong("active_user_id", -1);
            if (userId == -1) {
                Toast.makeText(this, "Please login first", Toast.LENGTH_SHORT).show();
                return;
            }
            DatabaseHelper dbHelper = new DatabaseHelper(this);
            SQLiteDatabase db = dbHelper.getWritableDatabase();

            ContentValues values = new ContentValues();
            values.put(DatabaseHelper.COL_SD_USER_ID, userId);
            values.put(DatabaseHelper.COL_SD_NAME, name);
            values.put(DatabaseHelper.COL_SD_SPECIALITY, speciality);
            values.put(DatabaseHelper.COL_SD_EXP, exp);
            values.put(DatabaseHelper.COL_SD_FEE, fee);
            values.put(DatabaseHelper.COL_SD_INITIALS, initials);

            long rowId = db.insert(DatabaseHelper.TABLE_SAVED_DOCTORS, null, values);
            if (rowId != -1) {
                Toast.makeText(this, "Doctor Saved!", Toast.LENGTH_SHORT).show();
            } else {
                Toast.makeText(this, "Failed to save doctor", Toast.LENGTH_SHORT).show();
            }
        });

        findViewById(R.id.btnBookAppointment).setOnClickListener(v -> {
            SharedPreferences prefs = getSharedPreferences("SymptoCarePrefs", Context.MODE_PRIVATE);
            long userId = prefs.getLong("active_user_id", -1);
            if (userId == -1) {
                Toast.makeText(this, "Please login first", Toast.LENGTH_SHORT).show();
                return;
            }

            java.util.Calendar calendar = java.util.Calendar.getInstance();
            int year = calendar.get(java.util.Calendar.YEAR);
            int month = calendar.get(java.util.Calendar.MONTH);
            int day = calendar.get(java.util.Calendar.DAY_OF_MONTH);

            android.app.DatePickerDialog datePickerDialog = new android.app.DatePickerDialog(this,
                    (view, selectedYear, selectedMonth, selectedDay) -> {
                        int hour = calendar.get(java.util.Calendar.HOUR_OF_DAY);
                        int minute = calendar.get(java.util.Calendar.MINUTE);

                        android.app.TimePickerDialog timePickerDialog = new android.app.TimePickerDialog(this,
                                (timeView, selectedHour, selectedMinute) -> {
                                    java.util.Calendar selectedDateTime = java.util.Calendar.getInstance();
                                    selectedDateTime.set(selectedYear, selectedMonth, selectedDay, selectedHour, selectedMinute);

                                    String formattedDate = new SimpleDateFormat("dd MMM yyyy, hh:mm a", Locale.getDefault()).format(selectedDateTime.getTime());

                                    DatabaseHelper dbHelper = new DatabaseHelper(DoctorProfileActivity.this);
                                    SQLiteDatabase db = dbHelper.getWritableDatabase();

                                    ContentValues values = new ContentValues();
                                    values.put(DatabaseHelper.COL_APP_USER_ID, userId);
                                    values.put(DatabaseHelper.COL_APP_DOC_NAME, name);
                                    values.put(DatabaseHelper.COL_APP_SPECIALITY, speciality);
                                    values.put(DatabaseHelper.COL_APP_DATETIME, formattedDate);

                                    long rowId = db.insert(DatabaseHelper.TABLE_APPOINTMENTS, null, values);
                                    if (rowId != -1) {
                                        Toast.makeText(DoctorProfileActivity.this, "Appointment Booked for " + formattedDate, Toast.LENGTH_LONG).show();
                                        finish();
                                    } else {
                                        Toast.makeText(DoctorProfileActivity.this, "Failed to book appointment", Toast.LENGTH_SHORT).show();
                                    }
                                }, hour, minute, false);
                        timePickerDialog.show();
                    }, year, month, day);
            datePickerDialog.getDatePicker().setMinDate(System.currentTimeMillis());
            datePickerDialog.show();
        });
    }
}
