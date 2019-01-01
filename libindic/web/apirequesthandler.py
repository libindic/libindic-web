from json import loads, dumps
from .modulehelper import modules, modulenames, MODULES, enabled_modules, \
        load_modules


class APIRequestHandlerException(Exception):
    pass

class BadServiceRequest(APIRequestHandlerException):
    pass


class MethodNotFoundException(APIRequestHandlerException):
    def __init__(self, name):
        self.methodname = name


class APIRequestHandler(object):

    def __init__(self):
        '''
         This should be only once called. Atleast my assumption
        '''
        load_modules()

    def translate_result(self, result, error, id_):
        if error != None:
            error = {"name": error.__class__.__name__, "message": error}
            result = None

        try:
            data = dumps({"result": result, "id": id_, "error": error})
        except:
            error = {"name": "JSONEncodeException", \
                    "message": "Result object is not serializable"}
            data = dumps({"result": None, "id": id_, "error": error})

        return data

    def call(self, method, args):
        _args = None
        for arg in args:
            if arg != '':
                if _args == None:
                    _args = []
                _args.append(arg)

        if _args == None:
            # No arguments
            return method()
        else:
            return method(*_args)

    def handle_request(self, req):
        err = None
        method = None
        id_ = ''
        result = None
        args = None

        if err == None:
            try:
                id_ = req['id']
                method = req['method']
                module = req['module']
                try:
                    args = req['params']
                except:
                    pass
            except:
                err = BadServiceRequest(json)

            module_instance = None
            if err == None:
                try:
                    module_instance = MODULES.get(module)
                except:
                    err = MethodNotFoundException(module)


            if err == None and method != None and module_instance != None :
                result = self.call(getattr(module_instance, method), args)

            return self.translate_result(result, err, id_)
