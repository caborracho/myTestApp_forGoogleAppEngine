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

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	templateValues = {
            'source':      "Template"
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
        
		except (TypeError, ValueError):
			self.response.write("Invalid inputs")

		

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/sumfuction', SumHandler)
], debug=True)
