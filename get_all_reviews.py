import openreview
import json
import os

from tqdm import tqdm
from IPython import embed


client = openreview.Client(baseurl='https://openreview.net')
review_iterator = openreview.tools.iterget_notes(
        client,
        invitation='ICLR.cc/2019/Conference/-/Paper.*/Official_Review'
)

for review in tqdm(review_iterator, desc='Review'):

    note_id = review.id
    paper_id = review.forum

    os.makedirs(f'Data/{paper_id}', exist_ok=True)

    with open(f'Data/{paper_id}/{note_id}.json', 'w') as f:
        json.dump(review.content, f)
