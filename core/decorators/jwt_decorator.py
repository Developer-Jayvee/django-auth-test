from functools import wraps
from django.http import JsonResponse

def jwt_required(view_func):

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        if not request.user or not request.user.is_authenticated:
            return JsonResponse({
                'message' : 'Unauthenticated'
            },status=401)

        return view_func(request, *args,**kwargs)

    return wrapper