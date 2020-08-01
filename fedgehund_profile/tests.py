from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTest(TestCase):
	def test_user_model_has_profile(self):
		user = User(
			email = "newuser@gmail.com",
			username = "newuser",
			password = "qp10al29zm38"
		)
		user.save()

		self.assertTrue(
			hasattr(user, 'profile')
		)