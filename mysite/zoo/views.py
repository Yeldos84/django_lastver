from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .models import Parent, Child, Icecream, Kiosk
# Create your views here.
def zoo(request):
    return HttpResponse("This is ZOO page")

def parents_create(request):
    p1 = Parent(firts_name='Ivan', last_name='Ivanov', age=45, gender='M')
    p1.save()
    print(Parent.objects.all())
    p1.delete()
    print(Parent.objects.all())
    return HttpResponse ('OK')

def parents_delete(request):
    Parent.objects.all().delete()
    Child.objects.all().delete()
    return HttpResponse('deleted!')

def childs_to_parents(request):

    # p2 = Parent(firts_name='Stas', last_name='Petrov', age=50, gender='M')
    # p2.save()
    # c1 = Child(firts_name='Inna', last_name='Ivanova', age=15, parents=p2)
    # c1.save()
    p = Parent.objects.get(firts_name='Stas')
    c2 = Child()
    c2.firts_name = 'Irina'
    c2.last_name = 'Tes'
    c2.age = 11
    c2.parents = p
    c2.save()
    # p2.Child_set.add(c1)
    return HttpResponse('Good!')