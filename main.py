import pridobi_podatke
import csv

with open('knjige.csv', 'w', newline='') as csvfile:
    fieldnames = ['id', 'naslov', 'avtor', 'rating', 'num_rating', 'num_review', 'ganres', 'pages', 'vezava', 'leto']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    n = 10000
    zbrani_naslovi = set()
    
    for i in range(1, n):
        print(f"Scraping  page {i} out of {n}")
        
        try:
            url = f"https://www.goodreads.com/book/show/{i}-the-old-willis-place"
            html = pridobi_podatke.pridobi_html(url)
            podatki = pridobi_podatke.izlusci(html, i)
            
            naslov_avtor = podatki['naslov'] + podatki['avtor']
            if naslov_avtor not in zbrani_naslovi:
                writer.writerow(podatki)
                zbrani_naslovi.add(naslov_avtor)
            else:
                print(f"{podatki['naslov']} is already in csv")
            
        except Exception:
            pass            
