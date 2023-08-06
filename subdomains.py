import requests
import time
from tabulate import tabulate



def check_subdomains(subdomains):
    results = []

    for subdomain in subdomains:
        url = f"http://{subdomain}.google.com"  
        try:
            response = requests.get(url, timeout=5)
            status = "UP" if response.status_code == 200 else "DOWN"
        except requests.ConnectionError:
            status = "DOWN"
        except requests.Timeout:
            status = "TIMEOUT"
        except Exception as e:
            status = "ERROR"

        results.append((subdomain, status))

    return results

def main():
    subdomains = ["www", "map","photos","calendar"]  

    while True:
        results = check_subdomains(subdomains)

        headers = ["Subdomain", "Status"]
        table = tabulate(results, headers=headers, tablefmt="grid")
        print("Subdomain Status:")
        print(table)

        time.sleep(5) 

if __name__ == "__main__":
    main()

