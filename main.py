from bs4 import BeautifulSoup
import requests
import lxml
from smtplib import SMTP
import os

headers={
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Referer": "https://www.google.com/"
}
url="https://www.amazon.in/OnePlus-Charcoal-Snapdragon%C2%AE-Personalised-Game-Changing/dp/B0FZSXYV6K/ref=sr_1_33_sspa?crid=30E8YIS7TIF4X&dib=eyJ2IjoiMSJ9.HdDcMgq7zST1Lq56dQ5wn56PlhsvVdF2b-C727YFyonGjHj071QN20LucGBJIEps.6kUhLGJ9Vrzt30dTk6Ew4VLBSg3d03kQBxJjcCWnAIg&dib_tag=se&keywords=phone%2Bunder%2B25k%2B&qid=1781855427&sprefix=phone%2Caps%2C338&xpid=FBWmj6CT96Jkm&aref=q58bZ7Pqsc&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGZfbmV4dA&th=1"

response=requests.get(url,headers=headers)
response.raise_for_status()
website=response.text
soup=BeautifulSoup(website,"lxml")

title=soup.find("span",class_="a-size-large product-title-word-break").text

price=soup.find("span",class_="a-offscreen")
price_text=price.text
actual_price=price_text.split("₹")[1]
convert_to_int=int(float(actual_price.replace(",", "")))

buying_price=40000

if float(buying_price)>=convert_to_int:

    myemail = os.environ["EMAIL"]
    pass1 = os.environ["EMAIL_PASSWORD"]
    receiver_email = os.environ["RECEIVER_EMAIL"]

    with SMTP("smtp.gmail.com",587) as server:
        server.starttls()
        server.login(myemail,pass1)
        server.sendmail(
            from_addr=myemail,
            to_addrs=receiver_email,
            msg=f"Subject:Amazon Price Deals!\n\n{title}\nyour coated price ₹{buying_price} and now it is at ₹{actual_price}\n{url}".encode("utf-8")
        )
    print("Email sent successfully")
else:
    myemail = os.environ["EMAIL"]
    pass1 = os.environ["EMAIL_PASSWORD"]
    receiver_email = os.environ["RECEIVER_EMAIL"]

    with SMTP("smtp.gmail.com",587) as server:
        server.starttls()
        server.login(myemail,pass1)
        server.sendmail(
            from_addr=myemail,
            to_addrs=receiver_email,
            msg=f"Subject:Amazon Price Deals!\n\nIt is expensive now"
        )
