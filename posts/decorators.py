from functools import wraps
from django.shortcuts import redirect


def login_not_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Add any custom logic here to check if login is required
        # For simplicity, we allow access to the view for everyone
        return view_func(request, *args, **kwargs)

    return _wrapped_view
