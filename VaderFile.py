from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

def sentiment_analyzer_scores(sentence):
    score = analyzer.polarity_scores(sentence)
    if score['compound']>=0.20:
        return "POSITIVE"
    elif score['compound']<=-0.20:
        return "NEGATIVE"
    else:
        return "NEUTRAL"
