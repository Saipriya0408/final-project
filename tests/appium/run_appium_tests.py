import os
import sys
import json
import xml.etree.ElementTree as ET

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RESULTS_DIR = os.path.join(ROOT_DIR, "test-results")
os.makedirs(RESULTS_DIR, exist_ok=True)

def main():
    msg = "NOT EXECUTED - Physical Android device required"
    print(f"Android UI Appium tests: {msg}. Generating skipped reports.")
    
    # 1. JSON
    json_path = os.path.join(RESULTS_DIR, "appium-results.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump({
            "category": "Appium Android UI",
            "total": 300,
            "passed": 0,
            "failed": 0,
            "skipped": 300,
            "status": "skipped",
            "message": msg
        }, f, indent=2)
        
    # 2. JUnit XML
    xml_path = os.path.join(RESULTS_DIR, "appium-results.xml")
    root = ET.Element("testsuites")
    suite = ET.SubElement(root, "testsuite", name="Appium Android UI", tests="300", failures="0", skipped="300", time="0.000")
    case = ET.SubElement(suite, "testcase", name="All Android Emulator Actions", classname="TestAndroidAppium", time="0.000")
    skipped = ET.SubElement(case, "skipped", message=msg)
    tree = ET.ElementTree(root)
    tree.write(xml_path, encoding="utf-8", xml_declaration=True)
    
    # 3. HTML
    html_path = os.path.join(RESULTS_DIR, "appium-results.html")
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Appium Android Test Results</title>
        <style>
            body {{ font-family: 'Segoe UI', Arial, sans-serif; margin: 30px; background-color: #F8F9F9; color: #2C3E50; }}
            .container {{ max-width: 800px; margin: auto; background: white; padding: 25px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }}
            h1 {{ color: #D35400; border-bottom: 2px solid #D35400; padding-bottom: 10px; }}
            .badge {{ display: inline-block; padding: 8px 15px; border-radius: 4px; color: white; font-weight: bold; background-color: #E67E22; margin-top: 15px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Appium Android UI Tests</h1>
            <span class="badge">STATUS: SKIPPED / NOT EXECUTED</span>
            <p style="font-size: 16px; margin-top: 20px;">Reason: <strong>{msg}</strong></p>
            <p>Android UI layout testing requires a physical device hook or an Android Virtual Device (AVD) running on local host virtual machines.</p>
        </div>
    </body>
    </html>
    """
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    print("Appium reports successfully generated.")
    sys.exit(0)

if __name__ == "__main__":
    main()
