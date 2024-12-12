from flask import Blueprint, render_template

genral_router = Blueprint('genral', __name__)

# TODO add titles as page pramiters


@genral_router.route('/')
def index():
    return render_template('base.html', content_template='index.html', title='Home')


@genral_router.route('/login')
def login():
    return render_template('base.html', content_template='login.html', title='Login')


@genral_router.route('/signup')
def signup():
    return render_template('base.html', content_template='signup.html', title='Sign up')


@genral_router.route('/about')
def about():
    return render_template('base.html', content_template='about.html', title='About')


@genral_router.route('/contact')
def contact():
    return render_template('base.html', content_template='contact.html', title='Contact us')


@genral_router.route('/termsandconditions')
def termsandconditions():
    return render_template('base.html', content_template='terms.html', title='T&C')


@genral_router.route('/privacy')
def privacy():
    return render_template('base.html', content_template='privacy.html', title='Privacy')


# customers


@genral_router.route("/serch")
def serch():
    return render_template('base.html', content_template='serch.html', title='Serch')


@genral_router.route("/bassket")
def bassket():
    return render_template('base.html', content_template='bassket.html', title='Basket')


@genral_router.route("/payment")
def payment():
    return render_template('base.html', content_template='pay.html', title='Payment')

# account


@genral_router.route("/dashboard")
def dashboard():
    return render_template('base.html', content_template='dashboard.html', title='Dashboard')


@genral_router.route("/orders")
def order():
    return render_template('base.html', content_template='order.html', title='Orders')


@genral_router.route("/settings")
def settings():
    return render_template('base.html', content_template='settings.html', title='Settings')


@genral_router.route("/bookings")
def bookings():
    return render_template('base.html', content_template='bookings.html', title='Bookings')
