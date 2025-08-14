from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def games(request):
    return render(request, 'games.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def advertisers(request):
    return render(request, 'advertisers.html')

def careers(request):
    return render(request, 'careers.html')

def media_coverage(request):
    return render(request, 'media_coverage.html')

def our_supporters(request):
    return render(request, 'our_supporters.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')




