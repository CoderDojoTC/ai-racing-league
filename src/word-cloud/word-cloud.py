import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import string

# Fetch the text
url = "https://towardsdatascience.com/personal-knowledge-graphs-9a23a0b099af"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
text = soup.get_text()

# Preprocess the text
text = text.lower()
text = text.translate(str.maketrans('', '', string.punctuation))
stop_words = set(stopwords.words('english'))
tokens = word_tokenize(text)
tokens = [i for i in tokens if not i in stop_words]
ps = PorterStemmer()
tokens = [ps.stem(i) for i in tokens]

# Create the word cloud
wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                stopwords = stop_words, 
                min_font_size = 10).generate(' '.join(tokens))

# Plot the word cloud
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 

plt.show()
