from django.utils.deprecation import MiddlewareMixin

from uauth.models import RequestCount


class ClickCountMiddleware(MiddlewareMixin):
    def process_request(self,request):
        if request.path == '/uauth/login/' and request.method == "POST":
            clickEvent = RequestCount.objects.get(c_path_name='c_login')
            clickEvent.c_path_count += 1
            clickEvent.save()
        elif request.path == '/uauth/logout/' and request.method == "GET" :
            clickEvent = RequestCount.objects.get(c_path_name='c_logout')
            clickEvent.c_path_count += 1
            clickEvent.save()
        elif request.path == '/stuapp/addstu/' and request.method == "POST":
            clickEvent = RequestCount.objects.get(c_path_name='c_addstu')
            clickEvent.c_path_count += 1
            clickEvent.save()