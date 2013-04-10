#encoding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext  # para hacer funcionar {% csrf_token %}
from pymongo import MongoClient
import datetime
import sys
import random

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
		# if request.method == "GET":  # envia una variable para seleccionar una organizacion
		# 	try:
		# 		name = request.GET['new_user']
		# 		try:
		# 			user.insert({'name':name})
		# 		except:
		# 			print 'Error intentando guardar dato'
		# 	except Exception:
		# 		print 'No hay variable get: new_user'
		try:
			daily_visits = db.daily_visits
			try:
				d = datetime.datetime.now()
				print d
				try: 
					daily_visits.insert({'date': d})
					# for i in range(5):
					# 	x = "2013-04-%s"%(int(random.random()*24)+1)
					# 	f = datetime.datetime.strptime(x,"%Y-%m-%d")
#						print f
						# daily_visits.insert({'date': f})
				except:
					print 'Error guardando datos', sys.exc_info()[0]
			except:
				print "Error con datetime", sys.exc_info()[0]
		except:
			print 'Error conectando daily_visits', sys.exc_info()[0]
		
		things = user.find()
	except:
		things = [{'name':'Ha ocurrido un error con la base de datos'}]
	# print things
	# for thing in things:
	# 	print thing['_id']
	ctx = {'things':things}

	return render_to_response('edwinfmesa/index.html', ctx, context_instance=RequestContext(request))

def visits(request):
	try:
		connection = MongoClient('localhost',27017)
	
		
		#	if connection.my_blog.authenticate('edwinfmesa','123456'):
		#		db = connection.my_blog
		#	else:
		#		print "Error de autenticacion"
	
		db = connection.users
		# user = db.user
		# if request.method == "GET":  # envia una variable para seleccionar una organizacion
		# 	try:
		# 		name = request.GET['new_user']
		# 		try:
		# 			user.insert({'name':name})
		# 		except:
		# 			print 'Error intentando guardar dato'
		# 	except Exception:
		# 		print 'No hay variable get: new_user'
		daily_visits = db.daily_visits
		# daily_visits.insert({'date': datetime.date.now()})
		try:
			visits2 = daily_visits.find().sort([("date",-1)])
			visits = daily_visits.find().sort([("date",1)])
			print '---------------------------------------',visits
			for i in visits2:
				print i
		except:
			print 'Error', sys.exc_info()[0]
	except:
		visits = [{}]
		print 'error', sys.exc_info()[0]

	visitas = {}
	for v in visits:
		try:
			visitas[datetime.datetime.strftime(v['date'],"%d")]=visitas[datetime.datetime.strftime(v['date'],"%d")]+1
		except:
			visitas[datetime.datetime.strftime(v['date'],"%d")]=1
	print '------------------------'
	for p in visitas:
		print p
	datos = []
	for v in visitas:
		datos.append([v,visitas[v]])
	print '------------------------'
	for p in datos:
		print p

	# from bson.code import Code
	# map = Code("function () {"
 #            "  this.date.forEach(function(z) {"
 #            "    emit(z, 1);"
 #            "  });"
 #           "}")
	# reduce = Code("function (key, values) {"
 #               "  var total = 0;"
 #               "  for (var i = 0; i < values.length; i++) {"
 #               "    total += values[i];"
 #               "  }"
 #               "  return total;"
 #              "}")
	# result = db.daily_visits.map_reduce(map, reduce, "myresults")
	# print visitas
	# print things
	# for thing in things:
	# 	print thing['_id']
	ctx = {'visitas':datos}

	return render_to_response('edwinfmesa/visits.html', ctx, context_instance=RequestContext(request))