package com.simats.symptocareappfrontend;

import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;
import androidx.fragment.app.Fragment;
import com.google.android.material.bottomnavigation.BottomNavigationView;

public class MainActivity extends AppCompatActivity {

    private BottomNavigationView bottomNav;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        bottomNav = findViewById(R.id.bottom_navigation);
        bottomNav.setOnItemSelectedListener(item -> {
            Fragment selectedFragment = null;
            int itemId = item.getItemId();
            
            if (itemId == R.id.nav_home) {
                selectedFragment = new HomeFragment();
            } else if (itemId == R.id.nav_symptoms) {
                selectedFragment = new SymptomsFragment();
            } else if (itemId == R.id.nav_doctors) {
                selectedFragment = new DoctorsFragment();
            } else if (itemId == R.id.nav_hospitals) {
                selectedFragment = new HospitalsFragment();
            } else if (itemId == R.id.nav_profile) {
                selectedFragment = new ProfileFragment();
            }

            if (selectedFragment != null) {
                getSupportFragmentManager().beginTransaction()
                    .replace(R.id.nav_host_fragment, selectedFragment)
                    .commit();
            }
            return true;
        });

        // Check if we need to open a specific tab (e.g., from AssessmentResultFragment)
        int openTab = getIntent().getIntExtra("openTab", -1);
        String filterSpecialty = getIntent().getStringExtra("filterSpecialty");
        if (filterSpecialty != null) {
            getSharedPreferences("AppPrefs", MODE_PRIVATE).edit().putString("filter_specialist", filterSpecialty).apply();
        }
        if (openTab != -1) {
            bottomNav.setSelectedItemId(openTab);
        } else if (savedInstanceState == null) {
            bottomNav.setSelectedItemId(R.id.nav_home);
        }
    }

    @Override
    protected void onNewIntent(android.content.Intent intent) {
        super.onNewIntent(intent);
        int openTab = intent.getIntExtra("openTab", -1);
        String filterSpecialty = intent.getStringExtra("filterSpecialty");
        if (filterSpecialty != null) {
            getSharedPreferences("AppPrefs", MODE_PRIVATE).edit().putString("filter_specialist", filterSpecialty).apply();
        }
        if (openTab != -1 && bottomNav != null) {
            bottomNav.setSelectedItemId(openTab);
        }
    }
}