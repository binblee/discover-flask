from flask_login import current_user
from tests.base import BaseTestCase
from project import bcrypt
from project.models import User


class UserViewsTests(BaseTestCase):
    def test_login_page_load(self):
        response = self.client.get('/login')
        # self.assertIn(b'Please login', response.data)
        assert b'Please login' in response.data

    def test_correct_login(self):
        with self.client:
            response = self.client.post(
                '/login', 
                data=dict(username='admin', password='admin'), 
                follow_redirects=True
            )
            # self.assertIn(b'You were logged in.', response.data)
            # self.assertTrue(current_user.name == 'admin')
            # self.assertTrue(current_user.is_active())
            assert b'You were logged in.' in response.data
            assert current_user.name == 'admin'
            assert current_user.is_active()

    # Ensure login behaves correctly with incorrect credentials
    def test_incorrect_login(self):
        with self.client:
            response = self.client.post(
                '/login',
                data=dict(username="wrong", password="wrong"),
                follow_redirects=True
            )
            # self.assertIn(b'Invalid credentials. Please try again.', response.data)
            # self.assertFalse(current_user.is_active)
            assert b'Invalid credentials. Please try again.' in response.data
            assert not current_user.is_active

    # Ensure logout behaves correctly
    def test_logout(self):
        with self.client:
            self.client.post(
                '/login',
                data=dict(username="admin", password="admin"),
                follow_redirects=True
            )
            response = self.client.get('/logout', follow_redirects=True)
            # self.assertIn(b'You were logged out', response.data)
            # self.assertFalse(current_user.is_active)
            assert b'You were logged out' in response.data
            assert not current_user.is_active

    # Ensure that logout page requires user login
    def test_logout_route_requires_login(self):
        response = self.client.get('/logout', follow_redirects=True)
        # self.assertIn(b'Please log in to access this page.', response.data)
        assert b'Please log in to access this page.' in response.data


class TestUser(BaseTestCase):
    def test_user_registeration(self):
        with self.client:
            response = self.client.post(
                '/register', 
                data=dict(username='user1', password='user1pass',
                          email='user1@email.org', confirm='user1pass'), 
                follow_redirects=True
            )
            # self.assertIn(b'Welcome to Flask!', response.data)
            # self.assertTrue(current_user.name == 'user1')
            # self.assertTrue(current_user.is_active())
            assert b'Welcome to Flask!' in response.data
            assert current_user.name == 'user1'
            assert current_user.is_active()

    def test_get_by_id(self):
        # Ensure id is correct for the current/logged in user
        with self.client:
            self.client.post('/login', data=dict(
                username="admin", password='admin'
            ), follow_redirects=True)
            # self.assertTrue(current_user.id == 1)
            # self.assertFalse(current_user.id == 20)
            assert current_user.id == 1
            assert current_user.id != 20

    def test_check_password(self):
        # Ensure given password is correct after unhashing
        user = User.query.filter_by(email='admin@test').first()
        # self.assertTrue(bcrypt.check_password_hash(user.password, 'admin'))
        # self.assertFalse(bcrypt.check_password_hash(user.password, 'foobar'))
        assert bcrypt.check_password_hash(user.password, 'admin')
        assert not bcrypt.check_password_hash(user.password, 'foobar')
