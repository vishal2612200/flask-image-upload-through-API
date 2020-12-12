
import time
import json
import unittest

from assignment.database import db
from assignment.models import User
from tests.base import BaseTestCase


def register_user(self, username, password):
    return self.client.post(
        '/register',
        data=json.dumps(dict(
            username=username,
            password=password
        )),
        content_type='application/json',
    )

def login_user(self, username, password):
    return self.client.post(
        '/login',
        data=json.dumps(dict(
            username=username,
            password=password
        )),
        content_type='application/json',
    )


class TestAuthBlueprint(BaseTestCase):

    def test_registration(self):
        """ Test for user registration """
        with self.client:
            response = register_user(self, 'newuser', '123')
            data = json.loads(response.data.decode())
            self.assertTrue(data['message'] == 'Successfully registered.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 201)

    def test_registered_with_already_registered_user(self):
        """ Test registration with already registered email"""
        user = User(
            username='testuser',
            password='123'
        )
        db.session.add(user)
        db.session.commit()
        with self.client:
            response = register_user(self, 'testuser', '123')
            data = json.loads(response.data.decode())
            self.assertTrue(
                data['message'] == 'User already exists. Please Log in.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 202)

    def test_user_login(self):
        """ Test for login of registered-user login """
        with self.client:
            # registered user login
            resp_login = login_user(self, 'newuser', '123')
            data = json.loads(resp_login.data.decode())
            self.assertTrue(data['auth_token'])
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
    unittest.main()
