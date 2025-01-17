from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
web_page = response.text

soup = BeautifulSoup(web_page,"html.parser")


titles = soup.find_all(name="h2")
titles.pop(0)


with open("movies.txt", "w") as file:
    # ::-1 loops titles in reverse order
    for h2_tag in titles[::-1]:
        movie_name = h2_tag.text.strip()  # gets the movie name and remove extra spaces
        file.write(movie_name + "\n")  # writing name in next line


