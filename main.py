from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from db_connection import get_db_connection, get_all_comments, get_comments, limit, delete, update, create
import random


app = Flask(__name__)
api = Api(app)
CORS(app)

class comments(Resource):
    def get(self, id=0):
        if id == 0:
            count_of_records = limit()
            comments = get_comments(random.randint(1, count_of_records))
            comments_json = raw_to_json(comments)
            return comments_json
        comments = get_comments(id)
        if comments:
            comments_json = raw_to_json(comments)
            return comments_json

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("text")
        parser.add_argument("description")

        params = parser.parse_args()
        answer = create(params["text"], params["description"])
        json_data = jsonify(f"Records create with id {answer}")
        json_data.status_code = 201
        return json_data

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("text")
        parser.add_argument("description")

        params = parser.parse_args()
        update(id, params["text"], params["description"])
        json_data = jsonify(f"Records edit with id {id}")
        json_data.status_code = 202
        return json_data

    def delete(self, id):
        delete(id)
        json_data = jsonify(f"Records deleted with id {id}")
        json_data.status_code = 200
        return json_data


def raw_to_json(comments):

    return {"id": comments["id"],
"text": comments["text"],
"description": comments["description"]
}




SWAGGER_URL = "/swagger/"
API_URL = "/static/swagger.json"

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Comments API'
    }
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

api.add_resource(comments, "/api/v1.0/comments/", "/api/v1.0/comments/<int:id>")

if __name__ == "__main__":
    app.run(debug=True)