import os
import unittest
# from app import app
class RoutingTests(unittest.TestCase):
    # Function to set up testing connection
    def home(self):
         app.config["TESTING"] = True
         app.config["DEBUG"] = True
         self.app = app.test_client()
         self.assertEqual(app.debug,False)
         response = self.app.get('/', follow_redirects=True)
         self.assertEqual(response.status_code, 200)
    '''Function to teardown connection after testing
     def tear_down():
          pass
     def homepage():
          response = self.app.get('/', follow_redirects = True)
          self.assertEqual(response.status_code, 200)
    def aboutpage():
          response = self.app.get('/', follow_redirects = True)
          self.assertEqual(response.status_code, 200)'''


if __name__ == "__main__":
    unittest.main()