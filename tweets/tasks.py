import csv
import re

from celery import shared_task

from tweets.models import Tweet, Link



myString = "These are the links http://www.google.com  or https://mango.com/wep however that's not all"
print(re.findall(r'(https?://[^\s]+)', myString))

# @shared_task
def get_published_tips():
    count = Tweet.objects.count()
    path = 'python_tips.csv'
    with open(path, "r") as f:
        reader = csv.reader(f)
        next(reader) # skip header

        for row in [*reader][count:count+1]:
            tip = row[1]
            links = re.findall(r'(https?://[^\s]+)', tip)
            if links:
                Link.objects.create(link)

            tweet = Tweet.objects.create(timestamp=row[0], tip=row[1], author=row[2])


get_published_tips()



# links = models.ManyToManyField(Link)
# published = models.BooleanField(default=False)
