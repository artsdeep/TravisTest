import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


HTML = """
<!DOCTYPE html>
<html lang="en" class="full-height">
    <head>
        <title>Home | TravisCI</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="description" content="Social media analytic tool">
        <meta name="author" content="Michal Dyzma">
    </head>
    <body>
        <h2 style="color:red">Home Page</h2>
    </body>
</html>
"""

#  We have to disale this i pyllint, because pylint will fail our build every
#  time it encounters this "global" variable
app = Flask(__name__) # pylint: disable=invalid-name
app.config.from_object('config')
db = SQLAlchemy(app)

db.create_all()

@app.route('/')
def home():
    #print(str(db.session.query(Client).count()))

    """ Main route to the web app
    """
    return HTML
@app.route('/h')
def home1():
    from mod.models import Client
    print(str(db.session.query(Client).count()))
    i = db.session.query(Client).count()+1
    cl = Client(id=i, name="nameclient")
    db.session.add(cl)
    db.session.commit()
    """ Main route to the web app
    """
    return HTML