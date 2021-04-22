import boto3
from gsheets import Sheets
import os
import glob
import shutil


# Let's use Amazon S3
s3 = boto3.resource('s3')

# Open a Google Sheets document
sheets = Sheets.from_files('client_secrets.json', 'storage.json')
url = 'https://docs.google.com/spreadsheets/d/1vljuE6-M-e1VKmfhzQGkYrZFNgzUgWM0-xNzxJwme2k'
s = sheets.get(url)

# Export the sheets to local csv files
os.mkdir("csvs/" + s.title)
csv_name = lambda infos: 'csvs/%(title)s/%(sheet)s.csv' % infos
s.to_csv(make_filename=csv_name)

# Upload the files to the S3 bucket
for filename in glob.glob('csvs/' + s.title + '/*.csv'):
    data = open(filename, 'rb')
    s3.Bucket('gem.test.gsheets').put_object(Key=filename, Body=data)

# Delete the local CSVs
shutil.rmtree('csvs/' + s.title)
