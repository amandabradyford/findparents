import json
import re

### POINT OF THIS PROGRAM IS TO CREATE A DICT THAT CAN BE ACCESSED LATER
### THIS DICT INCLUDES, FOR EACH USER, THE FREQUENCY OF "KID WORDS" THEY HAVE USED
### AS WELL AS THE FREQUENCY OF "KID BUSINESSES" THEY HAVE REVIEWED.
### this will be used later in k means clustering.

#reads in the user dataset
def read_dataset(path):
  userdataset=[]
  with open(path) as f:
    for line in f:
      userdataset.append(json.loads(line))
  return userdataset

#reads in the REVIEW dataset
def read_reviewdataset(reviewpath):
  reviewdataset=[]
  with open(reviewpath) as f:
    for line in f:
      reviewdataset.append(json.loads(line))
  return reviewdataset
   
#gets the fields in the USER dataset
def getfields(userdataset):

  userid = [r['user_id'] for r in userdataset] #userid
  reviewcount = [r['review_count'] for r in userdataset] #how many reviews that user has done


def get_num_kid_words(reviewtext):
	count=0
#	print reviewtext
	pattern = ['my kid', 'my kids', 'kids', 'son', 'sons', 'daughter', 'daughters', 'baby', 'babies', 
		   'child', 'children', 'diaper', 'YO', 'little one', 'stroller'] #"kid words"
					   	
	for entry in pattern:
		match = re.findall(entry,reviewtext)
		count += len(match) #counts how many kid words there are
	return count
	
def make_business_dict(path):
#	path = './business.json'
	businessdataset=[]
	with open(path) as f:
		for line in f:
			businessdataset.append(json.loads(line))	
	dict = {} #creates an empty dict

	regexes = ['AZ', 'NV','WI','IL','NC','PA'] #only interested in U.S. reviews
	combined = "(" + ")|(".join(regexes) + ")"
	
	for business in businessdataset:
		address = business['full_address']
		match = re.search(combined, address)
		if match:			
			if business['business_id'] not in dict:
				dict[business['business_id']] = business['categories']
	return dict #returns the businessid and category of businesses
		
def make_user_dict(path):
#	path = './user.json'
	userdataset=[]
	with open(path) as f:
		for line in f:
			userdataset.append(json.loads(line))	
	dict = {}

	for user in userdataset:
		if user['user_id'] not in dict:
			dict[user['user_id']] = user['review_count']
	return dict
	
def get_num_kid_business(businessdict,businessid):

	regexes = ['Amusement Parks', 'Baby Gear and Furniture', 'Candy Stores', 
			   'Child Care & Daycare', 'Children\'s Clothing', 'Dance Schools',
			   'Dance Studios', 'Education', 'Elementary Schools', 'Go Karts', 'Gymnastics', 
			   'Horseback Riding', 'Ice Cream & Frozen Yogurt', 'Kids Activities', 'Magicians', 
			   'Maternity Wear', 'Middle Schools & High Schools', 'Mini Golf', 
			   'Musical Instruments & Teachers', 'Parks', 'Party & Event Planning', 
			   'Party Equipment Rentals', 'Party Supplies', 'Pediatric Dentists', 
			   'Pediatricians', 'Playgrounds', 'Preschools', 'Recreation Centers', 
			   'Religious Schools', 'Speech Therapists', 'Summer Camps', 
			   'Swimming Lessons/Schools', 'Toy Stores', 'Zoos'] #looked through the yelp categories and tagged these as possibly related to parents/kids

	combined = "(" + ")|(".join(regexes) + ")"

	count = 0 		
	if businessid in businessdict:
		length = len(businessdict[businessid])
		catlist = businessdict[businessid]
		#print catlist
		catstring = ''
		for string in catlist:
			catstring=catstring+' '+string
		
	#	print catstring
		match = re.search(combined,catstring)
    	if match:
        	count += 1
	return count #getting the count of "kid businesses"


def getreviewfields(reviewdataset,userpath,businesspath):

	dict = {}
	businessdict = make_business_dict(businesspath)
	userdict = make_user_dict(userpath)
  
	for review in reviewdataset:
		if review['business_id'] in businessdict:
		
			if review['user_id'] not in dict: #first time user appears
				#usertuple = ()
	
				kidwords = get_num_kid_words(review['text'])
				totalwords = len(review['text'])
				#percentwords = kidwords/float(totalwords)
				kidbusiness = get_num_kid_business(businessdict,review['business_id']) # 1 or 0
				reviewcount = userdict['user_id']
				
				totalbusiness = 1	

				#for each user, the following returns how many kidwords, how many total words, how many kid businesses, how many total businesses, and their review count.
				dict[review['user_id']] = [kidwords, totalwords, kidbusiness, totalbusiness, reviewcount] 
			else: #after the user has been seen before
	
				numlist = dict[review['user_id']] 
				numlist[0] += get_num_kid_words(review['text']) 
				numlist[1] += len(review['text'])
				numlist[2] += get_num_kid_business(businessdict,review['business_id'])  
				numlist[3] += 1
				dict[review['user_id']] = numlist
	print len(dict)	
	return dict


if __name__ == '__main__':
	#reviewpath = './review5k.json' #abridged files, for testing purposes. 
	#userpath = './usershort.json'
	#businesspath = './business5k.json'
	
	reviewpath = './yelp_academic_dataset_review.json'
	userpath = './yelp_academic_dataset_user.json'
	businesspath = './yelp_academic_dataset_business.json'

	reviewdataset=read_reviewdataset(reviewpath)
	userdata = getreviewfields(reviewdataset, userpath, businesspath)
	#for key in userdata:
	#	if userdata[key][0] >= 1:
#			print 'The reviews with kidwords'
#			print userdata[key]
#		if userdata[key][2] >= 1:
#			print '-----------The reviews of kid businesses'
#			print userdata[key]
			
	#write out dict to a new json file...
	with open('us_fulluserdataset_june11_withnumreviews.json','w') as fp:
		json.dump(userdata, fp)
#	print userdata

