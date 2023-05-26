import unittest

from translator import english_to_french, french_to_english

class Test_english_to_french(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(english_to_french("Hello"), "Hello","Text doesnt match") 
        self.assertEqual(english_to_french(""), False)  

class Test_french_to_english(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english(""), False) 
        
        
unittest.main()