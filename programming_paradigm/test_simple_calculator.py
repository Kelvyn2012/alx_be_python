import unittest
from simple_calculator import SimpleCalculator

class TestSimple_calculator(unittest.TestCase):
    def test_add(self):
        calc = SimpleCalculator()
        result = calc.add(3, 5)
        self.assertEqual(result, 8)

    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    unittest.main()