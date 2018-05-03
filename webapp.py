from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
POSTGRES_URL = "127.0.0.1:5432"
POSTGRES_USER = "app_user"
POSTGRES_PW = "app_user_pass"
POSTGRES_DB = "app"
DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)

#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = DB_URL
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']+"?sslmode=require"
print(SQLALCHEMY_DATABASE_URI)
#SQLALCHEMY_DATABASE_URI =DB_URL
DATABASE_CONNECT_OPTIONS = {}
SQLALCHEMY_TRACK_MODIFICATIONS = False

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

db = SQLAlchemy(app)
db.drop_all()
db.create_all()
@app.route('/')
def home():
    """ Main route to the web app
    """
    return HTML

if __name__ == '__main__':
    app.run()
