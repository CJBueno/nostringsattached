from django.shortcuts import render, redirect
from django.core import validators
from.models import *
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'nsa_app/index.html')

def signup(request):
    context = {
        'cities' : City.objects.all(),
    }
    return render(request, 'nsa_app/signup.html', context)

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/signup')
    else:
        hashed = bcrypt.hashpw(request.POST['signup_password'].encode(), bcrypt.gensalt())
        city = City.objects.get(id = int(request.POST['city']))
        new_user = User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],username=request.POST['signup_username'],birthday=request.POST['birthday'],gender="male",interests="Please enter interests",email=request.POST['signup_email'],password=hashed, city = city)
        request.session['logged_in_user'] = new_user.id
        return redirect('/success')

def user_info(request):
    user = User.objects.get(id=request.session['logged_in_user'])
    context = {
        'user' : user,
        'cities' : City.objects.all(),
    }
    return render(request, 'nsa_app/user_info.html', context)

def login(request):
    user = User.objects.filter(username=request.POST['login_username'])
    user = user[0]
    if bcrypt.checkpw(request.POST['login_password'].encode(), user.password.encode()):
        request.session['logged_in_user'] = user.id
        return redirect('/events_feed/'+str(user.city.id))

def edit(request, city_id):
    user = User.objects.get(id = request.session['logged_in_user'])
    user.first_name = request.POST['edit_first_name']
    user.last_name = request.POST['edit_last_name']
    user.username = request.POST['edit_username']
    city = City.objects.get(id = int(request.POST['city']))
    user.city = city
    user.interests = request.POST['edit_interests']
    user.email = request.POST['edit_email']
    form = request.FILES['edit_photo']
    user.photo = form
    user.save()
    return redirect('/events_feed/'+ str(user.city.id))

def events_feed(request, city_id):
    user = User.objects.get(id=request.session['logged_in_user'])
    context = {
        'user' : user,
        'city' : City.objects.get(id = city_id),
        'cities' : City.objects.all(),
        'events' : Event.objects.filter(city = City.objects.get(id = city_id)).order_by('-when'),
        'p' : City.objects.first()
    }
    return render(request, 'nsa_app/events_feed.html', context)

def filter_city(request, city_id):
    return redirect('/events_feed/'+str(city_id))

def apply(request):
    user = User.objects.get(id = request.session['logged_in_user'])
    event = Event.objects.get(id = request.POST['event'])
    user.events.add(event)
    print(event.title)
    print (event.users.all())
    return redirect('/events_feed/'+str(event.city.id))

def profile(request, other_user_id):
    user = User.objects.get(id=request.session['logged_in_user'])
    context = {
        'user' : user,
        'events' : Event.objects.filter(admin=other_user_id).order_by('-when'),
        'cities' : City.objects.all(),
        'otheruser' : User.objects.get(id = other_user_id)
    }
    return render(request, 'nsa_app/profile.html', context)

def post_an_event(request, city_id):
    user = User.objects.get(id=request.session['logged_in_user'])
    context = {
        'user' : user,
        'city' : City.objects.get(id = city_id),
        'cities' : City.objects.all(),
        'events' : Event.objects.filter(city = City.objects.get(id = city_id)).order_by('-when'),
        'p' : City.objects.first()
    }
    return render(request, 'nsa_app/post_event.html', context)

def post_event(request):
    title = request.POST['title']
    description = request.POST['description']
    when = request.POST['when']
    location = request.POST['location']
    nsa = request.POST['nsa']
    admin = User.objects.get(id=request.session['logged_in_user'])
    city = City.objects.get(id=request.POST['city'])
    new = Event.objects.create(title = title, description = description,when = when,location = location,nsa = nsa, admin = admin, city = city)
    photo = request.FILES['edit_photo']
    new.photo = photo
    new.save()
    return redirect('/events_feed/'+str(city.id))

def edit_events(request):
    user = User.objects.get(id = request.session['logged_in_user'])
    events = Event.objects.filter(admin=user)
    context = {
        'user' : user,
        'events' : events,
    }
    return render(request, 'nsa_app/edit_events.html', context)

def apply_event_changes(request):
    event = Event.objects.get(id = request.POST['event'])
    event.location = request.POST['location']
    event.description = request.POST['description']
    event.nsa = request.POST['nsa']
    event.save()
    print(event.description)
    # form = request.FILES['edit_photo']
    # event.photo = form
    # print(event.photo)
    return redirect('/edit_events')

def user_messages(request):
    context = {
        'user' : User.objects.get(id=request.session['logged_in_user']),
        'allusers' : User.objects.all(),
    }
    return render(request, 'nsa_app/user_messages.html', context)

def send_message(request):
    print(request.POST['sent'])
    print(request.POST['receiver'])
    return redirect('/user_messages')

def logout(request):
    request.session.clear()
    return redirect('/')
