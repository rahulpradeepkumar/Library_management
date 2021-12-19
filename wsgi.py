#!/bin/env python
"""
This script runs the Library_Management_System application using a development server.
importing application, Db, and API for WSGI file
"""

import os

from Library_Management_System import app as application
from Library_Management_System import db
from Library_Management_System.views import main

application.register_blueprint(main)
db.create_all()
if __name__ == "__main__":
    HOST = os.environ.get("SERVER_HOST", "localhost")
    try:
        #locally our project will be served at port 8080
        PORT = int(os.environ.get("SERVER_PORT", "8080"))
    except ValueError:
        PORT = 8080
    application.run(HOST, PORT, threaded=True)
