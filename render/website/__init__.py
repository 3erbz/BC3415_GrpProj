from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

# database initialisation
db = SQLAlchemy ()
DB_NAME = "database.db"

def create_app ():
    app = Flask(__name__)
    app.config ['SECRET_KEY'] = 'BC3415'
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATBASE_URL')
    db.init_app(app)
    
    # import views from different apps
    from .auth.start import auth_views
    from .pages.home import home_page
    from .pages.forum import forum_page
    from .pages.rewards import rewards_page
    from .pages.explore import explore_page
    from .pages.learning import learning_page
    from .pages.profile import profile_page

    # redirecting the user for when they are not logged in to their account
    login_manager = LoginManager()
    login_manager.login_view = 'auth_views.login'
    login_manager.init_app(app)

    app.register_blueprint (auth_views, url_prefix='/')
    app.register_blueprint (home_page, url_prefix='/')
    app.register_blueprint (forum_page, url_prefix='/')
    app.register_blueprint (rewards_page, url_prefix='/')
    app.register_blueprint (explore_page, url_prefix='/')
    app.register_blueprint (learning_page, url_prefix='/')
    app.register_blueprint (profile_page, url_prefix='/')

    from .models import User

    with app.app_context():
        db.create_all()

    @login_manager.user_loader
    def load_user (id):
        return User.query.get (int(id))

    return app

    
