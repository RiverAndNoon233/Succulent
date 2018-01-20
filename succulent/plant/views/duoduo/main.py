from flask import Blueprint, render_template
from plant.models import Posts, User, Goods


main = Blueprint('main', __name__)


@main.route('/')
def indexall():
    return render_template('duoduo/index.html')
