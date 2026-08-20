import re

file_path = r"C:\Users\srike\Desktop\WORK\CODE CURRENT\projects\Sympto Care\app frontend\app\src\main\res\layout\fragment_symptoms.xml"

with open(file_path, "r", encoding="utf-8") as f:
    xml_str = f.read()

# Make sure all are properly formatted. Let's just strip out all `android:id="@+id/symptom_.*"` first
xml_str = re.sub(r'\s*android:id="@+id/symptom_[^"]+"', '', xml_str)

def add_ids(match):
    block = match.group(0)
    str_match = re.search(r'android:text="@string/symp_([^"]+)"', block)
    if str_match:
        symp_name = str_match.group(1)
        # Add id right after LinearLayout
        block = block.replace('<LinearLayout', f'<LinearLayout\n                        android:id="@+id/symptom_{symp_name}"', 1)
    return block

# Find all <LinearLayout> blocks inside GridLayout
new_xml_str = re.sub(r'<LinearLayout[^>]*>[\s\S]*?android:text="@string/symp_[^"]+"[\s\S]*?</LinearLayout>', add_ids, xml_str)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_xml_str)
print("Updated XML IDs.")
