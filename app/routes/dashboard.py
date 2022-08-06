from flask import Blueprint, render_template

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

# seem to be getting a 404 when this is set up as @bp.route('/'). Can't seem to find a reason why, especially considering a backslash at the end of the url prefix does not cause any issues. 
@bp.route('')
def dash():
  return render_template('dashboard.html')

@bp.route('/edit/<id>')
def edit(id):
  return render_template('edit-post.html')