import unittest
from simple_calculator import SimpleCalculator

class TestSimple_calculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
    
    
    def test_add(self):
        self.assertEqual(self.calc.add(4,2),6)
        
    def test_subtract(self):
        result = self.calc.subtract(5,3)
        self.assertEqual(result,2)

    def test_multiply(self):
        result = self.calc.multiply(2,4)
        self.assertEqual(result,8)
        
  
    def test_divide_by_zero(self):
        result = self.calc.divide(4,0)
        self.assertIsNone(result,)    
    
        
    def test_divide(self):
        result = self.calc.divide(4,2)
        self.assertEqual(result,2)
    
    
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    unittest.main()