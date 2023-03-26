import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):
    
    def setUp(self): # This always runs automatically at the start
        print("setup\n")
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.python.org/")
    
    # Each method starting with the name "text_" will get executed automatically
    def test_1(self):
        assert True

    def test_1(self):
        assert False

    def tearDown(self): # This always runs at the end 
        self.driver.close()

# __name__ is a special variable that python assigns a value to
# If we run our file then __name__ becomes __main__
# If we run our file as an import in another file then __name__ becomes the name of our file e.g., anyname.py
# __name__ == "__main__" It prevents the code underneath from getting executed in another file as an import.
if __name__ == "__main__":
    unittest.main()