def Imports():
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
    from os import path
    
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
    
    import os
    
    
    from flask   import Flask, render_template, flash, request
    from wtforms import Form, BooleanField, StringField, PasswordField, validators
    from wtforms import TextField, TextAreaField, SubmitField, SelectField, DateField
    from wtforms import ValidationError
    
    
    
    from _4080_Project.Models.QueryFormStructure import QueryFormStructure 
    
    from _4080_Project.Models.QueryFormStructure import LoginFormStructure 
    from _4080_Project.Models.QueryFormStructure import UserRegistrationFormStructure 
    from _4080_Project.Models.LocalDatabaseRoutines import create_LocalDatabaseServiceRoutines
    return BooleanField, Counter, DataRequired, DateField, Figure, FigureCanvas, Flask, FlaskForm, Form, LoginFormStructure, PasswordField, QueryFormStructure, SelectField, StringField, SubmitField, TextAreaField, TextField, UserRegistrationFormStructure, ValidationError, app, base64, create_LocalDatabaseServiceRoutines, datetime, flash, io, json, make_response, np, os, pd, plt, redirect, render_template, request, requests, session, url_for, validators

BooleanField, Counter, DataRequired, DateField, Figure, FigureCanvas, Flask, FlaskForm, Form, LoginFormStructure, PasswordField, QueryFormStructure, SelectField, StringField, SubmitField, TextAreaField, TextField, UserRegistrationFormStructure, ValidationError, app, base64, create_LocalDatabaseServiceRoutines, datetime, flash, io, json, make_response, np, os, pd, plt, redirect, render_template, request, requests, session, url_for, validators = Imports()

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

from matplotlib.figure import Figure

def URL():
    URL_1 = "https://raw.githubusercontent.com/WhiteRose7303/Data/master/databaseM.csv"
    UURL_1 = requests.get(URL_1).content
    URL_2 = "https://raw.githubusercontent.com/WhiteRose7303/Data/master/WhatFP.csv"
    UURL_2 = requests.get(URL_2).content
    URL_3 = "https://raw.githubusercontent.com/WhiteRose7303/Data/master/FleetData.csv"
    UURL_3 = requests.get(URL_3).content
    return URL_1, URL_2, URL_3, UURL_1, UURL_2, UURL_3

URL_1, URL_2, URL_3, UURL_1, UURL_2, UURL_3 = URL()


URL_4 = 'https://raw.githubusercontent.com/WhiteRose7303/Flask-Project-H_O/25/2/20/4080%20Project/_4080_Project/static/Data/database.csv'

from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)
from  _4080_Project.Models.Forms import ExpandForm
from  _4080_Project.Models.Forms import CollapseForm


def plot_to_img(fig):
     pngImage = io.BytesIO()
     FigureCanvas(fig).print_png(pngImage)
     pngImageB64String = "data:image/png;base64,"
     pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
     return pngImageB64String



            
               
#chheck
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
    
    df = pd.read_csv(URL_3)
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


@app.route('/Account')
def Account():
    return render_template(
        'account.html',
        title='SiteMap',
        year=datetime.now().year,
        
    )


@app.route('/Rawd')
def rawd():
    rawdata_f = pd.read_csv(URL_3)
    rawf = rawdata_f.to_html()
    return render_template(
        'Rawd.html',
        title='SiteMap',
        year=datetime.now().year,
        rawf = rawf
        
    )

@app.route('/RawData')
def RawData():

    return render_template(
        'RawData.html',
        title='RawData',
        year=datetime.now().year,
      
        
    )

@app.route('/Soduku')
def Soduku():
    return render_template(
        'Soduku.html',
        title='Solver',
        year=datetime.now().year,
        
    )

#renders Data
@app.route('/Data')
def Data():
    df = pd.read_csv(URL_3)
   
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
    form1 = ExpandForm()
    form2 = CollapseForm()

    df = pd.read_csv(URL_1)
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

    if request.method == 'POST':
        if request.form['action'] == 'Expand' and form1.validate_on_submit():
            raw_data_table = df.to_html(classes = 'table table-hover')
        if request.form['action'] == 'Collapse' and form2.validate_on_submit():
            raw_data_table = ''
                         


    return render_template('qurey.html',
                           form= form,
                           name = capital,
                           raw_data_table = raw_data_table,
                           title = 'Query by the user',
                           year=datetime.now().year,
                           message='query input',
                           form1 = form1,
                           form2 = form2
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
    
    df = pd.read_csv(URL_2)
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


class QueryFormStructureFD(FlaskForm):
    name = SelectField('Aircraft? ', choices=[('A-7K', 'A-7K'), ('VC-9C', 'VC-9C'), ('F-4D', 'F-4D'), ('CURTIS C-46', 'CURTIS C-46'), ('C-130A', 'C-130A'), ('WC-130E', 'WC-130E'), ('BE-17', 'BE-17'), ('AC-130H', 'AC-130H'), ('C-137C', 'C-137C'), ('WACO', 'WACO'), ('C-130B', 'C-130B'), ('BRISTOL FRTR', 'BRISTOL FRTR'), ('FAIRCHILD FH227', 'FAIRCHILD FH227'), ('C-130Y', 'C-130Y'), ('A-7', 'A-7'), ('A-7D', 'A-7D'), ('BAC 1-11', 'BAC 1-11'), ('SAAB', 'SAAB'), ('F-111D', 'F-111D'), ('C-18B', 'C-18B'), ('KC-130', 'KC-130'), ('NORD 262', 'NORD 262'), ('RF-4C', 'RF-4C'), ('RKWL LARK', 'RKWL LARK'), ('OV-10A', 'OV-10A'), ('B-52G', 'B-52G'), ('SIKORSKY', 'SIKORSKY'), ('VC-137C', 'VC-137C'), ('AC-130', 'AC-130'), ('SUKHOI SU-29', 'SUKHOI SU-29'), ('FOKKER F28', 'FOKKER F28'), ('RKWL DARTER', 'RKWL DARTER'), ('B-STEARMAN', 'B-STEARMAN'), ('C-135C', 'C-135C'), ('F-4', 'F-4'), ('HAWKER-SDLY HS748', 'HAWKER-SDLY HS748'), ('TG-7A', 'TG-7A'), ('BE-UNKNOWN', 'BE-UNKNOWN'), ('F-4G', 'F-4G'), ('MAULE M-6', 'MAULE M-6'), ('PA-36-375', 'PA-36-375'), ('WC-130', 'WC-130'), ('T-3A', 'T-3A'), ('EC135E', 'EC135E'), ('CONVAIR 600', 'CONVAIR 600'), ('TC-18E', 'TC-18E'), ('LOCKHEED 188', 'LOCKHEED 188'), ('NAMC YS-11A', 'NAMC YS-11A'), ('C-130G', 'C-130G'), ('C-141', 'C-141'), ('LEARJET-23', 'LEARJET-23'), ('C-18', 'C-18'), ('C-20D', 'C-20D'), ('WC-135B', 'WC-135B'), ('WC-135', 'WC-135'), ('E-6A', 'E-6A'), ('FAIRCHILD 24', 'FAIRCHILD 24'), ('BELLANCA 260', 'BELLANCA 260'), ('VC-135E', 'VC-135E'), ('C-137', 'C-137'), ('MH-53J', 'MH-53J'), ('F/A-18', 'F/A-18'), ('C-23', 'C-23'), ('C-9', 'C-9'), ('T-41C', 'T-41C'), ('EC135H', 'EC135H'), ('CH-1N', 'CH-1N'), ('EC135C', 'EC135C'), ('AT-38A', 'AT-38A'), ('G-2', 'G-2'), ('P-3', 'P-3'), ('KC-135', 'KC-135'), ('DA-100 FALCON', 'DA-100 FALCON'), ('C-9B', 'C-9B'), ('C-22B', 'C-22B'), ('C-135B', 'C-135B'), ('CT-114', 'CT-114'), ('RC-135S', 'RC-135S'), ('BA-ATP', 'BA-ATP'), ('CONCORDE', 'CONCORDE'), ('AN-124', 'AN-124'), ('VOLPARE BE18', 'VOLPARE BE18'), ('BELL 47', 'BELL 47'), ('AT-502', 'AT-502'), ('RC-135U', 'RC-135U'), ('P-3C', 'P-3C'), ('SHORTS SC7', 'SHORTS SC7'), ('OA-10A', 'OA-10A'), ('LOCKHEED', 'LOCKHEED'), ('EC-18B', 'EC-18B'), ('T-41D', 'T-41D'), ('T-44A', 'T-44A'), ('F/A-18B', 'F/A-18B'), ('C-135A', 'C-135A'), ('C-12C', 'C-12C'), ('AC-130U', 'AC-130U'), ('C-141B', 'C-141B'), ('MERLIN', 'MERLIN'), ('BE-2000', 'BE-2000'), ('TH-53A', 'TH-53A'), ('WC-130H', 'WC-130H'), ('ROBIN R2000 SERIES', 'ROBIN R2000 SERIES'), ('UV-18B', 'UV-18B'), ('VC-137', 'VC-137'), ('BOEING UNKN', 'BOEING UNKN'), ('FOKKER F28 MK 1000', 'FOKKER F28 MK 1000'), ('FAIRCH SA227', 'FAIRCH SA227'), ('FOKKER F28 MK 4000', 'FOKKER F28 MK 4000'), ('HH-60J', 'HH-60J'), ('LOCKHEED 1329', 'LOCKHEED 1329'), ('BA-146-300', 'BA-146-300'), ('BE-77  SKIPPER', 'BE-77  SKIPPER'), ('L-1011-500', 'L-1011-500'), ('C-20A', 'C-20A'), ('C-20H', 'C-20H'), ('HELIO COURIER H295', 'HELIO COURIER H295'), ('DC-10-40', 'DC-10-40'), ('AYRES THRUSH', 'AYRES THRUSH'), ('LOCKHEED JETST', 'LOCKHEED JETST'), ('C-9A', 'C-9A'), ('CITATION VI', 'CITATION VI'), ('MOONEY UNKN', 'MOONEY UNKN'), ('FAIRCHILD F27', 'FAIRCHILD F27'), ('CV-580', 'CV-580'), ('STEARMAN', 'STEARMAN'), ('DORNIER', 'DORNIER'), ('REPUBLIC RC3', 'REPUBLIC RC3'), ('L-1011', 'L-1011'), ('AEROS SA341', 'AEROS SA341'), ('AEROS SN601', 'AEROS SN601'), ('DC-8-62', 'DC-8-62'), ('FOKKER F100', 'FOKKER F100'), ('C-12D', 'C-12D'), ('BE-80 QUEEN', 'BE-80 QUEEN'), ('BA-146-100', 'BA-146-100'), ('C-141C', 'C-141C'), ('C-38A', 'C-38A'), ('C-5C', 'C-5C'), ('GRUMMAN G73', 'GRUMMAN G73'), ('EC135L', 'EC135L'), ('MC-130E', 'MC-130E'), ('C-406 CARAVA', 'C-406 CARAVA'), ('C-9C', 'C-9C'), ('T-6B', 'T-6B'), ('AT-38B', 'AT-38B'), ('BA-146', 'BA-146'), ('BELL EH-1H', 'BELL EH-1H'), ('C-20B', 'C-20B'), ('C-12J', 'C-12J'), ('EC130E', 'EC130E'), ('CL-215', 'CL-215'), ('C-40C', 'C-40C'), ('MD-600N', 'MD-600N'), ('E-3B', 'E-3B'), ('LEARJET-24', 'LEARJET-24'), ('WC-135W', 'WC-135W'), ('HC-130N', 'HC-130N'), ('TC-135S', 'TC-135S'), ('E-8C', 'E-8C'), ('HAWKER', 'HAWKER'), ('UH-1H', 'UH-1H'), ('F-15D', 'F-15D'), ('C-40B', 'C-40B'), ('OC-135B', 'OC-135B'), ('C-32A', 'C-32A'), ('F-16A', 'F-16A'), ('F-16B', 'F-16B'), ('EC130H', 'EC130H'), ('BA-RJ85', 'BA-RJ85'), ('T-43A', 'T-43A'), ('DC-8-63', 'DC-8-63'), ('E-4B', 'E-4B'), ('C-26B', 'C-26B'), ('KC-135T', 'KC-135T'), ('RC-135W', 'RC-135W'), ('LAKE LA4-200', 'LAKE LA4-200'), ('C-37A', 'C-37A'), ('C-135E', 'C-135E'), ('MC-130H', 'MC-130H'), ('C-32B', 'C-32B'), ('F-117A', 'F-117A'), ('B-1B', 'B-1B'), ('F-15B', 'F-15B'), ('A-10A', 'A-10A'), ('AEROS SA315', 'AEROS SA315'), ('FOKKER F27', 'FOKKER F27'), ('F-15A', 'F-15A'), ('HC-130P', 'HC-130P'), ('KC-10A', 'KC-10A'), ('C-5A', 'C-5A'), ('E-3C', 'E-3C'), ('U-2S', 'U-2S'), ('LC-130H', 'LC-130H'), ('C-5B', 'C-5B'), ('F-15C', 'F-15C'), ('WC-130J', 'WC-130J'), ('MC-130P', 'MC-130P'), ('C-21A', 'C-21A'), ('RC-135V', 'RC-135V'), ('T-38C', 'T-38C'), ('B-52H', 'B-52H'), ('EC130J', 'EC130J'), ('TC-135W', 'TC-135W'), ('B-727', 'B-727'), ('AERONCA 7', 'AERONCA 7'), ('C-130E', 'C-130E'), ('KC-135E', 'KC-135E'), ('T-1A', 'T-1A'), ('WC-135C', 'WC-135C'), ('T-37B', 'T-37B'), ('F-16C', 'F-16C'), ('C-130H', 'C-130H'), ('C-17A', 'C-17A'), ('SIKORSKY S-61L', 'SIKORSKY S-61L'), ('KC-135R', 'KC-135R'), ('BELL HH-IH', 'BELL HH-IH'), ('AEROSTAR 600', 'AEROSTAR 600'), ('E-3', 'E-3'), ('FOKKER 70', 'FOKKER 70'), ('ALON A2', 'ALON A2'), ('AVIAT PITTS S1', 'AVIAT PITTS S1'), ('ERCO 415', 'ERCO 415'), ('GLOBE GC1', 'GLOBE GC1'), ('LOCKHEED 382', 'LOCKHEED 382'), ('AIRBUS', 'AIRBUS'), ('DC-8-61', 'DC-8-61'), ('CAP AVION MUDRY', 'CAP AVION MUDRY'), ('SOCATA TB9', 'SOCATA TB9'), ('CONVAIR 340', 'CONVAIR 340'), ('URBAN AIR LAMBADA', 'URBAN AIR LAMBADA'), ('G-164 AG CAT', 'G-164 AG CAT'), ('HELIO COURIER 800', 'HELIO COURIER 800'), ('C-305', 'C-305'), ('MD-902', 'MD-902'), ('BELL 230', 'BELL 230'), ('ZODIAC CH601', 'ZODIAC CH601'), ('GRUMAMER AA1', 'GRUMAMER AA1'), ('AGUST WESTLAND EH101', 'AGUST WESTLAND EH101'), ('F-16D', 'F-16D'), ('LUSCOMBE 8', 'LUSCOMBE 8'), ('C-U206F', 'C-U206F'), ('BELL-205A1', 'BELL-205A1'), ('BE-23 SUNDOWNER', 'BE-23 SUNDOWNER'), ('GIPPSLAND GA-8', 'GIPPSLAND GA-8'), ('MD-900', 'MD-900'), ('AT-301', 'AT-301'), ('C-175', 'C-175'), ('MERLIN IV', 'MERLIN IV'), ('B-747-300', 'B-747-300'), ('PA-12', 'PA-12'), ('DC-9-40', 'DC-9-40'), ('B-707', 'B-707'), ('RKWL CMDR112', 'RKWL CMDR112'), ('DC-8', 'DC-8'), ('RYAN NAVION', 'RYAN NAVION'), ('CRJ705', 'CRJ705'), ('SOCATA TB-10', 'SOCATA TB-10'), ('BELLANCA', 'BELLANCA'), ('BE-23 MUSKETEER', 'BE-23 MUSKETEER'), ('MBB-105', 'MBB-105'), ('LOCKHEED P3A', 'LOCKHEED P3A'), ('BELLANCA 1730', 'BELLANCA 1730'), ('C-303', 'C-303'), ('PA-30 TWIN COMANCHE', 'PA-30 TWIN COMANCHE'), ('FLIGHT DESIGN CTSW', 'FLIGHT DESIGN CTSW'), ('FAIRCHILD SA227', 'FAIRCHILD SA227'), ('G-159', 'G-159'), ('AEROS SA360', 'AEROS SA360'), ('B-727-100', 'B-727-100'), ('GRUMMAN S-2 TRACKER', 'GRUMMAN S-2 TRACKER'), ('SIKORSKY S-65C', 'SIKORSKY S-65C'), ('AA-5', 'AA-5'), ('DHC3-OTTER', 'DHC3-OTTER'), ('BE-18', 'BE-18'), ('LIBERTY XL-2', 'LIBERTY XL-2'), ('AEROS 355', 'AEROS 355'), ('DC-6', 'DC-6'), ('PA-60 601', 'PA-60 601'), ('BELL-212', 'BELL-212'), ('SA226 TC', 'SA226 TC'), ('BELLANCA CIT', 'BELLANCA CIT'), ('HUGHES 300', 'HUGHES 300'), ('LEARJET UNKN', 'LEARJET UNKN'), ('T-6A', 'T-6A'), ('M-28', 'M-28'), ('BELL-427', 'BELL-427'), ('BE-95', 'BE-95'), ('AIRBUS 377SGT', 'AIRBUS 377SGT'), ('FXWG', 'FXWG'), ('PA-23 APACHE', 'PA-23 APACHE'), ('C-170', 'C-170'), ('EC155', 'EC155'), ('MOONEY-20B/C', 'MOONEY-20B/C'), ('HU-25', 'HU-25'), ('RKWL SABRE60', 'RKWL SABRE60'), ('B-747-1/200', 'B-747-1/200'), ('H-60', 'H-60'), ('Q-4', 'Q-4'), ('DHC7 DASH 7', 'DHC7 DASH 7'), ('RKWL AC-680', 'RKWL AC-680'), ('EUROCOPTER', 'EUROCOPTER'), ('C-27', 'C-27'), ('PA-31T CHEYENNE II', 'PA-31T CHEYENNE II'), ('PA-25 PAWNEE', 'PA-25 PAWNEE'), ('HAWKER 600', 'HAWKER 600'), ('RKWL CMDR114', 'RKWL CMDR114'), ('WACO F', 'WACO F'), ('AG-5B', 'AG-5B'), ('RKWL OV 10', 'RKWL OV 10'), ('C-401', 'C-401'), ('BA-146-200', 'BA-146-200'), ('C-145', 'C-145'), ('AERO AT-4', 'AERO AT-4'), ('GROB', 'GROB'), ('BELLANCA DEC', 'BELLANCA DEC'), ('ENSTROM F28A', 'ENSTROM F28A'), ('A-318', 'A-318'), ('RKWL SABRLNR', 'RKWL SABRLNR'), ('CRJ440', 'CRJ440'), ('BE-24R SIERRA', 'BE-24R SIERRA'), ('BE-50 TWIN BONANZA', 'BE-50 TWIN BONANZA'), ('DC-8-70', 'DC-8-70'), ('C-207 SKYWAG', 'C-207 SKYWAG'), ('B C-17 GLOBEMASTER', 'B C-17 GLOBEMASTER'), ('HUGHES 500', 'HUGHES 500'), ('DC-9-50', 'DC-9-50'), ('DORNIER 228', 'DORNIER 228'), ('C-26', 'C-26'), ('HUGHES 369', 'HUGHES 369'), ('C-400', 'C-400'), ('CHAMP 8KCAB', 'CHAMP 8KCAB'), ('C-195', 'C-195'), ('C-404', 'C-404'), ('AA-1', 'AA-1'), ('V-22', 'V-22'), ('RKWL SABRLNR40', 'RKWL SABRLNR40'), ('PIPERSPORT', 'PIPERSPORT'), ('CASA C-212', 'CASA C-212'), ('IAI-1123', 'IAI-1123'), ('MU-300', 'MU-300'), ('C-188', 'C-188'), ('CHAMPION CITABRIA', 'CHAMPION CITABRIA'), ('PA-42', 'PA-42'), ('B-747', 'B-747'), ('AT-400', 'AT-400'), ('DHC6', 'DHC6'), ('AVIAT HUSKY A-1', 'AVIAT HUSKY A-1'), ('DHC2 BEAVER', 'DHC2 BEAVER'), ('SIKORSKY S-64', 'SIKORSKY S-64'), ('PA-J3', 'PA-J3'), ('LEARJET-25', 'LEARJET-25'), ('IAI ASTRA JT', 'IAI ASTRA JT'), ('BE-60 DUKE', 'BE-60 DUKE'), ('BELL-222', 'BELL-222'), ('BA-125-700', 'BA-125-700'), ('MD-87', 'MD-87'), ('CLASSIC WACO WMF', 'CLASSIC WACO WMF'), ('GRUMMAN GA7', 'GRUMMAN GA7'), ('HONDAJET', 'HONDAJET'), ('AT-802', 'AT-802'), ('PA-60 600', 'PA-60 600'), ('RKWL THRUSH', 'RKWL THRUSH'), ('BA-41 JETSTR', 'BA-41 JETSTR'), ('LEARJET', 'LEARJET'), ('PA-22 TP/COLT', 'PA-22 TP/COLT'), ('AT-602', 'AT-602'), ('MOONEY-20F', 'MOONEY-20F'), ('SIKORSKY UH-60', 'SIKORSKY UH-60'), ('CITATION VII', 'CITATION VII'), ('BELL-214', 'BELL-214'), ('CONVAIR 640', 'CONVAIR 640'), ('C-177', 'C-177'), ('C-120/140', 'C-120/140'), ('HAWKER-SDLY HS125', 'HAWKER-SDLY HS125'), ('DC-9', 'DC-9'), ('B-737-100', 'B-737-100'), ('E-8', 'E-8'), ('PA-38 TOMAHAWK', 'PA-38 TOMAHAWK'), ('C-20', 'C-20'), ('E-6', 'E-6'), ('E-4', 'E-4'), ('BE-T34A', 'BE-T34A'), ('C-21', 'C-21'), ('MAULE M-7', 'MAULE M-7'), ('LANCAIR COLUMBIA', 'LANCAIR COLUMBIA'), ('DA-10 FALCON', 'DA-10 FALCON'), ('LOCKHEED P3', 'LOCKHEED P3'), ('C-180', 'C-180'), ('FORD TRIMOTOR', 'FORD TRIMOTOR'), ('C-162', 'C-162'), ('A-10', 'A-10'), ('ROBINSON R66', 'ROBINSON R66'), ('PARTENAVIA68', 'PARTENAVIA68'), ('BE-76  DUCHESS', 'BE-76  DUCHESS'), ('BE-19', 'BE-19'), ('C-500', 'C-500'), ('RKWL SHRIKE', 'RKWL SHRIKE'), ('MD-520', 'MD-520'), ('SHORTS 330', 'SHORTS 330'), ('SAAB 2000', 'SAAB 2000'), ('AEROS SA 330 PUMA', 'AEROS SA 330 PUMA'), ('C-32', 'C-32'), ('MOONEY M20', 'MOONEY M20'), ('LANCAIR LC 40/42', 'LANCAIR LC 40/42'), ('EMB PHENOM 100', 'EMB PHENOM 100'), ('HELICOPTER', 'HELICOPTER'), ('AMD ALARUS CH2000', 'AMD ALARUS CH2000'), ('HOMEBUILT', 'HOMEBUILT'), ('C-5', 'C-5'), ('PA-18 SUPER CUB', 'PA-18 SUPER CUB'), ('TAYLORCR-BC', 'TAYLORCR-BC'), ('SWEARINGIN', 'SWEARINGIN'), ('MU2', 'MU2'), ('MOONEY-20E', 'MOONEY-20E'), ('GENERAL AVIA F-22', 'GENERAL AVIA F-22'), ('C-185 SKYWAG', 'C-185 SKYWAG'), ('MISC - OTHER', 'MISC - OTHER'), ('HH-60G', 'HH-60G'), ('EMB-110', 'EMB-110'), ('BELL-429', 'BELL-429'), ('C-425', 'C-425'), ('C-441 CONQUE', 'C-441 CONQUE'), ('BE-100 KING', 'BE-100 KING'), ('C-340', 'C-340'), ('MD-500', 'MD-500'), ('UH-1N', 'UH-1N'), ('RKWLTRBO 690', 'RKWLTRBO 690'), ('BA-31 JETSTR', 'BA-31 JETSTR'), ('F-15', 'F-15'), ('PIAGGIO P180', 'PIAGGIO P180'), ('GRUMMAN', 'GRUMMAN'), ('B-757', 'B-757'), ('SUKHOI SJ 100/95', 'SUKHOI SJ 100/95'), ('MQ9 (UA)', 'MQ9 (UA)'), ('DA FALCON 7X', 'DA FALCON 7X'), ('EADS CASA HC 144', 'EADS CASA HC 144'), ('LEARJET-36', 'LEARJET-36'), ('EMB-120', 'EMB-120'), ('MOONEY-20K', 'MOONEY-20K'), ('PITTS', 'PITTS'), ('B-737-200', 'B-737-200'), ('C-146', 'C-146'), ('AGUSTA 109', 'AGUSTA 109'), ('PAC 750XL', 'PAC 750XL'), ('SOCATA TB-20', 'SOCATA TB-20'), ('SOCATA TBM700', 'SOCATA TBM700'), ('SHORTS 360', 'SHORTS 360'), ('SA227 AC METRO III', 'SA227 AC METRO III'), ('HH-65', 'HH-65'), ('DA-50 FALCON', 'DA-50 FALCON'), ('T-38A', 'T-38A'), ('B-52', 'B-52'), ('C-320', 'C-320'), ('CESSNA LC-41', 'CESSNA LC-41'), ('MILITARY', 'MILITARY'), ('MERLIN III', 'MERLIN III'), ('BN-2A ISLAND', 'BN-2A ISLAND'), ('DIAMOND 20', 'DIAMOND 20'), ('MOONEY-20J', 'MOONEY-20J'), ('SA227 DC METRO 23', 'SA227 DC METRO 23'), ('CANADAIR', 'CANADAIR'), ('BELL-412', 'BELL-412'), ('F-15E', 'F-15E'), ('RAYTHEON 390', 'RAYTHEON 390'), ('IAI-1124', 'IAI-1124'), ('LEARJET-55', 'LEARJET-55'), ('BE-PREMIER I', 'BE-PREMIER I'), ('B-767-400', 'B-767-400'), ('C-414', 'C-414'), ('BELLANCA CMP', 'BELLANCA CMP'), ('ULTRA LIGHT', 'ULTRA LIGHT'), ('BRITISH AEROSPACE', 'BRITISH AEROSPACE'), ('AGUSTA A 119', 'AGUSTA A 119'), ('GULFSTREAM II', 'GULFSTREAM II'), ('ROCKWELL', 'ROCKWELL'), ('NORTH AMERICAN', 'NORTH AMERICAN'), ('T-38', 'T-38'), ('DA-900', 'DA-900'), ('SABRLNR-65', 'SABRLNR-65'), ('BOEING', 'BOEING'), ('BE-33', 'BE-33'), ('PA-31 NAVAJO', 'PA-31 NAVAJO'), ('T-6', 'T-6'), ('GULFAERO III', 'GULFAERO III'), ('ECLIPSE 500', 'ECLIPSE 500'), ('DORNIER 328J', 'DORNIER 328J'), ('CITATION EXL', 'CITATION EXL'), ('KC-10', 'KC-10'), ('IAI GALAXY', 'IAI GALAXY'), ('BE-35', 'BE-35'), ('C-37', 'C-37'), ('ROBINSON R22', 'ROBINSON R22'), ('PA-31T CHEYENNE', 'PA-31T CHEYENNE'), ('GRUMAMER AA5', 'GRUMAMER AA5'), ('DC-9-10', 'DC-9-10'), ('EC120', 'EC120'), ('C-40', 'C-40'), ('PA-34 SENECA', 'PA-34 SENECA'), ('C-12', 'C-12'), ('T-1', 'T-1'), ('SIKORSKY S-76', 'SIKORSKY S-76'), ('B-737-600', 'B-737-600'), ('C-210 CENTUR', 'C-210 CENTUR'), ('C-310', 'C-310'), ('C-152', 'C-152'), ('C-650', 'C-650'), ('DIAMOND 40', 'DIAMOND 40'), ('EUROCOPTER BK 117', 'EUROCOPTER BK 117'), ('C-206 STATIO', 'C-206 STATIO'), ('STINSON 108', 'STINSON 108'), ('PA-46 MALIBU', 'PA-46 MALIBU'), ('F-16', 'F-16'), ('LOCKHEED C-130', 'LOCKHEED C-130'), ('LEARJET-31', 'LEARJET-31'), ('GULFSTREAM GV1', 'GULFSTREAM GV1'), ('C-130J', 'C-130J'), ('C-337', 'C-337'), ('B-767', 'B-767'), ('PITTS S-2', 'PITTS S-2'), ('B-747-8 SERIES', 'B-747-8 SERIES'), ('C-17', 'C-17'), ('PA-23-250', 'PA-23-250'), ('BE-90  KING', 'BE-90  KING'), ('BE-1900', 'BE-1900'), ('EMBRAER', 'EMBRAER'), ('HC-130', 'HC-130'), ('BA-125-800', 'BA-125-800'), ('C-421', 'C-421'), ('PIPER', 'PIPER'), ('SABRLNR-80A', 'SABRLNR-80A'), ('CITATION X', 'CITATION X'), ('GULFSTREAM', 'GULFSTREAM'), ('GULFSTREAM G 280', 'GULFSTREAM G 280'), ('CITATION', 'CITATION'), ('C-135', 'C-135'), ('HAWKER 1000', 'HAWKER 1000'), ('EMB PHENOM 300', 'EMB PHENOM 300'), ('CITATION II', 'CITATION II'), ('DASSAULT', 'DASSAULT'), ('B-787-8', 'B-787-8'), ('DC-9-30', 'DC-9-30'), ('EXTRA 300', 'EXTRA 300'), ('GLOBAL EXPRS', 'GLOBAL EXPRS'), ('CESSNA', 'CESSNA'), ('ATR-72', 'ATR-72'), ('HAWKER 800', 'HAWKER 800'), ('DORNIER 328', 'DORNIER 328'), ('C-130', 'C-130'), ('BE-300 KING', 'BE-300 KING'), ('AGUSTA AW 139', 'AGUSTA AW 139'), ('U-28', 'U-28'), ('PA-24 COMANCHE', 'PA-24 COMANCHE'), ('LOCKHEED P3B', 'LOCKHEED P3B'), ('DC-10', 'DC-10'), ('AEROS SA365', 'AEROS SA365'), ('SIKORSKY S-92', 'SIKORSKY S-92'), ('HAWKER 900', 'HAWKER 900'), ('C-150', 'C-150'), ('PA-32', 'PA-32'), ('BELL-407', 'BELL-407'), ('BE-58  BARON', 'BE-58  BARON'), ('A-330', 'A-330'), ('ROBINSON R44', 'ROBINSON R44'), ('A-380', 'A-380'), ('BEECHCRAFT', 'BEECHCRAFT'), ('DA-200 FALCON', 'DA-200 FALCON'), ('DA-20 FALCON', 'DA-20 FALCON'), ('DIAMOND 42', 'DIAMOND 42'), ('T-38N', 'T-38N'), ('LEARJET-60', 'LEARJET-60'), ('BE-99', 'BE-99'), ('LEARJET-35', 'LEARJET-35'), ('GULFSTREAM V', 'GULFSTREAM V'), ('B-777-300', 'B-777-300'), ('PILATUS PC12', 'PILATUS PC12'), ('DC-3', 'DC-3'), ('LIGHT-SPORT', 'LIGHT-SPORT'), ('CL-601/604', 'CL-601/604'), ('GULFAERO IV', 'GULFAERO IV'), ('CHAMPION 7GC', 'CHAMPION 7GC'), ('B-727-200', 'B-727-200'), ('PA-31-350', 'PA-31-350'), ('A-340', 'A-340'), ('PA-44 SEMINOLE', 'PA-44 SEMINOLE'), ('HAWKER 4000', 'HAWKER 4000'), ('B-747-400', 'B-747-400'), ('C-560', 'C-560'), ('C-680', 'C-680'), ('MD-80', 'MD-80'), ('C-208', 'C-208'), ('GULFSTREAM 200', 'GULFSTREAM 200'), ('CL-600', 'CL-600'), ('CITATION MUSTANG 510', 'CITATION MUSTANG 510'), ('MD-88', 'MD-88'), ('C-182 SKYLAN', 'C-182 SKYLAN'), ('BE-55  BARON', 'BE-55  BARON'), ('EMB-190', 'EMB-190'), ('MD-90-30', 'MD-90-30'), ('LEARJET-45', 'LEARJET-45'), ('GULFSTREAM G150', 'GULFSTREAM G150'), ('BELL-430', 'BELL-430'), ('EMB-500', 'EMB-500'), ('B-777-200', 'B-777-200'), ('C-402', 'C-402'), ('CHALLENGER 300', 'CHALLENGER 300'), ('PA-28', 'PA-28'), ('SAAB-340', 'SAAB-340'), ('HUGHES 269A', 'HUGHES 269A'), ('BE-65 QUEEN', 'BE-65 QUEEN'), ('DA-2000', 'DA-2000'), ('B-767-300', 'B-767-300'), ('B-737-400', 'B-737-400'), ('C-550', 'C-550'), ('BE-200 KING', 'BE-200 KING'), ('EC135', 'EC135'), ('B-737-300', 'B-737-300'), ('CRJ700', 'CRJ700'), ('CIRRUS SR 20/22', 'CIRRUS SR 20/22'), ('BE-36', 'BE-36'), ('B-757-300', 'B-757-300'), ('B-787-9', 'B-787-9'), ('C-172', 'C-172'), ('B-737-900', 'B-737-900'), ('B-767-200', 'B-767-200'), ('MD-82', 'MD-82'), ('CASA CN-235', 'CASA CN-235'), ('A-321', 'A-321'), ('B-737-500', 'B-737-500'), ('BELL-206', 'BELL-206'), ('EMB-170', 'EMB-170'), ('EXPERIMENTAL', 'EXPERIMENTAL'), ('ATR-42', 'ATR-42'), ('AEROS 350', 'AEROS 350'), ('B-737', 'B-737'), ('BE-400 BJET', 'BE-400 BJET'), ('MD-11', 'MD-11'), ('DC-10-30', 'DC-10-30'), ('B-717-200', 'B-717-200'), ('A-319', 'A-319'), ('A-320', 'A-320'), ('B-737-800', 'B-737-800'), ('UNKNOWN', 'UNKNOWN'), ('B-757-200', 'B-757-200'), ('CRJ900', 'CRJ900'), ('B-777', 'B-777'), ('A-310', 'A-310'), ('A-300', 'A-300'), ('MD-83', 'MD-83'), ('EC130', 'EC130'), ('EMB-145', 'EMB-145'), ('EMB-135', 'EMB-135'), ('DC-10-10', 'DC-10-10'), ('B-737-700', 'B-737-700'), ('CITATIONJET', 'CITATIONJET'), ('DHC8 DASH 8', 'DHC8 DASH 8'), ('CRJ100/200', 'CRJ100/200')], validators = [DataRequired()])
    name2 = SelectField('Aircraft2? ', choices=[('A-7K', 'A-7K'), ('VC-9C', 'VC-9C'), ('F-4D', 'F-4D'), ('CURTIS C-46', 'CURTIS C-46'), ('C-130A', 'C-130A'), ('WC-130E', 'WC-130E'), ('BE-17', 'BE-17'), ('AC-130H', 'AC-130H'), ('C-137C', 'C-137C'), ('WACO', 'WACO'), ('C-130B', 'C-130B'), ('BRISTOL FRTR', 'BRISTOL FRTR'), ('FAIRCHILD FH227', 'FAIRCHILD FH227'), ('C-130Y', 'C-130Y'), ('A-7', 'A-7'), ('A-7D', 'A-7D'), ('BAC 1-11', 'BAC 1-11'), ('SAAB', 'SAAB'), ('F-111D', 'F-111D'), ('C-18B', 'C-18B'), ('KC-130', 'KC-130'), ('NORD 262', 'NORD 262'), ('RF-4C', 'RF-4C'), ('RKWL LARK', 'RKWL LARK'), ('OV-10A', 'OV-10A'), ('B-52G', 'B-52G'), ('SIKORSKY', 'SIKORSKY'), ('VC-137C', 'VC-137C'), ('AC-130', 'AC-130'), ('SUKHOI SU-29', 'SUKHOI SU-29'), ('FOKKER F28', 'FOKKER F28'), ('RKWL DARTER', 'RKWL DARTER'), ('B-STEARMAN', 'B-STEARMAN'), ('C-135C', 'C-135C'), ('F-4', 'F-4'), ('HAWKER-SDLY HS748', 'HAWKER-SDLY HS748'), ('TG-7A', 'TG-7A'), ('BE-UNKNOWN', 'BE-UNKNOWN'), ('F-4G', 'F-4G'), ('MAULE M-6', 'MAULE M-6'), ('PA-36-375', 'PA-36-375'), ('WC-130', 'WC-130'), ('T-3A', 'T-3A'), ('EC135E', 'EC135E'), ('CONVAIR 600', 'CONVAIR 600'), ('TC-18E', 'TC-18E'), ('LOCKHEED 188', 'LOCKHEED 188'), ('NAMC YS-11A', 'NAMC YS-11A'), ('C-130G', 'C-130G'), ('C-141', 'C-141'), ('LEARJET-23', 'LEARJET-23'), ('C-18', 'C-18'), ('C-20D', 'C-20D'), ('WC-135B', 'WC-135B'), ('WC-135', 'WC-135'), ('E-6A', 'E-6A'), ('FAIRCHILD 24', 'FAIRCHILD 24'), ('BELLANCA 260', 'BELLANCA 260'), ('VC-135E', 'VC-135E'), ('C-137', 'C-137'), ('MH-53J', 'MH-53J'), ('F/A-18', 'F/A-18'), ('C-23', 'C-23'), ('C-9', 'C-9'), ('T-41C', 'T-41C'), ('EC135H', 'EC135H'), ('CH-1N', 'CH-1N'), ('EC135C', 'EC135C'), ('AT-38A', 'AT-38A'), ('G-2', 'G-2'), ('P-3', 'P-3'), ('KC-135', 'KC-135'), ('DA-100 FALCON', 'DA-100 FALCON'), ('C-9B', 'C-9B'), ('C-22B', 'C-22B'), ('C-135B', 'C-135B'), ('CT-114', 'CT-114'), ('RC-135S', 'RC-135S'), ('BA-ATP', 'BA-ATP'), ('CONCORDE', 'CONCORDE'), ('AN-124', 'AN-124'), ('VOLPARE BE18', 'VOLPARE BE18'), ('BELL 47', 'BELL 47'), ('AT-502', 'AT-502'), ('RC-135U', 'RC-135U'), ('P-3C', 'P-3C'), ('SHORTS SC7', 'SHORTS SC7'), ('OA-10A', 'OA-10A'), ('LOCKHEED', 'LOCKHEED'), ('EC-18B', 'EC-18B'), ('T-41D', 'T-41D'), ('T-44A', 'T-44A'), ('F/A-18B', 'F/A-18B'), ('C-135A', 'C-135A'), ('C-12C', 'C-12C'), ('AC-130U', 'AC-130U'), ('C-141B', 'C-141B'), ('MERLIN', 'MERLIN'), ('BE-2000', 'BE-2000'), ('TH-53A', 'TH-53A'), ('WC-130H', 'WC-130H'), ('ROBIN R2000 SERIES', 'ROBIN R2000 SERIES'), ('UV-18B', 'UV-18B'), ('VC-137', 'VC-137'), ('BOEING UNKN', 'BOEING UNKN'), ('FOKKER F28 MK 1000', 'FOKKER F28 MK 1000'), ('FAIRCH SA227', 'FAIRCH SA227'), ('FOKKER F28 MK 4000', 'FOKKER F28 MK 4000'), ('HH-60J', 'HH-60J'), ('LOCKHEED 1329', 'LOCKHEED 1329'), ('BA-146-300', 'BA-146-300'), ('BE-77  SKIPPER', 'BE-77  SKIPPER'), ('L-1011-500', 'L-1011-500'), ('C-20A', 'C-20A'), ('C-20H', 'C-20H'), ('HELIO COURIER H295', 'HELIO COURIER H295'), ('DC-10-40', 'DC-10-40'), ('AYRES THRUSH', 'AYRES THRUSH'), ('LOCKHEED JETST', 'LOCKHEED JETST'), ('C-9A', 'C-9A'), ('CITATION VI', 'CITATION VI'), ('MOONEY UNKN', 'MOONEY UNKN'), ('FAIRCHILD F27', 'FAIRCHILD F27'), ('CV-580', 'CV-580'), ('STEARMAN', 'STEARMAN'), ('DORNIER', 'DORNIER'), ('REPUBLIC RC3', 'REPUBLIC RC3'), ('L-1011', 'L-1011'), ('AEROS SA341', 'AEROS SA341'), ('AEROS SN601', 'AEROS SN601'), ('DC-8-62', 'DC-8-62'), ('FOKKER F100', 'FOKKER F100'), ('C-12D', 'C-12D'), ('BE-80 QUEEN', 'BE-80 QUEEN'), ('BA-146-100', 'BA-146-100'), ('C-141C', 'C-141C'), ('C-38A', 'C-38A'), ('C-5C', 'C-5C'), ('GRUMMAN G73', 'GRUMMAN G73'), ('EC135L', 'EC135L'), ('MC-130E', 'MC-130E'), ('C-406 CARAVA', 'C-406 CARAVA'), ('C-9C', 'C-9C'), ('T-6B', 'T-6B'), ('AT-38B', 'AT-38B'), ('BA-146', 'BA-146'), ('BELL EH-1H', 'BELL EH-1H'), ('C-20B', 'C-20B'), ('C-12J', 'C-12J'), ('EC130E', 'EC130E'), ('CL-215', 'CL-215'), ('C-40C', 'C-40C'), ('MD-600N', 'MD-600N'), ('E-3B', 'E-3B'), ('LEARJET-24', 'LEARJET-24'), ('WC-135W', 'WC-135W'), ('HC-130N', 'HC-130N'), ('TC-135S', 'TC-135S'), ('E-8C', 'E-8C'), ('HAWKER', 'HAWKER'), ('UH-1H', 'UH-1H'), ('F-15D', 'F-15D'), ('C-40B', 'C-40B'), ('OC-135B', 'OC-135B'), ('C-32A', 'C-32A'), ('F-16A', 'F-16A'), ('F-16B', 'F-16B'), ('EC130H', 'EC130H'), ('BA-RJ85', 'BA-RJ85'), ('T-43A', 'T-43A'), ('DC-8-63', 'DC-8-63'), ('E-4B', 'E-4B'), ('C-26B', 'C-26B'), ('KC-135T', 'KC-135T'), ('RC-135W', 'RC-135W'), ('LAKE LA4-200', 'LAKE LA4-200'), ('C-37A', 'C-37A'), ('C-135E', 'C-135E'), ('MC-130H', 'MC-130H'), ('C-32B', 'C-32B'), ('F-117A', 'F-117A'), ('B-1B', 'B-1B'), ('F-15B', 'F-15B'), ('A-10A', 'A-10A'), ('AEROS SA315', 'AEROS SA315'), ('FOKKER F27', 'FOKKER F27'), ('F-15A', 'F-15A'), ('HC-130P', 'HC-130P'), ('KC-10A', 'KC-10A'), ('C-5A', 'C-5A'), ('E-3C', 'E-3C'), ('U-2S', 'U-2S'), ('LC-130H', 'LC-130H'), ('C-5B', 'C-5B'), ('F-15C', 'F-15C'), ('WC-130J', 'WC-130J'), ('MC-130P', 'MC-130P'), ('C-21A', 'C-21A'), ('RC-135V', 'RC-135V'), ('T-38C', 'T-38C'), ('B-52H', 'B-52H'), ('EC130J', 'EC130J'), ('TC-135W', 'TC-135W'), ('B-727', 'B-727'), ('AERONCA 7', 'AERONCA 7'), ('C-130E', 'C-130E'), ('KC-135E', 'KC-135E'), ('T-1A', 'T-1A'), ('WC-135C', 'WC-135C'), ('T-37B', 'T-37B'), ('F-16C', 'F-16C'), ('C-130H', 'C-130H'), ('C-17A', 'C-17A'), ('SIKORSKY S-61L', 'SIKORSKY S-61L'), ('KC-135R', 'KC-135R'), ('BELL HH-IH', 'BELL HH-IH'), ('AEROSTAR 600', 'AEROSTAR 600'), ('E-3', 'E-3'), ('FOKKER 70', 'FOKKER 70'), ('ALON A2', 'ALON A2'), ('AVIAT PITTS S1', 'AVIAT PITTS S1'), ('ERCO 415', 'ERCO 415'), ('GLOBE GC1', 'GLOBE GC1'), ('LOCKHEED 382', 'LOCKHEED 382'), ('AIRBUS', 'AIRBUS'), ('DC-8-61', 'DC-8-61'), ('CAP AVION MUDRY', 'CAP AVION MUDRY'), ('SOCATA TB9', 'SOCATA TB9'), ('CONVAIR 340', 'CONVAIR 340'), ('URBAN AIR LAMBADA', 'URBAN AIR LAMBADA'), ('G-164 AG CAT', 'G-164 AG CAT'), ('HELIO COURIER 800', 'HELIO COURIER 800'), ('C-305', 'C-305'), ('MD-902', 'MD-902'), ('BELL 230', 'BELL 230'), ('ZODIAC CH601', 'ZODIAC CH601'), ('GRUMAMER AA1', 'GRUMAMER AA1'), ('AGUST WESTLAND EH101', 'AGUST WESTLAND EH101'), ('F-16D', 'F-16D'), ('LUSCOMBE 8', 'LUSCOMBE 8'), ('C-U206F', 'C-U206F'), ('BELL-205A1', 'BELL-205A1'), ('BE-23 SUNDOWNER', 'BE-23 SUNDOWNER'), ('GIPPSLAND GA-8', 'GIPPSLAND GA-8'), ('MD-900', 'MD-900'), ('AT-301', 'AT-301'), ('C-175', 'C-175'), ('MERLIN IV', 'MERLIN IV'), ('B-747-300', 'B-747-300'), ('PA-12', 'PA-12'), ('DC-9-40', 'DC-9-40'), ('B-707', 'B-707'), ('RKWL CMDR112', 'RKWL CMDR112'), ('DC-8', 'DC-8'), ('RYAN NAVION', 'RYAN NAVION'), ('CRJ705', 'CRJ705'), ('SOCATA TB-10', 'SOCATA TB-10'), ('BELLANCA', 'BELLANCA'), ('BE-23 MUSKETEER', 'BE-23 MUSKETEER'), ('MBB-105', 'MBB-105'), ('LOCKHEED P3A', 'LOCKHEED P3A'), ('BELLANCA 1730', 'BELLANCA 1730'), ('C-303', 'C-303'), ('PA-30 TWIN COMANCHE', 'PA-30 TWIN COMANCHE'), ('FLIGHT DESIGN CTSW', 'FLIGHT DESIGN CTSW'), ('FAIRCHILD SA227', 'FAIRCHILD SA227'), ('G-159', 'G-159'), ('AEROS SA360', 'AEROS SA360'), ('B-727-100', 'B-727-100'), ('GRUMMAN S-2 TRACKER', 'GRUMMAN S-2 TRACKER'), ('SIKORSKY S-65C', 'SIKORSKY S-65C'), ('AA-5', 'AA-5'), ('DHC3-OTTER', 'DHC3-OTTER'), ('BE-18', 'BE-18'), ('LIBERTY XL-2', 'LIBERTY XL-2'), ('AEROS 355', 'AEROS 355'), ('DC-6', 'DC-6'), ('PA-60 601', 'PA-60 601'), ('BELL-212', 'BELL-212'), ('SA226 TC', 'SA226 TC'), ('BELLANCA CIT', 'BELLANCA CIT'), ('HUGHES 300', 'HUGHES 300'), ('LEARJET UNKN', 'LEARJET UNKN'), ('T-6A', 'T-6A'), ('M-28', 'M-28'), ('BELL-427', 'BELL-427'), ('BE-95', 'BE-95'), ('AIRBUS 377SGT', 'AIRBUS 377SGT'), ('FXWG', 'FXWG'), ('PA-23 APACHE', 'PA-23 APACHE'), ('C-170', 'C-170'), ('EC155', 'EC155'), ('MOONEY-20B/C', 'MOONEY-20B/C'), ('HU-25', 'HU-25'), ('RKWL SABRE60', 'RKWL SABRE60'), ('B-747-1/200', 'B-747-1/200'), ('H-60', 'H-60'), ('Q-4', 'Q-4'), ('DHC7 DASH 7', 'DHC7 DASH 7'), ('RKWL AC-680', 'RKWL AC-680'), ('EUROCOPTER', 'EUROCOPTER'), ('C-27', 'C-27'), ('PA-31T CHEYENNE II', 'PA-31T CHEYENNE II'), ('PA-25 PAWNEE', 'PA-25 PAWNEE'), ('HAWKER 600', 'HAWKER 600'), ('RKWL CMDR114', 'RKWL CMDR114'), ('WACO F', 'WACO F'), ('AG-5B', 'AG-5B'), ('RKWL OV 10', 'RKWL OV 10'), ('C-401', 'C-401'), ('BA-146-200', 'BA-146-200'), ('C-145', 'C-145'), ('AERO AT-4', 'AERO AT-4'), ('GROB', 'GROB'), ('BELLANCA DEC', 'BELLANCA DEC'), ('ENSTROM F28A', 'ENSTROM F28A'), ('A-318', 'A-318'), ('RKWL SABRLNR', 'RKWL SABRLNR'), ('CRJ440', 'CRJ440'), ('BE-24R SIERRA', 'BE-24R SIERRA'), ('BE-50 TWIN BONANZA', 'BE-50 TWIN BONANZA'), ('DC-8-70', 'DC-8-70'), ('C-207 SKYWAG', 'C-207 SKYWAG'), ('B C-17 GLOBEMASTER', 'B C-17 GLOBEMASTER'), ('HUGHES 500', 'HUGHES 500'), ('DC-9-50', 'DC-9-50'), ('DORNIER 228', 'DORNIER 228'), ('C-26', 'C-26'), ('HUGHES 369', 'HUGHES 369'), ('C-400', 'C-400'), ('CHAMP 8KCAB', 'CHAMP 8KCAB'), ('C-195', 'C-195'), ('C-404', 'C-404'), ('AA-1', 'AA-1'), ('V-22', 'V-22'), ('RKWL SABRLNR40', 'RKWL SABRLNR40'), ('PIPERSPORT', 'PIPERSPORT'), ('CASA C-212', 'CASA C-212'), ('IAI-1123', 'IAI-1123'), ('MU-300', 'MU-300'), ('C-188', 'C-188'), ('CHAMPION CITABRIA', 'CHAMPION CITABRIA'), ('PA-42', 'PA-42'), ('B-747', 'B-747'), ('AT-400', 'AT-400'), ('DHC6', 'DHC6'), ('AVIAT HUSKY A-1', 'AVIAT HUSKY A-1'), ('DHC2 BEAVER', 'DHC2 BEAVER'), ('SIKORSKY S-64', 'SIKORSKY S-64'), ('PA-J3', 'PA-J3'), ('LEARJET-25', 'LEARJET-25'), ('IAI ASTRA JT', 'IAI ASTRA JT'), ('BE-60 DUKE', 'BE-60 DUKE'), ('BELL-222', 'BELL-222'), ('BA-125-700', 'BA-125-700'), ('MD-87', 'MD-87'), ('CLASSIC WACO WMF', 'CLASSIC WACO WMF'), ('GRUMMAN GA7', 'GRUMMAN GA7'), ('HONDAJET', 'HONDAJET'), ('AT-802', 'AT-802'), ('PA-60 600', 'PA-60 600'), ('RKWL THRUSH', 'RKWL THRUSH'), ('BA-41 JETSTR', 'BA-41 JETSTR'), ('LEARJET', 'LEARJET'), ('PA-22 TP/COLT', 'PA-22 TP/COLT'), ('AT-602', 'AT-602'), ('MOONEY-20F', 'MOONEY-20F'), ('SIKORSKY UH-60', 'SIKORSKY UH-60'), ('CITATION VII', 'CITATION VII'), ('BELL-214', 'BELL-214'), ('CONVAIR 640', 'CONVAIR 640'), ('C-177', 'C-177'), ('C-120/140', 'C-120/140'), ('HAWKER-SDLY HS125', 'HAWKER-SDLY HS125'), ('DC-9', 'DC-9'), ('B-737-100', 'B-737-100'), ('E-8', 'E-8'), ('PA-38 TOMAHAWK', 'PA-38 TOMAHAWK'), ('C-20', 'C-20'), ('E-6', 'E-6'), ('E-4', 'E-4'), ('BE-T34A', 'BE-T34A'), ('C-21', 'C-21'), ('MAULE M-7', 'MAULE M-7'), ('LANCAIR COLUMBIA', 'LANCAIR COLUMBIA'), ('DA-10 FALCON', 'DA-10 FALCON'), ('LOCKHEED P3', 'LOCKHEED P3'), ('C-180', 'C-180'), ('FORD TRIMOTOR', 'FORD TRIMOTOR'), ('C-162', 'C-162'), ('A-10', 'A-10'), ('ROBINSON R66', 'ROBINSON R66'), ('PARTENAVIA68', 'PARTENAVIA68'), ('BE-76  DUCHESS', 'BE-76  DUCHESS'), ('BE-19', 'BE-19'), ('C-500', 'C-500'), ('RKWL SHRIKE', 'RKWL SHRIKE'), ('MD-520', 'MD-520'), ('SHORTS 330', 'SHORTS 330'), ('SAAB 2000', 'SAAB 2000'), ('AEROS SA 330 PUMA', 'AEROS SA 330 PUMA'), ('C-32', 'C-32'), ('MOONEY M20', 'MOONEY M20'), ('LANCAIR LC 40/42', 'LANCAIR LC 40/42'), ('EMB PHENOM 100', 'EMB PHENOM 100'), ('HELICOPTER', 'HELICOPTER'), ('AMD ALARUS CH2000', 'AMD ALARUS CH2000'), ('HOMEBUILT', 'HOMEBUILT'), ('C-5', 'C-5'), ('PA-18 SUPER CUB', 'PA-18 SUPER CUB'), ('TAYLORCR-BC', 'TAYLORCR-BC'), ('SWEARINGIN', 'SWEARINGIN'), ('MU2', 'MU2'), ('MOONEY-20E', 'MOONEY-20E'), ('GENERAL AVIA F-22', 'GENERAL AVIA F-22'), ('C-185 SKYWAG', 'C-185 SKYWAG'), ('MISC - OTHER', 'MISC - OTHER'), ('HH-60G', 'HH-60G'), ('EMB-110', 'EMB-110'), ('BELL-429', 'BELL-429'), ('C-425', 'C-425'), ('C-441 CONQUE', 'C-441 CONQUE'), ('BE-100 KING', 'BE-100 KING'), ('C-340', 'C-340'), ('MD-500', 'MD-500'), ('UH-1N', 'UH-1N'), ('RKWLTRBO 690', 'RKWLTRBO 690'), ('BA-31 JETSTR', 'BA-31 JETSTR'), ('F-15', 'F-15'), ('PIAGGIO P180', 'PIAGGIO P180'), ('GRUMMAN', 'GRUMMAN'), ('B-757', 'B-757'), ('SUKHOI SJ 100/95', 'SUKHOI SJ 100/95'), ('MQ9 (UA)', 'MQ9 (UA)'), ('DA FALCON 7X', 'DA FALCON 7X'), ('EADS CASA HC 144', 'EADS CASA HC 144'), ('LEARJET-36', 'LEARJET-36'), ('EMB-120', 'EMB-120'), ('MOONEY-20K', 'MOONEY-20K'), ('PITTS', 'PITTS'), ('B-737-200', 'B-737-200'), ('C-146', 'C-146'), ('AGUSTA 109', 'AGUSTA 109'), ('PAC 750XL', 'PAC 750XL'), ('SOCATA TB-20', 'SOCATA TB-20'), ('SOCATA TBM700', 'SOCATA TBM700'), ('SHORTS 360', 'SHORTS 360'), ('SA227 AC METRO III', 'SA227 AC METRO III'), ('HH-65', 'HH-65'), ('DA-50 FALCON', 'DA-50 FALCON'), ('T-38A', 'T-38A'), ('B-52', 'B-52'), ('C-320', 'C-320'), ('CESSNA LC-41', 'CESSNA LC-41'), ('MILITARY', 'MILITARY'), ('MERLIN III', 'MERLIN III'), ('BN-2A ISLAND', 'BN-2A ISLAND'), ('DIAMOND 20', 'DIAMOND 20'), ('MOONEY-20J', 'MOONEY-20J'), ('SA227 DC METRO 23', 'SA227 DC METRO 23'), ('CANADAIR', 'CANADAIR'), ('BELL-412', 'BELL-412'), ('F-15E', 'F-15E'), ('RAYTHEON 390', 'RAYTHEON 390'), ('IAI-1124', 'IAI-1124'), ('LEARJET-55', 'LEARJET-55'), ('BE-PREMIER I', 'BE-PREMIER I'), ('B-767-400', 'B-767-400'), ('C-414', 'C-414'), ('BELLANCA CMP', 'BELLANCA CMP'), ('ULTRA LIGHT', 'ULTRA LIGHT'), ('BRITISH AEROSPACE', 'BRITISH AEROSPACE'), ('AGUSTA A 119', 'AGUSTA A 119'), ('GULFSTREAM II', 'GULFSTREAM II'), ('ROCKWELL', 'ROCKWELL'), ('NORTH AMERICAN', 'NORTH AMERICAN'), ('T-38', 'T-38'), ('DA-900', 'DA-900'), ('SABRLNR-65', 'SABRLNR-65'), ('BOEING', 'BOEING'), ('BE-33', 'BE-33'), ('PA-31 NAVAJO', 'PA-31 NAVAJO'), ('T-6', 'T-6'), ('GULFAERO III', 'GULFAERO III'), ('ECLIPSE 500', 'ECLIPSE 500'), ('DORNIER 328J', 'DORNIER 328J'), ('CITATION EXL', 'CITATION EXL'), ('KC-10', 'KC-10'), ('IAI GALAXY', 'IAI GALAXY'), ('BE-35', 'BE-35'), ('C-37', 'C-37'), ('ROBINSON R22', 'ROBINSON R22'), ('PA-31T CHEYENNE', 'PA-31T CHEYENNE'), ('GRUMAMER AA5', 'GRUMAMER AA5'), ('DC-9-10', 'DC-9-10'), ('EC120', 'EC120'), ('C-40', 'C-40'), ('PA-34 SENECA', 'PA-34 SENECA'), ('C-12', 'C-12'), ('T-1', 'T-1'), ('SIKORSKY S-76', 'SIKORSKY S-76'), ('B-737-600', 'B-737-600'), ('C-210 CENTUR', 'C-210 CENTUR'), ('C-310', 'C-310'), ('C-152', 'C-152'), ('C-650', 'C-650'), ('DIAMOND 40', 'DIAMOND 40'), ('EUROCOPTER BK 117', 'EUROCOPTER BK 117'), ('C-206 STATIO', 'C-206 STATIO'), ('STINSON 108', 'STINSON 108'), ('PA-46 MALIBU', 'PA-46 MALIBU'), ('F-16', 'F-16'), ('LOCKHEED C-130', 'LOCKHEED C-130'), ('LEARJET-31', 'LEARJET-31'), ('GULFSTREAM GV1', 'GULFSTREAM GV1'), ('C-130J', 'C-130J'), ('C-337', 'C-337'), ('B-767', 'B-767'), ('PITTS S-2', 'PITTS S-2'), ('B-747-8 SERIES', 'B-747-8 SERIES'), ('C-17', 'C-17'), ('PA-23-250', 'PA-23-250'), ('BE-90  KING', 'BE-90  KING'), ('BE-1900', 'BE-1900'), ('EMBRAER', 'EMBRAER'), ('HC-130', 'HC-130'), ('BA-125-800', 'BA-125-800'), ('C-421', 'C-421'), ('PIPER', 'PIPER'), ('SABRLNR-80A', 'SABRLNR-80A'), ('CITATION X', 'CITATION X'), ('GULFSTREAM', 'GULFSTREAM'), ('GULFSTREAM G 280', 'GULFSTREAM G 280'), ('CITATION', 'CITATION'), ('C-135', 'C-135'), ('HAWKER 1000', 'HAWKER 1000'), ('EMB PHENOM 300', 'EMB PHENOM 300'), ('CITATION II', 'CITATION II'), ('DASSAULT', 'DASSAULT'), ('B-787-8', 'B-787-8'), ('DC-9-30', 'DC-9-30'), ('EXTRA 300', 'EXTRA 300'), ('GLOBAL EXPRS', 'GLOBAL EXPRS'), ('CESSNA', 'CESSNA'), ('ATR-72', 'ATR-72'), ('HAWKER 800', 'HAWKER 800'), ('DORNIER 328', 'DORNIER 328'), ('C-130', 'C-130'), ('BE-300 KING', 'BE-300 KING'), ('AGUSTA AW 139', 'AGUSTA AW 139'), ('U-28', 'U-28'), ('PA-24 COMANCHE', 'PA-24 COMANCHE'), ('LOCKHEED P3B', 'LOCKHEED P3B'), ('DC-10', 'DC-10'), ('AEROS SA365', 'AEROS SA365'), ('SIKORSKY S-92', 'SIKORSKY S-92'), ('HAWKER 900', 'HAWKER 900'), ('C-150', 'C-150'), ('PA-32', 'PA-32'), ('BELL-407', 'BELL-407'), ('BE-58  BARON', 'BE-58  BARON'), ('A-330', 'A-330'), ('ROBINSON R44', 'ROBINSON R44'), ('A-380', 'A-380'), ('BEECHCRAFT', 'BEECHCRAFT'), ('DA-200 FALCON', 'DA-200 FALCON'), ('DA-20 FALCON', 'DA-20 FALCON'), ('DIAMOND 42', 'DIAMOND 42'), ('T-38N', 'T-38N'), ('LEARJET-60', 'LEARJET-60'), ('BE-99', 'BE-99'), ('LEARJET-35', 'LEARJET-35'), ('GULFSTREAM V', 'GULFSTREAM V'), ('B-777-300', 'B-777-300'), ('PILATUS PC12', 'PILATUS PC12'), ('DC-3', 'DC-3'), ('LIGHT-SPORT', 'LIGHT-SPORT'), ('CL-601/604', 'CL-601/604'), ('GULFAERO IV', 'GULFAERO IV'), ('CHAMPION 7GC', 'CHAMPION 7GC'), ('B-727-200', 'B-727-200'), ('PA-31-350', 'PA-31-350'), ('A-340', 'A-340'), ('PA-44 SEMINOLE', 'PA-44 SEMINOLE'), ('HAWKER 4000', 'HAWKER 4000'), ('B-747-400', 'B-747-400'), ('C-560', 'C-560'), ('C-680', 'C-680'), ('MD-80', 'MD-80'), ('C-208', 'C-208'), ('GULFSTREAM 200', 'GULFSTREAM 200'), ('CL-600', 'CL-600'), ('CITATION MUSTANG 510', 'CITATION MUSTANG 510'), ('MD-88', 'MD-88'), ('C-182 SKYLAN', 'C-182 SKYLAN'), ('BE-55  BARON', 'BE-55  BARON'), ('EMB-190', 'EMB-190'), ('MD-90-30', 'MD-90-30'), ('LEARJET-45', 'LEARJET-45'), ('GULFSTREAM G150', 'GULFSTREAM G150'), ('BELL-430', 'BELL-430'), ('EMB-500', 'EMB-500'), ('B-777-200', 'B-777-200'), ('C-402', 'C-402'), ('CHALLENGER 300', 'CHALLENGER 300'), ('PA-28', 'PA-28'), ('SAAB-340', 'SAAB-340'), ('HUGHES 269A', 'HUGHES 269A'), ('BE-65 QUEEN', 'BE-65 QUEEN'), ('DA-2000', 'DA-2000'), ('B-767-300', 'B-767-300'), ('B-737-400', 'B-737-400'), ('C-550', 'C-550'), ('BE-200 KING', 'BE-200 KING'), ('EC135', 'EC135'), ('B-737-300', 'B-737-300'), ('CRJ700', 'CRJ700'), ('CIRRUS SR 20/22', 'CIRRUS SR 20/22'), ('BE-36', 'BE-36'), ('B-757-300', 'B-757-300'), ('B-787-9', 'B-787-9'), ('C-172', 'C-172'), ('B-737-900', 'B-737-900'), ('B-767-200', 'B-767-200'), ('MD-82', 'MD-82'), ('CASA CN-235', 'CASA CN-235'), ('A-321', 'A-321'), ('B-737-500', 'B-737-500'), ('BELL-206', 'BELL-206'), ('EMB-170', 'EMB-170'), ('EXPERIMENTAL', 'EXPERIMENTAL'), ('ATR-42', 'ATR-42'), ('AEROS 350', 'AEROS 350'), ('B-737', 'B-737'), ('BE-400 BJET', 'BE-400 BJET'), ('MD-11', 'MD-11'), ('DC-10-30', 'DC-10-30'), ('B-717-200', 'B-717-200'), ('A-319', 'A-319'), ('A-320', 'A-320'), ('B-737-800', 'B-737-800'), ('UNKNOWN', 'UNKNOWN'), ('B-757-200', 'B-757-200'), ('CRJ900', 'CRJ900'), ('B-777', 'B-777'), ('A-310', 'A-310'), ('A-300', 'A-300'), ('MD-83', 'MD-83'), ('EC130', 'EC130'), ('EMB-145', 'EMB-145'), ('EMB-135', 'EMB-135'), ('DC-10-10', 'DC-10-10'), ('B-737-700', 'B-737-700'), ('CITATIONJET', 'CITATIONJET'), ('DHC8 DASH 8', 'DHC8 DASH 8'), ('CRJ100/200', 'CRJ100/200')], validators = [DataRequired()])
    submit = SubmitField('Enter')



@app.route('/AvsA' , methods = ['GET' , 'POST'])
def AvsA():
    chart = None
    name = None
    name2 = None
    print("running from qurey()")
    form = QueryFormStructureFD(request.form)
    if (request.method == 'POST' ):
        df = pd.read_csv(URL_4)
        name = form.name.data
        name2 = form.name2.data
        print(name)
        print(name2)
        if (name == name2):
            flash("error")
            name = None
            name2 = None
            
        
        Air1 = df[(df['Aircraft'] == name)].size
        Air2 = df[(df['Aircraft'] == name2)].size
        if (Air1 == 0):
            flash("your first aircraft dosn't have any events related to him")
        if (Air2 ==0):
            flash("your secconed aircraft dosn't have any events related to him")
        if (Air1 == 0 )&(Air2 == 0):
            flash("both your aircrafts have no events related to them please try agian")
            return redirect(url_for('AvsA'))
        if (name != None)&(name2 != None):
            sizes = [Air1, Air2]
            names = [name,name2]
            fig = plt.figure()
            plt.scatter(names , sizes)
            chart = plot_to_img(fig)

        


    return render_template('AvsA.html',
                           form= form,
                           title = 'Query by the user',
                           year=datetime.now().year,
                           message='query input',
                           chart = chart ,
                           height = "500" ,
                           width = "750" 
                           )

