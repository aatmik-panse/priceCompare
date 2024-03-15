import requests
def fetchAndSaveFile(url, path):
    r=requests.get(url)
    with open(path , "w") as f:
        f.write(r.text)
url = "https://google.com"

fetchAndSaveFile(url, "data/fetchingtdata4.html")