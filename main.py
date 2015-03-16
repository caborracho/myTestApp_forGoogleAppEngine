#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import webapp2
from google.appengine.ext.webapp.template import render
from google.appengine.api import users
from Models.SumEntity import SumEntity as Sum 
from Models.StudientEntity import StudientEntity as Studient
import Controllers.UserController as  UserController

SERVER_TYPE = "prod" #dev/prod
#JQUERY_SOURCE = "/libs/jquery/jquery-2.1.3.min.js" if os.environ['SERVER_SOFTWARE'].startswith('Dev') else "https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"#"https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"
JQUERY_SOURCE = "/libs/jquery/jquery-2.1.3.min.js" if SERVER_TYPE == "dev" else "https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"



class MainHandler(webapp2.RequestHandler):
    def get(self):

    	
    	userName = UserController.loadUser(self,self.request.uri)
    	# user =  users.get_current_user()

    	# if not user:
    	# 	self.redirect(users.create_login_url(self.request.uri))
    	# else:
    	# 	userName = user.nickname()
    	# 	if "@" in user.nickname():
	    # 		userName = userName[:user.nickname().find("@")]
	    # 	else:
	    # 		userName = user.nickname()

	    # 	myStudient = Studient.getStudientByName(userName)
	    # 	if not myStudient:
	    # 		myNewStudient = Studient(userName)
	    # 		myNewStudient.store()

    	templateValues = {
            'source':       "Template",
            'jQuerySource': JQUERY_SOURCE,
            'userName':     userName
        }
    	mainPageTemplate = os.path.join(os.path.dirname(__file__), 'Views/MainPage.html')
        self.response.write(render(mainPageTemplate, templateValues))
		


class SumHandler(webapp2.RequestHandler):
	"""docstring for SumHandler"""
	def get(self):
		try:
			first = int(self.request.get('first'))
			second = int(self.request.get('second'))
			self.response.write(str(first + second))


        
		except Exception as e:
			self.response.write("invalid inputs. "+ str(e)+ "   user "+UserController.loadUser(self))
			pass
		
		stud = UserController.getStudient(self)
		studID = stud.getID()
		self.mySum = Sum(studID,first,second, first+second)
		self.mySum.store()

class SumHistoryHandler(webapp2.RequestHandler):
	"""docstring for SumHystoryHandler"""
	def get(self):
		stud = UserController.getStudient(self)
		self.sums = stud.getAllSums()
		for self.sum in self.sums:
			self.response.write("<p>%s+%s=%s</p>" % (self.sum.getN1(),self.sum.getN2(),self.sum.getResult()))



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/sumfunction', SumHandler),
    ('/sumhistory', SumHistoryHandler),
], debug=True)
