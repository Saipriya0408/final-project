package com.simats.symptocareappfrontend;

import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

public class AssessmentLoadingFragment extends Fragment {

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_assessment_loading, container, false);

        // Simulate network/AI processing delay
        new Handler(Looper.getMainLooper()).postDelayed(() -> {
            if (isAdded() && getActivity() instanceof GuidedAssessmentActivity) {
                ((GuidedAssessmentActivity) getActivity()).loadFragment(new AssessmentResultFragment(), false);
            }
        }, 2000); // 2 seconds

        return view;
    }
}
