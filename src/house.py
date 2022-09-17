from urllib import request
import uvicorn
import pymongo
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List



app=FastAPI()

client=pymongo.MongoClient("mongodb+srv://gayathri:Sairambaba@cluster1.davwpcs.mongodb.net/?retryWrites=true&w=majority")
db=client['suriya_db']
house_collection = db['Rent_house_registry']

def get_collection():
    return house_collection

class Rent_house(BaseModel):
    house_id:int
    place:str
    squarefeet:int
    type:str
    rent:float

class House_list(BaseModel):
    data : List [Rent_house]

def house_list_serializer(houselist):
    return [house.dict() for house in houselist]

    
@app.get('/api/view_all',tags=['No_broker']) 
def view_all():  
    try:
        collection = get_collection()
        curser = list(collection.find({},{"_id":0}))
        return {"data":curser}
    except Exception as e:
        print("error on viewing all data :" +str(e))

@app.get('/api/view/{house_id}',tags=['No_broker'])
def view(house_id):
    try:
        collection = get_collection()
        curser = collection.find_one({"house_id":int(house_id)},{"_id":0})
        return {"data":curser}
    except Exception as e:
        print("error on viewing data :" +str(e))

@app.post('/api/add_house',tags=['No_broker'])
def add(house : Rent_house):
    try:
        collection = get_collection()
        resp = collection.insert_one(house.dict())
        return {"status": "House details added successfully"}   
    except Exception as e:
        print("error on adding:" +str(e))

@app.post('/api/add_house_list',tags=['No_broker'])
def add_many(house : House_list):
    try:

        collection = get_collection()
        house_list = house_list_serializer(house.data)
        collection.insert_many(house_list)
        return {"status":200}
    except Exception as e:
        print("error on adding list :" +str(e))

if __name__ == ('__main__'):
    uvicorn.run("house:app",reload=True)