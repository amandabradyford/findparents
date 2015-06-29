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

#got these from result of sql query, was too lazy to set up an automated sql query to do it but will next time.

previews = [153788.0, 123178.0, 5705.0, 1201.0, 7788.0, 20908.0]
areviews = [588893.0, 677525.0, 43584.0,12109.0, 65977.0, 95387.0]

foo=sum(previews)
print foo
boo=sum(areviews)


#ratio=[0.26, 0.18, 0.13, 0.099, 0.12, 0.22]
ratio=[0.26, 0.22, 0.18, 0.13, 0.12, 0.099] #reordered from largest to smallest % reviews

print previews
print areviews

tries = [0,1,2,3,4,5]#,7,8,9,10,11,12]


matplotlib.rcParams.update({'font.size': 18})

xlabels = ['Phoenix','Charlotte','Las Vegas','Madison', 'Pittsburgh','Urb-Chpgn']

#plt.plot(tries, ratio, color='blue', linestyle='dashed', marker='o', markerfacecolor='blue', markersize=8)
plt.bar(tries, ratio, color='blue') 
plt.xticks(tries,xlabels,rotation=45)
plt.margins(0.2)
#plt.axhline(y=coo,color='black') #emily didn't like this, suggested taking out
plt.subplots_adjust(bottom=0.25)
plt.ylim([0,0.3])
#plt.legend(['','average'])

plt.ylabel(r'Parent reviews / Total reviews')
plt.xlabel(r'City')
plt.title(r'Where are Parents Reviewing?')

#plt.show()

filepath='/Users/aford/yelp/figures/'
filename='yelp_where2'+'.ps'
filenamefoo=filepath+filename
plt.savefig(filenamefoo,bbox_inches=0)

plt.show()






