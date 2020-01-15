from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html',{'hiMan':"I'm 20yr old"}) #the third argument is a python dictionary

def eggs(request):
    return HttpResponse('eggs are great')

def count(request):
    fulltext = request.GET['fulltext'] #gives the words from the url of count.html
    wordlist = fulltext.split() #the work of .split() is to seperate each word from one another in order to count them

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #increase 
            worddictionary[word] += 1
        else:
            #add to dictionary
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key = operator.itemgetter(1), reverse=True)

    return render(request,'count.html',{'FULLTEXT':fulltext,'countthewords':len(wordlist),'sortedwords':sortedwords})

def about(request):
    return render(request,'about.html')
