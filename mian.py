from flask import Flask, request, jsonify, render_template
# import json
import jwt


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

# genral


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/termsandconditions')
def termsandconditions():
    return render_template('terms.html')


@app.route('/privacy')
def privacy():
    return render_template('privacy.html')


# customers


@app.route("/serch")
def serch():
    return render_template('serch.html')


@app.route("/bassket")
def bassket():
    return render_template('bassket.html')


@app.route("/order")
def order():
    return render_template('order.html')


@app.route("/payment")
def payment():
    return render_template('pay.html')


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
    pass
    # data = request.json
    # print(data)
    # return jsonify(data)


@app.route('/api/basket/remove', methods=['POST'])
def api_basket_remove():
    pass


@app.route('/api/basket/update', methods=['POST'])
def api_basket_update():
    pass

# car sale


@app.route("/api/seller/add")
def seller_add():
    pass


@app.route("/api/seller/edit")
def seller_edit():
    pass


@app.route("/api/seller/delete")
def seller_delete():
    pass


@app.route("/api/seller/acept")
def seller_acept():
    pass


app.run(host='0.0.0.0', port=5000, debug=True)
