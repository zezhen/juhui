
import cherrypy, socket
import os, tempfile
# import cjson
# import calendar
# from datetime import datetime

# sys.path.append("./service")

#serverHostname = socket.gethostname()
serverHostname = '127.0.0.1'
servicePort = 9999
cherrypy.config.update({'server.socket_host':serverHostname, 'server.socket_port': servicePort,})

# def jsonify_tool_callback(*args, **kwargs):
#	  response = cherrypy.response
#	  response.headers['Content-Type'] = 'application/json'
# cherrypy.tools.jsonify = cherrypy.Tool('before_finalize', jsonify_tool_callback, priority=30)

class App(object):

	@cherrypy.expose
	# @cherrypy.tools.jsonify()
	def index(self, **args):
		# cherrypy.response.headers['Content-Type'] = 'application/json'
		return file('index.html')


if __name__ == '__main__':
	js_dir = os.path.join(os.path.abspath("."), "js")
	conf = {
		'/': {
			'tools.sessions.on': True,
			'tools.staticdir.root': os.path.abspath(os.getcwd())
		},
		'/static': {
			'tools.staticdir.on': True,
			'tools.staticdir.dir': './public',
		},
		'/js': {
			'tools.staticdir.on': True,
			'tools.staticdir.dir': js_dir
		}
	}
	webapp = App()
	#webapp.generator = StringGeneratorWebService()
	cherrypy.quickstart(webapp, '/', conf)