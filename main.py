#Imports Dependencies
import config #your config file will contain your different tokens from the twitter api
import tweepy
import pandas
from textblob import TextBlob

#Initializes our tweepy client
Client = tweepy.Client(config.bearer_token,
    consumer_key=config.api_key,
    consumer_secret=config.api_key_secret,
    access_token=config.access_token,
    access_token_secret=config.access_token_secret)

#Asks user for their subject
tweetSubject = input('Enter a one-word subject for your tweets. This word will be used to search for tweets containing your subject matter.\n')

#Searches recent tweets on twitter
tweetSet = Client.search_recent_tweets(tweetSubject, max_results=30)

#Initializes our lists
tweetList = []
polarityList = []
subjectivityList = []

#Loops through all of the tweets gathered and adds them to their designated lists    
for tweet in tweetSet.data:
    analyze = TextBlob(tweet.text)

    if (analyze.sentiment.polarity and analyze.sentiment.subjectivity) == 0.000000: #getting rid of the outlier tweets that textblob analyzes
        continue
    
    tweetList.append(tweet.text)
    polarityList.append(analyze.sentiment.polarity)
    subjectivityList.append(analyze.sentiment.subjectivity)

#Setting up the pandas DataFrame
data = {'Tweets':tweetList, 'Polarity':polarityList, 'Subjectivity':subjectivityList}
dataFrame = pandas.DataFrame(data)

#Calculating the averages of the polarity and subjectivity values
avgPolarity = dataFrame['Polarity'].mean()
avgSubjectivity = dataFrame['Subjectivity'].mean()

#Analyzing the averages
polarityAnalysis = ''
subjectivityAnalysis = ''

if avgPolarity > 0:
    polarityAnalysis = '(Relatively Positive)'
else:
    polarityAnalysis = '(Relatively Negative)'

if avgSubjectivity > 0.5:
    subjectivityAnalysis = '(Relatively Subjective)'
else:
    subjectivityAnalysis = '(Relatively Objective)'    

#Displaying our data and analysis
print(dataFrame)
print(f'\nAVERAGES & ANALYSIS OF RECENT TWEETS CONTAINING THE WORD {tweetSubject.upper()}:\n{polarityAnalysis} Polarity: {avgPolarity}\n{subjectivityAnalysis} Subjectivity: {avgSubjectivity}')
input('Press ENTER to exit') 