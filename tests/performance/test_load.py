import time
import urllib.request
import json
import threading
import socket
import sys
import io

# Reconfigure stdout/stderr to use UTF-8 (resolves Windows character map errors)
try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except AttributeError:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

BASE_URL = "http://127.0.0.1:5000/api"

def is_server_running():
    try:
        with socket.create_connection(("127.0.0.1", 5000), timeout=1):
            return True
    except OSError:
        return False

# Thread-local storage for metrics
latencies = []
status_codes = []
lock = threading.Lock()

def make_request(path):
    url = f"{BASE_URL}{path}"
    start = time.time()
    try:
        req = urllib.request.Request(url, method="GET")
        with urllib.request.urlopen(req, timeout=10) as response:
            latency = (time.time() - start) * 1000
            with lock:
                latencies.append(latency)
                status_codes.append(response.status)
    except urllib.error.HTTPError as e:
        latency = (time.time() - start) * 1000
        with lock:
            latencies.append(latency)
            status_codes.append(e.code)
    except Exception as e:
        latency = (time.time() - start) * 1000
        with lock:
            latencies.append(latency)
            status_codes.append(500)

def run_load_test(path="/health", concurrency=10, total_requests=50):
    global latencies, status_codes
    latencies = []
    status_codes = []
    
    if not is_server_running():
        print(f"Skipping performance load test for {path}: backend server is not running on port 5000.")
        return None
        
    print(f"Starting load test on {path} with {concurrency} VUs (concurrency), total {total_requests} requests...")
    
    start_time = time.time()
    threads = []
    
    # We distribute total_requests among threads
    requests_per_thread = total_requests // concurrency
    
    def worker():
        for _ in range(requests_per_thread):
            make_request(path)
            
    for _ in range(concurrency):
        t = threading.Thread(target=worker)
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
        
    total_time = time.time() - start_time
    
    if not latencies:
        print("Error: No requests completed.")
        return None
        
    successful_requests = len([c for c in status_codes if 200 <= c < 300])
    success_rate = (successful_requests / len(status_codes)) * 100.0
    throughput = len(status_codes) / total_time
    
    sorted_latencies = sorted(latencies)
    avg_latency = sum(latencies) / len(latencies)
    min_latency = sorted_latencies[0]
    max_latency = sorted_latencies[-1]
    
    # Percentiles
    p50 = sorted_latencies[int(len(sorted_latencies) * 0.50)]
    p90 = sorted_latencies[int(len(sorted_latencies) * 0.90)]
    p99 = sorted_latencies[int(len(sorted_latencies) * 0.99)]
    
    results = {
        "Target Endpoint": f"{BASE_URL}{path}",
        "Total Requests": len(status_codes),
        "Successful Requests": f"{successful_requests} ({success_rate:.1f}% success)",
        "Throughput (Req/Sec)": f"{throughput:.2f} req/s",
        "Average Latency": f"{avg_latency:.2f} ms",
        "Min / Max Latency": f"{min_latency:.2f} ms / {max_latency:.2f} ms",
        "P50 / P90 / P99 Latency": f"{p50:.2f} ms / {p90:.2f} ms / {p99:.2f} ms",
        "Status": "🟢 PASSED" if success_rate > 95.0 else "🔴 FAILED"
    }
    
    print("\n--- Performance Metrics Summary ---")
    for key, value in results.items():
        print(f"{key:25} : {value}")
    print("-----------------------------------\n")
    return results

if __name__ == "__main__":
    run_load_test("/health", concurrency=5, total_requests=25)
