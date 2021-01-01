from flask import (
    Blueprint,
    render_template
)

from ..backend.models import Todo

ui_bp=Blueprint('ui',__name__,template_folder='./templates')

@ui_bp.route('/')
def todo_ui():
    todos=Todo.query.order_by(Todo.id.desc()).all()
    complete=Todo.query.filter_by(complete=True).count()
    return render_template('index.html',todos=todos,complete=complete)

