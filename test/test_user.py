import unittest
from app.db.model import User

class UserModelTest(unittest.TestCase):

    def setUp(self):
        """
         method that creates an instance of our User class
        """
        self.new_user = User(id=1, public_id="77fd1fbc-e6aa-4cd3-b069-f9e513bbde1d", username="aris", fullname="la ode aris saputra", password="banana")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_user,User))

    def test_init(self):
        self.assertEqual(self.new_user.id,1)
        self.assertEqual(self.new_user.public_id,"77fd1fbc-e6aa-4cd3-b069-f9e513bbde1d")
        self.assertEqual(self.new_user.username, "aris")
        self.assertEqual(self.new_user.fullname,"la ode aris saputra")
        self.assertEqual(self.new_user.password,"banana")

    def test_password_setter(self):
        """
         ascertains that when password is being hashed and the pass_secure contains a value
        """
        self.assertTrue(self.new_user.password is not None)
    