from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from mymeal import db, login_manager, app
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    recipes = db.relationship('Recipe', backref='author', lazy=True)

    def get_reset_token(self, expires_secs=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_secs)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    description = db.Column(db.Text, nullable=False)
    serves = db.Column(db.Integer, nullable=False, default='01')
    recipe_type = db.Column(db.String(15), nullable=False)
    ingredients = db.relationship('Ingredient', backref='meal', lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    recipe_book = db.Column(db.String(100))
    recipe_book_page = db.Column(db.Integer, default='01')

    def __repr__(self):
        return f"Recipe('{self.title}', '{self.description}', '{self.date_posted}')"

    def as_dict(self):
        return {'title': self.title}


class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    quantity = db.Column(db.String(20), nullable=False, default='01')
    purchased_at = db.Column(db.String(15), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)

    def __repr__(self):
        return f"ingredient('{self.name}', '{self.quantity}', '{self.purchased_at}')"
