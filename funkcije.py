import requests
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
    
    
def izlusci(html, zaporedni_id, goodreads_id):
    soup = BeautifulSoup(html, 'html.parser')
    
    title = soup.find(class_='Text__title1').text
    author = soup.find(class_='ContributorLink__name').text
    rating = soup.find(class_='RatingStatistics__rating').text
    num_rating = soup.find('span', {'data-testid': 'ratingsCount'}).text.split()[0].replace(',', '')
    num_review = soup.find('span', {'data-testid': 'reviewsCount'}).text.split()[0].replace(',', '')
    zanri = soup.find(class_='CollapsableList')  #nov soup za zanre
    
    try:
        pages_info = soup.find('p', {'data-testid': 'pagesFormat'}).text.split(',')
        pages = pages_info[0].split()[0].replace(',', '')
        vezava = pages_info[1].strip()
    except AttributeError:
        pages = "0"
        vezava = "Unknown"
        
    try:
        leto = soup.find('p', {'data-testid': 'publicationInfo'}).text.split()[-1]
    except AttributeError:
        leto = "Unknown"

    
    ganres_sklop = zanri.findAll(class_='Button__labelItem')
    ganres = ','.join([genre.text for genre in ganres_sklop if 'more' not in genre.text])
    if ganres == "Book details & editions,":
        ganres = "Unknown"

            
    return {
        "count_id": zaporedni_id,
        "goodreads_id": goodreads_id,
        "title": title,
        "author": author,
        "rating": rating,
        "num_rating": num_rating,
        "num_review": num_review,
        "ganres": ganres,
        "pages": pages,
        "formating": vezava,
        "year": leto
    }
    

def neveljaven_id_knjige(html):
    napis_napake = "Sorry, we couldn’t find the page you were looking for."
    return napis_napake in html
    
    


