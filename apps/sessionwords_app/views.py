# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'sessionwords_app/index.html')

def add(request):
    # new_word = []
    # for key, value in request.POST.iteritems():
    #     if key != 'color' and key != 'font':
    #         new_word[key] = value
    #     if key == 'font':
    #         new_word[key] = 'font'
    #     else:
    #         new_word['font'] = ''
    if request.method == 'POST':
        request.session['word'] = request.POST['word']
        # request.session['color'] = request.POST['color']
        return redirect('/results')   

def result(request):
    return render(request, 'sessionwords_app/index.html')
