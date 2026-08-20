import re

def fix_constraints(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the RecyclerView tag and remove the bottom constraint
    pattern = r'<androidx\.recyclerview\.widget\.RecyclerView.*?</androidx\.constraintlayout\.widget\.ConstraintLayout>'
    
    # We can just string replace the exact line
    content = content.replace('app:layout_constraintBottom_toBottomOf="parent"\n', '')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

fix_constraints(r'C:\Users\srike\Desktop\WORK\CODE CURRENT\projects\Sympto Care\app frontend\app\src\main\res\layout\fragment_doctors.xml')
fix_constraints(r'C:\Users\srike\Desktop\WORK\CODE CURRENT\projects\Sympto Care\app frontend\app\src\main\res\layout\fragment_hospitals.xml')
print("Removed bottom constraints")
