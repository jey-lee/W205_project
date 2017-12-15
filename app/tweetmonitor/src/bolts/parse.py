from __future__ import absolute_import, print_function, unicode_literals

import re
from streamparse.bolt import Bolt

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

################################################################################
# Function to check if the string contains only ascii chars
################################################################################
def ascii_string(s):
  return all(ord(c) < 128 for c in s)

class ParseTweet(Bolt):

    def initialize(self, conf, ctx):
        self.conn = self.conn = psycopg2.connect(database ="tcount", user ="postgres", password ="pass", host = "localhost", port ="5432")

    def process(self, tup):
        tweet = tup.values[0]  # extract the tweet

        # Split the tweet into words
        words = tweet.split()

        # Filter out the hash tags, RT, @ and urls
        valid_words = []
        for word in words:
            self.log('%s ' % word)

            # Filter the hash tags
            if word.startswith("#"): continue

            # Filter the user mentions
            if word.startswith("@"): continue

            # Filter out retweet tags
            if word.startswith("RT"): continue

            # Filter out the urls
            if word.startswith("http"): continue

            # Strip leading and lagging punctuations
            aword = word.strip("\"?><,'.:;)")

            # now check if the word contains only ascii
            if len(aword) > 0 and ascii_string(word):
                valid_words.append([aword])

        if not valid_words: return

        # Check sentiment score for each valid word
        tweet_score = 0
        cnt = 0
        for valid_word in valid_words:
            cur = self.conn.cursor()
            cur.execute("SELECT score FROM review_words_avg WHERE word=%s AND count > 100",valid_word)
            records = cur.fetchall()
            word_score = 0
            if cur.rowcount == 0:
                word_score = 0
            else:
                for rec in records:
                    cnt = cnt + 1
                    word_score = word_score + float(rec[0])
        if cnt != 0:
            tweet_score = round(word_score/cnt, 5)

        # Log the tweet and score
        self.log('%s : %f' % (tweet.encode("utf-8"), tweet_score))

        # Emit all the words
        self.emit_many(valid_words)

        # tuple acknowledgement is handled automatically
