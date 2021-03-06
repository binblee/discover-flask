from .base import BaseTestCase


class FlaskTestCase(BaseTestCase):

    # Ensure that flask was set up correctly
    def test_index(self):
        response = self.client.get('/login', content_type='html/text')
        # self.assertEqual(response.status_code, 200)
        assert response.status_code == 200

    # Ensure that main page requires user login
    def test_main_route_requires_login(self):
        response = self.client.get('/', follow_redirects=True)
        # self.assertIn(b'Please log in to access this page.', response.data)
        assert b'Please log in to access this page.' in response.data

    # Ensure that posts show up on the main page
    def test_posts_show_up_on_main_page(self):
        response = self.client.post(
            '/login',
            data=dict(username="admin", password="admin"),
            follow_redirects=True
        )
        # self.assertIn(b"This is a test post.", response.data)
        assert b"This is a test post." in response.data

    def test_welcome_page(self):
        response = self.client.get('/welcome')
        # self.assertEqual(response.status_code, 200)
        # self.assertIn(b'Welcome to Flask!', response.data)
        assert response.status_code == 200
        assert b'Welcome to Flask!' in response.data
