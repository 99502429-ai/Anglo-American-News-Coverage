import feedparser
import pandas as pd
import json
from datetime import datetime

with open('feeds.json', 'r') as f:
    feeds = json.load(f)

fox_feed = feedparser.parse(feeds['fox_latest'])

titles = []
links = []
contents = []
publish_dates = []
if fox_feed.status == 200:
    for entry in fox_feed.entries:
        publish_dates.append(datetime.strptime(entry.published, "%a, %d %b %Y %H:%M:%S %z").date())
        contents.append(entry.content[0]['value'])
        links.append(entry.link)
        titles.append(entry.title)

df = pd.DataFrame({
    "title": titles, 
    "text": contents,
    "link": links,
    "publish_date": publish_dates
    })
df.to_csv(f"data/fox_latest_{datetime.now()}.csv")