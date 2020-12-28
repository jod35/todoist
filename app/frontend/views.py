from flask import (
    Blueprint,
    render_template
)

from ..backend.models import Todo

ui_bp=Blueprint('ui',__name__,template_folder='./templates')

@ui_bp.route('/')
def todo_ui():
    todos=Todo.query.all()
    return render_template('index.html',todos=todos)

