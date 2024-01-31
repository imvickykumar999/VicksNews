
from django.shortcuts import render
import requests, random, datetime


def get_news(source, api_key='e1b57251b1b94ed894f3c60d25551eb2'):
    try:
        gets = f'https://newsapi.org/v1/articles?source={source}&sortBy=top&apiKey={api_key}'
        req = requests.get(gets)
        box = req.json()['articles']

    except:
        gets = f'https://newsapi.org/v1/articles?source={source}&sortBy=top&apiKey=5f69434d32434ea8bdb16b347f71cca2'
        req = requests.get(gets)
        box = req.json()['articles']
    
    print(box)
    return box


def good_day():
    currentTime = datetime.datetime.now() + datetime.timedelta(hours=6)

    if currentTime.hour < 12:
        return 'Good morning'
    elif 12 <= currentTime.hour < 18:
        return 'Good afternoon'
    else:
        return 'Good evening'
    
def index(request):
    source = ['bbc-news', 'cnn', 'the-verge', 'time', 'the-wall-street-journal']
    source = random.choice(source)

    data = get_news(source)
    return render(request, "main/index.html", 
        {
            'data' : data, 
            'good' : good_day()
        }
    )
