#!/usr/bin/env python3

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from app import db

class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    bio = db.Column(db.String(80))

    def __repr__(self):
        return "%s)%s - %s" %(self.id,self.name,self.bio)

class Medium(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(80), unique=True)

class Classification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(80), unique=True)

class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(80), unique=True)

class Art(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    ## Artist
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'))
    artist = db.relationship('Artist',
        backref=db.backref('art_works', lazy='dynamic'))

    medium_id = db.Column(db.Integer, db.ForeignKey('medium.id'))
    medium = db.relationship('Medium',
        backref=db.backref('others_in_medium', lazy='dynamic'))

    classification_id = db.Column(db.Integer, db.ForeignKey('classification.id'))
    classification = db.relationship('Classification',
        backref=db.backref('others_in_class', lazy='dynamic'))

    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))
    department = db.relationship('Department',
        backref=db.backref('others_in_department', lazy='dynamic'))

    dimensions = db.Column(db.String(128))
    curator_approved = db.Column(db.Boolean)
    museem_of_modern_art_number = db.Column(db.String(12))
    object_id = db.Column(db.Integer)
    url = db.Column(db.String(256))

def get_or_create(_type,**kwargs):

    temp = _type.query.filter_by(**kwargs).first()
    if not temp:
        temp = _type(**kwargs)
        db.session.add(temp)
    return temp


def main():
    db.drop_all()
    db.create_all()
    # print(get_or_create(Artist,name="dave"))

if __name__ == '__main__':
    main()
