from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'name': 'Django',
        'title': 'Tadbirkorlik statistikasi'
    }
    return render(request, 'mb/index.html', context)

def siat(request):
    context = {
        'name': 'Django',
        'title': 'Siat.stat.uz'
    }
    return render(request, 'mb/siat.html', context)

def view_siat(request, siat_id):
    context = {
        'id': siat_id,
        'name': 'Django',
        'title': 'Siat.stat.uz'
    }
    return render(request, 'mb/siat_id.html', context)


def view_siat_api(request, siat_api_id):
    context = {
        'id': siat_api_id,
        'name': 'Django',
        'title': 'Siat.stat.uz'
    }
    return render(request, 'mb/siat_api_id.html', context)


def view_davr(request, siat_api_id, davr):
    context = {
        'id': siat_api_id,
        'davr': davr,
        'name': 'Django',
        'title': 'Siat.stat.uz'
    }
    return render(request, 'mb/siat_davr.html', context)



def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')



def email_view(request):
    # Your logic here
    return render(request, 'email_template.html')