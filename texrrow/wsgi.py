from texrrow.application import create_app


def health_check(_application, health_url):
    def health_check_wrapper(environ, start_response):
        if environ.get('PATH_INFO') == health_url:
            start_response('200 OK', [('Content-Type', 'text/plain')])
            return []
        return _application(environ, start_response)
    return health_check_wrapper


application = health_check(create_app(), '/health/')
