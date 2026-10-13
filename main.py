import requests
r = requests.get("https://мир-ии-для-бизнеса.рф/")
print(r.status_code)