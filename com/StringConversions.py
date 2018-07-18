from urllib.request import urlopen

myurl = "http://www.google.com/"
print(myurl)
mylist = [myurl]
mydict = {}
for i in mylist:
    print(i)
    mydict = {"url":i}

print(mydict["url"])
print(mydict)
mytouple = (mydict["url"],mydict["url"])

urlString = ''.join(mytouple[0])
print(urlString)
urlopen(urlString)
