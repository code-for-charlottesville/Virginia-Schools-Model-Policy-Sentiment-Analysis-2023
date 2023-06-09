# Virginia Schools Model Policy Sentiment Analysis (2023)

This repository functions as a shared resource for our ongoing
effort to classify ~72,000 public comments on a public town hall
forum run by the state of Virginia. The comments were made in
reference to a "model policy" proposed by the Youngkin
administration, which applies to all Virginia Public Schools.

## Links

- [Comment Forum (townhall.virginia.gov)](https://townhall.virginia.gov/l/GDocForum.cfm?GDocForumID=1953)
- [Scraped Comments (S3, JSONL, 65MB)](https://austin-schaffer.s3.amazonaws.com/virginia-town-hall/scraped-public-comments/2022+Virginia+Public+Schools+Model+Policy+Public+Comments.jsonl)
- [Scraped Comments (S3, CSV, 58MB)](https://austin-schaffer.s3.amazonaws.com/virginia-town-hall/scraped-public-comments/2022+Virginia+Public+Schools+Model+Policy+Public+Comments.csv) 
- [Hand-Labeled Sample of 500 (Google Sheets)](https://docs.google.com/spreadsheets/d/1ZDifcVyUBzwGyuJ8NpkOWGP78OOMVMzpoZLOaEKYo-M/edit?usp=sharing)

## Processing Results

- [Machine-Labeled Corpus (Google Drive)](https://drive.google.com/file/d/1E_WIJ46Of7LRE1qmTAtC56q710MHW-i6/view?usp=sharing)
- https://aclu-model-policy-comments.s3.amazonaws.com/classifications.csv
- https://aclu-model-policy-comments.s3.amazonaws.com/comments.csv
- https://aclu-model-policy-comments.s3.amazonaws.com/dupe_group_comments.csv
- https://aclu-model-policy-comments.s3.amazonaws.com/dupe_groups.csv

## Related Projects

- [Public Comment Web Scraper](https://github.com/AustinTSchaffer/Virginia-Town-Hall-Public-Comment-Scraper)
- [polo2](https://github.com/ontoligent-design/polo2)
