from unicodedata import name
from app import app
from flask import (jsonify,render_template, 
                   request,redirect,url_for,flash)
from app.models.modelUser import (Update,AllUsers,getDeleteId,
getUserID,UserPost,user_schema)


#  rootes API REST


# GET - usuarios

@app.route('/', methods=['GET'], defaults={"page": 1}) 
@app.route('/<int:page>', methods=['GET'])

def index(page):
    users,pages = AllUsers(page)
    return render_template('index.html', users = users, pages=pages)

@app.route('/add_user')
def add_user():
    return render_template('add.html')

#  POST - agregar usuario
@app.route('/add_user/new_user', methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        username = request.form['username']
        name = request.form['name']
        email = request.form['email']
        new_user = UserPost(username,name,email)
        flash('¡Usuario agregado exitosamente!')
        return redirect(url_for('add_user'))

#  GET - por ID
@app.route('/user/<id>', methods=['GET'])      
def getUserID(id):
    user = getUserID(id)
    return user_schema.jsonify(user)

# Update category
@app.route('/category/<id>',methods=['PUT'])
def UpdateCategory(id):
    data = request.get_json(force=True)
    cat_name = data['cat_name']
    cat_description = data['cat_description']
    categoryUpdate = Update(id,cat_name,cat_description)
    return jsonify("update successfully!")
    
# DELETE
@app.route('/userdelete/<id>', methods = ['POST','GET'])
def deleteUser(id):
    delete = getDeleteId(id)
    return redirect(url_for('index'))