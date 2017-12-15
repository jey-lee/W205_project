from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()
        self.conn = self.conn = psycopg2.connect(database ="tcount", user ="postgres", password ="pass", host = "localhost", port ="5432")


    def process(self, tup):
        tweet = tup.values[0]
        score = tup.values[1]
        # Increment the local count
        self.counts[tweet] += 1
        self.emit([tweet,score])

        # Log the count - just to see the topology running
        #self.log('%s: %d' % (word, self.counts[word]))

        cur = self.conn.cursor()
        cur.execute("INSERT INTO tweetmonitor (tweet,score) VALUES (%s, %s)", (tweet,score))

        self.conn.commit()

