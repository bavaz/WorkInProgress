# Copyright 2016 Google Inc.
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

import webapp2
import cgi


class MainPage(webapp2.RequestHandler):   
	def form(self, display=""):
		global form
	 	form = """<!doctype html>
	 				<head>
	 					<meta charset="utf-8"/>
     					<title> Signup </title>
     				</head>
     				<body>
     					<div>
     						<b>Enter some text to ROT13</b>
     					</div>
     					<form action="/rot_13" method="post">
     						<textarea name="text" placeholder="Enter text here...">%(text)s</textarea>
	 	    					<div>
     							<input type="submit" value="Enter">
     						</div>
     					</form>
     				</body>
     			</html>"""
		self.response.write(form % {"text":display})
     
	def get(self):
		self.response.headers['Content-Type'] = 'text/html; charset=utf-8'
		self.form("")
		
class Rot_13(webapp2.RequestHandler):
	
	def rot13(self, text):
		result = ''
		for s in text:
			if s.isalpha():
				ascii_val = ord(s)
				if ascii_val > 77 :
					if ascii_val > 109 :
						val = (ascii_val + 13)%26 + 97
					elif ascii_val <= 90 :
						val = (ascii_val + 13)%26 + 65
					else :
						val = ascii_val + 13
				else :
					val = ascii_val + 13
			else :
				val = ord(s)
			result = result + str(unichr(val))
		return result;
	
	def escape_html(self, text):
		return cgi.escape(text, quote=True);
	
	def post(self):
		self.response.headers['Content-Type'] = 'text/html'
		text_entered = self.request.get('text')
		rot_13_result = self.rot13(text_entered)
		rot_13_result = self.escape_html(rot_13_result)
		#m = MainPage()
		#m.form(rot_13_result)
		self.response.write(form % {"text":rot_13_result})
		#self.response.write(rot_13_result)

app = webapp2.WSGIApplication([
    ('/', MainPage), ('/rot_13',Rot_13 )
], debug=True)

