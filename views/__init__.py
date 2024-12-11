# This file initializes the views package and ensures the routes are properly registered.

from flask import Blueprint

# Initialize Blueprints for tasks and users
task_views = Blueprint('task_views', __name__)
user_views = Blueprint('user_views', __name__)

# Import routes to register them with the Blueprints
from . import task_routes, user_routes
