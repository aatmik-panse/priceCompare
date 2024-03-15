from bs4 import BeautifulSoup
import requests as rq

url="https://www.amazon.in/dp/B09YV4RG4D/ref=s9_acsd_al_bw_c2_x_2_t?pf_rd_m=AT95IG9ONZD7S&pf_rd_s=merchandised-search-5&pf_rd_r=ZKCB1FEE7S8EYSK5K1ZF&pf_rd_t=101&pf_rd_p=4714343b-1ee0-4ace-92c1-7115aca5ee21&pf_rd_i=11599648031"

headers={
    "Accept-Language" : "en-US,en;q=0.9",
    "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}

r=rq.get(url, headers=headers)

soup=BeautifulSoup(r.content, "html.parser")

description = soup.find('h1',{"class": "a-size-large a-spacing-none"})
    #print(title.text.strip())
nam = description.find('span', 'a-size-large product-title-word-break').text
print(nam)
