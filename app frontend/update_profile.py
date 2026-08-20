import re

signin_path = r"C:\Users\srike\Desktop\WORK\CODE CURRENT\projects\Sympto Care\app frontend\app\src\main\res\layout\activity_signin.xml"
with open(signin_path, "r", encoding="utf-8") as f:
    xml = f.read()
xml = xml.replace('<EditText\n                    android:layout_width="match_parent"\n                    android:layout_height="match_parent"\n                    android:layout_marginStart="12dp"\n                    android:background="@null"\n                    android:hint="@string/hint_email_phone"',
                  '<EditText\n                    android:id="@+id/etEmail"\n                    android:layout_width="match_parent"\n                    android:layout_height="match_parent"\n                    android:layout_marginStart="12dp"\n                    android:background="@null"\n                    android:hint="@string/hint_email_phone"')
with open(signin_path, "w", encoding="utf-8") as f:
    f.write(xml)

signup_path = r"C:\Users\srike\Desktop\WORK\CODE CURRENT\projects\Sympto Care\app frontend\app\src\main\res\layout\activity_signup.xml"
with open(signup_path, "r", encoding="utf-8") as f:
    xml = f.read()
xml = xml.replace('<EditText\n                    android:layout_width="match_parent"\n                    android:layout_height="match_parent"\n                    android:layout_marginStart="12dp"\n                    android:background="@null"\n                    android:hint="@string/hint_full_name"',
                  '<EditText\n                    android:id="@+id/etName"\n                    android:layout_width="match_parent"\n                    android:layout_height="match_parent"\n                    android:layout_marginStart="12dp"\n                    android:background="@null"\n                    android:hint="@string/hint_full_name"')
xml = xml.replace('<EditText\n                    android:layout_width="match_parent"\n                    android:layout_height="match_parent"\n                    android:layout_marginStart="12dp"\n                    android:background="@null"\n                    android:hint="@string/hint_email"',
                  '<EditText\n                    android:id="@+id/etEmail"\n                    android:layout_width="match_parent"\n                    android:layout_height="match_parent"\n                    android:layout_marginStart="12dp"\n                    android:background="@null"\n                    android:hint="@string/hint_email"')
with open(signup_path, "w", encoding="utf-8") as f:
    f.write(xml)

signin_java = r"C:\Users\srike\Desktop\WORK\CODE CURRENT\projects\Sympto Care\app frontend\app\src\main\java\com\simats\symptocareappfrontend\SignInActivity.java"
with open(signin_java, "r", encoding="utf-8") as f:
    code = f.read()
code = code.replace("import android.view.View;", "import android.view.View;\nimport android.widget.EditText;\nimport android.content.SharedPreferences;\nimport android.content.Context;")
code = code.replace("View btnGuest = findViewById(R.id.btnGuest);", "View btnGuest = findViewById(R.id.btnGuest);\n        EditText etEmail = findViewById(R.id.etEmail);")
code = code.replace("startActivity(new Intent(SignInActivity.this, MainActivity.class));",
"""if (etEmail != null && etEmail.getText() != null) {
                String email = etEmail.getText().toString();
                String name = email.split("@")[0]; // Use first part of email as name
                SharedPreferences prefs = getSharedPreferences("SymptoCarePrefs", Context.MODE_PRIVATE);
                prefs.edit().putString("userName", name).putString("userEmail", email).apply();
            }
            startActivity(new Intent(SignInActivity.this, MainActivity.class));""")
with open(signin_java, "w", encoding="utf-8") as f:
    f.write(code)

signup_java = r"C:\Users\srike\Desktop\WORK\CODE CURRENT\projects\Sympto Care\app frontend\app\src\main\java\com\simats\symptocareappfrontend\SignUpActivity.java"
with open(signup_java, "r", encoding="utf-8") as f:
    code = f.read()
code = code.replace("import android.view.View;", "import android.view.View;\nimport android.widget.EditText;\nimport android.content.SharedPreferences;\nimport android.content.Context;")
code = code.replace("View btnCreateAccount = findViewById(R.id.btnCreateAccount);", "View btnCreateAccount = findViewById(R.id.btnCreateAccount);\n        EditText etName = findViewById(R.id.etName);\n        EditText etEmail = findViewById(R.id.etEmail);")
code = code.replace("startActivity(new Intent(SignUpActivity.this, MainActivity.class));",
"""if (etName != null && etEmail != null) {
                SharedPreferences prefs = getSharedPreferences("SymptoCarePrefs", Context.MODE_PRIVATE);
                prefs.edit().putString("userName", etName.getText().toString()).putString("userEmail", etEmail.getText().toString()).apply();
            }
            startActivity(new Intent(SignUpActivity.this, MainActivity.class));""")
with open(signup_java, "w", encoding="utf-8") as f:
    f.write(code)

profile_java = r"C:\Users\srike\Desktop\WORK\CODE CURRENT\projects\Sympto Care\app frontend\app\src\main\java\com\simats\symptocareappfrontend\ProfileFragment.java"
with open(profile_java, "r", encoding="utf-8") as f:
    code = f.read()
code = code.replace("import android.view.ViewGroup;", "import android.view.ViewGroup;\nimport android.widget.TextView;\nimport android.content.SharedPreferences;\nimport android.content.Context;")
code = code.replace("View btnLogout = view.findViewById(R.id.btnLogout);",
"""
        TextView tvName = view.findViewById(R.id.tvProfileName);
        TextView tvEmail = view.findViewById(R.id.tvProfileEmail);
        TextView tvInitials = view.findViewById(R.id.tvProfileInitials);
        
        SharedPreferences prefs = getContext().getSharedPreferences("SymptoCarePrefs", Context.MODE_PRIVATE);
        String name = prefs.getString("userName", "John Doe");
        String email = prefs.getString("userEmail", "john.doe@email.com");
        
        if (tvName != null) tvName.setText(name);
        if (tvEmail != null) tvEmail.setText(email);
        
        if (tvInitials != null && name != null && !name.isEmpty()) {
            String[] parts = name.split(" ");
            StringBuilder init = new StringBuilder();
            for (String p : parts) {
                if (p.length() > 0) init.append(p.charAt(0));
            }
            tvInitials.setText(init.toString().toUpperCase());
        }

        View btnLogout = view.findViewById(R.id.btnLogout);
""")
with open(profile_java, "w", encoding="utf-8") as f:
    f.write(code)

print("Updated Profile info extraction successfully")
