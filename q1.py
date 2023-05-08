import pandas as pd 
import matplotlib.pyplot as plt 
import requests

session = requests.Session()
response = session.get('https://www.thehivelaw.com/blog/how-often-do-planes-crash-statistics-how-many-planes-crash-a-year', headers={'User-Agent': 'Mozilla/5.0'})

print(response.status_code)

dfs = pd.read_html(response.text)
print(dfs)