import json
import csv

file_name = "March 2021 - Model Policies for the Treatment of Transgender Students in Virginia's Public Schools.jsonl"
csv_file_name = file_name.replace("jsonl", "csv")

fd = open(file_name, "r")
data = list(map(json.loads, fd.readlines()))
fd.close()

def clean_string(data: str) -> str:
    return data.replace("\n", " ")

for i, doc in enumerate(data):
    data[i] = {
        'doc_key': doc['url'],
        'doc_label': 'not_applicable',
        'doc_title': clean_string(doc['title']),
        'doc_content': clean_string(doc['comment_text']),
        'doc_original': clean_string(doc['comment_html']),
        'doc_date': clean_string(doc['date']),
        'doc_author': clean_string(doc['commenter']),
    }

keys = list(data[0].keys())

fd = open(csv_file_name, "w")
dw = csv.DictWriter(fd, keys, delimiter='|')

dw.writeheader()
dw.writerows(data)

fd.close()
