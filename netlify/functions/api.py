import serverless_wsgi
from app import app

def handler(event, context):
    return serverless_wsgi.handle(app, event, context)
