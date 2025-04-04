from django.db import connection
from django.db.utils import OperationalError
from django.http import HttpResponse
from django.template.loader import render_to_string

class DatabaseErrorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
            return self.get_response(request)
        except OperationalError:
            content = render_to_string('errors/db_error.html')
            return HttpResponse(content, status=503)