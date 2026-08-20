package com.simats.symptocareappfrontend;

import androidx.appcompat.app.AppCompatActivity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.content.SharedPreferences;
import android.content.Context;
import android.widget.Toast;

import com.simats.symptocareappfrontend.api.ApiClient;
import com.simats.symptocareappfrontend.api.ApiService;
import com.simats.symptocareappfrontend.models.SignupRequest;
import com.simats.symptocareappfrontend.models.AuthResponse;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class SignUpActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_signup);

        View tvSignInLink = findViewById(R.id.tvSignInLink);
        View btnCreateAccount = findViewById(R.id.btnCreateAccount);
        EditText etName = findViewById(R.id.etName);
        EditText etEmail = findViewById(R.id.etEmail);
        EditText etPhone = findViewById(R.id.etPhone);
        
        tvSignInLink.setOnClickListener(v -> {
            startActivity(new Intent(SignUpActivity.this, SignInActivity.class));
            finish();
        });

        btnCreateAccount.setOnClickListener(v -> {
            if (etName != null && etEmail != null && etPhone != null) {
                String name = etName.getText().toString().trim();
                String email = etEmail.getText().toString().trim();
                String phone = etPhone.getText().toString().trim();
                EditText etPassword = findViewById(R.id.etPassword);
                String password = etPassword != null ? etPassword.getText().toString() : "";
                EditText etConfirmPassword = findViewById(R.id.etConfirmPassword);
                String confirmPassword = etConfirmPassword != null ? etConfirmPassword.getText().toString() : "";
                
                if (name.isEmpty() || email.isEmpty() || phone.isEmpty() || password.isEmpty() || confirmPassword.isEmpty()) {
                    Toast.makeText(SignUpActivity.this, "Please fill in all fields", Toast.LENGTH_SHORT).show();
                    return;
                }
                
                if (!password.equals(confirmPassword)) {
                    Toast.makeText(SignUpActivity.this, "Passwords do not match", Toast.LENGTH_SHORT).show();
                    return;
                }

                // Show a simple toast indicating progress
                Toast.makeText(SignUpActivity.this, "Creating account...", Toast.LENGTH_SHORT).show();
                btnCreateAccount.setEnabled(false);

                ApiService apiService = ApiClient.getClient().create(ApiService.class);
                SignupRequest request = new SignupRequest(name, phone, email, password);

                apiService.signup(request).enqueue(new Callback<AuthResponse>() {
                    @Override
                    public void onResponse(Call<AuthResponse> call, Response<AuthResponse> response) {
                        btnCreateAccount.setEnabled(true);
                        if (response.isSuccessful() && response.body() != null && response.body().isSuccess()) {
                            long newRowId = response.body().getData().getUser().getId();
                            
                            SharedPreferences prefs = getSharedPreferences("SymptoCarePrefs", Context.MODE_PRIVATE);
                            prefs.edit().putLong("active_user_id", newRowId)
                                 .putString("active_user_name", response.body().getData().getUser().getName())
                                 .putString("active_user_email", response.body().getData().getUser().getEmail())
                                 .apply();
                            
                            Toast.makeText(SignUpActivity.this, "Account created successfully", Toast.LENGTH_SHORT).show();
                            startActivity(new Intent(SignUpActivity.this, MainActivity.class));
                            finish();
                        } else {
                            String errorMsg = "Error creating account";
                            if (response.body() != null && response.body().getError() != null) {
                                errorMsg = response.body().getError().getMessage();
                            }
                            Toast.makeText(SignUpActivity.this, errorMsg, Toast.LENGTH_SHORT).show();
                        }
                    }

                    @Override
                    public void onFailure(Call<AuthResponse> call, Throwable t) {
                        btnCreateAccount.setEnabled(true);
                        Toast.makeText(SignUpActivity.this, "Network error: " + t.getMessage(), Toast.LENGTH_SHORT).show();
                    }
                });
            }
        });
    }
}
