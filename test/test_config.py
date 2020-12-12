
import unittest

from flask import current_app
from flask_testing import TestCase

from assignment.addjwt import app


class TestTestingConfig(TestCase):

    def test_app_is_testing(self):
        self.assertFalse(app.config['SECRET_KEY'] is 'assignment secret key')
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///assignmentdb.db'
        )


if __name__ == '__main__':
    unittest.main()
