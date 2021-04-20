from gsheets import Sheets

sheets = Sheets.from_files('client_secrets.json', 'storage.json')
url = 'https://docs.google.com/spreadsheets/d/1vljuE6-M-e1VKmfhzQGkYrZFNgzUgWM0-xNzxJwme2k'

# https://docs.google.com/spreadsheets/d/1vljuE6-M-e1VKmfhzQGkYrZFNgzUgWM0-xNzxJwme2k
# /edit?ts=60766e34#gid=1902486401
s = sheets.get(url)
csv_name = lambda infos: '%(title)s - %(sheet)s.csv' % infos
s.to_csv(make_filename=csv_name)
