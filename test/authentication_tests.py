

from unittest import TestCase 
from mock import patch
import main.authentication as auth

class AuthTests(TestCase):
	
	@patch('__builtin__.open')
	def test_login(self, mock_open):
		mock_open.return_value.read.return_value = \
			"george|bosco\n"
		self.assertTrue(auth.login('george', 'bosco'))
