from flask_sqlalchemy import SQLAlchemy 

from assignment.addjwt import *


#This should be changes during production
app.config['SECRET_KEY'] = 'assignment secret key'
# database name 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///assignmentdb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# creates SQLALCHEMY object 
db = SQLAlchemy(app) 
