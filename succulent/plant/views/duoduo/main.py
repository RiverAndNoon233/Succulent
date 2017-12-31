from flask import Blueprint, render_template
from plant.models import Posts, User, News, Goods


main = Blueprint('main',__name__)

@main.route('/')
def indexall():
    return render_template('duoduo/main.html')



