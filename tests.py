import unittest

class TestSequenceFunctions(unittest.TestCase):
    
    def test_python(self):
        """ If this fails then that means that python does not work """
        self.assertEquals(True, True)
        
    def test_resources(self):
        """ Resources should return appropriate values """
        from resources import a, b, factory
        
        self.assertTrue(isinstance(a, str))
        # TODO - test on b
        # TODO - test on factory        
        