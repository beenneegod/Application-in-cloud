#Project created by:
#           Serhii Burenkov
#           Dmytro Tvedovskyi
#           Rostyslav Pyrozhenko
# for class: Interned applications created in cloud 


from flask import Flask, render_template, Blueprint, url_for, redirect, flash, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)

class Note(db.Model):
    __tablename__ = "Notes"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(128), nullable=False)
    addedAt = db.Column(db.DateTime(timezone=True), nullable=False)
    updatedAt = db.Column(db.DateTime(timezone=True), nullable=True)

    def __init__(self, content, addedAt, updatedAt):
        self.content = content
        self.addedAt = addedAt
        self.updatedAt = updatedAt


@app.route("/", methods=['GET', 'POST'])
def getNotes():
    notes = Note.query.all()
    return render_template('index.html', notes=notes)

@app.route("/create", methods=['GET', 'POST'])
def createNote():
    if request.method == 'POST':
        content = request.form['content']
        addedAt = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        note = Note(content=content, addedAt=addedAt, updatedAt=None)
        db.session.add(note)
        db.session.commit()
        return redirect(url_for('getNotes'))
    return render_template('create.html')

@app.route("/edit/<string:id>", methods=['GET', 'POST'])
def editNote(id):
    note = Note.query.filter_by(id=id).first()
    if note:
        if request.method == 'POST':
            note.content = request.form['content']
            note.updatedAt = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
            db.session.merge(note)
            db.session.commit()
            return redirect(url_for('getNotes'))
    else:
        return redirect(url_for('getNotes'))
    return render_template('edit.html', note=note)

@app.route("/delete/<string:id>", methods=['GET', 'POST'])
def deleteNote(id):
    note = Note.query.filter_by(id=id).first()
    if note:
            db.session.delete(note)
            db.session.commit()
    else:
        return redirect(url_for('getNotes'))
    return redirect(url_for('getNotes'))