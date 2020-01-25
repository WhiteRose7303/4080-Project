"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from flask import request
from flask import redirect
from flask import make_response
from _4080_Project import app
from pandas import pandas as pd
import matplotlib.pyplot as plt
import os

import io
import base64

from datetime import datetime
from flask import render_template
from _4080_Project import app


from datetime import datetime
from flask import render_template, redirect, request

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#check
import json 
import requests

import pandas as pd
import matplotlib.pyplot as plt

import io
import base64

from os import path

from flask   import Flask, render_template, flash, request
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms import TextField, TextAreaField, SubmitField, SelectField, DateField
from wtforms import ValidationError


app.config['SECRET_KEY'] = 'The first argument to the field'


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

class QueryFormStructure(FlaskForm):
    name = StringField('Country Name?' , validators = [DataRequired()])
    submit = SubmitField('Submit')

@app.route('/qurey' , methods = ['GET' , 'POST'])
def qurey():
    print("running from qurey()")
    name = None
    capital = ''
    df = pd.read_csv(path.join(path.dirname(__file__) , 'static\\Data\\Capitals.csv'))
    df = df.set_index('Country')
    form = QueryFormStructure(request.form)
    if (request.method == 'POST' ):
        name = form.name.data
        if (name in df.index):
            capital = df.loc[name,'Capital']
        else:
            capital = name+ ', no such country'
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



