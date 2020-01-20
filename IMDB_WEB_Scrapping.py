import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://www.imdb.com/search/title?release_date=2019&sort=num_votes,desc&page=1"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
movie_containers = soup.find_all('div', class_='lister-item mode-advanced')

# Lists to store scraped data
names = []
years = []
imdb_ratings = []
votes = []

# Extract data from individual movie container
for container in movie_containers:
        name = container.h3.a.text
        names.append(name)
        year = container.h3.find('span', class_='lister-item-year').text
        years.append(year)
        imdb = float(container.strong.text)
        imdb_ratings.append(imdb)
        vote = container.find('span', attrs={'name': 'nv'})['data-value']
        votes.append(int(vote))

df = pd.DataFrame({
    'Movie': names,
    'Year': years,
    'Imdb': imdb_ratings,
    'Votes': votes
})

print(df)
