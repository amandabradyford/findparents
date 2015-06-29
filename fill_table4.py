#!/usr/bin/python

import MySQLdb
import json 
import re


def filluser(path,db): #review set
    cursor = db.cursor()
    reviewdataset=[]
    with open(path) as f:
        for line in f:
            reviewdataset.append(json.loads(line))
    print 'the length of review data set is'
    print len(reviewdataset)
    

    cursor.execute("DROP TABLE IF EXISTS USER4")
    
    sql = """CREATE TABLE USER4 (
             USERID VARCHAR(1000),
             REVIEWTEXT TEXT,
             BUSINESSID VARCHAR(1000),
             STARS VARCHAR(10),
             FLAG INT)"""

    cursor.execute(sql)
    
    pattern = ['my kid', 'my kids', 'my son', 'my sons', 'my daughter', 'my daughters', 'my baby', 'my babies', 
 		   'my child', 'my children', 'my baby', 'our kid', 'our kids', 'our son','our sons', 'our babies',
 		   'our daughter','our daughters','our son and daughter', 'our daughter and son', 'my wife and son', 'my wife and sons', 'my wife and daughter', 
 		   'my wife and daughters', 'my wife and kids', 'my husband and son', 'my husband and sons', 'my husband and daughter', 
 		   'my husband and daughters', 'my husband and kids', 'my hubby and son', 'my hubby and sons', 'my hubby and daughter', 
 		   'my hubby and daughters', 'my hubby and kids', 'i\'m a parent', 'as a parent', 'i am a parent', 'i have kids']
		   
    combined = "(" + ")|(".join(pattern) + ")"
    
    print 'line 38'
    
    count=0
    
    for review in reviewdataset:   					   	
        flag=0
        match = re.search(combined,review['text'],re.IGNORECASE) #i think this should work...
        if match:
            #print "the match is"
            #print match.group()
            flag=1
            count += 1
        else:
            flag=0
               
        try:
            # Execute the SQL command
            cursor.execute("""INSERT INTO USER4 VALUES (%s, %s, %s, %s, %s)""", 
            (review['user_id'].encode('utf8'), review['text'].encode('utf8'), 
            review['business_id'].encode('utf8'),review['stars'],flag))
        

           # Commit your changes in the database
            db.commit()
        except Exception as e:
            #print 'line 42'
            print e
                  # Rollback in case there is any error
            db.rollback()
    print 'line 61'
    print 'and the count is'     
    print count
   
def fillbusiness(path,db):
 
    businessdataset=[]
    with open(path) as f:
        for line in f:
            businessdataset.append(json.loads(line))
    print 'length of business dataset is'
    print len(businessdataset)

    cursor = db.cursor()
    
    # Drop table if it already exist using execute() method.
    cursor.execute("DROP TABLE IF EXISTS BUSINESS4")

# Create table as per requirement
    sql = """CREATE TABLE BUSINESS4 (
          CITY  VARCHAR(1000) NOT NULL,
          STATE VARCHAR(10),
          CATEGORY  VARCHAR(1000),
          BUSINESSNAME VARCHAR(1000),
          BUSINESSID VARCHAR(1000))"""
         
    cursor.execute(sql)
    
    regexes = ['AZ', 'NV','WI','IL','NC','PA']
    combined = "(" + ")|(".join(regexes) + ")"

    for business in businessdataset: 
        match = re.search(combined, business['state'])
        if match:
            categories = business['categories']
            for entry in categories:
    
                try:
                   # Execute the SQL command
                   cursor.execute("""INSERT INTO BUSINESS4 VALUES (%s, %s, %s, %s, %s)""", 
                              (business['city'], business['state'], entry, business['name'],business['business_id']))

                   # Commit your changes in the database
                   db.commit()
                except Exception as e:
                   print 'line 87'
                   print e
                   # Rollback in case there is any error
                   db.rollback()


if __name__ == '__main__':

    # Open database connection
    db = MySQLdb.connect("localhost","root","","testdb" )

    print 'line 115'
    userpath = '/Users/aford/yelp/yelp_academic_dataset_review.json' #getting user data from review file
    businesspath = '/Users/aford/yelp/yelp_academic_dataset_business.json'

#    businesspath = '/Users/aford/yelp/business10k.json'
#    userpath = '/Users/aford/yelp/review10k.json' #getting user data from review file!
    
    filluser(userpath,db)
    fillbusiness(businesspath,db)
    
    # disconnect from server
    db.close()
