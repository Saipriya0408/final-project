package com.simats.symptocareappfrontend;

import android.content.Intent;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

public class AssessmentResultFragment extends Fragment {

    // Maps each category to its prediction data
    private static class PredictionData {
        String conditions;
        String recommendation;
        String specialistLabel;
        String specialistDesc;
        String filterSpecialty; // what to send to the backend API

        PredictionData(String conditions, String recommendation, String specialistLabel, String specialistDesc, String filterSpecialty) {
            this.conditions = conditions;
            this.recommendation = recommendation;
            this.specialistLabel = specialistLabel;
            this.specialistDesc = specialistDesc;
            this.filterSpecialty = filterSpecialty;
        }
    }

    private PredictionData getPredictionForCategory(String category) {
        if (category == null) category = "General";

        switch (category) {
            case "General":
                return new PredictionData(
                    "1. Viral Fever (High Match)\n2. Common Cold (Medium Match)\n3. Influenza (Low Match)",
                    "Rest, stay hydrated, and monitor your temperature. If fever persists beyond 48 hours or exceeds 103°F, consult a physician immediately.",
                    "Primary Care Provider",
                    "Find general physicians near you",
                    "Primary Care Provider"
                );
            case "Digestive":
                return new PredictionData(
                    "1. Gastroenteritis (High Match)\n2. Acid Reflux / GERD (Medium Match)\n3. Food Intolerance (Low Match)",
                    "Avoid spicy and oily foods. Stay hydrated with ORS. If symptoms include blood in stool or severe cramping, seek immediate medical help.",
                    "Gastroenterologist",
                    "Find digestive specialists near you",
                    "Gastroenterologist"
                );
            case "Skin":
                return new PredictionData(
                    "1. Contact Dermatitis (High Match)\n2. Eczema (Medium Match)\n3. Fungal Infection (Low Match)",
                    "Avoid scratching the affected area. Apply a mild moisturizer. If rash spreads or causes blistering, consult a dermatologist.",
                    "Dermatologist",
                    "Find skin specialists near you",
                    "Dermatologist"
                );
            case "Respiratory":
                return new PredictionData(
                    "1. Upper Respiratory Infection (High Match)\n2. Bronchitis (Medium Match)\n3. Allergic Rhinitis (Low Match)",
                    "Use steam inhalation and stay in a well-ventilated room. Avoid cold drinks. If you experience difficulty breathing, seek emergency care.",
                    "Pulmonologist",
                    "Find respiratory specialists near you",
                    "Pulmonologist"
                );
            case "Heart & Cardio":
                return new PredictionData(
                    "1. Hypertension (High Match)\n2. Tachycardia (Medium Match)\n3. Angina (Low Match)",
                    "Monitor your blood pressure regularly. Reduce salt intake and avoid strenuous activity until evaluated by a cardiologist.",
                    "Cardiologist",
                    "Find heart specialists near you",
                    "Cardiologist"
                );
            case "Joints":
                return new PredictionData(
                    "1. Osteoarthritis (High Match)\n2. Muscle Strain (Medium Match)\n3. Tendinitis (Low Match)",
                    "Apply ice packs to the affected joint. Avoid heavy lifting. If swelling persists or joint locks, consult an orthopedic specialist.",
                    "Orthopedic",
                    "Find orthopedic specialists near you",
                    "Orthopedic"
                );
            default:
                return new PredictionData(
                    "1. General Discomfort (High Match)\n2. Stress-Related Symptoms (Medium Match)",
                    "Rest well and stay hydrated. If symptoms persist, consult a general physician.",
                    "Primary Care Provider",
                    "Find doctors near you",
                    "Primary Care Provider"
                );
        }
    }

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_assessment_result, container, false);

        // Get the selected category from the parent activity
        String category = "General";
        if (getActivity() instanceof GuidedAssessmentActivity) {
            category = ((GuidedAssessmentActivity) getActivity()).getSelectedCategory();
        }
        final PredictionData prediction = getPredictionForCategory(category);

        // Populate the UI dynamically
        TextView tvConditions = view.findViewById(R.id.tvConditions);
        TextView tvRecommendation = view.findViewById(R.id.tvRecommendation);
        TextView tvSpecialistName = view.findViewById(R.id.tvSpecialistName);
        TextView tvSpecialistDesc = view.findViewById(R.id.tvSpecialistDesc);

        if (tvConditions != null) tvConditions.setText(prediction.conditions);
        if (tvRecommendation != null) tvRecommendation.setText(prediction.recommendation);
        if (tvSpecialistName != null) tvSpecialistName.setText(prediction.specialistLabel);
        if (tvSpecialistDesc != null) tvSpecialistDesc.setText(prediction.specialistDesc);

        // "Return to Home" button
        View btnDone = view.findViewById(R.id.btnDone);
        if (btnDone != null) {
            btnDone.setOnClickListener(v -> {
                if (getActivity() != null) {
                    getActivity().finish();
                }
            });
        }

        // Specialist card + Find Doctors button — navigate to Doctors tab with correct filter
        View cardSpecialist = view.findViewById(R.id.cardSpecialist);
        View btnBook = view.findViewById(R.id.btnBookSpecialist);

        View.OnClickListener openDoctors = v -> {
            Intent intent = new Intent(getActivity(), MainActivity.class);
            intent.putExtra("openTab", R.id.nav_doctors);
            intent.putExtra("filterSpecialty", prediction.filterSpecialty);
            intent.setFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP | Intent.FLAG_ACTIVITY_SINGLE_TOP);
            startActivity(intent);
            if (getActivity() != null) getActivity().finish();
        };

        if (cardSpecialist != null) cardSpecialist.setOnClickListener(openDoctors);
        if (btnBook != null) btnBook.setOnClickListener(openDoctors);

        return view;
    }
}
