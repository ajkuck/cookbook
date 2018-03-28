from flask import Flask
from flask_sqlalchemy import SQLAlchemy


if __name__ == '__main__':
    app = Flask('cookbook_ws')
    app.config.from_pyfile('../main.ini')
    db = SQLAlchemy(app)

    # Annoyingly, this import has to be in the middle of the script (after SQLAlchemy(), before create_all()),
    # otherwise SQLAlchemy won't recognise the imported models.
    from cookbook_ws.orm import *

    db.create_all()
