from flask import Flask, render_template, jsonify

app = Flask(__name__)

# ROUTES
@app.route("/")
def index():
    """
    MAIN PAGE (ONEPAGE LAYOUT)
    """
    return "Hello World"


# PROJECT ROUTES
@app.route("/project/<project_name>")
def project(project_name:str):
    return

# (API CALLS)
@app.route("/project/create")
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
    return

@app.route("/project/delete")
def project_delete() -> jsonify:
    """
    DELETE PROJECT => ONLY ADMIN

    PARAMS:
        :name:
        :id:
    """
    return

@app.route("/project/random")
def project_random() -> jsonify:
    return jsonify({"msg": "test"})

# START
if __name__ == '__main__':
    app.run(debug=True)