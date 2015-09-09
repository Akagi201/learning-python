import newspaper

cnn_paper = newspaper.build('http://cnn.com')

# for article in cnn_paper.articles:
#     print(article.url)

for category in cnn_paper.category_urls():
    print(category)

article = cnn_paper.articles[0]
article.download()
print(article.html)
article.parse()
print(article.authors)
print(article.text)
print(article.top_image)
print(article.movies)
print(article.nlp())
print(article.keywords)
print(article.summary)
