from twython import TwythonStreamer
>>> c_k="****************"
>>> c_s="*************************"
>>> a_t="********************************************"
>>> a_s="**********************************************"
# The Above 4 variables are actually 4 keys unique for each person using Twitter Api;
#Hence I hid it
>>> c=0

>>> def found():
...     global c
...     c=c+1
...     if ( c > 2  ):
...             print "Ian G. Harris is popular!/ Any Message you wanna Tweet!"
... 

>>> class MyStreamer(TwythonStreamer):
...     def on_success(self,data):
...             if 'text' in data:
...                     found()
... 

>>> stream=MyStreamer(c_k,c_s,a_t,a_s)
>>> stream.statuses.filter(track="Ian G. Harris/Any Search String On Your Twitter Page")

Ian G. Harris is popular! #OUTPUT For Third time
Ian G. Harris is popular! #OUTPUT for Fourth time
