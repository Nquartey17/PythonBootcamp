import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

#Fake URL for practice
url = "https://appbrewery.github.io/instant_pot/"
#Live URL: Note - Subject to change. If bs4 fails, check Amazon for changes
# url = "https://www.amazon.com/Apple-Bluetooth-Headphones-Personalized-Effortless/dp/B0DGHMNQ5Z/ref=sr_1_1_sspa?crid=1BWIQLE3HMU2M&dib=eyJ2IjoiMSJ9.CI7bjSuQSQBx0GaAVvRN7sZKdmIeg5NZU-hRqMqF9GB2hJWy1j6bnla3VymYHYHxTErLINZWo6ABC5COoYdbvp8g0AmU5n2pvZ7gbIIlRmnDEWZSOH1-ytoJT3dP6v543QtsvEjKM8H_i5TKmh0LmgM-Zlf5DNXg0_2J-uuQx9fg4gnyFFZwitqgrFwd8TQDl8VsCjkSCGGkkv7NLCT_DWpPjGXunGWMYKZCnnzo4qQ.PiFPkKX7VOwKzidix49rwzxrOJXf8EWk_piR7ekCHZk&dib_tag=se&keywords=airpods&qid=1770077624&sprefix=airpods%2Bpro%2B2%2Caps%2C403&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"

response = requests.get(url, headers={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                                      "Accept-Encoding": "gzip, deflate, br, zstd",
                                      "Accept-Language": "en-US,en;q=0.5",
                                      "Priority": "u=0, i",
                                      "Sec-Ch-Ua": "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Google Chrome\";v=\"144\"",
                                      "Sec-Ch-Ua-Mobile": "?0",
                                      "Sec-Ch-Ua-Platform": "\"Windows\"",
                                      "Sec-Fetch-Dest": "document",
                                      "Sec-Fetch-Mode": "navigate",
                                      "Sec-Fetch-Site": "none",
                                      "Sec-Fetch-User": "?1",
                                      "Upgrade-Insecure-Requests": "1",
                                      "User-Agent": "CCBot/2.0 (https://commoncrawl.org/faq/)"
                                      })
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
product_name = soup.find(id="productTitle").get_text().split()
updated_name = " ".join(product_name)
price = soup.find(class_="a-offscreen").get_text()
converted_price = float(price.split("$")[1])

#Send email if price is less than $100
if converted_price < 100:
    # use port 587 for secure TCP
    with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
        connection.starttls()
        connection.login(user=os.environ["EMAIL_ADDRESS"], password=os.environ["EMAIL_PASSWORD"])
        connection.sendmail(from_addr=os.environ["EMAIL_ADDRESS"],
                            #email price change to yourself
                            to_addrs=os.environ["EMAIL_ADDRESS"],
                            msg=f"Subject:Price Reduction\n\n{updated_name} is on sale for {converted_price}")


print(price)