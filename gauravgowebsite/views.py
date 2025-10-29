from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db.models import Q

from GauravGoWeb import settings
from gauravgowebsite.models import Games, Contact


def get_file_size(file):
    """Convert file size in bytes to human-readable format."""
    size = file.size
    if size < 1024:
        return f"{size} bytes"
    elif size < 1024 * 1024:
        return f"{size // 1024} KB"
    else:
        return f"{size // (1024 * 1024)} MB"


def index(request):
    # Fetch latest games for display on home page
    latest_games = Games.objects.all().order_by('-creationdate')[:8]  # Get latest 8 games
    context = {
        'latest_games': latest_games,
    }
    return render(request, 'index.html', context)

def games(request):
    # Optional type filter by query param: ?type=ftp|br|fps|rpg|sim|other
    gtype = request.GET.get('type')
    if gtype:
        games_qs = Games.objects.filter(game_type=gtype).order_by('-creationdate')
    else:
        games_qs = Games.objects.all().order_by('-creationdate')
    # also provide per-type lists for the sliders
    ftp_games = Games.objects.filter(game_type='ftp').order_by('-creationdate')
    br_games = Games.objects.filter(game_type='br').order_by('-creationdate')
    fps_games = Games.objects.filter(game_type='fps').order_by('-creationdate')
    rpg_games = Games.objects.filter(game_type='rpg').order_by('-creationdate')
    sim_games = Games.objects.filter(game_type='sim').order_by('-creationdate')

    context = {
        'games': games_qs,
        'total_games': games_qs.count(),
        'selected_type': gtype,
        'ftp_games': ftp_games,
        'br_games': br_games,
        'fps_games': fps_games,
        'rpg_games': rpg_games,
        'sim_games': sim_games,
    }
    return render(request, 'games.html', context)

def game_detail(request, pid):
    game = get_object_or_404(Games, id=pid)
    return render(request, 'game_detail.html', {'game': game})

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
        booking = Games.objects.filter(Q(title__icontains=sd) | Q(description__icontains=sd))
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
        game_type = request.POST.get('game_type', 'other')

        if not title:
            messages.error(request, "Please provide a title.")
            return render(request, 'add_games.html', {})   # consistent template name

        try:
            game = Games.objects.create(
                title=title,
                description=description,
                image=image,
                logo=logo,
                game_type=game_type,
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
        game_type = request.POST.get('game_type', game.game_type if hasattr(game, 'game_type') else 'other')

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
            # save game_type if provided
            try:
                game.game_type = game_type
                game.save()
            except Exception:
                pass
            messages.success(request, "Game updated successfully.")
            return redirect('manage_games')
        except Exception as e:
            # optionally log exception e
            messages.error(request, "Something went wrong while updating the game.")
            return render(request, 'edit_games.html', {'game': game})

    # GET
    return render(request, 'edit_games.html', {'game': game})



def delete_games(request, pid):
    service = Games.objects.get(id=pid)
    service.delete()
    return redirect('manage_games')

def add_game_details(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')

    game = get_object_or_404(Games, id=pid)

    if request.method == "POST":
        background_image = request.FILES.get('background_image')
        additional_description = request.POST.get('additional_description', '').strip()
        file_upload = request.FILES.get('file_upload')
        release_date = request.POST.get('release_date')
        publisher = request.POST.get('publisher', 'GauravGo Games').strip()
        rating = request.POST.get('rating', '5.0')
        file_size = request.POST.get('file_size', '31mb').strip()
        platforms = request.POST.get('platforms', 'Web, Android, iOS').strip()
        play_store_link = request.POST.get('play_store_link', '').strip()
        youtube_link = request.POST.get('youtube_link', '').strip()

        # Calculate file size if file is uploaded
        if file_upload:
            file_size = get_file_size(file_upload)

        # Update the game instance
        if background_image:
            game.background_image = background_image
        if additional_description:
            game.additional_description = additional_description
        if file_upload:
            game.file_upload = file_upload
        if play_store_link:
            if not play_store_link.startswith(('http://', 'https://')):
                play_store_link = 'https://' + play_store_link
            game.play_store_link = play_store_link
        if release_date:
            from datetime import datetime
            game.release_date = datetime.strptime(release_date, '%Y-%m-%d').date()
        if publisher:
            game.publisher = publisher
        if rating:
            game.rating = float(rating)
        if file_size:
            game.file_size = file_size
        if platforms:
            game.platforms = platforms
        if youtube_link:
            game.youtube_link = youtube_link

        try:
            game.save()
            messages.success(request, "Game details added successfully.")
            return redirect('manage_games')
        except Exception as e:
            messages.error(request, "Something went wrong while saving the details.")
            return render(request, 'add_game_details.html', {'game': game})

    # GET
    return render(request, 'add_game_details.html', {'game': game})

def queries_list_all(request):
    unread_list = Contact.objects.filter(is_resolved=False).order_by('-created_at')
    read_list = Contact.objects.filter(is_resolved=True).order_by('-created_at')
    all_list = Contact.objects.all().order_by('-created_at')
    return render(request, 'queries/list.html', {
        'unread_list': unread_list,
        'read_list': read_list,
        'all_list': all_list,
    })

def queries_unread(request):
    unread_list = Contact.objects.filter(is_resolved=False).order_by('-created_at')
    return render(request, 'queries/list.html', {'unread_list': unread_list, 'read_list': [], 'all_list': unread_list})

def queries_read(request):
    read_list = Contact.objects.filter(is_resolved=True).order_by('-created_at')
    return render(request, 'queries/list.html', {'unread_list': [], 'read_list': read_list, 'all_list': read_list})

def query_detail(request, pk):
    q = get_object_or_404(Contact, pk=pk)
    # Optionally mark as read when opening:
    if not q.is_resolved:
        # don't auto-mark resolved — only mark as read flag if you have that field; here is_resolved used as unread/resolved
        pass
    return render(request, 'queries/detail.html', {'query': q})

def toggle_resolved(request, pk):
    q = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        q.is_resolved = not q.is_resolved
        q.save()
        messages.success(request, 'Status updated.')
    return redirect(request.META.get('HTTP_REFERER', 'queries:all'))

def reply_to_query(request, pk):
    q = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        subject = request.POST.get('subject', '').strip()
        body = request.POST.get('body', '').strip()
        # send email (ensure EMAIL settings configured in settings.py)
        if q.emailid:
            try:
                send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [q.emailid])
                messages.success(request, 'Reply sent.')
            except Exception as e:
                messages.error(request, f'Failed to send email: {e}')
        else:
            messages.error(request, 'No email available for this contact.')
    return redirect('queries:detail', pk=pk)

def delete_query(request, pk):
    q = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        q.delete()
        messages.success(request, 'Query deleted.')
        return redirect('queries:all')
    return redirect('queries:detail', pk=pk)


def submit_query(request):
    """
    Accept POST from the public contact form and save a Contact record.
    Expected POST fields: name, email (emailid), contact, company, message
    """
    if request.method == 'POST':
        name = request.POST.get('name', '').strip() or None
        email = request.POST.get('email', '').strip() or None
        contact = request.POST.get('contact', '').strip() or None
        company = request.POST.get('company', '').strip() or None
        message_text = request.POST.get('message', '').strip() or ''

        # Basic validation: message required
        if not message_text:
            messages.error(request, 'Please provide a message.')
            return redirect(request.META.get('HTTP_REFERER', '/'))

        try:
            Contact.objects.create(
                name=name,
                emailid=email,
                contact=contact,
                company=company,
                message=message_text,
            )
            messages.success(request, 'Your query has been submitted. Thank you!')
        except Exception as e:
            # log or print for debugging
            print('Failed to save contact:', e)
            messages.error(request, 'Failed to submit your query. Please try again later.')

    return redirect(request.META.get('HTTP_REFERER', '/'))