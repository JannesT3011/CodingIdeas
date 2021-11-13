from flask import Flask, render_template, request, jsonify, redirect, url_for
import random
import os
from datetime import datetime
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
import uuid
import random

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///projects.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

def generate_uuid():
    """
    GENERATE A UUID(4)
    """
    return str(uuid.uuid4())

def generate_id():
    """
    GENERATE A ID OF 5 NUMBERS
    """
    one = str(random.randrange(0,9))
    two = str(random.randrange(0,9)) 
    three = str(random.randrange(0,9)) 
    four = str(random.randrange(0,9))  
    five = str(random.randrange(0,9))  

    return one+two+three+four+five

class Project(db.Model):
    """
    PROJECT MODEL OF PROJECT
    """
    id = db.Column(db.String, primary_key=True, default=generate_id, unique=True)
    name = db.Column(db.String(20))
    mail = db.Column(db.String(320))
    small_description = db.Column(db.String(100))
    description = db.Column(db.String(500))
    level = db.Column(db.String(15)) # three levels: beginner, expercienced or pro
    #tags = db.Column(db.Array()) # TODO later feature
    github_url = db.Column(db.String(2048))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)


@app.route("/", methods=["GET"])
def index() -> render_template:
    """
    MAIN PAGE (ONEPAGE LAYOUT)
    """

    return render_template("index.html", projects=get_projects())

def get_projects() -> list:
    """
    RETURNS ALL PROJECTS (LIST OF DICTS)
    MAYBE PUT THIS FUNCTIONS IN THE THE db.py file in database/
    """
    all_projects = []
    projects = Project.query.order_by(desc(Project.date_created)).all()
    for project in projects:
        pproject = {
            "id": project.id,
            "title": project.name,
            "level": project.level,
            "description": project.description,
            "github_url": project.github_url,
        }
        all_projects.append(pproject)

    return all_projects

# PROJECT ROUTES
@app.route("/project/<project_id>/<project_name>", methods=["GET"])
def project(project_id:str, project_name:str):
    """
    LOAD THE PROJECT TO GET MORE DETAILS

    PARAMS:
        :project_name:
    """
    
    project = Project.query.filter_by(id=project_id).first()
    name = project.name
    level = project.level
    description = project.description
    github_url = project.github_url

    return render_template("project.html", project_name=name, project_level=level, project_description=description, project_githuburl=github_url), 200

# (API CALLS)
@app.route("/project/create", methods=["POST"])
def project_create() -> jsonify:
    """
    CREATE PROJECT 

    RATE LIMIT (only can create every 10 minutes from same ip)

    PARAMS:
        :name:
        :mail:
        :project_title:
        :description:
        :github_links:

        :id for database (created automaticly):
    """
    name = request.form["projectName"]
    mail = request.form["projectEmail"]
    description = request.form["projectDescription"]
    level = request.form["dropdown"]
    github_url = request.form["projectUrl"]

    project = Project(
        name=name,
        mail=mail,
        small_description=description[0:99],
        description=description,
        level=level,
        github_url=github_url
    )

    db.session.add(project)
    db.session.commit()

    #jsonify({"message": f"Project {name}({id}) created!"})
    return redirect("/")

@app.route("/project/delete", methods=["POST"])
def project_delete() -> jsonify:
    """
    DELETE PROJECT => ONLY ADMIN

    PARAMS:
        :name:
        :id:
    """
    data = request.get_json()
    id = data["id"]
    #name = data["name"]

    Project.query.filter_by(id=id).delete()
    db.session.commit()

    return jsonify({"message": f"Project {id} deleted!"}), 200

@app.route("/project/random", methods=["GET"])
def project_random() -> jsonify:
    """
    GET A RANDOM PROJECT
    """
    projects = get_projects()
    random_project = random.choice(projects)
    
    return jsonify(random_project), 200

if __name__ == '__main__':
    app.run()