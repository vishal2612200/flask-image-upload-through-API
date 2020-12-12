from flask import Flask
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)


app = Flask(__name__)
auth_jwt = JWTManager(app)
