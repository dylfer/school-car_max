from flask import Flask
# import json
import jwt
from routes import register_routes


app = Flask(__name__, static_url_path='',
            template_folder='web/templates', static_folder='web/static')


register_routes(app)


app.run(host='0.0.0.0', port=80, debug=True)
