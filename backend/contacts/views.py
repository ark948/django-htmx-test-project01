from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q


from .forms import ContactForm

# Create your views here.


@login_required
def index(request):
    contacts = request.user.contacts.all().order_by('-created_at') # minus means descending
    context = {
        'contacts': contacts,
        'form': ContactForm()
    }
    return render(request, 'contacts.html', context)



@login_required
def search_contacts(request):
    import time
    time.sleep(1) # used to test the loading incdicator
    query = request.GET.get('search', "") # name of the search input field, default to empty if not provided
    contacts = request.user.contacts.filter(
        Q(name__icontains=query) | Q(email__icontains=query)
    )
    return render(request, 'partials/contact_list.html', {"contacts": contacts})