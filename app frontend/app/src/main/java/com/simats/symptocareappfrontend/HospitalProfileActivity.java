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

public class HospitalProfileActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_hospital_profile);

        Intent intent = getIntent();
        String name = intent.getStringExtra("hosp_name");
        String address = intent.getStringExtra("hosp_address");
        double rating = intent.getDoubleExtra("hosp_rating", 0.0);
        int reviewCount = intent.getIntExtra("hosp_review_count", 0);
        boolean emergency = intent.getBooleanExtra("hosp_emergency", false);
        String departments = intent.getStringExtra("hosp_departments");

        TextView tvName = findViewById(R.id.tvHospName);
        TextView tvAddress = findViewById(R.id.tvHospAddress);
        TextView tvRating = findViewById(R.id.tvHospRating);
        TextView tvEmergency = findViewById(R.id.tvEmergencyBadge);
        TextView tvDepartments = findViewById(R.id.tvHospDepartments);

        if (name != null) tvName.setText(name);
        if (address != null) tvAddress.setText(address);
        tvRating.setText("⭐ " + rating + " (" + reviewCount + " reviews)");
        tvEmergency.setVisibility(emergency ? View.VISIBLE : View.GONE);
        if (departments != null) tvDepartments.setText(departments);

        findViewById(R.id.btnBack).setOnClickListener(v -> finish());

        findViewById(R.id.btnSaveHospital).setOnClickListener(v -> {
            SharedPreferences prefs = getSharedPreferences("SymptoCarePrefs", Context.MODE_PRIVATE);
            long userId = prefs.getLong("active_user_id", -1);
            if (userId == -1) {
                Toast.makeText(this, "Please login first", Toast.LENGTH_SHORT).show();
                return;
            }

            DatabaseHelper dbHelper = new DatabaseHelper(this);
            SQLiteDatabase db = dbHelper.getWritableDatabase();

            ContentValues values = new ContentValues();
            values.put(DatabaseHelper.COL_SH_USER_ID, userId);
            values.put(DatabaseHelper.COL_SH_NAME, name);
            values.put(DatabaseHelper.COL_SH_LOCATION, address);
            values.put(DatabaseHelper.COL_SH_DEPARTMENTS, departments);
            values.put(DatabaseHelper.COL_SH_RATING, String.valueOf(rating));
            values.put(DatabaseHelper.COL_SH_EMERGENCY, emergency ? 1 : 0);

            long rowId = db.insert(DatabaseHelper.TABLE_SAVED_HOSPITALS, null, values);
            if (rowId != -1) {
                Toast.makeText(this, "Hospital Saved!", Toast.LENGTH_SHORT).show();
            } else {
                Toast.makeText(this, "Failed to save hospital", Toast.LENGTH_SHORT).show();
            }
        });
    }
}
