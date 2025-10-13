from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, logout, authenticate
from gauravgowebsite.models import Games

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

def add_games(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')

    if request.method == "POST":
        title = request.POST.get('servicetitle', '').strip()
        description = request.POST.get('description', '').strip()
        image = request.FILES.get('image')
        logo  = request.FILES.get('logo')

        if not title:
            messages.error(request, "Please provide a title.")
            return render(request, 'add_games.html', {})   # consistent template name

        try:
            game = Games.objects.create(
                title=title,
                description=description,
                image=image,
                logo=logo
            )
            messages.success(request, "Game added successfully.")
            return redirect('manage_games')
        except Exception as e:
            # optional: print or logging for debugging
            print("Error saving game:", e)
            messages.error(request, "Something went wrong while saving the game.")
            return render(request, 'add_games.html', {})

    # GET
    return render(request, 'add_games.html', {})


def manage_games(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')

    games = Games.objects.all().order_by('-creationdate')
    return render(request, 'manage_games.html', {'games': games})


def edit_games(request, pid):
    """
    GET:  render edit_games.html with the game instance in context as 'game'
    POST: update title/description and optionally image; then redirect to manage_games
    """
    game = get_object_or_404(Games, id=pid)

    if request.method == "POST":
        # field names kept same as your form: servicetitle, description, image
        title = request.POST.get('servicetitle', '').strip()
        description = request.POST.get('description', '').strip()

        # Basic validation
        if not title:
            messages.error(request, "Please enter a title for the game.")
            return render(request, 'edit_games.html', {'game': game})

        game.title = title
        game.description = description

        # handle uploaded image (safe .get)
        uploaded_image = request.FILES.get('image')
        if uploaded_image:
            game.image = uploaded_image

        # Optionally handle logo if your form includes it:
        uploaded_logo = request.FILES.get('logo')
        if uploaded_logo:
            # if your model has `logo` field
            try:
                game.logo = uploaded_logo
            except Exception:
                # ignore if model doesn't have logo field
                pass

        try:
            game.save()
            messages.success(request, "Game updated successfully.")
            return redirect('manage_games')
        except Exception as e:
            # optionally log exception e
            messages.error(request, "Something went wrong while updating the game.")
            return render(request, 'edit_games.html', {'game': game})

    # GET
    return render(request, 'edit_games.html', {'game': game})



def delete_games(request, pid):
    """
    GET:  show delete confirmation page (delete_games.html) with 'game' in context
    POST: actually delete the object and redirect to manage_games
    """
    game = get_object_or_404(Games, id=pid)

    if request.method == "POST":
        try:
            game.delete()
            messages.success(request, "Game deleted successfully.")
        except Exception as e:
            # optionally log e
            messages.error(request, "Could not delete game. Try again later.")
        return redirect('manage_games')

    # GET -> render a confirmation template
    return render(request, 'delete_games.html', {'game': game})