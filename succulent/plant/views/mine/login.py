import os
from flask import Blueprint, render_template, flash, redirect, url_for, request, current_app
# from plant.forms import RegisterForm, LoginForm, ModiUserForm, IconForm, FoundPasswd, ChangeMailForm
from plant.models import User
from plant.extensions import db, photos, api,Resource
from plant.email import send_mail
from flask_login import login_user, logout_user, login_required, current_user
# from flask_restful import Resource

login = Blueprint('login', __name__)

# 添加资源类
class UserAPI(Resource):
    def get(self):
        return {'User':'GET'}
# 将资源添加到api
api.add_resource(UserAPI,'/users/')