import webapp2
import os
# import logging


class Demo(webapp2.RequestHandler):

    def get(self, parent=None):
        if parent:
            self = parent

        self.response.headers['Content-Type'] = 'text/html'


        self.response.write('<html>')
        self.response.write('<title>Geolocation Demo on Google App Engine</title>')
        self.response.write('<body>')

        self.response.write('Current City: ' + os.environ.get('HTTP_X_APPENGINE_CITY', 'Unknown City'))
        self.response.write('<br/>')
        self.response.write('Current Country: ' + os.environ.get('HTTP_X_APPENGINE_COUNTRY', 'Unknown Country'))

        self.response.write('</body>')
        self.response.write('</html>')



app = webapp2.WSGIApplication([
    ('/geolocation', Demo),
], debug=True)
