import nltk 
import json 
import re
import string
from operator import itemgetter
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

#very similar to bigrams_separate.py but now taking out stop words...

def read_dataset(path):
    reviewdataset=[]
    with open(path) as f:
        for line in f:
            reviewdataset.append(json.loads(line))
    return reviewdataset
    
    

def get_topbigrams(reviewdataset):
    initflag = 0
#    tokenizer = RegexpTokenizer(r'\w+')
#    print stopwords.words("english")
    for review in reviewdataset:        
        textblock = review['text']
#        tokens = tokenizer.tokenize(textblock)
#        words = [w for w in words if not w in stopwords.words("english")]
        tokens = [word.strip(string.punctuation) for word in textblock.split(' ')]
        tokens = [f for f in tokens if f]
        tokens = [w.lower() for w in tokens]
        tokens = [w for w in tokens if not w in stopwords.words("english")]
 #       print 'and the tokens are'
 #       print tokens
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

    pattern = ['my kid', 'my kids', 'my son', 'my sons', 'my daughter', 'my daughters', 'my baby', 'my babies', 
 		   'my child', 'my children', 'my baby', 'our kid', 'our kids', 'our son','our sons', 'our babies',
 		   'our daughter','our daughters','our son and daughter', 'our daughter and son', 'my wife and son', 'my wife and sons', 'my wife and daughter', 
 		   'my wife and daughters', 'my wife and kids', 'my husband and son', 'my husband and sons', 'my husband and daughter', 
 		   'my husband and daughters', 'my husband and kids', 'my hubby and son', 'my hubby and sons', 'my hubby and daughter', 
 		   'my hubby and daughters', 'my hubby and kids', 'i\'m a parent', 'as a parent', 'i am a parent', 'i have kids'] #using a broader range of kid words to test them out... many of these are optional and can be commented out.


 #   pattern = ['my kid', 'my kids', 'my son', 'my sons', 'my daughter', 'my daughters', 'my babies', 'my child', 'my children', 'my baby']
    combined = "(" + ")|(".join(pattern) + ")"
#    tokenizer = RegexpTokenizer(r'\w+')
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
    print 'starting here'

    f=open("bigramsdiff_fullset_stopsremoved_june17.csv", 'w')
    for item in difflist:
        f.write(item[0][0].encode('utf8')+' '+item[0][1].encode('utf8')+','
        +str(item[1]).encode('utf8')+'\n') #printing both elements of the tuple 
         #and then the string of the number
    f.close()
    
    
    
