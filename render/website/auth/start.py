from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
import torch
from diffusers import StableDiffusionPipeline
import time

auth_views = Blueprint ('auth_views', __name__, template_folder='website/templates')

# about page
@auth_views.route('/about', methods = ['GET','POST'])
def about ():
    return render_template('about.html',user=current_user)

@auth_views.route ('/login', methods = ['GET', 'POST'])
def login ():
    from website.models import User
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by (email=email).first ()
        if user:
            if check_password_hash (user.password, password):
                flash ('Logged in successfully!', category='success')
                login_user (user, remember=True)
                return redirect (url_for('home_page.news'))
            else:
                flash ('Incorrect password.', category='error')
        else:
            flash ('Email not found.', category='error')

    return render_template ("login.html",user=current_user)

# to be placed in the home page or under account settings
# make sure that after the user logs in, there would only be 5 tabs to click on
@auth_views.route ('/logout', methods = ['GET'])
@login_required
def logout ():
    logout_user ()
    return redirect (url_for('auth_views.login'))

@auth_views.route ('/sign-up/confirm', methods = ['GET', 'POST'])
def sign_up_confirm ():
    from website.models import User
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by (email=email).first ()

        if user:
            flash ('Email already exists.', category='error')
        elif len (email) < 4: 
            flash ('Email must be greater than 4 characters.', category='error')
        elif len (first_name) < 3: 
            flash ('First name must be greater than 2 characters.', category='error')
        elif password1 != password2:
            flash ('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash ('Password must be at least be 8 characters.', category='error')
        else:
            from website import db
            new_user = User (email=email, first_name=first_name, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add (new_user)
            db.session.commit ()
            flash ('Account created', category='success')
            return redirect (url_for('auth_views.login'))

    return render_template ("sign_up_confirm.html", user=current_user)

@auth_views.route('/sign-up', methods=['GET','POST'])
def sign_up():
    return render_template("sign_up.html", user=current_user)

@ auth_views.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    firstName = data['firstName']

    # stable diffusion model
    model_id = "Meina/MeinaMix_V11"
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float32, use_safetensors=True )
    pipe.safety_checker = None

    # generate image from model
    prompt = f"generate a profile picture for {firstName}, without any signs of visible text"

    steps = 50
    h = 240
    w = 240

    image = pipe (prompt, height=h, width=w, number_of_inference_steps=steps).images [0]

    image.save("website/static/assets/output.png")

    # simulate processing time
    time.sleep(2) 

    return "hello"