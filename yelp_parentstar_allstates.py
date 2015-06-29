import codecs
import json
import numpy as np 
import scipy as sp
import matplotlib.pyplot as plt 
import matplotlib
#from sklearn.ensemble import RandomForestClassifier
#from sklearn import svm 
#from sklearn.naive_bayes import GaussianNB 
from numpy import genfromtxt, savetxt
import csv

#to make a bar plot showing difference in parent and all reviews...

pstars = [3.74, 3.72, 3.71, 3.71, 3.78, 3.67]
astars = [3.77, 3.72, 3.75, 3.70, 3.77, 3.71]



diff = [ -0.04,-0.04,-0.03, 0.0, 0.01, 0.01] #from sql queries


tries = [0,1,2,3,4,5]#,7,8,9,10,11,12]
tries2 = [0.5, 1.5,2.5,3.5,4.5,5.5]

matplotlib.rcParams.update({'font.size': 18})

#xlabels = ['Las Vegas',,'Urb-Chpgn','Pittsburgh',]
xlabels = ['Madison','Charlotte','Phoenix', 'Las Vegas','Urb-Chpgn','Pittsburgh'] 

width=0.4
#plt.bar(tries,pstars,width,color='blue')
#plt.bar(tries2,astars,width,color='black')
plt.bar(tries, diff, color='blue')
#plt.plot(tries, pstars, color='blue', linestyle='dashed', marker='*', markerfacecolor='blue', markersize=8) 
#plt.plot(tries, astars, color='black', linestyle='solid', marker='o', markerfacecolor='black', markersize=8)
plt.xticks(tries,xlabels,rotation='45')
plt.margins(0.2)
#plt.axhline(y=coo,color='black')
plt.subplots_adjust(bottom=0.25, left=0.25)
#plt.ylim([0,0.3])
#plt.legend(['Parents','All'])

#plt.ylim((3.5,3.9))
plt.ylabel(r'Diff from Average Rating')
plt.xlabel(r'City')
plt.title(r'How Are Parents Reviewing?')


#plt.show()

filepath='/Users/aford/yelp/figures/'
filename='yelpstars3'+'.ps'
filenamefoo=filepath+filename
plt.savefig(filenamefoo,bbox_inches=0)

plt.show()
#plt.savefig(filenamefoo,bbox_inches=0)

 #     mylabels = ['all','yeses','nos']
    
 #     plt.clf() #seem to need to clear the plot 
 #     #plt.hist([feature,yeses,nos],normed=1,label=mylabels)#,bins=fbins)
 #     plt.hist([feature,yeses,nos],normed=1,label=mylabels,bins=fbins)#,bins=fbins
 #     plt.legend()
#      plt.xlabel(f)
#      plt.ylabel(r'normalized # of requests')
#      filepath='/Users/aford/datsci/figures/'
#      filename=progress+'.ps'
#      filenamefoo=filepath+filename
#      plt.savefig(filenamefoo,bbox_inches=0)
 #     plt.clf()





