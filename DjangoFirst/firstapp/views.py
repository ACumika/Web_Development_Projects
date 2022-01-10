from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .models import Person
from .forms import UserForm

# Create your views here.

# получение данных из бд
def index(request):
    people = Person.objects.all()
    return render(request, "index.html", {"people": people})

# сохранение данных в бд
def create(request):
    if request.method == "POST":
        tom = Person()
        tom.name = request.POST.get("name")
        tom.age = request.POST.get("age")
        tom.save()
    return HttpResponseRedirect("/")


# изменение данных в бд
def edit(request, id):
    try:
        person = Person.objects.get(id=id)

        if request.method == "POST":
            person.name = request.POST.get("name")
            person.age = request.POST.get("age")
            person.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"person": person})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


# удаление данных из бд
def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

#def index(request):
#    header = "Personal Data"  # обычная переменная
#    langs = ["English", "German", "Spanish"]  # массив
#    user = {"name": "Tom", "age": 23}  # словарь
#    addr = ("Абрикосовая", 23, 45)  # кортеж
#    data = {"header": header, "langs": langs, "user": user, "address": addr}
#    return render(request, "index.html", context=data)

#def index(request):
#    if request.method == "POST":
#        #name = request.POST.get("name")
#        #return HttpResponse("<h2>Hello, {0}</h2>".format(name))
#        userform = UserForm(request.POST)
#        if userform.is_valid():
#            name = userform.cleaned_data["name"]
#            return HttpResponse("<h2>Hello, {0}</h2>".format(name))
        #else:
        #    return HttpResponse("Ivalid data")
#        return render(request, "index.html", {"form": userform})
#    else:
#        userform = UserForm()
#        return render(request, "index.html", {"form": userform})

def about(request):
    return HttpResponse("<h2>About</h2>")

def contact(request):
    return HttpResponseRedirect("/about")

def details(request):
    return HttpResponsePermanentRedirect("/")

def users(request, id, name):
    output = "<h2>User</h2><h3>id: {0} name: {1}</h3>".format(id, name)
    return HttpResponse(output)
def products(request, productid=2):
    output = '<h2>Product # {0}</h2>'.format(productid)
    return HttpResponse(output)

#def m304(request):
#    return HttpResponseNotModified()


#def m400(request):
#    return HttpResponseBadRequest("<h2>Bad Request</h2>")


#def m403(request):
#    return HttpResponseForbidden("<h2>Forbidden</h2>")


#def m404(request):
#    return HttpResponseNotFound("<h2>Not Found</h2>")


#def m405(request):
#    return HttpResponseNotAllowed("<h2>Method is not allowed</h2>")


#def m410(request):
#    return HttpResponseGone("<h2>Content is no longer here</h2>")


#def m500(request):
#    return HttpResponseServerError("<h2>Something is wrong</h2>")