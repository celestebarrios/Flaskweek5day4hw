from avengers import app, db, Message, mail
from flask import render_template, request, redirect, url_for
#Import for Forms
from avengers.forms import LoginForm, UserInfoForm
#Import Model
from avengers.models import User, Number,check_password_hash
#Import for Flask Login --login_required, login_user, current_user, log_out
from flask_login import login_required, login_user, current_user, logout_user 
# Home Route
@app.route('/')
def home():
    form = Number.query.all()
    return render_template("home.html", form = form)


# CREATE User
@app.route('/register', methods=['GET','POST'])
def register():
    form = UserInfoForm()
    if request.method == 'POST' and form.validate():
        #Get Information
        username = form.username.data
        password = form.password.data
        email = form.email.data
        print("\n",username,password,email)#to make sure we have the correct data
        #Create an instance of User
        user = User(username, email, password)
        #Open and insert into database
        db.session.add(user)
        #Save info into database
        db.session.commit()

        #flask Email Sender
        msg = Message(f'Thanks for signing up{email}', recipients=[email])
        msg.body =('Congrats on signing up! Looking forward to your posts!')
        msg.html = ('<h1 >Welcome to Avengers Forum</h1>''<p>This will be super duper!</p>')

        mail.send(msg)

    return render_template('register.html', form = form)
#Create Number
@app.route('/number', methods=['GET','POST'] )
@login_required
def number():
    form = NumberForm()
    if request.method == 'POST' and form.validate():
        #Get Information
        number = form.number.data
        number_update = form.number_update.data
        print(number)#to make sure we have the correct data
        #Create an instance of User
        user = Number(number, number_update)
        #Open and insert into database
        db.session.add(user)
        #Save info into database
        db.session.commit()
    return render_template('number.html', form = form)


#UPDATE 
@app.route('/number/update/<int:number_id>', methods= ['GET','POST'])
@login_required
def number_update(number_id):
    number = Number.query.get_or_404(number_id)
    update_form = UserInfoForm()
    if request.method == 'POST' and update_form.validate():
        update = update_form.number.data
        username = update_form.username.data
        user_id = current_user.id
        print(update, username,user_id)

        #update will get added to the DB
        update.number = number
        update.username = username
        update.user_id = user_id

        db.session.commit()
        return redirect(url_for('home'))
    return render_template('number_update.html', update_form = update_form)

#DELETE Number
@app.route('/number/delete/<int:number_id>', methods = ['POST'])
@login_required
def number_delete(number_id):
    number = User.query.get_or_404(number_id)
    if request.method == 'POST':
        db.session.delete(number)
        db.session.commit()
        return redirect(url_for('home'))
   
    
@app.route('/number_detail/<int:number_id>')
@login_required
def number_detail(number_id):
    number = Post.query.get_or_404(number_id)
    return render_template('number_detail.html', number = number)

#Login Form Route
@app.route('/login', methods= ['GET','POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = form.password.data
        logged_user = User.query.filter(User.email == email).first()
        logged_user1 = User.query.filter(User.number == number).first()
        if logged_user and logged_user1 and check_password_hash(logged_user.password, password):
            login_user(logged_user)
            login_user(logged_user1)
            return redirect(url_for('home'))
        else:
            return redirect(url_for('login'))

#Logout
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

