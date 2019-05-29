from flask import Flask 

app = Flask(__name__)

app.config.from_object('app.config')
app.config.from_object('app.credentials')

from .api import bp as api_bp
app.register_blueprint(api_bp)

from .models.application import db
db.init_app(app)
db.create_all(app=app)

# from .models.db import db
# db.init_app(app)
# db.create_all(app=app) #!important