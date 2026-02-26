from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config
from routes.user_routes import user_bp
from routes.auth_routes import auth_bp


app = Flask(__name__)
app.config.from_object(Config)

jwt = JWTManager(app)

# create table when app starts


app.register_blueprint(user_bp)
app.register_blueprint(auth_bp, url_prefix="/auth")

if __name__ == "__main__":
    app.run(debug=True)