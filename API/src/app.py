from flask import Flask
from src.controller.employee_controller import bp_employee
from src.controller.refund_controller import bp_refund
from src.model import db
from flask_migrate import Migrate
from config import Config
import os
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
load_dotenv()

def create_app():
    app = Flask(__name__)
    jwt = JWTManager(app)
    from flask_cors import CORS
    origin = os.getenv('LINK_DEPLOY_FRONT')
    CORS(app, origins='*')
    
    app.register_blueprint(bp_employee)
    app.register_blueprint(bp_refund)
    app.secret_key = os.environ.get('SECRET_KEY')
    
    app.config.from_object(Config)
    migrate = Migrate()
    
    
        
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
    migrate.init_app(app, db)
    
    return app