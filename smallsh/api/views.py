from django.http import JsonResponse

def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]
    return JsonResponse(routes, safe=False)

def sillyRoute(request):
    return JsonResponse('here ya go', safe=False)