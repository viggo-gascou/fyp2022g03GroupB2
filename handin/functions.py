import contractions
import numpy as np
import regex as re


# Dictionary for normalizing certain tokens
NORMALIZATIONS = {
    "w/": "with",
    "w/o": "without"
}


def preprocess(text):
    """Preprocesses a string of tweets separated by newlines for use with the classifier
    Input: String of tweets separated by newlines
    Output: 1-dimensional numpy array with 1 tweet per element
    """
    # Normalize links to @link
    link_normalize = re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+|www\.\w+\.\w{3}")
    text = re.sub(link_normalize, "@link", text)
    # Normalize any number of .,!? to only 3
    punct_normalize = re.compile(r"([!,.?]{3})[!,.?]+")
    text = re.sub(punct_normalize, r"\1", text)
    tweets = np.array(text.split("\n"))
    new_tweets = []
    # Go through one tweet at a time, split at space. Expand contractions and normalize words in dictionary
    for i, tweet in enumerate(tweets):
        word_list = []
        for word in tweet.split(" "):
            word = contractions.fix(word.lower())
            word_list.append(NORMALIZATIONS.get(word, word))
        tweet = " ".join(word_list)
        new_tweets.append(tweet)
    return np.asarray(new_tweets)


def preprocess_tweet(tweet):
    """Preprocessees a single tweet for use with the classifier
    Input: A string containing a single tweet
    Ouput: A string containing a single tweet"""
    # Normalize @ mentions to @user
    tweet = re.sub("@\w+", "@user", tweet)
    tweet = re.sub("\n", " ", tweet)
    # Normalize links to @link
    link_normalize = re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+|www\.\w+\.\w{3}")
    tweet = re.sub(link_normalize, "@link", tweet)
    # Normalize any number of .,!? to only 3
    punct_normalize = re.compile(r"([!,.?]{3})[!,.?]+")
    tweet = re.sub(punct_normalize, r"\1", tweet)
    word_list = []
    # Go through each word in the tweet and expand contractions and normalize word according to the dictionary
    for word in tweet.split(" "):
        word = contractions.fix(word.lower())
        word_list.append(NORMALIZATIONS.get(word, word))
    return " ".join(word_list)