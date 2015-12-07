import webapp2
import os


class Demo(webapp2.RequestHandler):

    def get(self, parent=None):
        if parent:
            self = parent

        self.response.headers['Content-Type'] = 'text/html'


        self.response.write('<html>')
        self.response.write('<title>os.environ attributes on Google App Engine</title>')

        self.response.write("""<style>
body{font-family:arial;}
tr:first-child{font-weight:bold;}
tr:nth-child(even){background-color:#eee;}
td{padding:4px;}
</style>""")
        self.response.write('<body>')


        self.response.write('<table>')

        # table header
        self.response.write('<tr>')
        self.response.write('<td>key</td>')
        self.response.write('<td>os.environ[key]</td>')
        self.response.write('</tr>')


        keys = os.environ.keys()
        keys.sort()

        for k in keys:

            self.response.write('<tr>')
            self.response.write('<td>')
            self.response.write(k)
            self.response.write('</td>')
            self.response.write('<td>')

            output = os.environ[k]

            # use this line of code for normal case.
            # self.response.write(output)

            # To protect the demo environment, some values are not disclosed here. We use the following code instead.
            if k == "APPLICATION_ID" or k == "CURRENT_VERSION_ID" or k == "DEFAULT_VERSION_HOSTNAME" or \
                    k == "HTTP_X_ZOO" or k == "INSTANCE_ID" or \
                    k == "PATH_TRANSLATED" or k == "REQUEST_ID_HASH" or k == "REQUEST_LOG_ID":
                output = "<i>Hidden value in demo application. Try on your own application.</i>"

            self.response.write(output)

            self.response.write('</td>')
            self.response.write('</tr>')

        self.response.write('</table>')

        self.response.write('</body>')
        self.response.write('</html>')



app = webapp2.WSGIApplication([
    ('/os_environ', Demo),
], debug=True)
