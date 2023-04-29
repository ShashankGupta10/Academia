from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from urllib import *
import sys,os
from pymongo import MongoClient


client = MongoClient("mongodb+srv://shashankgupta2003:Shashank10@cluster0.x6bsdlb.mongodb.net/test")
db = client['IOP']

result = db.Student_Data.find_one({"username": "shashankgupta2003"})
print(result)
# welcome = result["name"].upper()