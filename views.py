from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import User
# load login_required
from .decorators import login_required
# Create your views here.


def login(request):
    return render(request, 'login.html')


def login_post(request):
    userid = request.POST['userid'].upper()
    password = request.POST['password'].upper()
    if User.objects.filter(userid=userid).exists():
        user = User.objects.get(userid=userid)
        if password == user.password:
            # simpan data session
            request.session['userid'] = user.userid
            request.session['username'] = user.username
            request.session.save()
            messages.success(request, 'BERHASIL LOGIN')
            return redirect('dashboard')
        else:
            messages.error(request, 'PASSWORD SALAH')
    else:
        messages.error(request, 'USER TIDAK DITEMUKAN')
    return redirect('login')


def logout(request):
    # hapus data session
    request.session.flush()
    messages.success(request, 'BERHASIL LOGOUT')
    return redirect('login')


@login_required()
@user_level_required('A') # A adalah user level yg boleh mengakses
def dashboard(request):
    return HttpResponse('halaman dashboard')
