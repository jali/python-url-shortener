# Python base60 URL shortener

Just a small python class for a base60 URL shortener

###### Why base60?

I'm removing uppercase i, o and lowercase L to prevent confusion when reading the short url.


###### In order to test this

```
from shortener import Shortener
short = Shortener()
s = short.shorten('http://google.com')
print s
l = short.expand(s)
print l
```
