import requests
r=requests.get("https://financialmodelingprep.com/api/v3/quote/AAPL?apikey=demo")
print(r)
print(r.text)
print(r.status_code)
print(r.headers)
print(r.url)