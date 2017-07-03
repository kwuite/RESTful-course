import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

#conn = sqlite3.connect('testdata.db')

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', 
        type=str,
        required=True,
        help="This field cannot be blank!"
    )

    parser.add_argument('password', 
        type=str,
        required=True,
        help="This field cannot be blank!"
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"messgae": "A user with that username already exists."}, 400

#        user = UserModel(data['username'], data['password'])
        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully."}, 201

