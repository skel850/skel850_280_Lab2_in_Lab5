import unittest     # Import the Python unit testing framework
import maths        # Our code to test


class MathsTest(unittest.TestCase):
    ''' Unit tests for our maths functions. '''

    def test_add(self):
        ''' Tests the add function. '''
        self.assertEqual(maths.add(5,5), 10, "The add functions returned an incorrect value.")

    def test_fibonacci(self):
        ''' Tests the fibonacci function. '''
        self.assertEqual(maths.fibonacci(5), 5, "The fibonacci function returned an incorrect value.")

    def test_convert_base_under_10(self):
        '''Tests the convert_base_under_10 function with a base under 10'''
        self.assertEqual(maths.convert_base(300,16,2),"100101100","The convert_base function returned an incorrect value.")
            
    def test_convert_base_over_10(self):
        '''Tests the convert_base_over_10 function with a base over 10'''
        self.assertEqual(maths.convert_base(300,2,16),"12C","The convert_base function returned an incorrect value.")


# This allows running the unit tests from the command line (python test_maths.py)
if __name__ == '__main__':
    unittest.main()
