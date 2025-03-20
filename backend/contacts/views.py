from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.decorators.http import require_http_methods
from django.http.response import JsonResponse, HttpResponse
from django.http.request import HttpRequest


from .forms import ContactForm
from .models import Contact

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



# my own
@login_required
@require_http_methods(['POST'])
def new_contact(request, *args, **kwargs):
    form = ContactForm(request.POST)
    if form.is_valid():
        new_contact = Contact(name=form.cleaned_data['name'], email=form.cleaned_data['email'], user=request.user)
        new_contact.save()
        return HttpResponse("Successfully added.")
    


@login_required
@require_http_methods(['POST'])
def create_contact(request):
    form = ContactForm(request.POST, initial={'user': request.user})
    if form.is_valid():
        contact = form.save(commit=False)
        contact.user = request.user
        contact.save()
        context = {'contact': contact}
        response = render(request, 'partials/contact_row.html', context=context)
        response['HX-Trigger'] = 'success'
        return response
    else:
        response = render(request, 'partials/add_contact_modal.html', {'form': form})
        response['HX-Retarget'] = "#contact_modal"
        response['HX-Reswap'] = 'outerHTML'
        response['HX-Trigger-After-Settle'] = "fail"
        return response
    


class ContacList(ListView):
    template_name = "contacts.html"
    model = Contact
    context_object_name = "contacts"

    def get_queryset(self) -> QuerySet[Any]:
        user = self.request.user
        return user.contacts.all()
    


def custom_htmx_process01(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        message = request.POST['message']
        context = {
            'message': message
        }
        response = render(request, 'partials/show_message.html', context=context)
        response['HX-Trigger'] = 'success'
        return response
    else:
        response = render(request, 'test_page.html', context={})
        return response


def custom_htmx_process02(request: HttpRequest) -> JsonResponse:
    if request.method == "POST":
        message = request.POST['message']
        data = {'message': message}
        resposne = JsonResponse(data)
        resposne['HX-Trigger'] = 'success'
        return resposne
    else:
        resposne = render(request, 'test_page.html', context={})
        return resposne
