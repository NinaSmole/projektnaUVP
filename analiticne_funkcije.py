import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def strani_vs_ocena(knjige):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='pages', y='rating', data=knjige, alpha=0.6)
    sns.regplot(x='pages', y='rating', data=knjige, scatter=False, color='pink')
    plt.ylim(0, 5.5)
    plt.xlim(0, 5000)
    plt.xlabel('Število strani')
    plt.ylabel('Ocena')
    plt.title('Ocena knjige v odvisnosti od števila strani')
    plt.show()
    

def pogostost_vezave(knjige):
    format_counts = knjige['formating'].value_counts().reset_index(name='count')
    format_counts['percentage'] = (format_counts['count'] / format_counts['count'].sum()) * 100

    format_counts.loc[format_counts['percentage'] < 1, 'formating'] = 'Other'
    grouped_format_counts = format_counts.groupby('formating')['count'].sum().reset_index()

    grouped_format_counts['percentage'] = (grouped_format_counts['count'] / grouped_format_counts['count'].sum()) * 100
    grouped_format_counts = grouped_format_counts.sort_values('percentage')

    plt.pie(grouped_format_counts['count'], labels=grouped_format_counts['formating'], autopct='%1.1f%%', colors=sns.color_palette('pink'))
    plt.title('Najpogosteje izdaje vezave');
    

def ocena_vezave(knjige):
    ocene_format = knjige.groupby('formating')['rating'].mean().reset_index().sort_values(by='rating')
    plt.figure(figsize=(12, 12))
    sns.barplot(x='rating', y='formating', data=ocene_format, color='pink')
    plt.xlabel('Ocena'), plt.ylabel('Vezava knjige')
    plt.title('Povprečna ocena vezave');
    

def max_knjige(knjige):
    filtrirane = knjige[knjige['num_rating'] >= 10]
    top_knjiga = filtrirane.loc[filtrirane['rating'].idxmax()]
    low_knjiga = filtrirane.loc[filtrirane['rating'].idxmin()]

    print(f'Najbolje ocenejena knjiga je {top_knjiga.author}: {top_knjiga.title} z oceno {top_knjiga.rating}')
    print(f'Najslabše ocenejena knjiga je {low_knjiga.author}: {low_knjiga.title} z oceno {low_knjiga.rating}')


def max_avtor(knjige):
    top_avtor = (knjige[knjige['author'].isin(knjige['author'].value_counts()[lambda x: x > 2].index)]
             .groupby('author')
             .agg(st=('author', 'size'), avg=('rating', 'mean'), best=('rating', 'max'))
             .reset_index()
             .loc[lambda df: df['avg'].idxmax()])
    print(f"Avtor z najbolje ocenjenimi knjigami je {top_avtor.author}: je avtor {top_avtor.st} knjig na seznamu, njihova povprečna ocena je {top_avtor.avg:.1f}, najboljša pa {top_avtor.best}.")


def strani_vs_leto(knjige):
    sns.scatterplot(x='year', y='pages', data=knjige, alpha=0.6)
    sns.regplot(x='year', y='pages', data=knjige, scatter=False, color='pink')
    plt.xlim(0, 2050), plt.ylim(0, 4000)
    plt.xlabel('Leto objave'), plt.ylabel('Število strani')
    plt.title('Število strani v odvisnosti od leta izdaje');


def strani_vs_desetletje(knjige):
    knjige['decade'] = (knjige['year'] // 10) * 10
    strani_desetletje = knjige.groupby('decade')['pages'].mean().reset_index()

    plt.figure(figsize=(25, 6))
    sns.barplot(x='decade', y='pages', data=strani_desetletje, color='pink')
    plt.xlabel('Desetletje izdaje'), plt.ylabel('Povprečno število strani'), plt.xticks(rotation=45)
    plt.title('Povprečno število strani v odvisnosti od desetletja izdaje');


def ocena_vs_komentarji(knjige):
    filtered_books = knjige[knjige['num_review'] > 50]
    sns.scatterplot(x='num_review', y='rating', data=filtered_books, alpha=0.6)
    sns.regplot(x='num_review', y='rating', data=filtered_books, scatter=False, color='pink')
    plt.xlabel('Število komentarjev'), plt.ylabel('Ocena')
    plt.title('Ocena v odvisnosti od števila komentarjev');


def pogostost_zanra(knjige):
    pd.set_option('display.max_rows', 120)
    
    knjige['decade'] = (knjige['year'] // 10) * 10
    genres_expanded = knjige.assign(ganres=knjige['ganres'].str.split(',')).explode('ganres')
    genres_expanded = genres_expanded[genres_expanded['ganres'].notna() & (genres_expanded['ganres'] != 'Unknown')]
    
    genres_grouped = genres_expanded.groupby('decade')['ganres'].apply(lambda x: pd.Series(x).mode()[0]).reset_index(name='most_popular_genre')
    return genres_grouped
