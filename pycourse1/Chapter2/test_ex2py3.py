# test_ex2py3.py 

from unittest.mock import patch
from unittest import TestCase
import ex2py3

class NamePromptTestCase(TestCase):

	"""Tests for the name 'John' in 'ex2py3.py'."""
	@patch('ex2py3.get_input', return_value='John')
	def test_for_name_John(self, input):
		self.assertEqual(namePrompt(), 'Hello John')
	

	"""Tests for a blank entry in 'ex2py3.py'."""
	@patch('ex2py3.get_input', return_value='')
	def test_for_no_name(self, input):
		self.assertEqual(namePrompt(), 'Cat got your tongue? Try again!')

