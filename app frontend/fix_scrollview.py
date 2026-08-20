import re

def fix_xml(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Change ScrollView to NestedScrollView
    content = content.replace('<ScrollView', '<androidx.core.widget.NestedScrollView')
    content = content.replace('</ScrollView>', '</androidx.core.widget.NestedScrollView>')

    # Add nestedScrollingEnabled="false" to RecyclerView if not present
    if 'android:nestedScrollingEnabled="false"' not in content:
        content = content.replace('<androidx.recyclerview.widget.RecyclerView', 
                                  '<androidx.recyclerview.widget.RecyclerView\n            android:nestedScrollingEnabled="false"')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

fix_xml(r'C:\Users\srike\Desktop\WORK\CODE CURRENT\projects\Sympto Care\app frontend\app\src\main\res\layout\fragment_doctors.xml')
fix_xml(r'C:\Users\srike\Desktop\WORK\CODE CURRENT\projects\Sympto Care\app frontend\app\src\main\res\layout\fragment_hospitals.xml')
print("Fixed ScrollViews")
