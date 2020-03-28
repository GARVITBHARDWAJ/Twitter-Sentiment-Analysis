from VaderFile import sentiment_analyzer_scores
#sentence = "Our country is suffering from cancer"
#sentiment_analyzer_scores(sentence)
import tweepy
import time
import csv
import json
access_token  = "991533423419379712-8Fe9nVX28s1pTa6mJZKhJ0D048J1DKl"
access_token_secret = "7FrIjtNLhOjtiBV67LUBvS1yR5X5kSPHnTwqdFinDkpTF"
consumer_key = "jFGZhbkfDXp7qMqCF36qB6nef"
consumer_secret = "lu9ATF5y03U79suFSN6FGJo4jkpyUEW6z0XnirsxiLQeT3YEvc"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.get_user( screen_name = "_garvitbhardwaj")
print (user.followers_count)
print (user.friends_count)


trends = api.trends_place(1)
data = trends[0]
trends = data['trends']
for trend in trends:
    result = sentiment_analyzer_scores(trend['name'])
    print(trend['name'] + '   ' + str(trend['tweet_volume']) + '  ' + result + '\n')
"""
names =  [trend['name'] for trend in trends]
number = [trend['tweet_volume'] for trend in trends]
trends_name = ' \t'.join(names)
tweet_number = '\t'.join(str(number))
print(trends_name + tweet_number)
"""
search_hashtag = tweepy.Cursor(api.search, q = 'coronavirus').items(20)
for tweet in search_hashtag:
    with open('u.csv','w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([tweet.text.encode('utf-8')])
with open('u.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile,delimiter='\n')
    st = ""
    for row in spamreader:
        ','.join(row)
        print(row)
        for els in row:
            st = st + els
"""

    ##print json.dumps(tweet)
##print json.dumps(trends, indent = 1)
   ## print json.dumps(tweet)
##print json.dumps(trends, indent=1)


"""
print("\n")
User = "@narendramodi"
tweets = api.user_timeline( User, count = 100, tweet_mode = 'extended')
tw = ""
print("Sentiment Analysis of "+ " "+ User + " " + "is :")
for t in tweets:
    tw = tw + t.full_text
result = sentiment_analyzer_scores(tw)
print(result)


