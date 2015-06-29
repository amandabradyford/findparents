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


#from sql query 
pstarsAZ = [3.66, 3.93, 3.67, 3.98]
astarsAZ = [3.69, 3.99, 3.73, 3.89]

pstarsNV = [3.64, 3.95, 3.68, 3.78] 
astarsNV = [3.62, 4.00, 3.71, 3.71]

pstarsWI = [3.57, 3.43, 3.62, 4.31] 
astarsWI = [3.66, 3.65, 3.70, 4.17]
diffWI = [-0.44, -0.22, -0.19, -0.09,-0.09,-0.08, 0.06,0.14, 0.26]  #in different order than above

pstarsPA = [3.56, 4.03, 3.71, 4.11]
astarsPA = [3.61, 4.09, 3.72, 4.06]

pstarsNC = [3.55, 3.76, 3.60] #0]
astarsNC = [3.54, 3.85, 3.67] #0]


#astarsAZ = [3.77, 3.72, 3.75, 3.70, 3.77, 3.71]

matplotlib.rcParams.update({'font.size': 17})

tries = [0,1,2,3,4,5,6,7,8]#,7,8,9,10,11,12]

xlabels = ['Museums','Ice Cream', 'Pizza', 'Bars','Nightlife','Restaurants','Coffee & Tea','Zoos','Hotels & Travel']

plt.bar(tries, diffWI, color='blue') 
#plt.plot(tries, pstarsAZ, lw=0, color='blue', marker='*', markerfacecolor='blue', markersize=8) 
#plt.plot(tries, astarsAZ, lw=0, color='blue', marker='o', markerfacecolor='blue', markersize=8)
##plt.plot(tries, pstarsNV, lw=0, color='black', marker='*', markerfacecolor='black', markersize=8) 
#plt.plot(tries, astarsNV, lw=0, color='black',marker='o', markerfacecolor='black', markersize=8)
#plt.plot(tries, pstarsWI, lw=0, color='red', marker='*', markerfacecolor='red', markersize=8) 
##plt.plot(tries, astarsWI, lw=0, color='red', marker='o', markerfacecolor='red', markersize=8)
#plt.plot(tries, pstarsPA, lw=0, color='orange', marker='*', markerfacecolor='orange', markersize=8) 
#plt.plot(tries, astarsPA, lw=0, color='orange', marker='o', markerfacecolor='orange', markersize=8)


plt.xticks(tries,xlabels,rotation=60)
plt.margins(0.3)
#plt.axhline(y=coo,color='black')
plt.subplots_adjust(bottom=0.25)
#plt.legend(['Parents','All'])

plt.ylabel(r'Diff From Average Rating')
#plt.xlabel(r'Category')
plt.title(r'Parent Reviews (Wisconsin)')

#plt.show()

filepath='/Users/aford/yelp/figures/'
filename='parentdiffWI'+'.ps'
filenamefoo=filepath+filename
plt.savefig(filenamefoo,bbox_inches=0)

plt.show()


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





