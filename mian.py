from flask import Flask, request, jsonify, render_template
import json
import jwt


app = Flask(__name__, static_url_path='',
            template_folder='web/templates', static_folder='web/static')


@app.before_request
def before_request():
    if request.path in ['/dashboard']:
        pass  # auth check
        # token = request.headers.get('Authorization')
        # if not token:
        #     return jsonify({'message': 'Missing token'}), 401
        # try:
        #     jwt.decode(token, 'secret', algorithms=['HS256'])
        # except jwt.ExpiredSignatureError:
        #     return jsonify({'message': 'Expired token'}), 401
        # except jwt.InvalidTokenError:
        #     return jsonify({'message': 'Invalid token'}), 401


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


# API

# auth
@app.route('/api/login', methods=['POST'])
def api_login():
    data = request.json
    print(data)
    return jsonify(data)


@app.route('/api/signup', methods=['POST'])
def api_signup():
    data = request.json
    print(data)
    return jsonify(data)


# order

@app.route('/api/basket/add', methods=['POST'])
def api_basket_add():
    # data = request.json
    # print(data)
    # return jsonify(data)


@app.route('/api/basket/remove', methods=['POST'])
def api_basket_remove():
    pass


@app.route('/api/basket/update', methods=['POST'])
def api_basket_update():
    pass


app.run(host='0.0.0.0', port=5000, debug=True)
