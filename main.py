from tensorflow.keras.models import Model
from tensorflow.keras.models import load_model
import os
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

urllib.request.urlretrieve('https://storage.googleapis.com/laurencemoroney-blog.appspot.com/training_cleaned.csv', 'training.csv')


# SAVED_PATH = './temp/content/saved-model/sonnet-lstm'
#
# model = load_model(filepath=SAVED_PATH)
# model.summary()
#
# print(model.predict([[557, 485], [232, 38]]))

# print(os.listdir('./temp/content/saved-model/sonnet-lstm'))

