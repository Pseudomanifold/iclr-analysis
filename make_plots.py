#!/usr/bin/env python
#
# A simple script that makes use of Seaborn to create a set of
# interesting plots to analyse the reviews. Please note that I
# hard-coded everything for ICLR 2020 for now.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


sns.set_style("dark")

df = pd.read_csv('2020.csv', index_col='review_id')
df['experience'] = df.experience.astype('category')
df['rating'] = df.rating.astype('category')

plt.figure(figsize=(4, 5))

ax = sns.boxplot(x=df['rating'], y=df['n_words'], data=df)

ax.set_xlabel('Rating')
ax.set_ylabel('Number of words')

plt.tight_layout()
plt.savefig('ICLR_2020_boxplots_01.svg')

plt.clf()

ax = sns.boxplot(x=df['experience'], y=df['n_words'], data=df)

ax.set_xlabel('Experience')
ax.set_ylabel('Number of words')

plt.tight_layout()
plt.savefig('ICLR_2020_boxplots_02.svg')

plt.clf()

g = sns.catplot(
    x='rating',
    y='n_words',
    col='experience',
    kind='box',
    data=df,
    aspect=0.6
)

g.set_axis_labels('Rating', 'Number of words')
g.set_titles('Experience = {col_name}')

plt.tight_layout()
plt.savefig('ICLR_2020_boxplots_03.svg')

plt.clf()

g = sns.FacetGrid(data=df, row='experience', hue='rating')
g = g.map(sns.countplot, 'rating')

#ax.set_xlabel('Experience')
#ax.set_ylabel('Rating')

plt.tight_layout()
plt.savefig('ICLR_2020_boxplots_04.svg')

plt.show()
