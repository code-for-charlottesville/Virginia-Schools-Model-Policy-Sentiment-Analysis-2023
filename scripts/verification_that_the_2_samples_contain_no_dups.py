"""
Script to generate a 2nd CSV for allowing volunteers to label
the sentiment for 250 additional public comments. There should
be no overlap between the previous sample of 500 comments and
the new sample of 250 comments.
"""

# %%

import random
import csv

CORPUS_FILENAME = "../data/2022 Virginia Public Schools Model Policy Public Comments.csv"
SAMPLE_500_FILENAME = "../data/2022 Virginia Public Schools Model Policy Public Comments - 500 Row Sample.csv"
SAMPLE_250_FILENAME = "../data/2022 Virginia Public Schools Model Policy Public Comments - 250 Row Sample.csv"

# %%

with open(SAMPLE_250_FILENAME, "r") as new_sample_fd:
    next(new_sample_fd)
    sample_250 = list(csv.DictReader(
        new_sample_fd,
        fieldnames=[
            'labeler_1',
            'labeler_2',
            'sentiment',
            'doc_key',
            'doc_title',
            'doc_author',
        ],
        delimiter="|",
    ))

with open(SAMPLE_500_FILENAME, "r") as prev_sample_fd:
    next(prev_sample_fd)
    sample_500 = list(csv.DictReader(
        prev_sample_fd,
        fieldnames=['url', 'commenter', 'title'],
        delimiter=","
    ))

# %%

sample_500_urls = {r['url'] for r in sample_500}
sample_250_urls = {r['doc_key'] for r in sample_250}

dup_urls = sample_250_urls.intersection(sample_500_urls)
assert len(dup_urls) == 0

# %%
