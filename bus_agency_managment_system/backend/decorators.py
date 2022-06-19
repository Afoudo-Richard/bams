
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User, Group

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

# def allowed_users(allowed_roles=[]):
#     def decorator(view_func):
#         def wrapper_func(request, *args, **kwargs):
#             # group = None
#             # if request.user.groups.exist():
#             #     group = request.user.groups.all()[0].name
#             # if group in allowed_roles:
#             #     return view_func(request,*args, **kwargs)
#             # else:
#             #     return HttpResponse('You are not authorized to view this page')
#             is_staff = request.user.is_staff

#             if is_staff == 1:
#                 return view_func(request,*args, **kwargs)
#             else:
#                 return HttpResponse('You are not authorized to view this page')
            
#         return wrapper_func
#     return decorator


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            user_groups = Group.objects.filter(user = request.user)
            if user_groups.exists():
                group =user_groups[0].name

            if group in allowed_roles:
                return view_func(request,*args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')
        return wrapper_func
    return decorator


def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None

        user_groups = Group.objects.filter(user = request.user)
        if user_groups.exists():
            group =user_groups[0].name
            
        if group == 'customer':
            return redirect('user_dashboard')
        if group == 'admin':
            return view_func(request, *args, **kwargs)
    return wrapper_function