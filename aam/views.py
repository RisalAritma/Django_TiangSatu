from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime

tanggal_now = datetime.now().date()

def custom_404(request, exception):
    return render(request, "404.html", status=404)

def home(request):
    context = {
        'title' : 'Home',
        'heading' : 'Tiang Satu',
    }
    return render(request,'home.html', context) 

def galeri(request, kabupaten=None):

    if kabupaten == 'enrekang':
        context = {
            'title' : 'Galeri Enrekang',
            'heading' : 'Galeri Enrekang',
            'fotos' : [
                'enrekang (1).jpg',
                'enrekang (2).jpg',
                'enrekang (3).jpg',
                'enrekang (4).jpg',
                'enrekang (5).jpg',
                'enrekang (6).jpg',
                'enrekang (7).jpg',
            ]
        }
    elif kabupaten == 'sinjai':
        context = {
            'title' : 'Galeri Sinjai',
            'heading' : 'Galeri Sinjai',
            'fotos' : [
                'sinjai (1).jpg',
                'sinjai (2).jpg',
                'sinjai (3).jpg',
                'sinjai (4).jpg',
                'sinjai (5).jpg',
                'sinjai (6).jpg',
                'sinjai (7).jpg',
            ]
        }
    elif kabupaten == 'soppeng':
        context = {
            'title' : 'Galeri Soppeng',
            'heading' : 'Galeri Soppeng',
            'fotos' : [
                'soppeng (1).jpg',
                'soppeng (2).jpg',
                'soppeng (3).jpg',
                'soppeng (4).jpg',
                'soppeng (5).jpg',
                'soppeng (6).jpg',
                'soppeng (7).jpg',
            ]
        }
    elif kabupaten == 'wajo':
        context = {
            'title' : 'Galeri Wajo',
            'heading' : 'Galeri Wajo',
            'fotos' : [
                'wajo (1).jpg',
                'wajo (2).jpg',
                'wajo (3).jpg',
                'wajo (4).jpg',
                'wajo (5).jpg',
                'wajo (6).jpg',
                'wajo (7).jpg',
            ]
        }


    return render(request,'galeri.html', context) 

