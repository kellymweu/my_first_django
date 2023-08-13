from django.http import HttpResponse
from django.template import loader
from .models import Member
# Create your views here.

def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, slug):
    mymember = Member.objects.get(slug=slug)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def main(request, id):
    template = loader.get_template('main.html')
    return HttpResponse(template.render(request))

# def testing(request, id):
#     template = loader.get_template('template.html')
#     context = {
#         'fruits': ['Apple', 'Banana', 'Cherry'],
#     }
#     return HttpResponse(template.render(context, request))

def testing(request):
    template = loader.get_template('template.html')
    context = {
        'firstname': 'Linus',
    }
    return HttpResponse(template.render(context, request))

def testing(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('template.html')
    context = {
        'mymembers': mymembers
    }
    return HttpResponse(template.render(context, request))

def testing(request):
    template = loader.get_template('template.html')
    return HttpResponse(template.render())
    
def testing(request):
    # mydata = Member.objects.all().values()
    # mydata = Member.objects.values_list('firstname')
    mydata = Member.objects.filter(firstname='Emil').values()
    template = loader.get_template('template.html')
    context = {
        'mymembers': mydata
    }
    return HttpResponse(template.render(context, request))