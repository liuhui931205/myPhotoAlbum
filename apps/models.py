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


class ShuYanCommodity(db.Model):
    # __bind_key__ = "design"
    __tablename__ = "commodity"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    img_url = db.Column(db.String(500))
    title = db.Column(db.String(255))
    new_price = db.Column(db.String(50))
    old_price = db.Column(db.String(50))


    def to_dict(self):
        return {"img_url": BASE_URL+self.img_url, "title": self.title, "new_price": self.new_price, "id": self.id,"old_price":self.old_price}

class ShuYanCommodityDetail(db.Model):
    # __bind_key__ = "design"
    __tablename__ = "commodity_detail"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    commodity_id = db.Column(db.Integer)
    img_urls = db.Column(db.TEXT(5000))
    title = db.Column(db.String(255))
    new_price = db.Column(db.String(50))
    old_price = db.Column(db.String(50))
    detail_url = db.Column(db.TEXT(5000))

    def to_dict(self):
        return {"img_urls": list(map(lambda x:BASE_URL+x, self.img_urls.split(","))), "title": self.title, "new_price": self.new_price, "id": self.id,"old_price":self.old_price,"detail_url":list(map(lambda x:BASE_URL+x, self.detail_url.split(",")))}


class ShuYanCommodityStyle(db.Model):
    # __bind_key__ = "design"
    __tablename__ = "commodity_style"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    commodity_id = db.Column(db.Integer)
    properties = db.Column(db.String(255))
    inventory = db.Column(db.Integer,default=0)
    color = db.Column(db.String(100))

    def to_dict(self):
        return {"properties": self.properties, "inventory": self.inventory, "color": self.color}


class ShuYanUser(db.Model):
    # __bind_key__ = "design"
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    name = db.Column(db.String(255))
    url = db.Column(db.String(500))
    phone = db.Column(db.String(100))
    gender = db.Column(db.Integer,default=1)

    def to_dict(self):
        return {"name": self.name, "url": self.url, "phone": self.phone,"id":self.id}