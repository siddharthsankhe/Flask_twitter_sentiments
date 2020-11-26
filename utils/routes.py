from utils import app
from utils.forms import InputForm
from flask import Flask,render_template,url_for,redirect,request
from utils.util import get_stats
import os


@app.route("/")
@app.route("/hello", methods=('GET', 'POST'))
def hello():
	form=InputForm()
	#if  form.validate_on_submit() :
	if request.method=='POST':
		username=form.tag.data
		
		

		full_filename = os.path.join(app.root_path,'static', '2_'+str(username)+'.png')
		graph = os.path.join(app.root_path,'static', 'graph_'+str(username)+'.png')
		if os.path.exists(full_filename):
  			os.remove(full_filename)
		if os.path.exists(graph):
  			os.remove(graph) 
		get_stats(username)
		graph1 = os.path.join('static', 'graph_'+str(username)+'.png')
		full_filename1 = os.path.join('static', '2_'+str(username)+'.png')
		return render_template('home.html',full_filename = full_filename1,graph=graph1,username=username)
	
	username=form.validate_on_submit()
	return render_template('home.html',form=form,username= request.method)

@app.route("/get_senti",methods=['GET','POST'])
def get_senti():
	form=InputForm()
	if  form.validate_on_submit() :
		username=form.tag.data
		
		
		return render_template('homess.html',username=username)
	return render_template('home.html',form=form,username= 'ds')