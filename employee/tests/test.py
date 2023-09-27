from django.test import TestCase
from django.contrib.auth.models import User, Group
from employee.tests.util import is_operator
# from tests.util import is_operator


class UserAuthenticationTests(TestCase):
    def setUp(self):
        # Create a user and a group for testing
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.operator_group = Group.objects.create(name='operator')
        self.user.groups.add(self.operator_group)

    def test_is_operator_with_operator_user(self):
        """
        Test the is_operator function with a user in the 'operator' group.
        """
        is_operator_result = is_operator(self.user)
        self.assertTrue(is_operator_result)

    def test_is_operator_with_non_operator_user(self):
        """
        Test the is_operator function with a user not in the 'operator' group.
        """
        # Remove the user from the 'operator' group for this test
        self.user.groups.remove(self.operator_group)
        
        is_operator_result = is_operator(self.user)
        self.assertFalse(is_operator_result)

    def test_is_operator_with_nonexistent_user(self):
        """
        Test the is_operator function with a user that doesn't exist.
        """
        nonexistent_user = User.objects.create_user(username='nonexistentuser', password='testpassword')
        is_operator_result = is_operator(nonexistent_user)
        self.assertFalse(is_operator_result)

    # def is_operator(user):
    #     return user.groups.filter(name='operator').exists()

