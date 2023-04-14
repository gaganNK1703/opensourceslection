from app import app
from flask import request
from model.repository_model import repository_model
repo=repository_model()


@app.route("/user/repository",methods=["POST"])
def repository():

    return repo.repository_search(request.form)

