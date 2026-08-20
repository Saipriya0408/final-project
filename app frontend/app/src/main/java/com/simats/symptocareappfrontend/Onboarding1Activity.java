package com.simats.symptocareappfrontend;

import androidx.appcompat.app.AppCompatActivity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;

public class Onboarding1Activity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        
        android.content.SharedPreferences prefs = getSharedPreferences("SymptoCarePrefs", MODE_PRIVATE);
        if (prefs.getLong("active_user_id", -1) != -1) {
            startActivity(new Intent(this, MainActivity.class));
            finish();
            return;
        }

        setContentView(R.layout.activity_onboarding1);

        View btnNext = findViewById(R.id.btnNext);
        View tvSkip = findViewById(R.id.tvSkip);

        btnNext.setOnClickListener(v -> {
            startActivity(new Intent(Onboarding1Activity.this, Onboarding2Activity.class));
            finish();
        });

        tvSkip.setOnClickListener(v -> {
            startActivity(new Intent(Onboarding1Activity.this, SignUpActivity.class));
            finish();
        });
    }
}
