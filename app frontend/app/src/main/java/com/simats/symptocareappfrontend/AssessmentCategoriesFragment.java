package com.simats.symptocareappfrontend;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

public class AssessmentCategoriesFragment extends Fragment {

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_assessment_categories, container, false);

        setupCategory(view, R.id.catGeneral, "General", new FeverSymptomsFragment());
        setupCategory(view, R.id.catDigestive, "Digestive", new DigestiveSymptomsFragment());
        setupCategory(view, R.id.catSkin, "Skin", new SkinAllergyFragment());
        setupCategory(view, R.id.catRespiratory, "Respiratory", new ColdCoughSymptomsFragment());
        setupCategory(view, R.id.catHeart, "Heart & Cardio", new HeartCardioSymptomsFragment());
        setupCategory(view, R.id.catJoints, "Joints", new JointSymptomsFragment());

        return view;
    }

    private void setupCategory(View root, int viewId, String category, Fragment targetFragment) {
        View catView = root.findViewById(viewId);
        if (catView != null) {
            catView.setOnClickListener(v -> {
                if (getActivity() instanceof GuidedAssessmentActivity) {
                    GuidedAssessmentActivity activity = (GuidedAssessmentActivity) getActivity();
                    activity.setSelectedCategory(category);
                    activity.loadFragment(targetFragment, true);
                }
            });
        }
    }
}
