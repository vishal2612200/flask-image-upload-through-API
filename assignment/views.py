from flask import request, jsonify, make_response, send_from_directory, render_template
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy 
from uuid import uuid4# for public id 
from werkzeug.security import generate_password_hash, check_password_hash 
from datetime import datetime, timedelta
from logging import FileHandler, INFO
from os import path, makedirs, listdir
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from assignment.database import *
from assignment.models import *


file_handler = FileHandler('server.log')
app.logger.addHandler(file_handler)
app.logger.setLevel(INFO)

PROJECT_HOME = path.dirname(path.realpath(__file__))
UPLOAD_FOLDER = '{}/uploads/'.format(PROJECT_HOME)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 #16MB
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']

uploaded_file_name = {}

# default value
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)


@app.route('/register', methods =['POST']) 
def register(): 
	# creates a json of the request
	data = request.get_json()
	print(data)
	# gets name, email and password 
	username = data["username"] 
	password = data["password"]

	# checking for existing user 
	user = User.query.filter_by(username = username).first() 
	if not user: 
		# database ORM object 
		user = User( 
			public_id = str(uuid4()), 
			username = username, 
			password = generate_password_hash(password) 
		) 
		# insert user 
		db.session.add(user) 
		db.session.commit() 

		return make_response('Successfully registered.', 201) 
	else: 
		# returns 202 if user already exists 
		return make_response('User already exists. Please Log in.', 202) 

 
@app.route('/login', methods =['POST'])
@limiter.limit("5 per minute")
def login(): 
	# creates json of request
	auth_data = request.get_json()
	username = auth_data['username']
	password = auth_data['password']

	if not auth_data or not username or not password: 

		return make_response( 
			'Could not verify', 
			401, 
			{'WWW-Authenticate' : 'Basic realm ="Some value of your input missing"'} 
		) 

	user = User.query.filter_by(username = username).first() 

	if not user: 

		return make_response( 
			'Could not verify', 
			401, 
			{'WWW-Authenticate' : 'Basic realm ="Look like user don\'t exist "'} 
		) 

	if check_password_hash(user.password, password): 
		# generates the JWT Token 
		access_token = create_access_token(identity=username) 

		return make_response(jsonify({'auth_token' : access_token}), 201) 
	
	return make_response( 
		'Could not verify', 
		403, 
		{'WWW-Authenticate' : 'Basic realm ="Password is incorrect."'} 
	) 


@app.route('/user', methods =['GET'])
@jwt_required
@limiter.limit("5 per minute")
def get_all_users():
	# querying the database 
	# for all the entries in it 
	users = User.query.all() 
	# converting the query objects 
	# to list of jsons 
	output = [] 
	for user in users: 
		# appending the user data json 
		# to the response list 
		output.append({ 
			'public_id': user.public_id, 
			'username' : user.username,
		}) 

	return jsonify({'users': output}) 

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def create_new_folder(local_dir):
    newpath = local_dir
    if not path.exists(newpath):
        makedirs(newpath)
    return newpath

def upload_image(uploaded_files):
	app.logger.info(PROJECT_HOME)
	global uploaded_file_name
	# To make previously added dict empty
	uploaded_file_name = {}
	if 'files' in uploaded_files:
		files = uploaded_files.getlist('files')
		for img in files:
			app.logger.info(app.config['UPLOAD_FOLDER'])
			if img and allowed_file(img.filename):
				img_name = secure_filename(img.filename)
				create_new_folder(app.config['UPLOAD_FOLDER'])
				saved_path = path.join(app.config['UPLOAD_FOLDER'], img_name)
				app.logger.info("saving {}".format(saved_path))
				img.save(saved_path)
				uploaded_file_name[img.filename] = saved_path
		return True
	else:
		return False	

# API limit: 5/min
@app.route('/upload', methods = ['POST'])
@jwt_required
@limiter.limit("5 per minute")
def image_upload():
	if upload_image(request.files):
		return make_response(jsonify({'Message' : "Success", 'image_name' : uploaded_file_name}), 201)
	else:
		return make_response(jsonify({'error': 'Image does not Found in request'}), 404)


@app.route('/uploadimage', methods = ['POST'])
@limiter.exempt
def form_image_upload():
	if upload_image(request.files):
		return render_template('layout/default.html',
						content=render_template( 'pages/image.html', data = uploaded_file_name))
	else:
		return make_response(jsonify({'error': 'Image does not Found in request'}), 404)


# no limit on api call
@app.route("/files")
@jwt_required
@limiter.exempt
def list_files():
	"""Endpoint to list files on the server."""
	files = []
	for filename in listdir(app.config['UPLOAD_FOLDER']):
		file_path = path.join(app.config['UPLOAD_FOLDER'], filename)
		if path.isfile(file_path):
			files.append(filename)
	return make_response(jsonify(files),201)

@app.route('/', methods = ['GET', 'POST'])
def image_page():
	return render_template('layout/default.html',
                            content=render_template( 'pages/upload.html'))

@app.route('/webcam', methods = ['GET', 'POST'])
def webcam_page():
	return render_template('layout/default.html',
                            content=render_template( 'pages/webcam.html'))

