from django.shortcuts import render,  HttpResponse , redirect
from RealTodo.models import Data , HotelBooking
from .forms import TodoForm 
from .forms import Hotelbooking_form


# Create your views here.
def index(request):
    return HttpResponse("Hello Sufyan")

def tasks(request):
    All_tasks = Data.objects.all()  
    context = {'det' :  All_tasks}
    template = 'RealTodo/tasks.html'
    return render(request ,template , context) 


def tasksall(request , pk):
    task_obj = Data.objects.get(id = pk)
    template_name = 'RealTodo/detail.html'
    context={}
    context['task_id'] = task_obj.id
    context['task_title'] = task_obj.title
    context['task_text'] = task_obj.text
    return render(request , template_name , context)

def Home(request):
    print("=============" , request.POST)
    template =  'RealTodo/Home.html'
    if request.method == 'POST':
        form = TodoForm(request.POST or None)
        print("Form Recieved")
        if form.is_valid():
            form.save()
            All_tasks = Data.objects.all()  
            context = {'det' :  All_tasks}
            template = 'RealTodo/Home.html'
            return render(request ,template , context)
        else:
            print('Form NOT VALIDATED')
            all_items = Data.objects.all
            return render(request, template , {'det': all_items})
    
    else:
        all_items = Data.objects.all
        return render(request, template, {'det': all_items})


def home(request):
    print("=============" , request.POST)
    template =  'RealTodo/HotelBooking.html'
    if request.method == 'POST':
        form = Hotelbooking_form(request.POST or None)
        print("Form Recieved")
        if form.is_valid():
            print('Form is Valid')
            form.save()
            #All_tasks = HotelBooking.objects.all()  
            #context = {'det' :  All_tasks}
            #template = 'RealTodo/HotelBooking.html'
            #return render(request ,template , context)
        else:
            print('Form NOT VALIDATED')
    booking_form = Hotelbooking_form()
    #all_items = HotelBooking.objects.all
   # context =  {'det': all_items , 'form': booking_form}
    context =  { 'form': booking_form}
   
    return render(request, template , context)
    

def AboutUs(request):

    return render(request , 'RealTodo/AboutUs.html')
    
def Details(request):
    template_name = 'RealTodo/Details.html'
    all_items = HotelBooking.objects.all
    context =  {'det': all_items}
    return render(request, template_name , context)
    
def Pricing(request):
    template_name = 'RealTodo/pricing.html'
    return render(request , template_name)
        

def booking_details(request , pk):
    booking_obj = HotelBooking.objects.get(id = pk)
    template_name = 'RealTodo/booking_details.html'
    context={}
    context['task_id'] = booking_obj.id
    context['task_name'] = booking_obj.name
    context['task_booking_details'] = booking_obj.booking_details
    return render(request , template_name , context)
    
