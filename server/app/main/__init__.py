from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .config import Config

# Initialize Flask extensions
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # 使用 SQLite 数据库
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

    db.init_app(app)
    login_manager.init_app(app)

    from . import routes
    app.register_blueprint(routes.bp)

    return app
