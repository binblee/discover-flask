from project import db
from project.models import BlogPost

db.create_all()

db.session.add(BlogPost("Good", "I'm good."))
db.session.add(BlogPost("Well", "I'm well."))
db.session.add(BlogPost("Postgresql", "Setup for postgresql"))

db.session.commit()