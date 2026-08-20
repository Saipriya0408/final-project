package com.simats.symptocareappfrontend;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

public class HeadacheSymptomsFragment extends Fragment {

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_headache_symptoms, container, false);

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
}
