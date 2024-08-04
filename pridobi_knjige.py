import requests
import csv
from bs4 import BeautifulSoup


def pridobi_html(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    }

    try:
        odgovor = requests.get(url, headers=headers)
        odgovor.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")
        return ""
    return odgovor.text
    
def izlusci(html):
    soup = BeautifulSoup(html, 'html.parser')
    rating = soup.find(class_='RatingStatistics__rating').text
    naslov = soup.find(class_='Text__title1').text
    return {
        "id": 1,
        "naslov": naslov,
        "rating": rating
    }
    
    
with open('knjige.csv', 'w', newline='') as csvfile:
    fieldnames = ['id', 'naslov', 'rating']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    
    
    url = "https://www.goodreads.com/book/show/1-the-old-willis-place"
    html = pridobi_html(url)
    podatki = izlusci(html) 
    print(podatki)
    writer.writerow(podatki)


