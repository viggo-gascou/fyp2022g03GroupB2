import contractions
import numpy as np
import regex as re


NORMALIZATIONS = {
    "w/": "with",
    "w/o": "without"
}


def preprocess(text):
    link_normalize = re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+|www\.\w+\.\w{3}")
    text = re.sub(link_normalize, "@link", text)
    punct_normalize = re.compile(r"([!,.?]{3})[!,.?]+")
    text = re.sub(punct_normalize, r"\1", text)
    tweets = np.array(text.split("\n"))
    new_tweets = []
    for i, tweet in enumerate(tweets):
        word_list = []
        for word in tweet.split(" "):
            word = contractions.fix(word.lower())
            word_list.append(NORMALIZATIONS.get(word, word))
        tweet = " ".join(word_list)
        new_tweets.append(tweet)
    return np.asarray(new_tweets)

def preprocess_tweet(tweet):
    tweet = re.sub("@\w+", "@user", tweet)
    tweet = re.sub("\n", " ", tweet)
    link_normalize = re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+|www\.\w+\.\w{3}")
    tweet = re.sub(link_normalize, "@link", tweet)
    punct_normalize = re.compile(r"([!,.?]{3})[!,.?]+")
    tweet = re.sub(punct_normalize, r"\1", tweet)
    word_list = []
    for word in tweet.split(" "):
        word = contractions.fix(word.lower())
        word_list.append(NORMALIZATIONS.get(word, word))
    return " ".join(word_list)