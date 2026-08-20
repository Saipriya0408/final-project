package com.simats.symptocareappfrontend;

import androidx.appcompat.app.AppCompatActivity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;

public class Onboarding2Activity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_onboarding2);

        View btnNext = findViewById(R.id.btnNext);
        View tvSkip = findViewById(R.id.tvSkip);

        btnNext.setOnClickListener(v -> {
            startActivity(new Intent(Onboarding2Activity.this, Onboarding3Activity.class));
            finish();
        });

        tvSkip.setOnClickListener(v -> {
            startActivity(new Intent(Onboarding2Activity.this, SignUpActivity.class));
            finish();
        });
    }
}
