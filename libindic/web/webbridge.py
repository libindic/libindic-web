'''
  WebBridge is a bridging class between the flask front end of SILPA with
  the module related information like rendering appropriate templates and
  answering the JSONRPC requests and RESTful requests.

  This class is derived from MethodView class from flask.views
'''

from flask.views import MethodView
from flask import render_template, request, globals
from .modulehelper import modulenames, enabled_modules, BASEURL,SITE, MODULES
from .apirequesthandler import APIRequestHandler

handler = APIRequestHandler()


class WebBridge(MethodView):
    def __init__(self):
        self.app = globals.current_app

    def get(self):
        '''
         Method from MethodView class which handles all HTTP GET requests
         depending on request path render required template.

         If the query string is not None then its a RESTful request respond
         with a proper response format
        '''
        self.app.logger.debug('REQUEST PATH {0} and Base URL {1}' \
                .format(request.path, BASEURL))
        if request.path == BASEURL:
            # request is for document root
            return render_template('index.html', title=SITE, \
                    main_page=BASEURL, modules=enabled_modules)
        elif request.path == BASEURL+ "License":
            return render_template('license.html', title="License",
                    main_page=BASEURL, modules=enabled_modules)
        elif request.path == BASEURL+ "Credits":
            return render_template('credits.html', title="Credits", \
                    main_page=BASEURL, modules=enabled_modules)
        elif request.path == BASEURL+ "Contact":
            return render_template('contact.html', title="Contact", \
                    main_page=BASEURL, modules=enabled_modules)

        elif len(request.args) == 0:
            # This is not query so lets serve the page
            pathcomponent = request.path.split('/')[-1]
            for module, name in  modulenames.items():
                if pathcomponent == name:
                    return render_template(module + '.html', title=SITE, modulename=name,\
                            main_page=BASEURL, modules=enabled_modules,
                            data=getattr(MODULES[module], "data", {}))

    def post(self):
        '''
         Method from MethodView class which handles all HTTP POST requests

        '''
        if request.path.endswith("api"):
            if request.json != None:
                return handler.handle_request(request.json)
