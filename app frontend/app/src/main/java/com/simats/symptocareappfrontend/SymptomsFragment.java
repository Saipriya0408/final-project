package com.simats.symptocareappfrontend;

import android.app.AlertDialog;
import android.app.ProgressDialog;
import android.os.Bundle;
import android.text.TextUtils;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

import com.simats.symptocareappfrontend.api.ApiClient;
import com.simats.symptocareappfrontend.api.ApiService;
import com.simats.symptocareappfrontend.models.AnalysisRequest;
import com.simats.symptocareappfrontend.models.AnalysisResponse;

import java.util.ArrayList;
import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

import android.Manifest;
import android.content.Context;
import android.content.SharedPreferences;
import android.content.pm.PackageManager;
import android.location.Location;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;
import com.google.android.gms.location.FusedLocationProviderClient;
import com.google.android.gms.location.LocationServices;
import com.google.android.gms.tasks.OnSuccessListener;

public class SymptomsFragment extends Fragment {

    private boolean isTextInputMode = true;
    private List<String> selectedSymptoms = new ArrayList<>();
    private EditText etSymptoms;

    private FusedLocationProviderClient fusedLocationClient;
    private static final int LOCATION_PERMISSION_REQUEST_CODE = 1001;

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_symptoms, container, false);

        TextView tabTextInput = view.findViewById(R.id.tabTextInput);
        TextView tabSymptomIcons = view.findViewById(R.id.tabSymptomIcons);
        View layoutTextInput = view.findViewById(R.id.layoutTextInput);
        View layoutSymptomIcons = view.findViewById(R.id.layoutSymptomIcons);
        etSymptoms = view.findViewById(R.id.etSymptoms);

        android.widget.TextView chipFever = view.findViewById(R.id.chipFever);
        android.widget.TextView chipCough = view.findViewById(R.id.chipCough);
        android.widget.TextView chipHeadache = view.findViewById(R.id.chipHeadache);
        android.widget.TextView chipFatigue = view.findViewById(R.id.chipFatigue);
        
        android.view.View.OnClickListener chipListener = v -> {
            String currentText = etSymptoms.getText().toString();
            String addedText = ((android.widget.TextView)v).getText().toString();
            if (currentText.isEmpty()) {
                etSymptoms.setText(addedText);
            } else {
                etSymptoms.setText(currentText + ", " + addedText);
            }
            etSymptoms.setSelection(etSymptoms.getText().length());
        };
        
        if(chipFever != null) chipFever.setOnClickListener(chipListener);
        if(chipCough != null) chipCough.setOnClickListener(chipListener);
        if(chipHeadache != null) chipHeadache.setOnClickListener(chipListener);
        if(chipFatigue != null) chipFatigue.setOnClickListener(chipListener);

        fusedLocationClient = LocationServices.getFusedLocationProviderClient(requireActivity());

        // Initial State: Text Input active
        setTabState(tabTextInput, tabSymptomIcons, layoutTextInput, layoutSymptomIcons, true);

        tabTextInput.setOnClickListener(v -> setTabState(tabTextInput, tabSymptomIcons, layoutTextInput, layoutSymptomIcons, true));
        tabSymptomIcons.setOnClickListener(v -> setTabState(tabTextInput, tabSymptomIcons, layoutTextInput, layoutSymptomIcons, false));

        // Setup symptom icon click listeners
        setupSymptomIcon(view, R.id.symptom_fever, "fever");
        setupSymptomIcon(view, R.id.symptom_headache, "headache");
        setupSymptomIcon(view, R.id.symptom_chest_pain, "chest_pain");
        setupSymptomIcon(view, R.id.symptom_cough, "cough");
        setupSymptomIcon(view, R.id.symptom_stomach_pain, "stomach_pain");
        setupSymptomIcon(view, R.id.symptom_fatigue, "fatigue");
        setupSymptomIcon(view, R.id.symptom_eye_problem, "eye_problem");
        setupSymptomIcon(view, R.id.symptom_breathing_issue, "breathing_issue");
        setupSymptomIcon(view, R.id.symptom_ear_pain, "ear_pain");
        setupSymptomIcon(view, R.id.symptom_skin_problem, "skin_problem");

        View btnAnalyze = view.findViewById(R.id.btnAnalyze);
        View btnBack = view.findViewById(R.id.btnBack);
        View btnGuidedAssessment = view.findViewById(R.id.btnGuidedAssessment);

        if (btnGuidedAssessment != null) {
            btnGuidedAssessment.setOnClickListener(v -> {
                android.content.Intent intent = new android.content.Intent(getActivity(), GuidedAssessmentActivity.class);
                startActivity(intent);
            });
        }

        if (btnAnalyze != null) {
            btnAnalyze.setOnClickListener(v -> {
                if (checkLocationPermission()) {
                    fetchLocationAndAnalyze();
                } else {
                    requestLocationPermission();
                }
            });
        }

        if (btnBack != null) {
            btnBack.setOnClickListener(v -> navigateToHome());
        }

        return view;
    }

    private void setTabState(TextView tabText, TextView tabIcon, View layoutText, View layoutIcon, boolean isTextMode) {
        this.isTextInputMode = isTextMode;
        if (isTextMode) {
            tabText.setBackgroundResource(R.drawable.bg_toggle_active);
            tabText.setTextColor(getResources().getColor(R.color.white, null));
            tabIcon.setBackgroundResource(R.drawable.bg_toggle_inactive);
            tabIcon.setTextColor(getResources().getColor(R.color.text_desc, null));
            layoutText.setVisibility(View.VISIBLE);
            layoutIcon.setVisibility(View.GONE);
        } else {
            tabIcon.setBackgroundResource(R.drawable.bg_toggle_active);
            tabIcon.setTextColor(getResources().getColor(R.color.white, null));
            tabText.setBackgroundResource(R.drawable.bg_toggle_inactive);
            tabText.setTextColor(getResources().getColor(R.color.text_desc, null));
            layoutIcon.setVisibility(View.VISIBLE);
            layoutText.setVisibility(View.GONE);
        }
    }

    private void setupSymptomIcon(View parentView, int viewId, String symptomKey) {
        View symptomView = parentView.findViewById(viewId);
        if (symptomView == null) return;

        symptomView.setOnClickListener(v -> {
            if (selectedSymptoms.contains(symptomKey)) {
                selectedSymptoms.remove(symptomKey);
                symptomView.setBackgroundResource(R.drawable.bg_card_white);
            } else {
                selectedSymptoms.add(symptomKey);
                symptomView.setBackgroundResource(R.drawable.bg_button_light_blue);
            }
        });
    }

    private boolean checkLocationPermission() {
        return ContextCompat.checkSelfPermission(requireContext(), Manifest.permission.ACCESS_FINE_LOCATION) == PackageManager.PERMISSION_GRANTED;
    }

    private void requestLocationPermission() {
        requestPermissions(new String[]{Manifest.permission.ACCESS_FINE_LOCATION, Manifest.permission.ACCESS_COARSE_LOCATION}, LOCATION_PERMISSION_REQUEST_CODE);
    }

    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
        if (requestCode == LOCATION_PERMISSION_REQUEST_CODE) {
            if (grantResults.length > 0 && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                fetchLocationAndAnalyze();
            } else {
                Toast.makeText(getContext(), "Location permission denied. Showing results without distance sorting.", Toast.LENGTH_SHORT).show();
                performAnalysis();
            }
        }
    }

    private void fetchLocationAndAnalyze() {
        if (ActivityCompat.checkSelfPermission(requireContext(), Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
            performAnalysis();
            return;
        }
        fusedLocationClient.getLastLocation().addOnSuccessListener(requireActivity(), new OnSuccessListener<Location>() {
            @Override
            public void onSuccess(Location location) {
                if (location != null) {
                    SharedPreferences prefs = requireActivity().getSharedPreferences("AppPrefs", Context.MODE_PRIVATE);
                    prefs.edit()
                            .putFloat("user_lat", (float) location.getLatitude())
                            .putFloat("user_lng", (float) location.getLongitude())
                            .apply();
                }
                performAnalysis();
            }
        }).addOnFailureListener(e -> {
            performAnalysis();
        });
    }

    private void performAnalysis() {
        AnalysisRequest request;

        if (isTextInputMode) {
            String message = etSymptoms.getText().toString().trim();
            if (TextUtils.isEmpty(message)) {
                Toast.makeText(getContext(), "Please describe your symptoms", Toast.LENGTH_SHORT).show();
                return;
            }
            request = new AnalysisRequest(message);
        } else {
            if (selectedSymptoms.isEmpty()) {
                Toast.makeText(getContext(), "Please select at least one symptom", Toast.LENGTH_SHORT).show();
                return;
            }
            request = new AnalysisRequest(selectedSymptoms);
        }

        ProgressDialog progressDialog = new ProgressDialog(getContext());
        progressDialog.setMessage("Analyzing symptoms...");
        progressDialog.setCancelable(false);
        progressDialog.show();

        ApiService apiService = ApiClient.getClient().create(ApiService.class);
        apiService.analyzeSymptoms(request).enqueue(new Callback<AnalysisResponse>() {
            @Override
            public void onResponse(Call<AnalysisResponse> call, Response<AnalysisResponse> response) {
                progressDialog.dismiss();
                if (response.isSuccessful() && response.body() != null) {
                    if (response.body().success) {
                        saveSearchHistory(request, response.body().data);
                        showResultDialog(response.body().data);
                    } else {
                        Toast.makeText(getContext(), "Analysis failed", Toast.LENGTH_SHORT).show();
                    }
                } else {
                    Toast.makeText(getContext(), "Failed to analyze symptoms", Toast.LENGTH_SHORT).show();
                }
            }

            @Override
            public void onFailure(Call<AnalysisResponse> call, Throwable t) {
                progressDialog.dismiss();
                Log.e("API_ERROR", "Error: " + t.getMessage());
                Toast.makeText(getContext(), "Network error", Toast.LENGTH_SHORT).show();
            }
        });
    }

    private void saveSearchHistory(AnalysisRequest request, AnalysisResponse.Data prediction) {
        if (getContext() == null) return;
        
        android.content.SharedPreferences prefs = getContext().getSharedPreferences("SymptoCarePrefs", android.content.Context.MODE_PRIVATE);
        long userId = prefs.getLong("active_user_id", -1);
        
        if (userId != -1) {
            String symptomsStr = "";
            if (request.symptoms != null && !request.symptoms.isEmpty()) {
                symptomsStr = android.text.TextUtils.join(", ", request.symptoms);
            } else if (request.message != null && !request.message.isEmpty()) {
                symptomsStr = request.message;
            }
            
            String currentDate = new java.text.SimpleDateFormat("dd MMM yyyy, hh:mm a", java.util.Locale.getDefault()).format(new java.util.Date());
            
            DatabaseHelper dbHelper = new DatabaseHelper(getContext());
            android.database.sqlite.SQLiteDatabase db = dbHelper.getWritableDatabase();
            
            android.content.ContentValues values = new android.content.ContentValues();
            values.put(DatabaseHelper.COL_HIST_USER_ID, userId);
            values.put(DatabaseHelper.COL_HIST_SYMPTOMS, symptomsStr);
            values.put(DatabaseHelper.COL_HIST_PREDICTION, prediction.predictedDisease);
            values.put(DatabaseHelper.COL_HIST_TIMESTAMP, currentDate);
            
            db.insert(DatabaseHelper.TABLE_HEALTH_HISTORY, null, values);
        }
    }

    private void showResultDialog(AnalysisResponse.Data prediction) {
        if (getContext() == null) return;

        String message = "Predicted Disease: " + prediction.predictedDisease + "\n\n" +
                         "Based on your symptoms, you should consult a " + prediction.recommendedSpecialist + ".";

        new AlertDialog.Builder(getContext())
                .setTitle("Analysis Result")
                .setMessage(message)
                .setPositiveButton("Find Nearby " + prediction.recommendedSpecialist + "s", (dialog, which) -> {
                    if (getActivity() != null) {
                        getActivity().getSharedPreferences("AppPrefs", android.content.Context.MODE_PRIVATE)
                                .edit()
                                .putString("filter_specialist", prediction.recommendedSpecialist)
                                .apply();
                    }
                    navigateToDoctors();
                })
                .setNegativeButton("Close", null)
                .show();
    }

    private void navigateToHome() {
        if (getActivity() != null) {
            com.google.android.material.bottomnavigation.BottomNavigationView bottomNav = getActivity().findViewById(R.id.bottom_navigation);
            if (bottomNav != null) {
                bottomNav.setSelectedItemId(R.id.nav_home);
            }
        }
    }

    private void navigateToDoctors() {
        if (getActivity() != null) {
            com.google.android.material.bottomnavigation.BottomNavigationView bottomNav = getActivity().findViewById(R.id.bottom_navigation);
            if (bottomNav != null) {
                bottomNav.setSelectedItemId(R.id.nav_doctors);
            }
        }
    }
}
