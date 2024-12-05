from flask import Blueprint, render_template

genral_router = Blueprint('genral', __name__)


@genral_router.route('/')
def index():
    return render_template('index.html')


@genral_router.route('/login')
def login():
    return render_template('login.html')


@genral_router.route('/signup')
def signup():
    return render_template('signup.html')


@genral_router.route('/about')
def about():
    return render_template('about.html')


@genral_router.route('/contact')
def contact():
    return render_template('contact.html')


@genral_router.route('/termsandconditions')
def termsandconditions():
    return render_template('terms.html')


@genral_router.route('/privacy')
def privacy():
    return render_template('privacy.html')


# customers


@genral_router.route("/serch")
def serch():
    return render_template('serch.html')


@genral_router.route("/bassket")
def bassket():
    return render_template('bassket.html')


@genral_router.route("/order")
def order():
    return render_template('order.html')


@genral_router.route("/payment")
def payment():
    return render_template('pay.html')
