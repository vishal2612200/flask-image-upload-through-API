from assignment.database import *


class User(db.Model): 
	id = db.Column(db.Integer, primary_key = True) 
	public_id = db.Column(db.String(50), unique = True) 
	username = db.Column(db.String(100)) 
	password = db.Column(db.String(80)) 
