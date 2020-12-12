# JWT token for API using Flask

# Feature

- JWT authentication
- Throttle limit on some API
- Upload Multiple Image file at same time
- Upload Single/Multiple file using Web Interface
- Server log for uploaded files
- unit test for some function
- Added Curl command documentation for all API
- API for all uploaded Files/ register Users
- hash password for user registration


# How to run the Application

- run the following command in the terminal

``` 
pip install -r requirements.txt

cd assignment

python main.py

```

# Curl Commands

### Image upload 
```
curl -H "Authorization: Bearer <token>" --output -X POST http://localhost:5000/upload -F files=@1.png
```

### Register User
```
curl -i -H "Content-Type: application/json" -X POST -d "{\"username\":\"<username>\", \"password\":\"<password>\"}" http://localhost:5000/register
```

### User Login 
```
curl -i -H "Content-Type: application/json" -X POST -d "{\"username\":\"<username>\", \"password\":\"<password>\"}" http://localhost:5000/login
```

### User List
```
curl -X GET 'http://localhost:5000/user' -H 'Authorization: Bearer <token>'
```

### Uploaded Image List
```
curl -H "Authorization: Bearer <token>" --output -X GET http://localhost:5000/files
```

# Curl Command Response

For more detailed info about API response reference to ```curl-format.txt``` file.

# Screenshots

![Image 1]('screenshots/assign1.png')

![Image 2]('screenshots/assign2.png')

![Image 3]('screenshots/assign3.png')

![Image 4]('screenshots/assign4.png')

![Image 5]('screenshots/assign5.png')

![Image 6]('screenshots/assign6.png')

![Image 7]('screenshots/assign7.png')

![Image 8]('screenshots/assign8.png')


# How to run user.sh and test.sh

Use the following command, but before that replace few of required parameters such as jwt token value.

```

sh user.sh

sh test.sh

```



# Contact Details

### Name

Vishal Sharma

### Email Address

- vishalsh533@gmail.com
- vishalsharma.gbpecdelhi@gmail.com
