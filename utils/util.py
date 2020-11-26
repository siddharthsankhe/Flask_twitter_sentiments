import time
import re
import pandas as pd
import nltk
from nltk.stem.porter import *
from wordcloud import WordCloud, STOPWORDS
import seaborn as sns
sns.set()
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from utils import app
import os
import numpy as np
from PIL import Image
import seaborn as sns
import matplotlib.pyplot as plt
sns.set()

# from keras.preprocessing.text import Tokenizer
# from keras.preprocessing.sequence import pad_sequences
# from keras.utils import to_categorical
# tokenizer= Tokenizer(num_words=10000)
api_key=''
api_key_secrete=''
access_token='2183088190-'
access_token_secrete='Z'
import tweepy
from tweepy import OAuthHandler

def get_tweets(Para):
	auth = OAuthHandler(api_key, api_key_secrete)
	auth.set_access_token(access_token, access_token_secrete)
	args = [Para]
	api = tweepy.API(auth,timeout=10)

	list_tweets = []
	query = args[0]
	if len(args) == 1:
	    for status in tweepy.Cursor(api.search,q=query+" -filter:retweets",lang='en',result_type='recent').items(100):
	        list_tweets.append(status.text)
	return list_tweets

analyser = SentimentIntensityAnalyzer()

def get_sentiments(Para):

	score = analyser.polarity_scores(Para)
	neg = str(score['neg'])
	pos =str( score['pos'])
	if neg>pos:
		sentiments='negative'
	elif pos>neg:
		sentiments='positive'
	else:
		sentiments='neutral'
	return sentiments

def word_cloud(wd_list,Para):
    stopwords = set(STOPWORDS)
    all_words = ' '.join([text for text in wd_list])
    wordcloud = WordCloud(
        background_color='white',
        stopwords=stopwords,
        width=1600,
        height=800,
        random_state=21,
        colormap='jet',
        max_words=50,
        max_font_size=200).generate(all_words)
    
    plt.figure(figsize=(12, 10))
    plt.axis('off')
    #plt.imshow(wordcloud, interpolation="bilinear")
    picture_fn='2_'+str(Para)+'.png'
    picture_path = os.path.join(app.root_path, 'static', picture_fn)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.savefig(picture_path)
def get_stats(hash_tag):
	list_tweets=get_tweets(hash_tag)
	total_pos = 0
	total_neg = 0
	total_neu=0
	filter_tweets=[]
	pos_tweets=[]
	neg_tweets=[]
	neutral_tweets=[]
	for tweet in list_tweets:
	    tweet = re.sub(r"^https://t.co/[a-zA-Z0-9]*\s", " ", tweet)
	    tweet = re.sub(r"\s+https://t.co/[a-zA-Z0-9]*\s", " ", tweet)
	    tweet = re.sub(r"\s+https://t.co/[a-zA-Z0-9]*$", " ", tweet)
	    # tweet = tweet.lower()
	    # tweet = re.sub(r"that's","that is",tweet)
	    # tweet = re.sub(r"there's","there is",tweet)
	    # tweet = re.sub(r"what's","what is",tweet)
	    # tweet = re.sub(r"where's","where is",tweet)
	    # tweet = re.sub(r"it's","it is",tweet)
	    # tweet = re.sub(r"who's","who is",tweet)
	    # tweet = re.sub(r"i'm","i am",tweet)
	    # tweet = re.sub(r"she's","she is",tweet)
	    # tweet = re.sub(r"he's","he is",tweet)
	    # tweet = re.sub(r"they're","they are",tweet)
	    # tweet = re.sub(r"who're","who are",tweet)
	    # tweet = re.sub(r"ain't","am not",tweet)
	    # tweet = re.sub(r"wouldn't","would not",tweet)
	    # tweet = re.sub(r"shouldn't","should not",tweet)
	    # tweet = re.sub(r"can't","can not",tweet)
	    # tweet = re.sub(r"couldn't","could not",tweet)
	    # tweet = re.sub(r"won't","will not",tweet)
	    # tweet = re.sub(r"\W"," ",tweet)
	    # tweet = re.sub(r"\d"," ",tweet)
	    # tweet = re.sub(r"\s+[a-z]\s+"," ",tweet)
	    # tweet = re.sub(r"\s+[a-z]$"," ",tweet)
	    # tweet = re.sub(r"^[a-z]\s+"," ",tweet)
	    # tweet = re.sub(r"\s+"," ",tweet)
	    sent = get_sentiments(tweet)

	    if sent== 'positive':
	        total_pos += 1
	        filter_tweets.append(tweet)
	    elif sent=='negative':
	        total_neg += 1
	        filter_tweets.append(tweet)
	    else:
	    	total_neu+=1
	    	filter_tweets.append(tweet)
	    filter_tweets.append(tweet)

	
	objects = ['Positive','Negative','Neutral']
	y_pos = np.arange(len(objects))

	
	picture_fn='graph_'+str(hash_tag)+'.png'
	picture_path1 = os.path.join(app.root_path, 'static', picture_fn)

	plt.bar(y_pos,[total_pos,total_neg,total_neu],alpha=0.5)
	plt.xticks(y_pos,objects)
	plt.ylabel('Number')
	plt.title('Number of Postive and NEgative Tweets')

	plt.savefig(picture_path1)
	word_cloud(filter_tweets,hash_tag)

	

	
	

	return 'pos '+str(total_pos)+' total_neg '+str(total_neg)+'total_neu '+str(total_neu)




