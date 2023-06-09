"""
Script to generate a 2nd CSV for allowing volunteers to label
the sentiment for 250 additional public comments. There should
be no overlap between the previous sample of 500 comments and
the new sample of 250 comments.
"""

# %% Consts.

import random
import csv

CORPUS_FILENAME = "../data/2022 Virginia Public Schools Model Policy Public Comments.csv"
PREV_SAMPLE_FILENAME = "../data/2022 Virginia Public Schools Model Policy Public Comments - 500 Row Sample.csv"
NEW_SAMPLE_FILENAME = "../data/2022 Virginia Public Schools Model Policy Public Comments - 250 Row Sample.csv"

# %% Load the corpus and the previous sample.

with open(CORPUS_FILENAME, "r") as corpus_fd:
    next(corpus_fd)
    corpus = list(csv.DictReader(
        corpus_fd,
        fieldnames=[
            'doc_key',
            'doc_label',
            'doc_title',
            'doc_content',
            'doc_original',
            'doc_date',
            'doc_author'
        ],
        delimiter="|",
    ))

with open(PREV_SAMPLE_FILENAME, "r") as prev_sample_fd:
    next(prev_sample_fd)
    prev_sample = list(csv.DictReader(
        prev_sample_fd,
        fieldnames=['url', 'commenter', 'title'],
        delimiter=","
    ))

# %% Build some dicts and some sets.

doc_index = {r['doc_key']: r for r in corpus}
urls_in_prev_sample = {r['url'] for r in prev_sample}
prev_used_titles_comments: set[tuple[str, str]] = set()

# %% Generate a list of the "available documents" i.e. unique title/comment combinations that haven't yet been included in a sample.

for url in urls_in_prev_sample:
    doc = doc_index[url]
    prev_used_titles_comments.add((doc['doc_title'], doc['doc_content']))

available_docs = []
for doc in corpus:
    if doc['doc_key'] in urls_in_prev_sample:
        continue

    if (doc['doc_title'], doc['doc_content']) in prev_used_titles_comments:
        continue

    available_docs.append(doc)
    prev_used_titles_comments.add((doc['doc_title'], doc['doc_content']))

# %% Take the sample.

sample_250 = random.sample(available_docs, 250)

# %% Add 2 labelers to each record and remove columns that we don't need in Google Sheets.

labelers = ["Austin", "Wolfgang", "Isaak", "Sirish", "Jon"]
for i, record in enumerate(sample_250):
    record: dict = record
    labeler_1 = labelers[(i // 50) % len(labelers)]
    labeler_2 = labelers[((i // 50) + 1) % len(labelers)]

    record['labeler_1'] = labeler_1
    record['labeler_2'] = labeler_2
    record['sentiment'] = None

    record.pop('doc_content', None)
    record.pop('doc_original', None)
    record.pop('doc_date', None)
    record.pop('doc_label', None)

# %% Save the new sample to a CSV.

with open(NEW_SAMPLE_FILENAME, "w") as new_sample_fd:
    dw = csv.DictWriter(
        new_sample_fd, [
            'labeler_1',
            'labeler_2',
            'sentiment',
            'doc_key',
            'doc_title',
            'doc_author',
        ],
        delimiter='|'
    )
    dw.writeheader()
    dw.writerows(sample_250)

# %%
