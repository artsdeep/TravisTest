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

POSTGRES_URL = "127.0.0.1:5432"
POSTGRES_USER = "app_user"
POSTGRES_PW = "app_user_pass"
POSTGRES_DB = "app"
DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)


SQLALCHEMY_DATABASE_URI = DB_URL
db = SQLAlchemy(app)

from mod.models import *

db.create_all()

@app.route('/')
def home():
    #print(str(db.session.query(Client).count()))

    """ Main route to the web app
    """
    return HTML
@app.route('/h')
def home1():

    print(str(db.session.query(Client).count()))
    i = db.session.query(Client).count()+1
    cl = Client(id=i, name="nameclient")
    db.session.add(cl)
    db.session.commit()
    """ Main route to the web app
    """
    return HTML