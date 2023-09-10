import unittest
from main import to_upper

class MyTestCase(unittest.TestCase):
    def test_to_uppper(self):
        name = "Prachita"
        upper_name = to_upper(name)
        self.assertEqual(upper_name,"PRACHITA")
        
if __name__ == '__main__':
    unittest.main()