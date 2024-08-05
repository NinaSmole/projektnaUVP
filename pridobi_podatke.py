import requests
from bs4 import BeautifulSoup
from datetime import datetime


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
    
    
def izlusci(html, stevilo_id):
    soup = BeautifulSoup(html, 'html.parser')
    
    naslov = soup.find(class_='Text__title1').text
    avtor = soup.find(class_='ContributorLink__name').text
    rating = soup.find(class_='RatingStatistics__rating').text
    num_rating = soup.find('span', {'data-testid': 'ratingsCount'}).text.split()[0].replace(',', '')
    num_review = soup.find('span', {'data-testid': 'reviewsCount'}).text.split()[0].replace(',', '')
    zanri = soup.find(class_='CollapsableList')
    pages = soup.find('p', {'data-testid': 'pagesFormat'}).text.split()[0].replace(',', '')
    vezava = soup.find('p', {'data-testid': 'pagesFormat'}).text.split(',')[1][1:]
    leto = soup.find('p', {'data-testid': 'publicationInfo'}).text.split()[-1]
    
    ganres_sklop = zanri.findAll(class_='Button__labelItem')
    ganres = ','.join([genre.text for genre in ganres_sklop if 'more' not in genre.text])

            
    return {
        "id": stevilo_id,
        "naslov": naslov,
        "avtor": avtor,
        "rating": rating,
        "num_rating": num_rating,
        "num_review": num_review,
        "ganres": ganres,
        "pages": pages,
        "vezava": vezava,
        "leto": leto
    }


