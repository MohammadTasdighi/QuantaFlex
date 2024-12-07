# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    features = db.Column(db.JSON)

class EntityProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    contact_info = db.Column(db.String(255))
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))

class SpecificProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entity_id = db.Column(db.Integer, db.ForeignKey('entity_profile.id'))
    profile_name = db.Column(db.String(150), nullable=False)
    profile_id = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    profile_details = db.Column(db.JSON)

class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    task_name = db.Column(db.String(150), nullable=False)
    task_date = db.Column(db.String(10), nullable=False)
    task_time = db.Column(db.String(5), nullable=False)
