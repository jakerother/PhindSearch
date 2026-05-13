# test_phindsearch.py
"""
Tests for PhindSearch module.
"""

import unittest
from phindsearch import PhindSearch

class TestPhindSearch(unittest.TestCase):
    """Test cases for PhindSearch class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PhindSearch()
        self.assertIsInstance(instance, PhindSearch)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PhindSearch()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
