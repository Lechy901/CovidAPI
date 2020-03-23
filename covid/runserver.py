"""
This script runs the covid application using a development server.
"""

from os import environ
from covid import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', '0.0.0.0')
    try:
        PORT = int(environ.get('SERVER_PORT', '55555'))
    except ValueError:
        PORT = 55555
        
    app.run(HOST, PORT)
