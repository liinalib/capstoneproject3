from flask import Blueprint, jsonify

import utils

api_bp = Blueprint('api', __name__, url_prefix='/api')


@api_bp.route("/post/")
def api_posts():
    posts = utils.load_posts()
    return jsonify(posts)

@api_bp.route("/post/<int:pk>")
def api_post(pk):
    post = utils.load_post(pk)
    return jsonify(post)