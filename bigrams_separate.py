import nltk 
import json 
import re
import string
from operator import itemgetter
from nltk.tokenize import RegexpTokenizer

#this program attempts to find bigrams that may separate parents from non-parents

#read in data set
def read_dataset(path):
    reviewdataset=[]
    with open(path) as f:
        for line in f:
            reviewdataset.append(json.loads(line))
    return reviewdataset
    
#get the most common bigrams used in reviews    
def get_topbigrams(reviewdataset):
    initflag = 0
#    tokenizer = RegexpTokenizer(r'\w+')

    for review in reviewdataset:        
        textblock = review['text']
#        tokens = tokenizer.tokenize(textblock)
        tokens = [word.strip(string.punctuation) for word in textblock.split(' ')] #strip punctuation
        tokens = [f for f in tokens if f]
        tokens = [w.lower() for w in tokens] #make all lowercase
        bgs = nltk.bigrams(tokens)
        if initflag == 0:
            fdist = nltk.FreqDist(bgs)
            initflag = 1
        else:
            for b in bgs:
                if b in fdist:
                    fdist[b] += 1./len(tokens)
                else:
                    fdist[b] = 1./len(tokens) #adds an item with key b and value 1  #
                    
    sortedlist=sorted(fdist.items(), key=itemgetter(1), reverse=True)
    sortedlist=sortedlist[0:500] #includes tuple (bigrams) and count                    
    fdist_sliced = {}
    for item in sortedlist:
#        print item
        fdist_sliced[item[0]]=item[1]                              
    return fdist_sliced 
    
def subtract_bigrams(reviewdataset, fdist):
    print 'fdist is'
    print len(fdist)
    #our kids???
    #for this first pass, use a limited set of "kid words"
    pattern = ['my kid', 'my kids', 'my son', 'my sons', 'my daughter', 'my daughters', 'my babies', 'my child', 'my children', 'my baby']
    combined = "(" + ")|(".join(pattern) + ")"
#    tokenizer = RegexpTokenizer(r'\w+')

#create dictionaries for parents and for an unknown class (maybe parents, maybe not)
    parentdict = {}
    unknowndict = {} 
    for k,v in fdist.items():
        parentdict[k]=0
        unknowndict[k]=0
    print 'length of parent dict'
    print len(parentdict)
    print 'length of non parent dict'
    print len(unknowndict)
    for review in reviewdataset:
        textblock = review['text']
        tokens = [word.strip(string.punctuation) for word in textblock.split(' ')]
        tokens = [f for f in tokens if f]
        #tokens = tokenizer.tokenize(textblock)
        tokens = [w.lower() for w in tokens]
     #   print 'AND THE TOKENS ARE-----'
     #   print tokens
        bgs = nltk.bigrams(tokens)
        match = re.search(combined, textblock)
        if match:
           # print match.group()
            for b in bgs:
                if b in parentdict:
                    parentdict[b] += 1./len(tokens)
                    
        else:
            #print 'no match here'
            for b in bgs:
                if b in unknowndict:
                    unknowndict[b] += 1./len(tokens)
#quantify the difference in frequency between bigrams used in parent and unknown set...
    difflist = []
    for k,v in parentdict.items():    
    #    print parentdict[k] - unknowndict[k]
        difflist.append((k,str(parentdict[k] - unknowndict[k])))
    difflist=sorted(difflist,key=itemgetter(1))

    print difflist
    return difflist        

if __name__ == '__main__':
 #   reviewpath = './review1k.json'
 #   reviewpath = './review10k.json'
    reviewpath = './yelp_academic_dataset_review.json'
    reviewdataset=read_dataset(reviewpath)
    bigramdict=get_topbigrams(reviewdataset)
    difflist = subtract_bigrams(reviewdataset,bigramdict)

    f=open("bigramsdiff_fullset.csv", 'w') #print out the top bigrams and the difference between parents and unknown class...
    for item in difflist:
        f.write(item[0][0].encode('utf8')+' '+item[0][1].encode('utf8')+','
        +str(item[1]).encode('utf8')+'\n') #printing both elements of the tuple 
         #and then the string of the number
    f.close()
    
    
    