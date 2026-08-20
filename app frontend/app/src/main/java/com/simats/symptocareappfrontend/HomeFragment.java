package com.simats.symptocareappfrontend;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import com.google.android.material.bottomnavigation.BottomNavigationView;

public class HomeFragment extends Fragment {

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_home, container, false);
        
        android.widget.TextView emojiGreat = view.findViewById(R.id.emojiGreat);
        android.widget.TextView emojiGood = view.findViewById(R.id.emojiGood);
        android.widget.TextView emojiOkay = view.findViewById(R.id.emojiOkay);
        android.widget.TextView emojiBad = view.findViewById(R.id.emojiBad);
        android.widget.TextView emojiAwful = view.findViewById(R.id.emojiAwful);
        
        android.view.View.OnClickListener emojiListener = v -> {
            emojiGreat.setBackgroundResource(R.drawable.bg_card_white);
            emojiGood.setBackgroundResource(R.drawable.bg_card_white);
            emojiOkay.setBackgroundResource(R.drawable.bg_card_white);
            emojiBad.setBackgroundResource(R.drawable.bg_card_white);
            emojiAwful.setBackgroundResource(R.drawable.bg_card_white);
            
            v.setBackgroundResource(R.drawable.bg_button_light_blue);
            android.widget.Toast.makeText(getContext(), "Thanks for checking in today!", android.widget.Toast.LENGTH_SHORT).show();
        };
        
        if(emojiGreat != null) emojiGreat.setOnClickListener(emojiListener);
        if(emojiGood != null) emojiGood.setOnClickListener(emojiListener);
        if(emojiOkay != null) emojiOkay.setOnClickListener(emojiListener);
        if(emojiBad != null) emojiBad.setOnClickListener(emojiListener);
        if(emojiAwful != null) emojiAwful.setOnClickListener(emojiListener);

        android.widget.ImageView ivBell = view.findViewById(R.id.ivBell);
        android.widget.ImageView ivProfile = view.findViewById(R.id.ivProfile);
        
        if (ivBell != null) {
            ivBell.setOnClickListener(v -> {
                android.widget.Toast.makeText(getContext(), "Notifications coming soon!", android.widget.Toast.LENGTH_SHORT).show();
            });
        }
        
        if (ivProfile != null) {
            ivProfile.setOnClickListener(v -> {
                android.widget.Toast.makeText(getContext(), "Profile settings coming soon!", android.widget.Toast.LENGTH_SHORT).show();
            });
        }
        
        View articleSleep = view.findViewById(R.id.articleSleep);
        View articleHeart = view.findViewById(R.id.articleHeart);
        
        if (articleSleep != null) {
            articleSleep.setOnClickListener(v -> {
                android.content.Intent browserIntent = new android.content.Intent(android.content.Intent.ACTION_VIEW, android.net.Uri.parse("https://www.sleepfoundation.org/how-sleep-works/why-do-we-need-sleep"));
                startActivity(browserIntent);
            });
        }
        
        if (articleHeart != null) {
            articleHeart.setOnClickListener(v -> {
                android.content.Intent browserIntent = new android.content.Intent(android.content.Intent.ACTION_VIEW, android.net.Uri.parse("https://www.mayoclinic.org/healthy-lifestyle/fitness/expert-answers/heart-rate/faq-20057979"));
                startActivity(browserIntent);
            });
        }
        
        View articleHydration = view.findViewById(R.id.articleHydration);
        if (articleHydration != null) {
            articleHydration.setOnClickListener(v -> {
                android.content.Intent browserIntent = new android.content.Intent(android.content.Intent.ACTION_VIEW, android.net.Uri.parse("https://www.mayoclinic.org/healthy-lifestyle/nutrition-and-healthy-eating/in-depth/water/art-20044256"));
                startActivity(browserIntent);
            });
        }
        
        View articleStress = view.findViewById(R.id.articleStress);
        if (articleStress != null) {
            articleStress.setOnClickListener(v -> {
                android.content.Intent browserIntent = new android.content.Intent(android.content.Intent.ACTION_VIEW, android.net.Uri.parse("https://www.apa.org/topics/stress/health"));
                startActivity(browserIntent);
            });
        }
        
        View articleNutrition = view.findViewById(R.id.articleNutrition);
        if (articleNutrition != null) {
            articleNutrition.setOnClickListener(v -> {
                android.content.Intent browserIntent = new android.content.Intent(android.content.Intent.ACTION_VIEW, android.net.Uri.parse("https://www.hsph.harvard.edu/nutritionsource/healthy-eating-plate/"));
                startActivity(browserIntent);
            });
        }

        return view;
    }
}
