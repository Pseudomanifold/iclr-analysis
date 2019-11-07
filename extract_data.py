import json
import os
import textblob

import numpy as np
import pandas as pd


def extract_data_from_review(review):
    rating = review['rating']
    rating = rating.split(':')[0]
    confidence = review['confidence']
    confidence = confidence.split(':')[0]
    n_words = len(review['review'].split())

    blob = textblob.TextBlob(review['review'])

    polarities = []
    subjectivities = []

    for sentence in blob.sentences:
        p, s = sentence.sentiment

        polarities.append(p)
        subjectivities.append(s)

    result = {
        'rating': rating,
        'confidence': confidence,
        'n_words': n_words,
        'mean_polarity': np.mean(polarities),
        'sdev_polarity': np.std(polarities),
        'mean_subjectivity': np.mean(subjectivities),
        'sdev_subjectivity': np.std(subjectivities)
    }

    print(result)


for root, dirs, files in os.walk('Data'):
    for filename in files:
        if filename.endswith('.json'):
            with open(os.path.join(root, filename)) as f:
                review = json.load(f)
                extract_data_from_review(review)
