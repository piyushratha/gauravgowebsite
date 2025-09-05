from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate

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


def admin_login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['username']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
                error = "yes"
    return render(request, 'admin_login.html', locals())


def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    
    return render(request,'admin_home.html', locals())

def Logout(request):
    logout(request)
    return redirect(index)

def search(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    sd = None
    if request.method == 'POST':
        sd = request.POST['searchdata']
    try:
        booking = SiteUser.objects.filter(Q(name=sd) | Q(mobile=sd))
    except:
        booking = ""
    print(booking)
    return render(request, 'search.html', locals())


def change_password(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""

    if request.method == "POST":
        o = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id) 
            if u.check_password(o):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"
    return render(request, 'change_password.html', locals())

