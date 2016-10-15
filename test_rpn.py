import unittest
import rpn

class TestBasics(unittest.TestCase):
	def test_addition(self):
		result = rpn.calculate("1 1 +")
		self.assertEqual(2, result)

	def test_subtraction(self):
		result = rpn.calculate("100 10 -")
		self.assertEqual(90, result)

	def test_bad_input(self):
		with self.assertRaises(TypeError):
			rpn.calculate("2 22 222 +")
	
	def test_multiplication(self):
		result = rpn.calculate("1 3 *")
		self.assertEqual(3, result)

	def test_divide(self):
		result = rpn.calculate("10 5 /")
		self.assertEqual(2, result)
