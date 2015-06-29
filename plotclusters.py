from pylab import plot, show
from numpy import vstack, array
from numpy.random import rand
from scipy.cluster.vq import kmeans, vq
from numpy import zeros
import sys
import matplotlib.pyplot as plt
import math

#point of this plot is to visualize some clusters
#develop some intuition if k-means clustering would be a reasonable approach here. 

import json 

def readfile(path):
     userdata = json.loads(open(path).read())
     print 'got the userdata, length is'
    # print userdata
     return userdata
     
     
def readparentfile(parentpath):
     parentuserdata = json.loads(open(parentpath).read())
     print 'got the parent userdata, length is'
     return parentuserdata


if __name__ == '__main__':
    #path = './parentshort.json'
    path = '/Users/aford/yelp/us_fulluserdataset_june9.json' #these files created from earlier scripts, I believe create_dict4.py and create_dict_defparents.py
    parentpath = '/Users/aford/yelp/us_morelikelyparents.json'
    
    
#MAYBE parent dataset  
#maybe parents defined as parents that used kid words or reviewed a kid business
    maybeparentlist=[]
    
    maybeparentuserdata = readparentfile(parentpath)
    for keys, values in maybeparentuserdata.iteritems():
        if (values[0] >= 1) or (values[2] >= 1): #values[0] is kid words, values[2] is kid businesses
            maybeparentlist.append(keys)
            
#DEF parent dataset  
#defined as using kid words

    defparentlist=[]
    
    defparentuserdata = readparentfile(parentpath)
    for keys, values in defparentuserdata.iteritems():
        if (values[0] >= 1): #kid words are present
            defparentlist.append(keys)
          
#total dataset
    
    kw = [] #kid words
    tw = [] #total words
    kc = [] #count of kid business categories
    tc= [] #total count of all businesses
    
    userdata = readfile(path)
    for keys, values in userdata.iteritems():
        kw.append(values[0]) #this is the number of 'kid words' 
        tw.append(values[1])
        kc.append(values[2])
        tc.append(values[3])
        
    print 'total length of json file is'
    print len(kw)
        
    X = []
    Y = []
    
    Xm = []
    Ym = []
    
    Xd = []
    Yd = []
    
    for i in range(0,len(kw)):
        
        #X.append(math.log10(kw[i] if kw[i]>0 else 1)) #LOG
        X.append(kw[i] if kw[i]>0 else 1) #not log
        Y.append(kc[i]/float(tc[i]))
    
    for maybeparent in maybeparentlist:
        if maybeparent in userdata:
            values=userdata[maybeparent]
            #Xm.append(math.log10(values[0] if values[0]>0 else 1)) #LOG
            Xm.append(values[0] if values[0]>0 else 1) #notlog 
            Ym.append(values[2]/float(values[3]))
            
    for defparent in defparentlist:
        if defparent in userdata:
            values=userdata[defparent]
 #           Xd.append(math.log10(values[0] if values[0]>0 else 1)) #LOG
            Xd.append(values[0] if values[0]>0 else 1) #notlog
            Yd.append(values[2]/float(values[3]))
    
    print 'but I\'m only reading in'
    print len(X)
    print len(Y)
    
    print 'of those only this many MAYBE parents'
    print len(Xm)
    
    print 'and this many are DEFINITELY parents'
    print len(Xd)
    
    
    
    #plt.clf()
    fig=plt.figure()
    ax1=fig.add_subplot(131)
    ax2=fig.add_subplot(132)
    ax3=fig.add_subplot(133)

    ax1.scatter(X,Y,s=10,marker='o',c='b',label='all')
    ax2.scatter(Xm,Ym,s=10,marker='+',c='r',label='maybe parents')
    ax3.scatter(Xd,Yd,s=10,marker='^',c='g',label='def parents') 
    #plt.title(r'June 11')
    ax2.set_xlabel(r'Number Kid Words')
    ax1.set_ylabel(r'Fraction Kid Categories')
    
 #   ax1.set_xlim([-0.01,300])
 #   ax2.set_xlim([-0.01,300])
 #   ax3.set_xlim([-0.01,300])
    
    ax1.set_ylim([-0.01,1.01])
    ax2.set_ylim([-0.01,1.01])
    ax3.set_ylim([-0.01,1.01])
    
    ax1.set_title('All Users')
    ax2.set_title('Maybe Parents')
    ax3.set_title('Definitely Parents')
    
    
    #plt.xlim([-0.,0.01])
    #plt.ylim([-0.05,0.4])
    #plt.legend(loc='upper left');
    
    plt.show()

    #plt.clf()
    
    filename = '/Users/aford/yelp/clusters_june11_notlog.ps' #also generates clusters_june11.ps, which is log...
    plt.savefig(filename,bbox_inches=0)
    
    plt.clf()
    

  
