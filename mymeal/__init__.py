from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

mail = Mail(app)

from mymeal.users.routes import users
from mymeal.recipes.routes import recipes
from mymeal.ingredients.routes import ingredients
from mymeal.main.routes import main
from mymeal.errors.handlers import errors

app.register_blueprint(users)
app.register_blueprint(recipes)
app.register_blueprint(ingredients)
app.register_blueprint(main)
app.register_blueprint(errors)


