# DeepESG-challenge
Data Processing Technical Challenge

Author: João Victor Rodrigues

1- It was created a bucket on Google Cloud Storage to upload the originals and treated xlsx files. The bucket was created on the console of the GCP website.
The chosen region of the bucket was US (multiple regions in United States) with the cost of $0.026 per GB-month. I chosed the multi-region type instead of only one because of the bigger availability and security. The bucket class is Standard because it's better for short-term storage and frequently accessed data.

2- The bucket has two folders: "originals_files" and "treated_files"

3- The entire coding was done on google colab. 

4- At first, the two xlsx files were imported from the bucket. Then, a backup was made and after that the treatment with pandas begun.

5- At the end, when the treatment finished, the chart of accounts was entire populated. So, the dataframe was saved as xlsx and I uploaded it to the "treated_files" folder in the bucket. A couple of lines of code was written to download a final local file too.
