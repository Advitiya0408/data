from wordcloud import WordCloud, STOPWORDS
import wikipedia

stords = set(STOPWORDS)
info = wikipedia.summary(input("Plese enter your search "))
print(info)
word_cloud = WordCloud(stopwords=stords).generate(info)
img = word_cloud.to_image()
img.show()
