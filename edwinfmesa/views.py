#encoding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext  # para hacer funcionar {% csrf_token %}
from pymongo import MongoClient

def home(request):
	#connect to database 
	connection = MongoClient('widmore.mongohq.com',10010)

	
	if connection.my_blog.authenticate('edwinfmesa','123456'):
		db = connection.my_blog
	else:
		print "Error de autenticacion"

	post = db.post

	things = post.find()
	# print things
	# for thing in things:
	# 	print thing['_id']
	ctx = {'things':things}

	return render_to_response('edwinfmesa/index.html', ctx, context_instance=RequestContext(request))
