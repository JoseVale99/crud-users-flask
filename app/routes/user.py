from app import app
from flask import jsonify,render_template, request
from app.models.modelUser import  (Update,AllUsers,getDelete,
getcatgoryID,getcatgoryPost,user_schema)


#  rootes API REST

# message of welcome
# @app.route('/', methods=['GET'])
# def index():
#     return jsonify({'Message':"Welcome back!"})
             
# GET all categories
@app.route('/',methods=['GET'])
def getCategories():
    data = AllUsers()
    return render_template('index.html', users = data)

#  GET for ID
@app.route('/category/<id>', methods=['GET'])      
def getCategoryID(id):
    category = getcatgoryID(id)
    return user_schema.jsonify(category)
    
#  POST
@app.route('/category', methods=['POST'])
def categoryNew():
    data = request.get_json(force=True)
    cat_name = data['cat_name']
    cat_description = data['cat_description']
    new_category = getcatgoryPost(cat_name,cat_description)
    return jsonify('add successfully new category!')
    
# Update category
@app.route('/category/<id>',methods=['PUT'])
def UpdateCategory(id):
    data = request.get_json(force=True)
    cat_name = data['cat_name']
    cat_description = data['cat_description']
    categoryUpdate = Update(id,cat_name,cat_description)
    return jsonify("update successfully!")
    
# DELETE
@app.route('/category/<id>', methods=['DELETE'])
def deleteCategory(id):
    delete = getDelete(id)
    return jsonify('delete successfully!')