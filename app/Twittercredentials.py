import tweepy

consumer_key = "w3lp51vcD8h4UKuXEUFX8y7OW";
#eg: consumer_key = "YisfFjiodKtojtUvW4MSEcPm";


consumer_secret = "QnivYtWPOFebYIouy4F2ZMLWNTSJ4JMWdC5R9jez4JNey2czdy";
#eg: consumer_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token = "58357218-XObIYB1I3ZSyt6Y8YcX7mwSL7dexCpAM9Fb017cNF";
#eg: access_token = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token_secret = "WcCY2p6YxhAgFQGU7eKOTuBUOz2t75Bq5tl7N0NdP6D4N";
#eg: access_token_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



