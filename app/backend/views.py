from flask import (
    Blueprint, json,
    jsonify,
    url_for,
    make_response,
    request,
)

from ..utils.database import db
from .models import Todo
from .schemas import TodoSchema

api_bp=Blueprint('api',__name__)

@api_bp.route('/',methods=['GET'])
def index():
    return make_response(
        jsonify(
            {"message":"Hello, from backend"}
        )
   ,200)

##############################
#### GET all todo resources ##
##############################
@api_bp.route('/todos',methods=["GET"])
def get_all_todos():
    todos=Todo.query.order_by(Todo.id.desc()).all()

    results=TodoSchema(many=True).dump(todos)

    return make_response(jsonify({"todos":results}),200)


########################
# POST a todo resource #
########################
@api_bp.route('/todos',methods=['POST'])
def create_todo():
    data=request.get_json()

    new_todo=Todo(
        name=data.get('name'),
        desc=data.get('desc')
    )

    new_todo.save()

    result=TodoSchema().dump(new_todo)

    return make_response(
        jsonify({
            "message":"Created",
            "todo":result
        }),201
    )


###########################
## GET A single resource ###
###########################
@api_bp.route('/todo/<int:id>')
def get_single_todo(id):
    todo = Todo.query.get_or_404(id)

    response=TodoSchema().dump(todo)

    return make_response(
        jsonify(
            {"success":True,
              "todo":response   
            }
        )
    )

############################
#####update a resource #####
############################
@api_bp.route('/todo/<int:id>',methods=['PATCH'])
def update_todo(id):

    todo=Todo.query.get_or_404(id)

    data=request.get_json()

    todo.name=data.get('name')

    todo.desc=data.get('desc')

    db.session.commit()


    response=TodoSchema().dump(todo)
    return make_response(
        jsonify({
            "message":"Updated",
            "todo": response,
            "success":True,
        }),200
    )

#############################
##### PUT a resource ########
#############################
@api_bp.route('/todo/<int:id>',methods=['PUT'])
def replace_todo(id):
    todo=Todo.query.get_or_404(id)

    data=request.get_json()

    todo.name=data.get('name')

    todo.desc=data.get('desc')

    db.session.commit()

    response=TodoSchema().dump(todo)

    return make_response(
        jsonify(
            {"message":"Replaced",
             "success":True,
             "todo":response
            }
        )
    )


############################
### DELETE A TODO ##########
############################
@api_bp.route('/todo/<int:id>',methods=["DELETE"])
def delete_todo(id):
    todo=Todo.query.get_or_404(id)

    todo.delete()

    response=TodoSchema().dump(todo)

    return make_response(
        jsonify(
            {
                "success":True,
                "message":"Deleted",
                "todo":response
            }
        )
    )

@api_bp.errorhandler(404)
def not_found(err):
    return make_response(jsonify(
        {
            "message":"RESOURCE NOT FOUND"
        }
    ),404)



@api_bp.errorhandler(500)
def server_error(err):
    return make_response(jsonify({
        "message":"OOOPS!!!! Something went wrong"
    }),500)