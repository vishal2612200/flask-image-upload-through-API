from views import *


if __name__ == "__main__":
    db.create_all()
	# setting debug to True enables hot reload 
	# and also provides a debuger shell 
	# if you hit an error while running the server
    app.run(debug = True) 
