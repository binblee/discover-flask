import flask_testing
from project import app, db
from project.models import BlogPost, User

class BaseTestCase(flask_testing.TestCase):
    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.add(User('admin', 'admin@test', 'admin'))
        db.session.add(BlogPost('Test', 'This is a test post.', 'admin'))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()