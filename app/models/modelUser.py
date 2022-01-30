from app import app # comentamos esta linea para ejecutar este archivo.
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Creamos nuestra base de datos aquí, asi que descomentamos 
# estas dos lineas para ejecutar este archivo.

# from flask import Flask
# app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:123456789@localhost:3306/userDataBase' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma  = Marshmallow(app)


# Crear la base de datos
class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(110))
    name  = db.Column(db.String(255))
    email = db.Column(db.String(110))

    def __init__(self, user_id, username,name,email):
        self.user_id = user_id
        self.username = username 
        self.name = name
        self.email = email

def Update(id,cat_name, cat_description):
    category = User.query.get(id)
    category.cat_name = cat_name
    category.cat_description = cat_description
    db.session.commit()
    return category 

def All():
    all_users = User.query.all()
    result = users_schema.dump(all_users) 
    return result
    
def getcatgoryID(id):
    user = User.query.get(id)
    return user

def getcatgoryPost(cat_name,cat_description):
    new_user = User(cat_name,cat_description)
    db.session.add(new_user)
    db.session.commit()
    return new_user
def getDelete(id):
    delete = User.query.get(id) 
    db.session.delete(delete)
    db.session.commit()
    return delete
# Define Schema with Marshmallow
# Schema category
class UserSchema(ma.Schema):
    class Meta:
        fields = ('user_id','username','name','email')

# One request
user_schema = UserSchema()
#  Many requests
users_schema = UserSchema(many=True)

if __name__ == "__main__":
    # Run this file directly to create the database tables.
    print ("Creating database tables...")
    db.create_all()
    print( "Done!")