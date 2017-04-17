import pymongo 
user={	 "id" : "1",
		"login":"mez",
		"pwd" : "aze",
 		"name" : "Mezlini Mohamed",
 		"active" : True,
 		 }
pymongo.MongoClient().site.users.save(user)
user={	 "id" : "2",
		"login":"elyes",
		"pwd" : "midou",
 		"name" : "Mohamed elyes",
 		"active" : True,
 		 }
pymongo.MongoClient().site.users.save(user)
user={	 "id" : "3",
		"login":"midou",
		"pwd" : "med",
 		"name" : "mohamed",
 		"active" : False,
 		 }
pymongo.MongoClient().site.users.save(user)
