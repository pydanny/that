import unittest


class TestSequenceFunctions(unittest.TestCase):

    def test_python(self):
        """ If this fails then that means that python does not work """
        self.assertEquals(True, True)
        self.assertIn(1, (None, True, False))
        self.assertNotEquals(0.1 + 0.3 * 3, 1.0)

    def test_resources(self):
        """ Resources should return appropriate values """
        from resources import a, b, factory

        self.assertTrue(isinstance(a, basestring))
        self.assertTrue(isinstance(b(), basestring))
