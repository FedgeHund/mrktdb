from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTest(TestCase):
	def test_user_model_has_profile(self):
		user = User(
			email = "newuser@gmail.com",
			password = "qp10al29zm38",
			first_name = "MrktDB",
			last_name = "Admin"
		)
		user.save()

		self.assertTrue(
			hasattr(user, 'profile')
		)