from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_wtf import CSRFProtect
from flask_moment import Moment
from config import Config
import markdown


db = SQLAlchemy()
bootstrap = Bootstrap()
moment = Moment()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    Config.init_app(app)
    CSRFProtect(app)

    db.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    login_manager.init_app(app)
    
    # 添加Markdown过滤器
    @app.template_filter('markdown')
    def markdown_filter(text):
        return markdown.markdown(text)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    # 将模型类添加到全局模板上下文，以便在模板中直接使用
    from .models import User, Article, ArticleType, Menu, Source, Comment, BlogInfo, Plugin, BlogView
    app.jinja_env.globals['User'] = User
    app.jinja_env.globals['Article'] = Article
    app.jinja_env.globals['ArticleType'] = ArticleType
    app.jinja_env.globals['Menu'] = Menu
    app.jinja_env.globals['Source'] = Source
    app.jinja_env.globals['Comment'] = Comment
    app.jinja_env.globals['BlogInfo'] = BlogInfo
    app.jinja_env.globals['Plugin'] = Plugin
    app.jinja_env.globals['BlogView'] = BlogView

    return app
