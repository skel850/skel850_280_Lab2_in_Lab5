import unittest     # Import the Python unit testing framework
import maths        # Our code to test


class MathsTest(unittest.TestCase):
    ''' Unit tests for our maths functions. '''

    def test_add(self):
        ''' Tests the add function. '''
        result = maths.add(5,5)
        self.assertEqual(result, 10, "The add functions returned an incorrect value.")

    def test_fibonacci(self):
        ''' Tests the fibonacci function. '''
        result = maths.fibonacci(5)
        self.assertEqual(result, 5, "The fibonacci function returned an incorrect value.")

    def test_convert_base_under_10(self):
        '''Tests the convert_base_under_10 function with a base under 10'''
        result = maths.convert_base(8,4)
        self.assertEqual(result,4,"The convert_base function returned an incorrect value.")
        
        
    def test_convert_base_over_10(self):
        '''Tests the convert_base_over_10 function with a base over 10'''
        result = maths.convert_base(12,4)
        self.assertEqual(result,6,"The convert_base function returned an incorrect value.")
# This allows running the unit tests from the command line (python test_maths.py)
if __name__ == '__main__':
    unittest.main()
