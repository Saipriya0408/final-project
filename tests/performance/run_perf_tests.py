import os
import sys
import time
import socket
import json
import subprocess

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT_DIR)

RESULTS_DIR = os.path.join(ROOT_DIR, "test-results")
os.makedirs(RESULTS_DIR, exist_ok=True)

# Helper to start/stop backend
def get_python_executable():
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
    proc = subprocess.Popen(
        [python_exe, app_py],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        cwd=os.path.join(ROOT_DIR, "backend")
    )
    return proc

def wait_for_server():
    for _ in range(15):
        try:
            with socket.create_connection(("127.0.0.1", 5000), timeout=1):
                return True
        except Exception:
            time.sleep(1)
    return False

def generate_reports(metrics):
    # 1. JSON
    json_path = os.path.join(RESULTS_DIR, "performance-results.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump({
            "category": "Load & Performance",
            "metrics": metrics
        }, f, indent=2)
        
    # 2. HTML
    html_path = os.path.join(RESULTS_DIR, "performance-results.html")
    status_color = "#117864" if metrics["status"] == "PASSED" else "#7B241C"
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>SymptoCare Performance Test Results</title>
        <style>
            body {{ font-family: 'Segoe UI', Arial, sans-serif; margin: 30px; background-color: #F8F9F9; color: #2C3E50; }}
            .container {{ max-width: 800px; margin: auto; background: white; padding: 25px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }}
            h1 {{ color: #8E44AD; border-bottom: 2px solid #8E44AD; padding-bottom: 10px; }}
            .metrics-table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
            .metrics-table td, .metrics-table th {{ padding: 12px; border: 1px solid #D5D8DC; text-align: left; }}
            .metrics-table th {{ background-color: #F2F4F4; font-weight: bold; }}
            .status-badge {{ display: inline-block; padding: 6px 12px; border-radius: 4px; color: white; font-weight: bold; background-color: {status_color}; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>SymptoCare Load & Performance Metrics</h1>
            <p>Target Endpoint: <strong>{metrics['endpoint']}</strong></p>
            <span class="status-badge">Status: {metrics['status']}</span>
            
            <table class="metrics-table">
                <tr>
                    <th>Metric</th>
                    <th>Measured Value</th>
                </tr>
                <tr>
                    <td>Total Requests</td>
                    <td>{metrics['total_requests']}</td>
                </tr>
                <tr>
                    <td>Throughput (Requests/Second)</td>
                    <td>{metrics['throughput_req_sec']} req/s</td>
                </tr>
                <tr>
                    <td>Average Latency</td>
                    <td>{metrics['average_latency_ms']} ms</td>
                </tr>
                <tr>
                    <td>P50 / P90 / P99 Latency</td>
                    <td>{metrics['p50_ms']} ms / {metrics['p90_ms']} ms / {metrics['p99_ms']} ms</td>
                </tr>
                <tr>
                    <td>Success Rate</td>
                    <td>{metrics['success_rate_pct']}%</td>
                </tr>
            </table>
        </div>
    </body>
    </html>
    """
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

def main():
    print("Starting Flask server for Performance load tests...")
    proc = start_backend()
    
    try:
        if not wait_for_server():
            print("Failed to start Flask server on port 5000.")
            sys.exit(1)
            
        from tests.performance.test_load import run_load_test
        
        print("Running local load execution (5 concurrent VUs, 25 requests)...")
        start_time = time.time()
        metric_summary = run_load_test(concurrency=5, total_requests=25)
        duration = time.time() - start_time
        
        # Check status from returned 'Status' key
        status = "PASSED" if "PASSED" in metric_summary.get("Status", "") else "FAILED"
        
        # Parse metrics
        throughput_str = metric_summary.get("Throughput (Req/Sec)", "0.00").split()[0]
        avg_lat_str = metric_summary.get("Average Latency", "0.00").split()[0]
        
        p_latencies = metric_summary.get("P50 / P90 / P99 Latency", "0 0 0").replace(" ms", "").split(" / ")
        p50 = p_latencies[0] if len(p_latencies) > 0 else "0.0"
        p90 = p_latencies[1] if len(p_latencies) > 1 else "0.0"
        p99 = p_latencies[2] if len(p_latencies) > 2 else "0.0"
        
        success_rate_str = metric_summary.get("Successful Requests", "0.0%").split("(")[-1].replace("% success)", "")
        
        metrics = {
            "endpoint": "http://127.0.0.1:5000/api/health",
            "total_requests": 25,
            "throughput_req_sec": float(throughput_str),
            "average_latency_ms": float(avg_lat_str),
            "p50_ms": float(p50),
            "p90_ms": float(p90),
            "p99_ms": float(p99),
            "success_rate_pct": float(success_rate_str),
            "status": status
        }
        
        generate_reports(metrics)
        print(f"Performance tests completed: {status}.")
        if status == "FAILED":
            sys.exit(1)
        sys.exit(0)
        
    finally:
        print("Stopping Flask backend server...")
        proc.terminate()
        proc.wait()

if __name__ == "__main__":
    main()
