import unittest #importing the unittest module

#<---First Class User---->#
from user import User #import the class from your other file.

class TestUser(unittest.TestCase):
    '''
    TestUser is a subclass of the parent class.
    unittest.TestCase helps in creating tests cases
    '''

    def setUp(self):#Setup Method is for defining instructions that will be executed before each test method.
        self.create_account = User("Claudia", "Njeri", "claudianjeri04@gmail", "claudia")

    # def tearDown(self):
    #     User.user_createaccount = []

    def test_init(self):
        self.assertEqual(self.create_account.first_name, "Claudia")
        self.assertEqual(self.create_account.last_name, "Njeri")
        self.assertEqual(self.create_account.email, "claudianjeri04@gmail.com")
        self.assertEqual(self.create_account.first_name, "03134323")

    def test_first_name(self):
        self.create_account.save_account()
        self.assertEqual(len(User.user_createaccount), 1)

    

if __name__ == '__main__':
    unittest.main()
    
