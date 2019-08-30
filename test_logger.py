import unittest
import logger

class loggerTest(unittest.TestCase):
    
    def test_info(self):
        '''Tests the info function...'''
        x = logger.Logger()
        self.assertEqual(x.info("Information"), "[INFO] Information","That is not correct")
    
    def test_error(self):
        '''Tests the error function...'''
        x = logger.Logger()
        self.assertEqual(x.error("Error"), "[WARNING] Error","That is not correct")
        
if __name__ == '__main__':
    unittest.main()