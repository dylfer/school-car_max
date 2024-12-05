from flask import Flask, request, jsonify, render_template
# import json
import jwt
from .routes import register_routes


app = Flask(__name__, static_url_path='',
            template_folder='web/templates', static_folder='web/static')


@app.before_request
def before_request():
    if request.path in ['/dashboard']:
        token = request.json.get()
        if not token:
            return jsonify({'message': 'Missing token'}), 401
        try:
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Expired token'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token'}), 401


register_routes(app)


app.run(host='0.0.0.0', port=80, debug=True)
