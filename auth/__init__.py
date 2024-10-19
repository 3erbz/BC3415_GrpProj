from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy ()
DB_NAME = "database.db"

def create_app ():
    app = Flask (__name__)
    app.config['SECRET_KEY'] = 'BC3415'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # redirecting the user for when they are not logged in to their account
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .views_nologin import views_nologin
    from .auth import auth
    from .views_login import views_login

    app.register_blueprint (views_nologin, url_prefix='/')
    app.register_blueprint (auth, url_prefix='/')
    app.register_blueprint (views_login, url_prefix='/')

    from .models import User

    with app.app_context():
        db.create_all()

    @login_manager.user_loader
    def load_user (id):
        return User.query.get (int(id))

    return app