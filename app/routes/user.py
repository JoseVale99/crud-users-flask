from app import app
from flask import (render_template, 
                   request,redirect,url_for,flash)
from app.models.modelUser import (Update,AllUsers,getDeleteId,
getUserID,UserPost,user_schema)

# GET - usuarios
@app.route('/', methods=['GET'], defaults={"page": 1}) 
@app.route('/<int:page>', methods=['GET'])

def index(page):
    users,pages = AllUsers(page)
    return render_template('index.html', users = users, pages=pages)

@app.route('/add_user')
def add_user():
    return render_template('add.html')

# show user 
@app.route('/showuser/<id>', methods=['GET'])
def showuser(id):
    user = getUserID(id)
    return render_template('show.html', user = user)

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


# view return update user
@app.route('/update/<id>', methods=['GET'])
def getUserupdate(id):
    user = getUserID(id)
    return render_template('update.html',user=user)

# Update user
@app.route('/update/<id>',methods=['POST'])
def UpdateUser(id):
     if request.method == 'POST':
        username = request.form['username']
        name = request.form['name']
        email = request.form['email']
        new_user = Update(id,username,name,email)
        flash('¡Usuario actualizado exitosamente!')
        return redirect(url_for('index'))
    
# DELETE
@app.route('/userdelete/<id>', methods = ['POST','GET'])
def deleteUser(id):
    delete = getDeleteId(id)
    flash('¡Usuario eliminado con éxito!')
    return redirect(url_for('index'))