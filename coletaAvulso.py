from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

consumer_key="IG30duiFxhJNbSp4lH6zKa1Da"
consumer_secret="YGSbNItM2y3TAGojUa2a4DzZ0FL3PsbZpeRsbtnV22tT96XiOs"

access_token="4189851514-2uAkkD1quBEUSn42aPPrOmrZ4ioJI6IpUIxlZuF"
access_token_secret="SYXpsShbJqFeXNL18PQuUfoi9knEQ8Z4xLTQavpxkniDH"
lista = []
class StdOutListener(StreamListener):

    def on_status(self, status):
        data = status.user.screen_name+'|||'+status.text+'|||'+str(status.created_at)
        print(data)
        lista.append(data)
        with open('gravaColeta2.txt', 'w') as save:
            save.writelines(lista)
        return True 
	    
        #with open('grava.txt', 'w') as f:
        #    f.write(lista)
        

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    s = stream.filter(track=['suicidio'], languages=['pt'])
    
#    with open('grava2.txt', 'w') as f:
 #       f.writelines(s)
