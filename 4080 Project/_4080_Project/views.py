

from datetime import datetime
from flask import render_template
from flask import request
from flask import redirect
from flask import make_response
from flask import session, redirect, url_for
from _4080_Project import app



import matplotlib.pyplot as plt
import os
from collections import Counter
import pandas as pd


import io
import base64

from datetime import datetime
from flask import render_template
from _4080_Project import app

from flask import render_template, redirect, request


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import numpy as np
import matplotlib.pyplot as plt


import json 
import requests


import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


import io
import base64

from os import path


from flask   import Flask, render_template, flash, request
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms import TextField, TextAreaField, SubmitField, SelectField, DateField
from wtforms import ValidationError



from _4080_Project.Models.QueryFormStructure import QueryFormStructure 

from _4080_Project.Models.QueryFormStructure import LoginFormStructure 
from _4080_Project.Models.QueryFormStructure import UserRegistrationFormStructure 
from _4080_Project.Models.LocalDatabaseRoutines import create_LocalDatabaseServiceRoutines


#print("Push Pull or Run?")
#input = input("choose...")
#if (input == "push"):
#    os.system('git push git@github.com:WhiteRose7303/Flask-Project-H_O.git')
#elif (input == "pull"):
#    os.system('git pull git@github.com:WhiteRose7303/Flask-Project-H_O.git')
#else:
#    print("OK")
#os.system('git pull git@github.com:WhiteRose7303/Flask-Project-H_O.git')

app.config['SECRET_KEY'] = 'The first argument to the field'
db_Functions = create_LocalDatabaseServiceRoutines() 


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )
#add
@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='I would love to hear your feedback'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/Photoalbum')
def Photoalbum():
    """Renders the contact page."""
    return render_template(
        'Photoalbum.html',
        title='Photoalbum',
        year=datetime.now().year,
    )

@app.route('/Privacy')
def Privacy():
    """Renders the contact page."""
    return render_template(
        'Privacy.html',
        title='Privacy',
        year=datetime.now().year,
    )

@app.route('/SiteMap')
def SiteMap():
    """Renders the contact page."""
    return render_template(
        'SiteMap.html',
        title='SiteMap',
        year=datetime.now().year,
    )


@app.route('/Fleet')
def Fleet():
    #/home/HadarOva5384/4080-Project/4080 Project/_4080_Project/static/Data/FleetData.csv (this is the path)
    df = pd.read_csv(path.join(path.dirname(__file__) , 'static\Data\FleetData.csv'))
    four = df[(df['Aircraft Type'] == 'Boeing 747')|(df['Aircraft Type'] == 'Airbus A380')|(df['Aircraft Type'] == 'Airbus A340')]
    a = four.size
    notsafe = df.size - a
    """Renders the contact page."""
    return render_template(
        'Fleet.html',
        title='Is it safe?',
        year=datetime.now().year,
        a=a,
        notsafe = notsafe
    )





#renders Data
@app.route('/Data')
def Data():
    #/home/HadarOva5384/4080-Project/4080 Project/_4080_Project/static/Data/FleetData.csv (this is the path)
    df = pd.read_csv(path.join(path.dirname(__file__) , 'static\Data\FleetData.csv'))
   
    """Renders the Data page."""
    
    return render_template(
        'Data.html',
        title='Data:',
        year=datetime.now().year,
    )


#query page shit the data is multiplyied by 14 becuase the database is way too long for the site to handle
class QueryFormStructureAIR(FlaskForm):
    name = StringField('Airport (In icao) ' , validators = [DataRequired()])
    submit = SubmitField('Enter')

@app.route('/qurey' , methods = ['GET' , 'POST'])
def qurey():
    print("running from qurey()")
    name = None
    capital = ''
    #/home/HadarOva5384/4080-Project/4080 Project/_4080_Project/static/Data/databaseM.csv (this is the path)
    df = pd.read_csv(path.join(path.dirname(__file__) , 'static\Data\databaseM.csv'))
    a = df['Airport ID'].values
    df = df.set_index('Airport ID')
    form = QueryFormStructureAIR(request.form)
    if (request.method == 'POST' ):
        name = form.name.data
        if (name in df.index):
            capital = list(a).count(name)*14
            #df.loc[name,'amount']
        else:
            capital = name+ ', no such Airport'
        form.name.data= ''
    raw_data_table = df.to_html(classes = 'table table-hover')

    return render_template('qurey.html',
                           form= form,
                           name = capital,
                           raw_data_table = raw_data_table,
                           title = 'Query by the user',
                           year=datetime.now().year,
                           message='query input'
                           )

    

    

# -------------------------------------------------------
# Register new user page
# -------------------------------------------------------
@app.route('/register', methods=['GET', 'POST'])
def Register():
    form = UserRegistrationFormStructure(request.form)

    if (request.method == 'POST' and form.validate()):
        if (not db_Functions.IsUserExist(form.username.data)):
            db_Functions.AddNewUser(form)
            db_table = ""

            flash('Thanks for registering new user - '+ form.FirstName.data + " " + form.LastName.data )
            # Here you should put what to do (or were to go) if registration was good
        else:
            flash('Error: User with this Username already exist ! - '+ form.username.data)
            form = UserRegistrationFormStructure(request.form)

    return render_template(
        'register.html', 
        form=form, 
        title='Register New User',
        year=datetime.now().year,
        repository_name='Pandas',
        )

# -------------------------------------------------------
# Login page
# This page is the filter before the data analysis
# -------------------------------------------------------
@app.route('/login', methods=['GET', 'POST'])
def Login():
    form = LoginFormStructure(request.form)

    if (request.method == 'POST' and form.validate()):
        if (db_Functions.IsLoginGood(form.username.data, form.password.data)):
            flash('Login approved!')
            return redirect(url_for('Data'))
        else:
            flash('Error in - Username and/or password')
   
    return render_template(
        'login.html', 
        form=form, 
        title='Login to data analysis',
        year=datetime.now().year,
        repository_name='Pandas',
        )

class QueryFormStructureFP(FlaskForm):
    name = SelectField('Flight Phase? ', choices=[('CLIMB','Climb'), ('TAKEOFF RUN', 'Take Off'),('APPROACH', 'Approach'),('LANDING ROLL', 'Landing Roll'),('EN ROUTE', 'En Route'),('DESCENT', 'Descent')], validators = [DataRequired()])
    submit = SubmitField('Enter')


#renders the FP page
@app.route('/WhatFP' , methods = ['GET' , 'POST'])
def WhatFP():
    print("running from qurey()")
    name = None
    capital = ''
    #/home/HadarOva5384/4080-Project/4080 Project/_4080_Project/static/Data/WhatFP.csv (this is the path)
    df = pd.read_csv(path.join(path.dirname(__file__) , 'static\Data\WhatFP.csv'))
    a = df['Flight Phase'].values
    df = df.set_index('Flight Phase')
    form = QueryFormStructureFP(request.form)
    if (request.method == 'POST' ):
        name = form.name.data
        if (name in df.index):
            capital = list(a).count(name)*14
            #df.loc[name,'amount']
        else:
            capital = name+ ', no such Flight phase'
        form.name.data= ''
    raw_data_table = df.to_html(classes = 'table table-hover')

    return render_template('WhatFP.html',
                           form= form,
                           name = capital,
                           raw_data_table = raw_data_table,
                           title = 'Query by the user',
                           year=datetime.now().year,
                           message='query input'
                           )








