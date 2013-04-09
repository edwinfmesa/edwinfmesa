#encoding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext  # para hacer funcionar {% csrf_token %}
from pymongo import MongoClient

def home(request):
	#connect to database 
	# connection = MongoClient('widmore.mongohq.com',10010)
	try:
		connection = MongoClient('localhost',27017)
	
		
		#	if connection.my_blog.authenticate('edwinfmesa','123456'):
		#		db = connection.my_blog
		#	else:
		#		print "Error de autenticacion"
	
		db = connection.users
		user = db.user
		if request.method == "GET":  # envia una variable para seleccionar una organizacion
			try:
				name = request.GET['new_user']
				try:
					user.insert({'name':name})
				except:
					print 'Error intentando guardar dato'
			except Exception:
				print 'No hay variable get: new_user'
		
		things = user.find()
	except:
		things = [{'name':'Ha ocurrido un error con la base de datos'}]
	# print things
	# for thing in things:
	# 	print thing['_id']
	ctx = {'things':things}

	return render_to_response('edwinfmesa/index.html', ctx, context_instance=RequestContext(request))

