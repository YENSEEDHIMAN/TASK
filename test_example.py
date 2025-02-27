import unittest

class testing(unittest.TestCase):

    def test(self):
        a = 5
        b = 5
        c = 7
        self.assertEqual(a, b, 'a is not equal to b')
        self.assertNotEqual(a, c, 'a is not equal to c')
        self.assertGreater(c , b, 'c is greater than b')
        self.assertGreaterEqual(a , b,' a is equal to b')

if __name__=='__main__':
    unittest.main()



class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()



def add(a,b):
    return a+b

class add_testing(unittest.TestCase):

    def test_add_integer(self):
        self.assertEqual(add(2,3),5)

    def test_add_string(self):
        self.assertEqual(add('Hello','World'),'HelloWorld')

def sub(a,b):
    return a-b

class sub_testing(unittest.TestCase):

    def test_sub_int(self):
        self.assertEqual(sub(3,2),1)

if __name__ == '__main__':
    unittest.main()



import sys

class TestExample(unittest.TestCase):
    @unittest.skip("Skip this")
    def skip_test_example(self):
        self.assertEqual(1,1)

    @unittest.skipIf(sys.version_info<(3,8),'Require version greater than 3.8')
    def skip_test_if_example(self):
        self.assertEqual(1,1)

    @unittest.skipUnless(sys.platform.startswith("MAC"),'Requires Window OS')
    def test_skip_unless_example(self):
        self.assertTrue(True)

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(2,3)
if __name__ == '__main__':
    unittest.main()
