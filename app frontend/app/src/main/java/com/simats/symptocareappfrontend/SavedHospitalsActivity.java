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

import com.simats.symptocareappfrontend.adapters.HospitalAdapter;
import com.simats.symptocareappfrontend.models.Department;
import com.simats.symptocareappfrontend.models.Hospital;

import java.util.ArrayList;
import java.util.List;

public class SavedHospitalsActivity extends AppCompatActivity {

    private RecyclerView rvSavedHospitals;
    private TextView tvEmptyState;
    private HospitalAdapter adapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_saved_hospitals);

        rvSavedHospitals = findViewById(R.id.rvSavedHospitals);
        tvEmptyState = findViewById(R.id.tvEmptyState);

        rvSavedHospitals.setLayoutManager(new LinearLayoutManager(this));
        adapter = new HospitalAdapter();
        rvSavedHospitals.setAdapter(adapter);

        findViewById(R.id.btnBack).setOnClickListener(v -> finish());

        loadSavedHospitals();
    }

    private void loadSavedHospitals() {
        SharedPreferences prefs = getSharedPreferences("SymptoCarePrefs", Context.MODE_PRIVATE);
        long userId = prefs.getLong("active_user_id", -1);

        if (userId == -1) {
            tvEmptyState.setVisibility(View.VISIBLE);
            return;
        }

        DatabaseHelper dbHelper = new DatabaseHelper(this);
        SQLiteDatabase db = dbHelper.getReadableDatabase();

        String[] projection = {
                DatabaseHelper.COL_SH_NAME,
                DatabaseHelper.COL_SH_LOCATION,
                DatabaseHelper.COL_SH_DEPARTMENTS,
                DatabaseHelper.COL_SH_RATING,
                DatabaseHelper.COL_SH_EMERGENCY
        };

        String selection = DatabaseHelper.COL_SH_USER_ID + " = ?";
        String[] selectionArgs = { String.valueOf(userId) };

        Cursor cursor = db.query(
                DatabaseHelper.TABLE_SAVED_HOSPITALS,
                projection,
                selection,
                selectionArgs,
                null,
                null,
                DatabaseHelper.COL_SH_ID + " DESC"
        );

        List<Hospital> savedHospitals = new ArrayList<>();
        while (cursor.moveToNext()) {
            Hospital hosp = new Hospital();
            hosp.name = cursor.getString(cursor.getColumnIndexOrThrow(DatabaseHelper.COL_SH_NAME));
            hosp.address = cursor.getString(cursor.getColumnIndexOrThrow(DatabaseHelper.COL_SH_LOCATION));
            String ratingStr = cursor.getString(cursor.getColumnIndexOrThrow(DatabaseHelper.COL_SH_RATING));
            try { hosp.rating = Double.parseDouble(ratingStr); } catch (Exception e) { hosp.rating = 0.0; }
            hosp.emergency = cursor.getInt(cursor.getColumnIndexOrThrow(DatabaseHelper.COL_SH_EMERGENCY)) == 1;
            
            String deptsStr = cursor.getString(cursor.getColumnIndexOrThrow(DatabaseHelper.COL_SH_DEPARTMENTS));
            if (deptsStr != null && !deptsStr.isEmpty()) {
                String[] deptArray = deptsStr.split(",");
                hosp.departments = new ArrayList<>();
                for (String d : deptArray) {
                    Department dept = new Department();
                    dept.name = d.trim();
                    hosp.departments.add(dept);
                }
            }
            
            savedHospitals.add(hosp);
        }
        cursor.close();

        if (savedHospitals.isEmpty()) {
            tvEmptyState.setVisibility(View.VISIBLE);
            rvSavedHospitals.setVisibility(View.GONE);
        } else {
            tvEmptyState.setVisibility(View.GONE);
            rvSavedHospitals.setVisibility(View.VISIBLE);
            adapter.setHospitals(savedHospitals);
        }
    }
}
