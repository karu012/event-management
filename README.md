
# Event Management Web Application

A full-stack web application built using Flask, enabling users to register, log in, and manage their personal events. The app includes features like event CRUD operations, CAPTCHA-based user verification, and profile management — all backed by a MongoDB database and deployed via Visual Studio Code.

## Features

-- User Authentication

- Register/login with secure password handling

- CAPTCHA-based verification to prevent bot logins

- Profile management with password change feature

-- Event Management

- Create, view, update, and delete personal events

- Events stored per user with session-based control

--  Backend Logic

- Flask routes with session management

- MongoDB integration for users and events

- Modular code using models.py for event operations
## Teck Stack

Frontend:	HTML, CSS, Jinja2 Templates

Backend: Python (Flask Framework)

Database:MongoDB (via Flask-PyMongo)

Deployment:	Localhost via Visual Studio Code
## How it works

1.Users can register with a username, email, and password.

2.A CAPTCHA ensures the user is human before allowing login or registration.

3.After logging in, users can:

- View their personal list of events

- Create, edit, or delete events

- Edit their profile information

4.Session data is used to ensure users only access their own events.


## Setup Instructions

- Clone the repository:

      git clone https://github.com/yourusername/event-management-flask.git

      cd event-management-flask

- Create a virtual environment:

      python -m venv venv

      venv\Scripts\activate   # For Windows

- Install required packages:

      pip install flask flask-pymongo

- Run MongoDB locally, then:

      python app.py



## Website Preview
![Image Alt](https://github.com/karu012/event-management/blob/15871a1f8dac024fa92ccd45bba52301677830b2/Screenshot%202025-04-21%20223437.png)
![Image Alt](https://github.com/karu012/event-management/blob/15871a1f8dac024fa92ccd45bba52301677830b2/Screenshot%202025-04-21%20223522.png)
![Image Alt](https://github.com/karu012/event-management/blob/15871a1f8dac024fa92ccd45bba52301677830b2/Screenshot%202025-04-21%20223614.png)
![Image Alt](https://github.com/karu012/event-management/blob/15871a1f8dac024fa92ccd45bba52301677830b2/Screenshot%202025-04-21%20223827.png)
