import serverless_wsgi
import sys
import os

# Add the project root to the Python path to make `from app import app` reliable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from app import app

def handler(event, context):
    return serverless_wsgi.handle(app, event, context)
