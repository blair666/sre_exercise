import yaml
import requests
import time
import json
from collections import defaultdict
from urllib.parse import urlparse
from datetime import datetime

# Function to load configuration from the YAML file
def load_config(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

# Extract domain from URL
def get_domain(url):
    return urlparse(url).hostname

# Function to perform health checks
def check_health(endpoint):
    url = endpoint['url']
    method = endpoint.get('method','GET')
    headers = endpoint.get('headers',{})
    body = endpoint.get('body')
    json_body = json.loads(body) if body else None

    start_time = time.monotonic() #response time measurement
    try:
        response = requests.request(method, url, headers=headers, json=json_body, timeout=1)
        #the endpoint covert to milliseconds(ms)
        end_ms = (time.monotonic() - start_time) * 1000

        #if status is 200-299 and response is <= 500ms
        if 200 <= response.status_code < 300 and end_ms <=500:
            return "UP"
        else:
            return "DOWN"
    except requests.RequestException:
        return "DOWN"

# Main function to monitor endpoints
def monitor_endpoints(file_path):
    config = load_config(file_path)
    domain_stats = defaultdict(lambda: {"up": 0, "total": 0})

    while True:
        for endpoint in config:
            domain = get_domain(endpoint["url"])
            result = check_health(endpoint)

            domain_stats[domain]["total"] += 1
            if result == "UP":
                domain_stats[domain]["up"] += 1

        # Log cumulative availability percentages
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for domain, stats in domain_stats.items():
            availability = int(100 * stats["up"] / stats["total"]) # drop decimals
            print(f"[{timestamp}] {domain} has {availability}% availability percentage")

        print("---")
        time.sleep(15)

# Entry point of the program
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python monitor.py <config_file_path>")
        sys.exit(1)

    config_file = sys.argv[1]
    try:
        monitor_endpoints(config_file)
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")