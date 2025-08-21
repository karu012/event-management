from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_pymongo import PyMongo
from random import randint
from bson.objectid import ObjectId
from models import Event, init_db

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/event_planner'
app.secret_key = 'your_secret_key'
mongo = PyMongo(app)
app.debug = True
init_db(app)

def generate_captcha():
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    session['captcha_result'] = num1 + num2
    return f'{num1} + {num2}'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_captcha = request.form['captcha']

        if int(user_captcha) != session['captcha_result']:
            flash('Incorrect CAPTCHA. Please try again.')
            return render_template('login.html', captcha=generate_captcha())

        user = mongo.db.users.find_one({'username': username, 'password': password})
        if user:
            session['user_id'] = str(user['_id'])
            flash('Successfully logged in!', 'success')
            return redirect(url_for('events'))
        else:
            flash('Invalid username or password.')
    return render_template('login.html', captcha=generate_captcha())

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        user_captcha = request.form['captcha']

        if int(user_captcha) != session['captcha_result']:
            flash('Incorrect CAPTCHA. Please try again.')
            return render_template('register.html', captcha=generate_captcha())

        existing_user = mongo.db.users.find_one({'username': username})
        if existing_user:
            flash('Username already exists.')
        else:
            mongo.db.users.insert_one({'username': username, 'password': password, 'email': email})
            flash('Successfully registered! Please log in.', 'success')
            return redirect(url_for('login'))
    return render_template('register.html', captcha=generate_captcha())

@app.route('/events', methods=['GET'])
def events():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    events = Event.get_events_by_user(session['user_id'])
    return render_template('events.html', events=events)

@app.route('/add_event', methods=['GET', 'POST'])
def add_event():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        event_name = request.form['event_name']
        event_date = request.form['event_date']
        event_time = request.form['event_time']
        event_location = request.form['event_location']

        Event.create_event(event_name, event_date, event_time, event_location, session['user_id'])
        flash("Event created successfully!", 'success')
        return redirect(url_for('events'))

    return render_template('add_event.html')

@app.route('/edit_event/<event_id>', methods=['GET', 'POST'])
def edit_event(event_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    event = Event.get_event(event_id)

    if request.method == 'POST':
        event_name = request.form['event_name']
        event_date = request.form['event_date']
        event_time = request.form['event_time']
        event_location = request.form['event_location']
        
        Event.update_event(event_id, event_name, event_date, event_time, event_location)
        flash("Event updated successfully!", 'success')
        return redirect(url_for('events'))

    return render_template('edit_event.html', event=event)

@app.route('/delete_event/<event_id>', methods=['POST'])
def delete_event(event_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    Event.delete_event(event_id)
    flash("Event deleted successfully!", 'success')
    return redirect(url_for('events'))

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user = mongo.db.users.find_one({'_id': ObjectId(session['user_id'])})
    
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password == confirm_password:
            mongo.db.users.update_one({'_id': ObjectId(session['user_id'])}, {'$set': {'username': username, 'email': email, 'password': password}})
            flash("Profile updated successfully!", 'success')
            return redirect(url_for('profile'))
        else:
            flash("Passwords do not match.")

    return render_template('profile.html', user=user)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash("You have been logged out.", 'success')
    return redirect(url_for('home'))
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)


