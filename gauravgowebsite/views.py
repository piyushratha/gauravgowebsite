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


def footer(request):
    return render(request, 'footer.html')

def header(request):
    return render(request, 'header.html')

def simulation_projects(request):
    return render(request, 'simulation-projects.html')

def three_d_assets(request):
    return render(request, '3d-assets.html')

def game_development(request):
    return render(request, 'game-development.html')

def animation(request):
    return render(request, 'animation.html')

def blender_vfx(request):
    return render(request, 'blender-vfx.html')



