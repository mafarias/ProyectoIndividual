from flask import Flask,request,jsonify
from flask_sqlalchemy import sqlalchemy
from flask_marshmallow import Marshmallow
import os
#
app = Flask (__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI']='postgresql///'+os.path.join(basedir,'db.postgresql')
engine =postgresql://scott:tiger@localhost/Pmo
#
if __name__ =='__main__':
    app.run(debug=True)