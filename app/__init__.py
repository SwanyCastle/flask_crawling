from flask import Flask
from flask_wtf.csrf import CSRFProtect

from app.setting_db import db, migrate

import config

csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    csrf.init_app(app)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)

    # Blue Print
    from .routes import crawl_list
    app.register_blueprint(crawl_list.bp)
    
    return app