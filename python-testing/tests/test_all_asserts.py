import unittest

SERVER = 'server b'
class AllAsserts(unittest.TestCase):
    def test_assert(self):
        self.assertEqual(1, 1)
        self.assertEqual('hola', 'hola')
    
    def test_assert_true(self):
        self.assertTrue(1 == 1)
        self.assertTrue('hola' == 'hola')
    
    def test_assert_raises(self):
        with self.assertRaises(ValueError ):
            int("No soy un numero")
        
    def test_assert_in(self):
        self.assertIn(1, [1, 2 ,3])
        self.assertNotIn(4, [1, 2, 3])
    
    def test_asssert_dict(self):
        self.assertDictEqual({'name': 'johan', 'lastname': 'franco'}, {'name': 'johan', 'lastname': 'franco'})
    
    def test_setEqual(self):
        self.assertSetEqual({1, 2, 3}, 
                            {3, 2, 1})
    
    @unittest.skip("Trabajo en progeso")
    def test_skip(self):
        self.asserEqual('hola','chao')
    
    @unittest.skipIf(SERVER== 'server b', "No se puede ejecutar en este servidor")
    def test_skip_if(self):
        self.assertEqual('hola', 'chao')
   

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual('hola', 'chao')
    
    @unittest.skipUnless(SERVER == 'server a', "No se puede ejecutar en este servidor")
    def test_assert_skipunless(self):
        self.assertEqual('hola', 'chao')
