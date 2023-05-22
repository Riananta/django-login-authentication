from functools import wraps
from django.contrib import messages
from django.shortcuts import redirect


# function cek login
def login_required():
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if request.session.get('userid'):
                # Jika pengguna memiliki session userid (sudah login)
                return view_func(request, *args, **kwargs)
            else:
                # Jika pengguna tidak memiliki session userid (belum login)
                messages.error(request, "LOGIN TERLEBIH DAHULU")
                return redirect('login')
        return wrapper
    return decorator

# function hak akses
def user_level_required(user_level):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if request.session.get('userlevel') == user_level:
                # Jika pengguna memiliki level akses yang diizinkan, jalankan fungsi tampilan
                return view_func(request, *args, **kwargs)
            else:
                # Jika pengguna tidak memiliki level akses yang diizinkan, arahkan ke halaman lain (misalnya halaman login)
                messages.error(request, "ANDA TIDAK MEMILIKI AKSES")
                return redirect('dashboard')
        return wrapper
    return decorator
