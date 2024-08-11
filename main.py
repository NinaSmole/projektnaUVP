# OPOZORILO: sledeča koda je bila dokončana 8. 8. 2024, podatki uporabljeni v tej nalogi so bili iz interneta pobrani isti dan. 
# Goodreads je 9. 8. 2024 obnovil spletno stran in odstranil določene podatke o knjigah (leto izdaje, vezava in število strani),
# zato ta program ob zagonu ne vrne takšnih podatkov, kot so uporabljeni v nadljajni analizi.

import funkcije
import csv
import random

with open('knjige.csv', 'w', newline='') as csvfile:
    fieldnames = [
        'count_id', 'goodreads_id', 'title', 'author', 'rating', 'num_rating', 'num_review', 'ganres', 'pages', 'formating', 'year'
        ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    zeleno_st = 10
    zbrani_naslovi = set()
    zbrane_stevlike = set()
    
    stevec_knjig = 1
    
    while stevec_knjig <= zeleno_st:
        print(f"Scraping book {stevec_knjig} out of {zeleno_st}")
        goodreads_id = random.randint(1, 1995353)
        if goodreads_id in zbrane_stevlike:
            print(f"Goodreads ID {goodreads_id} is already processed.")
            continue

        try:
            url = f"https://www.goodreads.com/book/show/{goodreads_id}"
            html = funkcije.pridobi_html(url)
            
            if funkcije.neveljaven_id_knjige(html):
                continue
            
            podatki = funkcije.izlusci(html, stevec_knjig, goodreads_id)
            
            rating = float(podatki['num_rating'])
            naslov_avtor = podatki['title'] + podatki['author']
            
            if naslov_avtor not in zbrani_naslovi and rating != 0:
                writer.writerow(podatki)
                zbrani_naslovi.add(naslov_avtor)
                stevec_knjig += 1
            else:
                print(f"{podatki['title']} by {podatki['author']} is already in the CSV or has no ratings.")
        
        except Exception as e:
            print(f"Failed to process Goodreads ID {goodreads_id}: {e}")
    
        zbrane_stevlike.add(goodreads_id)
