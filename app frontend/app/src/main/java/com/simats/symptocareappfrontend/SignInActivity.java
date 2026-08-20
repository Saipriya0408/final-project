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
import com.simats.symptocareappfrontend.models.AuthRequest;
import com.simats.symptocareappfrontend.models.AuthResponse;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class SignInActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_signin);

        View tvSignUpLink = findViewById(R.id.tvSignUpLink);
        View btnLogin = findViewById(R.id.btnLogin);
        View btnGuest = findViewById(R.id.btnGuest);
        EditText etEmail = findViewById(R.id.etEmail);
        
        tvSignUpLink.setOnClickListener(v -> {
            startActivity(new Intent(SignInActivity.this, SignUpActivity.class));
            finish();
        });

        View.OnClickListener goToMain = v -> {
            if (etEmail != null && etEmail.getText() != null) {
                String identifier = etEmail.getText().toString().trim();
                EditText etPassword = findViewById(R.id.etPassword);
                String password = etPassword != null ? etPassword.getText().toString() : "";
                
                if (identifier.isEmpty() || password.isEmpty()) {
                    Toast.makeText(SignInActivity.this, "Please fill in all fields", Toast.LENGTH_SHORT).show();
                    return;
                }
                
                Toast.makeText(SignInActivity.this, "Signing in...", Toast.LENGTH_SHORT).show();
                btnLogin.setEnabled(false);

                ApiService apiService = ApiClient.getClient().create(ApiService.class);
                AuthRequest request = new AuthRequest(identifier, password);

                apiService.login(request).enqueue(new Callback<AuthResponse>() {
                    @Override
                    public void onResponse(Call<AuthResponse> call, Response<AuthResponse> response) {
                        btnLogin.setEnabled(true);
                        if (response.isSuccessful() && response.body() != null && response.body().isSuccess()) {
                            long userId = response.body().getData().getUser().getId();
                            
                            SharedPreferences prefs = getSharedPreferences("SymptoCarePrefs", Context.MODE_PRIVATE);
                            prefs.edit().putLong("active_user_id", userId)
                                 .putString("active_user_name", response.body().getData().getUser().getName())
                                 .putString("active_user_email", response.body().getData().getUser().getEmail())
                                 .apply();
                            
                            startActivity(new Intent(SignInActivity.this, MainActivity.class));
                            finish();
                        } else {
                            String errorMsg = "Invalid credentials";
                            if (response.body() != null && response.body().getError() != null) {
                                errorMsg = response.body().getError().getMessage();
                            }
                            Toast.makeText(SignInActivity.this, errorMsg, Toast.LENGTH_SHORT).show();
                        }
                    }

                    @Override
                    public void onFailure(Call<AuthResponse> call, Throwable t) {
                        btnLogin.setEnabled(true);
                        Toast.makeText(SignInActivity.this, "Network error: " + t.getMessage(), Toast.LENGTH_SHORT).show();
                    }
                });
            }
        };

        btnLogin.setOnClickListener(goToMain);
        
        btnGuest.setOnClickListener(v -> {
             startActivity(new Intent(SignInActivity.this, MainActivity.class));
             finish();
        });
    }
}
