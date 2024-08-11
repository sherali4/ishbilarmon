from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.db.models import Count
from .models import Category, Malumot
def index(request):
    context = {
        'name': 'Django',
        'title': 'Tadbirkorlik statistikasi'
    }
    return render(request, 'mb/index.html', context)
@login_required
def siat(request):
    # soni = Category.objects.annotate(items_count=Count('malumotlar'))
    # for s in soni:
    #     print(s.name, s.items_count)
    context = {
        'name': 'Django',
        'title': 'Siat.stat.uz'
    }
    return render(request, 'mb/siat.html', context)
@login_required
def view_siat(request, siat_id):
    context = {
        'id': siat_id,
        'name': 'Django',
        'title': 'Siat.stat.uz'
    }
    return render(request, 'mb/siat_id.html', context)

@login_required
def view_siat_api(request, siat_api_id):
    context = {
        'id': siat_api_id,
        'name': 'Django',
        'title': 'Siat.stat.uz'
    }
    return render(request, 'mb/siat_api_id.html', context)

@login_required
def view_davr(request, siat_api_id, davr):
    context = {
        'id': siat_api_id,
        'davr': davr,
        'name': 'Django',
        'title': 'Siat.stat.uz'
    }
    return render(request, 'mb/siat_davr.html', context)


@login_required
def about(request):
    return render(request, 'about.html')
@login_required
def services(request):
    return render(request, 'services.html')
@login_required
def contact(request):
    return render(request, 'contact.html')


@login_required
def email_view(request):
    # Your logic here
    return render(request, 'email_template.html')