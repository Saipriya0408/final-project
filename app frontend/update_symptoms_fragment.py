java_code = """package com.simats.symptocareappfrontend;

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

public class SymptomsFragment extends Fragment {

    private boolean isTextInputMode = true;
    private List<String> selectedSymptoms = new ArrayList<>();
    private EditText etSymptoms;

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_symptoms, container, false);

        TextView tabTextInput = view.findViewById(R.id.tabTextInput);
        TextView tabSymptomIcons = view.findViewById(R.id.tabSymptomIcons);
        View layoutTextInput = view.findViewById(R.id.layoutTextInput);
        View layoutSymptomIcons = view.findViewById(R.id.layoutSymptomIcons);
        etSymptoms = view.findViewById(R.id.etSymptoms);

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

        if (btnAnalyze != null) {
            btnAnalyze.setOnClickListener(v -> performAnalysis());
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
                    if ("success".equals(response.body().status)) {
                        showResultDialog(response.body().data.prediction);
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

    private void showResultDialog(AnalysisResponse.Prediction prediction) {
        if (getContext() == null) return;

        String precautions = "";
        if (prediction.precautions != null) {
            for (int i = 0; i < prediction.precautions.size(); i++) {
                precautions += "• " + prediction.precautions.get(i) + "\\n";
            }
        }

        String message = "Predicted Disease: " + prediction.disease + "\\n\\n" +
                         "Severity: " + prediction.severity + "\\n\\n" +
                         "Description:\\n" + prediction.description + "\\n\\n" +
                         "Precautions:\\n" + precautions + "\\n" +
                         "Recommended Specialist: " + prediction.specialist;

        new AlertDialog.Builder(getContext())
                .setTitle("Analysis Result")
                .setMessage(message)
                .setPositiveButton("Find Specialist", (dialog, which) -> {
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
"""

with open(r"C:\Users\srike\Desktop\WORK\CODE CURRENT\projects\Sympto Care\app frontend\app\src\main\java\com\simats\symptocareappfrontend\SymptomsFragment.java", "w", encoding="utf-8") as f:
    f.write(java_code)
print("Updated SymptomsFragment")
