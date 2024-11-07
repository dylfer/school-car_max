from flask import Flask, request, jsonify
import json
import jwt


app = Flask(__name__, static_url_path='',
            template_folder='web/templates', static_folder='web/static')


app.run(host='0.0.0.0', port=5000, debug=True)
s
