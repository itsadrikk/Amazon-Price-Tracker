URL="https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
MY_EMAIL= "yashjain22072003@gmail.com"
TO_EMAIL="shashankshah261@gmail.com"
MY_PASSWORD= "vnziawxrcnnneeaf"
import requests
import lxml
import smtplib
from bs4 import BeautifulSoup
response=requests.get(URL,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36','Accept-Language':'en-US,en;q=0.9'})
website = response.text
soup=BeautifulSoup(website,'lxml')
title = soup.find(name="span",id="productTitle").get_text().strip()
w_price=soup.find(name="span",class_="a-price-whole").getText()
f_price=soup.find(name="span",class_="a-price-fraction").getText()


price=float(w_price+f_price)

BUY_PRICE = 100

if price < BUY_PRICE:
    message = f"{title} is now {price}"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )