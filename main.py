from bs4 import BeautifulSoup
import requests
import smtplib
import os

# URL = "https://appbrewery.github.io/instant_pot/"
URL =(f"https://www.amazon.in/realme-Wireless-Earbuds-Spatial-Charging/dp/"
    f"B0CH1HLLBV/ref=sr_1_9?crid=2V4YIZSTCRZ6Z&dib=eyJ2IjoiMSJ9."
    f"y0Flg8Ut13KfY89OTCs06qEzWcrK2Nt2qgBGy8wQANjSfY1q1nc3RGK6bOsrfEywsbUA5zm0j"
    f"mkE1T4RVO-4lMwJ_iYwxGUSOeNh97lJR8RhWfmFZipjg4NSwDObWDUiUmfAPWbZUhKWzZ1ubt8esy6Z8pzh6y6QfrlqAfb_bhNYB_pz3JH85Pe"
    f"HxE3otOaluU4YZakgoRsoR0nq62MDvE30NAt9K_IT3o60USMM_xY.0RpegBfRZ8uSfNi09SJtON3QflZqUDOKEV2ebbL9XsA&dib_tag=se&"
    f"keywords=bluetooth+earbuds&qid=1725857973&sprefix=bluetooth+earbuds%2Caps%2C245&sr=8-9")
headers = {
    "Accept": f"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,"
              f"image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Dnt": "1",
    "Priority": "u=0, i",
}
response = requests.get(url=URL, headers=headers)
html_data = response.text
soup = BeautifulSoup(html_data, "html.parser")
price = soup.find(name="span", class_="aok-offscreen").getText().strip().split(" ")[0][1:]
price_cleaned = price.replace(",", "")
cost = float(price_cleaned)
to_addr = os.environ.get('to_addr')
EMAIL = os.environ.get('EMAIL')
PASSWORD = os.environ.get('PASSWORD')

if cost < 1798:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=to_addr,
            msg="hey the price has been dropped on your product !!"
        )
