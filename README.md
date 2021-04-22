# Google Sheets repo for GEM

This is a collection of proof-of-concept code for managing Google Sheets data.
It is intended to provide code snippets showing how to perform tasks including
the following:

## Google Sheets API examples
### quickstart.py

Google Cloud Platform's Quickstart script for reading and printing data from
Google Sheets.

### gsheets_gem.py

Reads all the sheets from a Google Sheets document and exports each sheet to a separate CSV file.

## AWS S3 API examples

### s3_test.py

Uploads a local file to an S3 bucket.

### gsheets_s3.py

- Exports all of the sheets from a Google Scheets document to CSVs.
- Uploads the CSVs to an S3 bucket.
- Deletes the local CSVs.

... and more to come!

## Setup instructions

To run these functions, you need an account with Google Cloud Platform (GCP) as well as an Amazon Web Services (AWS) account. Setting up the GCP account also entails defining an "organization," which defines its members' access to GCP services and resources. These include access keys and tokens that are stored in files named client_secrets.json, credentials.json, storage.json and token.json. Setting up an GCP organization is a bit complicated and requires owning a domain with its own email addresses so you can send and receive confirmation emails.

Setting up the AWS account also requires some work to set up user accounts and credentials, which can be stored locally on your laptop inside an invisible directory named .aws.

Setting up accounts, permissions and credentials is possibly the most time-consuming and difficult part of using GCP and AWS services. In my experience, AWS has better and more consistent documentation, whereas GCP's documentation often seems messy, with many documentation pages containing out-of-date information. This is one of the reasons why I tend to prefer AWS over GCP.

1. Clone this repo
1. Set up an account, organization, user account and credentials with Google Cloud Platform
1. Set up an account, S3 bucket, user account and credentials with Amazon Web Services
1. Install necessary Python requirements (Python 3, plus the packages listed in requirements.txt)
1. Add user access keys and tokens to your local clone of the repo.

To install python packages:
```
pip install <package_name>
```
## Running the scripts

To run the python scripts in this repo:
```
python quickstart.py
python gsheets_gem.py
python s3_test.py
python gsheets_s3.py
```
