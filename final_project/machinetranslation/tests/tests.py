import unittest

from translator import english_to_french, french_to_english

class Testenglish_to_french(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french("Hello"), "Bonjour") # test when 2 is given as input the output is 4.
        self.assertEqual(english_to_french(""), False)  # test when 3.0 is given as input the output is 9.0.

class Testfrench_to_english(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english("Bonjour"), "Hello") # test when 2 is given as input the output is 4.
        self.assertEqual(french_to_english(""), False) # test when -3.1 is given as input the output is -6.2.
        
        
unittest.main()