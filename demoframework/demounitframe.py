import unittest
from selenium import webdriver


class UnitFramework(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        print("start of all methods")

    def setUp(self):
        print("start of test method")

    def test_scenario1(self):
        print("method 1")

    def test_scenario2(self):
        print("method 2")

    def tearDown(self):
        print("end of test method")

    @classmethod
    def tearDownClass(cls):
        print("Teardown class")

if __name__ == '__main__':
    unittest.main()