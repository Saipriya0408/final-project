package com.simats.symptocareappfrontend;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.core.content.ContextCompat;
import androidx.fragment.app.Fragment;

public class HeartCardioSymptomsFragment extends Fragment {

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_heart_cardio_symptoms, container, false);

        setupToggle(view, R.id.sympChestPain);
        setupToggle(view, R.id.sympPalpitations);
        setupToggle(view, R.id.sympShortBreath);
        setupToggle(view, R.id.sympDizziness);
        setupToggle(view, R.id.sympFatigue);

        View btnAnalyze = view.findViewById(R.id.btnAnalyze);
        if (btnAnalyze != null) {
            btnAnalyze.setOnClickListener(v -> {
                if (getActivity() instanceof GuidedAssessmentActivity) {
                    ((GuidedAssessmentActivity) getActivity()).loadFragment(new AssessmentLoadingFragment(), true);
                }
            });
        }

        return view;
    }

    private void setupToggle(View root, int viewId) {
        TextView tv = root.findViewById(viewId);
        if (tv != null) {
            tv.setTag(false);
            tv.setOnClickListener(v -> {
                boolean isSelected = (Boolean) tv.getTag();
                isSelected = !isSelected;
                tv.setTag(isSelected);
                
                if (isSelected) {
                    tv.setBackgroundResource(R.drawable.bg_pill_blue);
                    tv.setTextColor(ContextCompat.getColor(requireContext(), R.color.white));
                } else {
                    tv.setBackgroundResource(R.drawable.bg_pill_outline);
                    tv.setTextColor(ContextCompat.getColor(requireContext(), R.color.text_desc));
                }
            });
        }
    }
}
