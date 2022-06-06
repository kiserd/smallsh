from django.http import HttpResponse

def index(request):
    body = request.body
    print('body: ', body)
    res = HttpResponse()
    res.status_code = 200
    return HttpResponse(body)
