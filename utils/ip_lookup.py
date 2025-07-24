import requests

def lookup_ip(ip):
    url = f"http://ip-api.com/json/{ip}"
    try:
        response = requests.get(url, timeout=3)
        data = response.json()
        return {
            "ip": ip,
            "country": data.get("country"),
            "region": data.get("regionName"),
            "city": data.get("city"),
            "isp": data.get("isp")
        }
    except Exception as e:
        return {"ip": ip, "error": str(e)}
