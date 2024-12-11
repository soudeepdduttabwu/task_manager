from flask import Blueprint

# Initialize the Blueprint for authentication
auth = Blueprint('auth', __name__)

# Import routes to register them with the Blueprint
from . import routes
