import os
import sys
import subprocess
import time
import socket
import unittest
import io

# Reconfigure stdout/stderr to use UTF-8 (resolves Windows character map errors)
try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except AttributeError:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Ensure the root of the project is in path
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

# Import test suites dynamically
from tests.api.test_backend_api import TestBackendAPI
from tests.security.test_vulnerability import TestVulnerabilityAPI
from tests.selenium.test_web_ui import TestWebUI, SELENIUM_INSTALLED, is_chrome_available
from tests.appium.test_android_app import TestAndroidAppium, APPIUM_INSTALLED, is_appium_server_running
from tests.performance.test_load import run_load_test

def get_python_executable():
    # Resolve venv python path if possible, fallback to sys.executable
    if os.name == 'nt':
        venv_python = os.path.join(ROOT_DIR, "backend", "venv", "Scripts", "python.exe")
    else:
        venv_python = os.path.join(ROOT_DIR, "backend", "venv", "bin", "python")
        
    if os.path.exists(venv_python):
        return venv_python
    return sys.executable

def start_backend():
    python_exe = get_python_executable()
    app_py = os.path.join(ROOT_DIR, "backend", "app.py")
    print(f"Starting Flask backend server using: {python_exe} {app_py}")
    
    # Run the server in a background process
    proc = subprocess.Popen(
        [python_exe, app_py],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=os.path.join(ROOT_DIR, "backend")
    )
    return proc

def wait_for_server():
    print("Waiting for Flask server to start on port 5000...")
    for i in range(15):
        try:
            with socket.create_connection(("127.0.0.1", 5000), timeout=1):
                print("Flask server successfully started and is listening on port 5000!")
                return True
        except OSError:
            time.sleep(1)
    return False

def main():
    server_process = None
    started_server = False
    
    # 1. Start backend server if not running
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        res = sock.connect_ex(("127.0.0.1", 5000))
        sock.close()
        
        if res != 0:
            server_process = start_backend()
            started_server = True
            if not wait_for_server():
                print("Error: Flask backend server failed to start within timeout.")
                if server_process:
                    server_process.terminate()
                sys.exit(1)
        else:
            print("Flask backend server is already running on port 5000.")
    except Exception as e:
        print(f"Error checking/starting backend server: {e}")
        sys.exit(1)
        
    # 2. Setup Unittest Suite
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestBackendAPI))
    suite.addTest(unittest.makeSuite(TestVulnerabilityAPI))
    suite.addTest(unittest.makeSuite(TestWebUI))
    suite.addTest(unittest.makeSuite(TestAndroidAppium))
    
    # Run tests
    print("\n=======================================================")
    print("  Running SymptoCare Functional, E2E & Security Tests  ")
    print("=======================================================\n")
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # 3. Run Performance Load Test
    perf_metrics = None
    if started_server or res == 0:
        perf_metrics = run_load_test("/health", concurrency=5, total_requests=25)
        
    # 4. Stop Backend Server if we started it
    if started_server and server_process:
        print("Stopping Flask backend server...")
        server_process.terminate()
        try:
            server_process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            server_process.kill()
        print("Flask backend server stopped.")
        
    # 5. Compile and print final actual CI/local results summary
    print("\n" + "="*60)
    print("                CI TEST EXECUTION RESULTS               ")
    print("="*60)
    
    # Determine Selenium and Appium statuses based on skips
    selenium_status = "PASSED"
    selenium_note = f"{len([t for t in result.failures + result.errors if 'TestWebUI' in str(t[0])])} failures"
    
    appium_status = "PASSED"
    appium_note = f"{len([t for t in result.failures + result.errors if 'TestAndroidAppium' in str(t[0])])} failures"
    
    # If skipped because of environment
    selenium_skipped = not (SELENIUM_INSTALLED and is_chrome_available())
    appium_skipped = not (APPIUM_INSTALLED and is_appium_server_running())
    
    if selenium_skipped:
        selenium_status = "SKIPPED"
        selenium_note = "Not executed - environment dependency unavailable (Chrome/Selenium missing)"
    elif len([t for t in result.failures + result.errors if "TestWebUI" in str(t[0])]) > 0:
        selenium_status = "FAILED"
        
    if appium_skipped:
        appium_status = "SKIPPED"
        appium_note = "Not executed - environment dependency unavailable (Emulator/Appium missing)"
    elif len([t for t in result.failures + result.errors if "TestAndroidAppium" in str(t[0])]) > 0:
        appium_status = "FAILED"
        
    api_failed_count = len([t for t in result.failures + result.errors if "TestBackendAPI" in str(t[0])])
    api_status = "PASSED" if api_failed_count == 0 else "FAILED"
    api_note = "All integration API endpoints verified successfully" if api_status == "PASSED" else f"{api_failed_count} tests failed"
    
    security_failed_count = len([t for t in result.failures + result.errors if "TestVulnerabilityAPI" in str(t[0])])
    security_status = "PASSED" if security_failed_count == 0 else "FAILED"
    security_note = "All SQLi/XSS/Auth checks passed safely" if security_status == "PASSED" else f"{security_failed_count} tests failed"
    
    perf_status = "PASSED" if perf_metrics and "PASSED" in perf_metrics.get("Status", "") else "FAILED"
    if not perf_metrics:
        perf_status = "SKIPPED"
        perf_note = "Not executed - Server unavailable"
    else:
        perf_note = f"Latency: {perf_metrics['Average Latency']} | Throughput: {perf_metrics['Throughput (Req/Sec)']}"
        
    print(f"API Integration     : {api_status} ({api_note})")
    print(f"Security / Vulnerability : {security_status} ({security_note})")
    print(f"Performance / Load   : {perf_status} ({perf_note})")
    print(f"Selenium E2E Web UI : {selenium_status} ({selenium_note})")
    print(f"Appium Android App  : {appium_status} ({appium_note})")
    print("="*60 + "\n")
    
    # 6. Generate action summary log file for GHA injection
    ci_summary_path = os.path.join(ROOT_DIR, "ci_test_summary.md")
    with open(ci_summary_path, "w", encoding="utf-8") as f:
        f.write(f"""
## ⚙️ Actual CI Test Suite Execution Details
| Test Category | Status | Details |
| :--- | :--- | :--- |
| **API Integration** | {"🟢 PASSED" if api_status == "PASSED" else "🔴 FAILED"} | {api_note} |
| **Security / Vulnerability** | {"🟢 PASSED" if security_status == "PASSED" else "🔴 FAILED"} | {security_note} |
| **Performance / Load** | {"🟢 PASSED" if perf_status == "PASSED" else "🟡 SKIPPED" if perf_status == "SKIPPED" else "🔴 FAILED"} | {perf_note} |
| **Selenium E2E Web UI** | {"🟢 PASSED" if selenium_status == "PASSED" else "🟡 SKIPPED" if selenium_status == "SKIPPED" else "🔴 FAILED"} | {selenium_note} |
| **Appium Android App** | {"🟢 PASSED" if appium_status == "PASSED" else "🟡 SKIPPED" if appium_status == "SKIPPED" else "🔴 FAILED"} | {appium_note} |
""")
    
    # If API or Security tests failed, exit with non-zero code to fail CI build
    if api_status == "FAILED" or security_status == "FAILED":
        sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    main()
