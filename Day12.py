import json 
from pymongo import MongoClient  
myclient = MongoClient("mongodb://localhost:8080/")  
db = myclient["GFG"]  
Collection = db["data"] 
with open('data.json') as file: 
    file_data = json.load(file) 
if isinstance(file_data, list): 
    Collection.insert_many(file_data)   
else: 
    Collection.insert_one(file_data) 
    
   
[
 {
   "id":"01",
   "name":"AAA",
   "branch":"IT"
 },
 {
   "id":"02",
   "name":"BBB",
   "branch":"CSE"
 },
]
