import re

# Fix DoctorResponse
dr_resp = r"C:\Users\srike\Desktop\WORK\CODE CURRENT\projects\Sympto Care\app frontend\app\src\main\java\com\simats\symptocareappfrontend\models\DoctorResponse.java"
with open(dr_resp, "r", encoding="utf-8") as f:
    code = f.read()
code = code.replace("public String status;", "public boolean success;")
with open(dr_resp, "w", encoding="utf-8") as f:
    f.write(code)

# Fix HospitalResponse
h_resp = r"C:\Users\srike\Desktop\WORK\CODE CURRENT\projects\Sympto Care\app frontend\app\src\main\java\com\simats\symptocareappfrontend\models\HospitalResponse.java"
with open(h_resp, "r", encoding="utf-8") as f:
    code = f.read()
code = code.replace("public String status;", "public boolean success;")
with open(h_resp, "w", encoding="utf-8") as f:
    f.write(code)

# Fix DoctorsFragment
dr_frag = r"C:\Users\srike\Desktop\WORK\CODE CURRENT\projects\Sympto Care\app frontend\app\src\main\java\com\simats\symptocareappfrontend\DoctorsFragment.java"
with open(dr_frag, "r", encoding="utf-8") as f:
    code = f.read()
code = code.replace('if ("success".equals(response.body().status))', 'if (response.body().success)')
with open(dr_frag, "w", encoding="utf-8") as f:
    f.write(code)

# Fix HospitalsFragment
h_frag = r"C:\Users\srike\Desktop\WORK\CODE CURRENT\projects\Sympto Care\app frontend\app\src\main\java\com\simats\symptocareappfrontend\HospitalsFragment.java"
with open(h_frag, "r", encoding="utf-8") as f:
    code = f.read()
code = code.replace('if ("success".equals(response.body().status))', 'if (response.body().success)')
with open(h_frag, "w", encoding="utf-8") as f:
    f.write(code)

print("Fixed responses!")
