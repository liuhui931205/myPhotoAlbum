import time

from apps.album import album
from flask import request, jsonify, g
from apps.models import *
from apps import db, redis_store
from util import qiniu_auth


@album.route('/list', methods=["GET"])
def image_list():
    results = db.session.query(ShuYanAlbum).filter(ShuYanAlbum.is_deleted == 0).all()
    data = []
    for o in results:
        data.append(o.to_dict())
    resp = jsonify(code=20000, data=data, message="查询成功")
    return resp


@album.route('/delete', methods=["GET"])
def image_delete():
    req_dict = request.args
    ids = req_dict.get("path")
    obj = db.session.query(ShuYanAlbum).filter(ShuYanAlbum.id == int(ids)).first()
    obj.is_deleted = 1
    try:
        db.session.add(obj)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e
    resp = jsonify(code=20000, data="", message="查询成功")
    return resp


@album.route('/add', methods=["POST"])
def image_add():
    req_dict = request.json
    path = req_dict.get("path")
    obj = ShuYanAlbum()
    obj.img_url = path
    try:
        db.session.add(obj)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e
    resp = jsonify(code=20000, data={"imgUrl": BASE_URL+path, "id": obj.id}, message="查询成功")
    return resp


@album.route('/get_token')
def get_up_token():
    token = qiniu_auth.get_qiu_auth().upload_token("liuhui-12")
    key = str(int(time.time()))

    resp = jsonify(code=20000, data={"token": token, "key": key}, message="查询成功")
    return resp


@album.route('/sakura', methods=["PUT"])
def set_sakura():
    req_dict = request.json
    tp = req_dict.get("type")
    a_id = req_dict.get("id")
    o = db.session.query(ShuYanAlbum).filter(ShuYanAlbum.id == int(a_id)).first()
    obj = db.session.query(ShuYanSakura).filter(ShuYanSakura.sakura_type == tp).first()
    if obj:
        obj.img_url = o.img_url
    else:
        obj = ShuYanSakura()
        obj.img_url = o.img_url
        obj.sakura_type = tp
    try:
        db.session.add(obj)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e
    resp = jsonify(code=20000, data="", message="查询成功")
    return resp


@album.route('/sakura', methods=["GET"])
def get_sakura():
    data = {}
    results = db.session.query(ShuYanSakura).all()
    for o in results:
        data.update({o.sakura_type:f"{BASE_URL}{o.img_url}"})
    resp = jsonify(code=20000, data=data, message="查询成功")
    return resp
