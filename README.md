# ICLR 2020 and 2019 reviews

This repository contains the data of all reviews of ICLR 2019 and ICLR
2020, crawled using the [OpenReview API](https://github.com/openreview/openreview-py).
See [my blog](https://bastian.rieck.me/blog/posts/2019/iclr_analysis)
for more information and plots.

# Data

Currently, only data for ICLR 2020 has been provided in a summary data
format. See [2020.csv](https://github.com/Pseudomanifold/iclr-analysis/blob/master/2020.csv) for more details.

The folders 'Data/2019' and 'Data/2020' contain *all* reviews of ICLR
2019 and 2020, respectively. Each folder follows the numerical ID that
OpenReview assigns to a paper. Each review is provided as a `JSON` file.

# Updating and modifying the data

- Use the script [`get_all_reviews.py`](https://github.com/Pseudomanifold/iclr-analysis/blob/master/get_all_reviews.py) to download all the reviews of a given year. Currently, everything is hard-coded in the script.

- Use the script [`extract_data.py`](https://github.com/Pseudomanifold/iclr-analysis/blob/master/extract_data.py) to extract data from the reviews and create a `CSV` file. This is where most of the magic happens currently. I added a cursory calculation  of NLP metrics but did *not* make use of the resulting values so far.

- Finally, to create the plots from the blog post, use the script
  [`make_plots.py`](https://github.com/Pseudomanifold/iclr-analysis/blob/master/make_plots.py).

I am actively working on all of these scripts, so stay tuned for
improved versions.
