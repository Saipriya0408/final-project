package com.simats.symptocareappfrontend;

import android.net.Uri;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;
import androidx.activity.result.ActivityResultLauncher;
import androidx.activity.result.contract.ActivityResultContracts;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.core.content.ContextCompat;
import androidx.fragment.app.Fragment;

public class SkinAllergyFragment extends Fragment {

    private ImageView ivPhoto;

    private final ActivityResultLauncher<String> mGetContent = registerForActivityResult(
            new ActivityResultContracts.GetContent(),
            uri -> {
                if (uri != null && ivPhoto != null) {
                    ivPhoto.setImageURI(uri);
                }
            });

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_skin_allergy_symptoms, container, false);

        ivPhoto = view.findViewById(R.id.ivPhoto);

        View btnUpload = view.findViewById(R.id.btnUpload);
        if (btnUpload != null) {
            btnUpload.setOnClickListener(v -> {
                mGetContent.launch("image/*");
            });
        }

        // Setup toggleable symptoms
        setupToggle(view, R.id.sympRedness);
        setupToggle(view, R.id.sympItching);
        setupToggle(view, R.id.sympRash);
        setupToggle(view, R.id.sympSwelling);
        setupToggle(view, R.id.sympDrySkin);

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
            tv.setTag(false); // Initially unselected
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
