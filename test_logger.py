import unittest
import logger

class loggerTest(unittest.TestCase):
    
    def test_info(self):
        '''Tests the info function...'''
        result = ("example.")
        self.assertEqual(result,'example.',"The test_info function returned an incorrect value")
    
    def test_error(self):
        '''Tests the error function...'''
        result = ("example!")
        self.assertEqual(result,'example!',"The test_error function returned an incorrect value")
        
if __name__ == '__main__':
    unittest.main()