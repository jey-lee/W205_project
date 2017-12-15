import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect(database ="tcount", user ="postgres", password ="pass", host = "localhost", port ="5432")
cur = conn.cursor()

if len(sys.argv) == 2:
    word = sys.argv[1]
    cur.execute("SELECT word, count, score  from review_words_avg where word = %s", (word,))
    records = cur.fetchall()

    if len(records) == 0:
        print "The word <",word,"> is not found in our database."
    for rec in records:
        print "Total number of occurrences of \"", rec[0], "\":", rec[1]
        print "Sentiment score of \"", rec[0], "\":", rec[2]

    conn.commit()
    conn.close()
    exit(1)

else:
    print 'Please add one argument.'
    exit(1)
