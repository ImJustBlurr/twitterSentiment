# Twitter Sentiment Analyzer
This project allows you to gather recent tweets about a subject of your choice and analyze the sentiment behind it. 
It uses a combination of the Twitter API, tweepy, and TextBlob to accomplish this. 

## Setting it up
You will need to do a few things before running the program.

* First, you will need to set up your `config.py` file. This file will contain all of your keys from the Twitter API.
```
api_key='api-key-here'
api_key_secret='api-key-secret-here'

access_token='access-token-here'
access_token_secret='access-token-secret-here'

bearer_token='bearer-token-here'
```
* Then, you will need to intall your dependencies. Do this by running these commands seperately in your command prompt.
```
pip install tweepy
pip install pandas
pip install textblob
```

## Note
You can edit the amount of tweets you gather by changing the `max_results` in `main.py`
```
tweetSet = Client.search_recent_tweets(tweetSubject, max_results=30)
```
