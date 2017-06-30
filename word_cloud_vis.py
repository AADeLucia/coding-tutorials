# Import necessary packages
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


# Read the text from our chosen file
text = open('plato_symposium.txt').read()

# Get image mask
cloud_mask = np.array(Image.open('symposium_sillohuette.png'))

# Set stopwords (words that we do not want in the word cloud)
stopwords = set(STOPWORDS)
stopwords.add("said")

# Instantiate word cloud
wc = WordCloud(width=2000,height=2000,background_color='white',mask=cloud_mask)

# Generate text from file
wc.generate(text)

# Display the image
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()
