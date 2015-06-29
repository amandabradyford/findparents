import pymysql as mdb
import csv

#gets results of various sql queries, to be plotted later...


db = mdb.connect(user="root",host="localhost", db="testdb", charset='utf8')


def star_diff():

#     categorylist = ['Bars','Frozen Yogurt & Ice Cream','Restaurants', 'Pets','Pediatricians','Zoos']
# 
#     statelist = ['AZ','NV','WI','IL','PA','NC']

    categorylist = ['Restaurants','Food','Nightlife','Bars','American (New)','American (Traditional)','Italian','Pizza','Arts & Entertainment','Shopping','Coffee & Tea','Mexican','Sandwiches','Burgers','Breakfast & Brunch','Chinese','Sushi Bars','Active Life','Thai','Event Planning & Services','Desserts','Pubs','Grocery','Seafood','Vegetarian','Japanese','Bakeries','Mediterranean','Specialty Food','Ice Cream & Frozen Yogurt','Steakhouses','Hotels & Travel','Diners','Beauty & Spas','Museums','Barbeque','Fashion']

 #   categorylist = ['Bars','Zoos']

    statelist = ['AZ','NV', 'WI','IL','PA','NC']
    
    masterlist = []
    for state in statelist:
        print state
        for category in categorylist:
            print category
            categoryrow = []
            categoryrow.append(state)
            categoryrow.append(category)
  
            with db:

                cur = db.cursor()
       
                #gets average star ratings from parents 
                cur.execute("select COUNT(rev), AVG(stars) from (SELECT DISTINCT REVIEWTEXT as rev, stars from parents_ONLY join (select * from business4 WHERE state='%s' AND category='%s') minisample ON parents_ONLY.BUSINESSID=minisample.bid) bb;"%(state,category)) 
    
                query_results = cur.fetchall()
                parentstarrating=query_results[0][1]
    
                #gets the overall average from everyone 
                cur.execute("select COUNT(rev), AVG(stars) from (SELECT DISTINCT REVIEWTEXT as rev, stars from USER4 join (select * from business4 WHERE state='%s' AND category='%s') minisample ON USER4.BUSINESSID=minisample.bid) bb;"%(state,category)) 
    
                query_results = cur.fetchall()
                allstarrating=query_results[0][1]
                
            categoryrow.append(parentstarrating)
            categoryrow.append(allstarrating) 
            categoryrow.append(parentstarrating-allstarrating)   
            masterlist.append(categoryrow)
   
#        print query_results[0][1]  #query_results[0] gives us the two results we need query_results[0][1] gives the star review
        print categoryrow
    
    return masterlist,statelist
    
    
    
# 
#   outputs = []
# 
#   for result in query_results:
# 
#     outputs.append(dict(category=result[0], city=result[1], businessname=result[2], reviewtext=result[3], stars=result[4]))
#     
#   the_result = ''
# 
#   return render_template("output.html", outputs = outputs, the_result = the_result)

if __name__ == '__main__':
    ratings,states = star_diff()
    
    f=open("stardiff_2.csv", 'w')
    writer=csv.writer(f)    
    for categoryrow in ratings:
        writer.writerow((categoryrow)) #printing both elements of the tuple 
        #and then the string of the number
    f.close()

