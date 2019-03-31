# import the basic modules needed for the
# testing of the application

import os
import unittest
from app import app

# declare the class which would hold the basic
# methods for seting up the test environment

class RoutingTests(unittest.TestCase):

	# define the method to setup the test
	# environment-- this should power up 

	def setUp(self):
		app.config["DEBUG"] = False
		app.config["TESTING"] = True
		self.app = app.test_client()
		self.assertEqual(app.debug, False)

	# define the methods to teardown the 
	# test class after all tests have been completed

	def tearDown(self):
		pass

	# write the test cases to be executed it 
	# should return a passing or failing test

	def testHomeApp(self):
		response = self.app.get('/', follow_redirects = True)
		self.assertEqual(response.status_code, 200)


	def testAboutPage(self):
		response = self.app.get('/about', follow_redirects = True)
		self.assertEqual(response.status_code, 200)

	def testMomentsPage(self):
		response = self.app.get('/moments', follow_redirects = True)
		self.assertEqual(response.status_code, 200)

	def testMonetizationPage(self):
		response = self.app.get('/monetization', follow_redirects = True)
		self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
	unittest.main()