from django.shortcuts import redirect


def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_superuser == True:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('base:home')
    return wrapper_func