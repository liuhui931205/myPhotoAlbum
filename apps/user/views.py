from apps.user import user
from flask import request, jsonify, g
from apps.models import *
from apps import db, redis_store


@user.route('/login', methods=["POST"])
def login():
    req_dict = request.json
    username = req_dict.get('username')
    password = req_dict.get('password')

    if username in ["liuhui","luodan"]:
        if password == "123456":
            resp = jsonify(code=20000, data={"token":username}, message="登录成功")
        else:
            resp = jsonify(code=-1, data="", message="密码不正确")
    else:
        resp = jsonify(code=-1, data="", message="用户名不正确")
    return resp

@user.route('/getInfo', methods=["GET"])
def get_info():
    req_dict = request.args
    token = req_dict.get('token')
    data = {
        "email":"648802794@qq.com",
        "name":"liuhui",
        "avatar":"http://cache.lhananld.xyz/avatar/liuhuiWechatIMG207.jpeg",
    }
    resp = jsonify(code=20000, data=data, message="查询成功")
    return resp

@user.route('/logout', methods=["POST"])
def logout():
    req_dict = request.args
    access_token = req_dict.get('access_token')
    data = {
        "email":"648802794@qq.com",
        "name":"liuhui",
        "avatar":"http://cache.lhananld.xyz/avatar/liuhuiWechatIMG207.jpeg",
    }
    resp = jsonify(code=20000, data="", message="查询成功")
    return resp


