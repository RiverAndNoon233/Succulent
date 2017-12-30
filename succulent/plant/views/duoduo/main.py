from flask import Blueprint, render_template


main = Blueprint('main',__name__)

@main.route('/')
def indexall():
    return render_template('duoduo/main.html')



