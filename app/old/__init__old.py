from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_moment import Moment

app = Flask(__name__)
app.config.from_object(Config)
mail = Mail(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login' #сообщаем фласк-логин название функции для авторизации, чтобы можно было потом не давать заходить на страницы которые нельзя смотреть без авторизации  @login_required
moment = Moment(app)

#регистрация ошибок
from app.errors import bp as errors_bp
app.register_blueprint(errors_bp)

# регистрация авторизации
from app.auth import bp as auth_bp
app.register_blueprint(auth_bp, url_prefix='/auth')

