#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Unit Test Template

import unittest
import calc

class TestStringMethods (unittest.TestCase):
    
    def setUp(self):
        pass
    
    # Returns True if the column 'accession' (sample ID) contain string 'GSM'
    
    def test_strings_GSM(self): 
        self.assertEqual(accession[1], 'GSM')
    
    # Return True if the string starts with capital letter'C', and lowercase afterwards
    # as we relabel 'non-cancel control' and 'other cancer' as 'Control
    '
    def test_title(self):
        self.assertEqual('control'.title(), 'Control')
        
    # check the column 'Title' with split method
    
    def test_split(self):
        s = 'bladder cancer'
        self.assertEqual(s.split(), ['bladder', 'cancer'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
    
    # Test values from the blood test are in a normal range
    
    def assertBetween(self, value, min, max):
    """Fail if value is not between min and max (inclusive)."""
        self.assertGreaterEqual(value, min)
        self.assertLessEqual(value, max)
    
    # Test some calculation functions with values from the blood test (use add function as an example)
    
    def test_add(self, value):
        result = calc.add(value, value)
        self.assertEqual(result, 15)

if __name__ =='__main__':
    unitest.main()

