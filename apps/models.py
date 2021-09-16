from sqlalchemy import text

from util.qiniu_auth import BASE_URL
from . import db
import math
import datetime
import hashlib
import re
import json


class ShuYanUser(db.Model):
    # __bind_key__ = "design"
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))



class ShuYanAlbum(db.Model):
    # __bind_key__ = "design"
    __tablename__ = "album"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    img_url = db.Column(db.String(500))
    is_deleted = db.Column(db.SmallInteger,default=0)


    def to_dict(self):
        return {"imgUrl": BASE_URL+self.img_url, "id": self.id}


class ShuYanSakura(db.Model):
    # __bind_key__ = "design"
    __tablename__ = "sakura"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    img_url = db.Column(db.String(500))
    sakura_type = db.Column(db.String(255))

    def to_dict(self):
        return {"img_url": BASE_URL+self.img_url, "type": self.sakura_type,  "id": self.id}


# class ShuYanUser(db.Model):
#     # __bind_key__ = "design"
#     __tablename__ = "user"
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
#     name = db.Column(db.String(255))
#     url = db.Column(db.String(500))
#     phone = db.Column(db.String(100))
#     gender = db.Column(db.Integer,default=1)
#
#     def to_dict(self):
#         return {"name": self.name, "url": self.url, "phone": self.phone,"id":self.id}