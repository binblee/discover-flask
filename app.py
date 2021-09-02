from project import app

if __name__ == '__main__':
    print(f"DB URL: {app.config['SQLALCHEMY_DATABASE_URI']}")
    app.run()