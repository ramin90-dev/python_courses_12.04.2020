import datetime

from time import time # noqa - from time import time' is identified as Stdlib and 'import datetime' is identified as Stdlib.

from teachers.models import Logger


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time()

        response = self.get_response(request)

        end = time()
        if request.path.startswith('/admin/'):
            diff = (end - start) // 1000000
            now = datetime.datetime.now()

            with open('admin_logs.log', 'a') as f:
                log = Logger.objects.create(method=request.method, path=request.path, execution_time=diff)
                f.write(f'{now} | {log.path} | {log.method} | {log.execution_time} ms | {log.created}\n') # noqa

        return response
