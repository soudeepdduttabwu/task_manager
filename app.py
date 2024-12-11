from flask import Flask
from models import db
from auth.routes import auth
from views.task_routes import task_views
from views.user_routes import user_views
from flask_login import LoginManager
from models import User

app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)

# Setup Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Register Blueprints
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(task_views, url_prefix='/tasks')
app.register_blueprint(user_views, url_prefix='/users')

if __name__ == '__main__':
    app.run(debug=True)
