from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
web_page = response.text

soup = BeautifulSoup(web_page,"html.parser")

articles = soup.find_all(name="span", class_="titleline")
article_texts = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
print(article_texts)


article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
print(article_upvotes)

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
print(largest_index)

print(article_texts[largest_index])