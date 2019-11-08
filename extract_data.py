import json
import os
import textblob

import numpy as np
import pandas as pd


# Required for ICLR 2020 since no numerical scores are present in the
# raw files.
experience_to_score = {
    'I have published in this field for several years.': 3,
    'I have published one or two papers in this area.': 2,
    'I have read many papers in this area.': 1,
    'I do not know much about this area.': 0
}


def extract_data_from_review(review):
    
    rating = review['rating']
    rating = rating.split(':')[0]

    if 'confidence' in review.keys():
        confidence = review['confidence']
        confidence = confidence.split(':')[0]
    else:
        confidence = None

    if 'experience_assessment' in review:
        experience = experience_to_score[review['experience_assessment']]
    else:
        experience = None

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
        'n_words': n_words,
        'mean_polarity': np.mean(polarities),
        'sdev_polarity': np.std(polarities),
        'mean_subjectivity': np.mean(subjectivities),
        'sdev_subjectivity': np.std(subjectivities)
    }

    if confidence:
        result['confidence'] = confidence

    if experience:
        result['experience'] = experience

    return result


df = pd.DataFrame()

for root, dirs, files in os.walk('Data/2020'):
    for filename in files:
        if filename.endswith('.json'):
            with open(os.path.join(root, filename)) as f:
                review = json.load(f)
                row = extract_data_from_review(review)

                row['review_id'] = os.path.splitext(
                    os.path.basename(filename))[0]

                row['paper_id'] = os.path.basename(
                    os.path.dirname(
                        os.path.join(root, filename)))

                df = df.append(row, ignore_index=True)

df.to_csv('2020.csv', index=False)
