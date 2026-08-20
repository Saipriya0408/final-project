package com.simats.symptocareappfrontend;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;
import android.content.SharedPreferences;
import android.content.Context;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

public class ProfileFragment extends Fragment {

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_profile, container, false);
        
        
        TextView tvName = view.findViewById(R.id.tvUserName);
        TextView tvEmail = view.findViewById(R.id.tvUserEmail);
        TextView tvPhone = view.findViewById(R.id.tvUserPhone);
        TextView tvInitials = view.findViewById(R.id.ivAvatar);
        
        SharedPreferences prefs = getContext().getSharedPreferences("SymptoCarePrefs", Context.MODE_PRIVATE);
        long userId = prefs.getLong("active_user_id", -1);
        
        String name = prefs.getString("active_user_name", "Guest");
        String email = prefs.getString("active_user_email", "");
        String phone = "Not provided"; // Phone is not stored in prefs yet

        
        if (tvName != null) tvName.setText(name);
        if (tvEmail != null) tvEmail.setText(email);
        if (tvPhone != null) {
            tvPhone.setText(phone);
            tvPhone.setVisibility(phone.equals("Not provided") ? View.GONE : View.VISIBLE);
            if (tvEmail != null) {
                tvEmail.setVisibility(email.equals("Not provided") ? View.GONE : View.VISIBLE);
            }
        }
        
        if (tvInitials != null && name != null && !name.isEmpty()) {
            String[] parts = name.split(" ");
            StringBuilder init = new StringBuilder();
            for (String p : parts) {
                if (p.length() > 0) init.append(p.charAt(0));
            }
            tvInitials.setText(init.toString().toUpperCase());
        }

        TextView tvStatAppointments = view.findViewById(R.id.tvStatAppointments);
        TextView tvStatHealthRecords = view.findViewById(R.id.tvStatHealthRecords);
        TextView tvStatSavedDoctors = view.findViewById(R.id.tvStatSavedDoctors);
        TextView tvStatSavedHospitals = view.findViewById(R.id.tvStatSavedHospitals);

        if (userId != -1) {
            updateStats();
        }

        View btnLogout = view.findViewById(R.id.btnLogout);

        if (btnLogout != null) {
            btnLogout.setOnClickListener(v -> {
                if (getActivity() != null) {
                    prefs.edit().remove("active_user_id").apply();
                    android.content.Intent intent = new android.content.Intent(getActivity(), SignInActivity.class);
                    intent.setFlags(android.content.Intent.FLAG_ACTIVITY_NEW_TASK | android.content.Intent.FLAG_ACTIVITY_CLEAR_TASK);
                    startActivity(intent);
                }
            });
        }
        
        // Setup Grid Clicks
        View boxAppointments = view.findViewById(R.id.boxAppointments);
        View boxHealthRecords = view.findViewById(R.id.boxHealthRecords);
        View boxSavedDoctors = view.findViewById(R.id.boxSavedDoctors);
        View boxSavedHospitals = view.findViewById(R.id.boxSavedHospitals);
        View boxRecoveryTasks = view.findViewById(R.id.boxRecoveryTasks);

        if (boxAppointments != null) {
             boxAppointments.setOnClickListener(v -> {
                 startActivity(new android.content.Intent(getActivity(), AppointmentsActivity.class));
             });
        }
        if (boxHealthRecords != null) {
             boxHealthRecords.setOnClickListener(v -> {
                 startActivity(new android.content.Intent(getActivity(), HealthHistoryActivity.class));
             });
        }
        if (boxSavedDoctors != null) {
             boxSavedDoctors.setOnClickListener(v -> {
                 startActivity(new android.content.Intent(getActivity(), SavedDoctorsActivity.class));
             });
        }
        if (boxSavedHospitals != null) {
             boxSavedHospitals.setOnClickListener(v -> {
                 startActivity(new android.content.Intent(getActivity(), SavedHospitalsActivity.class));
             });
        }
        if (boxRecoveryTasks != null) {
             boxRecoveryTasks.setOnClickListener(v -> {
                 startActivity(new android.content.Intent(getActivity(), RecoveryTasksActivity.class));
             });
        }
        
        android.widget.TextView btnAddWater = view.findViewById(R.id.btnAddWater);
        android.widget.ProgressBar progressWater = view.findViewById(R.id.progressWater);
        android.widget.TextView tvWaterProgress = view.findViewById(R.id.tvWaterProgress);
        
        if (btnAddWater != null && progressWater != null && tvWaterProgress != null) {
            btnAddWater.setOnClickListener(v -> {
                int current = progressWater.getProgress();
                if (current < 8) {
                    progressWater.setProgress(current + 1);
                    tvWaterProgress.setText((current + 1) + " / 8 Glasses");
                } else {
                    android.widget.Toast.makeText(getContext(), "Daily goal reached! Great job!", android.widget.Toast.LENGTH_SHORT).show();
                }
            });
        }
        
        return view;
    }

    @Override
    public void onResume() {
        super.onResume();
        updateStats();
    }

    private void updateStats() {
        if (getView() == null || getContext() == null) return;
        SharedPreferences prefs = getContext().getSharedPreferences("SymptoCarePrefs", Context.MODE_PRIVATE);
        long userId = prefs.getLong("active_user_id", -1);
        if (userId == -1) return;

        TextView tvStatAppointments = getView().findViewById(R.id.tvStatAppointments);
        TextView tvStatHealthRecords = getView().findViewById(R.id.tvStatHealthRecords);
        TextView tvStatSavedDoctors = getView().findViewById(R.id.tvStatSavedDoctors);
        TextView tvStatSavedHospitals = getView().findViewById(R.id.tvStatSavedHospitals);
        TextView tvStatRecoveryTasks = getView().findViewById(R.id.tvStatRecoveryTasks);

        DatabaseHelper dbHelper = new DatabaseHelper(getContext());
        android.database.sqlite.SQLiteDatabase db = dbHelper.getReadableDatabase();
        
        android.database.Cursor c1 = db.rawQuery("SELECT COUNT(*) FROM " + DatabaseHelper.TABLE_APPOINTMENTS + " WHERE " + DatabaseHelper.COL_APP_USER_ID + "=?", new String[]{String.valueOf(userId)});
        if (c1 != null && c1.moveToFirst()) {
            if (tvStatAppointments != null) tvStatAppointments.setText(String.valueOf(c1.getInt(0)));
            c1.close();
        }
        
        android.database.Cursor c2 = db.rawQuery("SELECT COUNT(*) FROM " + DatabaseHelper.TABLE_HEALTH_HISTORY + " WHERE " + DatabaseHelper.COL_HIST_USER_ID + "=?", new String[]{String.valueOf(userId)});
        if (c2 != null && c2.moveToFirst()) {
            if (tvStatHealthRecords != null) tvStatHealthRecords.setText(String.valueOf(c2.getInt(0)));
            c2.close();
        }

        android.database.Cursor c3 = db.rawQuery("SELECT COUNT(*) FROM " + DatabaseHelper.TABLE_SAVED_DOCTORS + " WHERE " + DatabaseHelper.COL_SD_USER_ID + "=?", new String[]{String.valueOf(userId)});
        if (c3 != null && c3.moveToFirst()) {
            if (tvStatSavedDoctors != null) tvStatSavedDoctors.setText(String.valueOf(c3.getInt(0)));
            c3.close();
        }

        android.database.Cursor c4 = db.rawQuery("SELECT COUNT(*) FROM " + DatabaseHelper.TABLE_SAVED_HOSPITALS + " WHERE " + DatabaseHelper.COL_SH_USER_ID + "=?", new String[]{String.valueOf(userId)});
        if (c4 != null && c4.moveToFirst()) {
            if (tvStatSavedHospitals != null) tvStatSavedHospitals.setText(String.valueOf(c4.getInt(0)));
            c4.close();
        }

        // Active recovery tasks for today
        String today = new java.text.SimpleDateFormat("yyyy-MM-dd", java.util.Locale.getDefault()).format(new java.util.Date());
        android.database.Cursor c5 = db.rawQuery("SELECT COUNT(*) FROM " + DatabaseHelper.TABLE_RECOVERY_TASKS + " WHERE " + DatabaseHelper.COL_RT_USER_ID + "=? AND " + DatabaseHelper.COL_RT_CREATED_DATE + "=?", new String[]{String.valueOf(userId), today});
        if (c5 != null && c5.moveToFirst()) {
            if (tvStatRecoveryTasks != null) tvStatRecoveryTasks.setText(String.valueOf(c5.getInt(0)));
            c5.close();
        }
    }
}
