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

import com.simats.symptocareappfrontend.adapters.DoctorAdapter;
import com.simats.symptocareappfrontend.models.Doctor;

import java.util.ArrayList;
import java.util.List;

public class SavedDoctorsActivity extends AppCompatActivity {

    private RecyclerView rvSavedDoctors;
    private TextView tvEmptyState;
    private DoctorAdapter adapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_saved_doctors);

        rvSavedDoctors = findViewById(R.id.rvSavedDoctors);
        tvEmptyState = findViewById(R.id.tvEmptyState);

        rvSavedDoctors.setLayoutManager(new LinearLayoutManager(this));
        adapter = new DoctorAdapter();
        rvSavedDoctors.setAdapter(adapter);

        findViewById(R.id.btnBack).setOnClickListener(v -> finish());

        loadSavedDoctors();
    }

    private void loadSavedDoctors() {
        SharedPreferences prefs = getSharedPreferences("SymptoCarePrefs", Context.MODE_PRIVATE);
        long userId = prefs.getLong("active_user_id", -1);

        if (userId == -1) {
            tvEmptyState.setVisibility(View.VISIBLE);
            return;
        }

        DatabaseHelper dbHelper = new DatabaseHelper(this);
        SQLiteDatabase db = dbHelper.getReadableDatabase();

        String[] projection = {
                DatabaseHelper.COL_SD_NAME,
                DatabaseHelper.COL_SD_SPECIALITY,
                DatabaseHelper.COL_SD_EXP,
                DatabaseHelper.COL_SD_FEE,
                DatabaseHelper.COL_SD_INITIALS
        };

        String selection = DatabaseHelper.COL_SD_USER_ID + " = ?";
        String[] selectionArgs = { String.valueOf(userId) };

        Cursor cursor = db.query(
                DatabaseHelper.TABLE_SAVED_DOCTORS,
                projection,
                selection,
                selectionArgs,
                null,
                null,
                DatabaseHelper.COL_SD_ID + " DESC"
        );

        List<Doctor> savedDoctors = new ArrayList<>();
        while (cursor.moveToNext()) {
            Doctor doc = new Doctor();
            doc.name = cursor.getString(cursor.getColumnIndexOrThrow(DatabaseHelper.COL_SD_NAME));
            doc.specialist = cursor.getString(cursor.getColumnIndexOrThrow(DatabaseHelper.COL_SD_SPECIALITY));
            String expStr = cursor.getString(cursor.getColumnIndexOrThrow(DatabaseHelper.COL_SD_EXP));
            try { doc.experience_years = Integer.parseInt(expStr.replaceAll("[^0-9]", "")); } catch(Exception e) { doc.experience_years = 0; }
            String feeStr = cursor.getString(cursor.getColumnIndexOrThrow(DatabaseHelper.COL_SD_FEE));
            try { doc.consultation_fee = Integer.parseInt(feeStr.replaceAll("[^0-9]", "")); } catch (Exception e) { doc.consultation_fee = 0; }
            savedDoctors.add(doc);
        }
        cursor.close();

        if (savedDoctors.isEmpty()) {
            tvEmptyState.setVisibility(View.VISIBLE);
            rvSavedDoctors.setVisibility(View.GONE);
        } else {
            tvEmptyState.setVisibility(View.GONE);
            rvSavedDoctors.setVisibility(View.VISIBLE);
            adapter.setDoctors(savedDoctors);
        }
    }
}
