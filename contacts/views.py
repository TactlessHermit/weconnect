import logging
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import generic
from .models import Contact
from .forms import ContactForm

# GENERIC VIEWS
class all_contacts(generic.ListView):
    """
    Description: 
    Shows contacts registered by current user (ListView)
    """

    model = Contact
    context_object_name = 'all_contacts'
    template_name = 'contacts/webpages/all_contacts.html'

class add_contact(LoginRequiredMixin, generic.CreateView):
    """
    Description: 
    Allows current user register new contact (CreateView)
    """
    
    model = Contact

    fields = ['first_name', 'last_name', 'sex', 'nationality',
              'email', 'job', 'experience', 'birthday', 'bio']
    
    # Overrides form_valid() to set contact.user to request.user
    def form_valid(self, form):
        form.instance.user = get_user(self.request)
        return super().form_valid(form)

    template_name = 'contacts/forms/create_contact.html'

class contact_details(generic.DetailView):
    """
    Description: 
    Shows details of contact registered by current user (DetailView)
    """

    model = Contact
    context_object_name = 'contact'
    template_name = 'contacts/webpages/contact_details.html'

class update_contact(generic.UpdateView):
    """
    Description: 
    Allows current user update details of a registered contact (UpdateView)
    """

    model = Contact
    fields = ['first_name', 'last_name', 'sex', 'nationality',
              'email', 'job', 'experience', 'birthday', 'bio']
    template_name = 'contacts/forms/update_contact.html'

class delete_contact(generic.DeleteView):
    """
    Description: 
    Allows current user delete a registered contact (DeleteView)
    """

    model = Contact
    template_name = 'contacts/forms/contact_confirm_delete.html'
    success_url = '/contacts/'


# CUSTOM VIEWS
def new_contact(request):
    """
    Description: 
    Registers new contact under current user

    Parameters:
    request
    """

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = get_user(request)
            contact.sex = form.cleaned_data['gender']
            contact.save()
            return redirect(reverse('contacts:all_contacts'))
        else:
            return HttpResponse('<h4> MEETING CREATION FAILED </h4>')

    else:
        form = ContactForm()

    return render(request, 'contacts/forms/create_contact.html', {'form': form})

def ViewContacts(request):
    """
    Description: 
    Shows contacts registered by current user

    Parameters:
    request
    """

    # Get all contacts
    contacts = Contact.objects.filter(user = get_user(request))

    # Get list of jobs and nationalities for filters
    job_list = getJobFilerOptions
    nat_list = getNatFilterOptions

    template_name = 'contacts/webpages/all_contacts.html'

    context = {
        'jobs': job_list,
        'nationality': nat_list,
        'all_contacts': contacts,
        'filtered': False
    }
    return render(request, template_name, context)

def getJobFilerOptions():
    """
    Description: 
    Gets options for job filter drop-down list based on all registered contacts regardless of user

    Parameters:
    request
    """

    jobs = Contact.objects.values_list('job', flat=True).distinct()
    job_list = list(jobs)

    return job_list

def getNatFilterOptions():
    """
    Description: 
    Gets options for nationality filter drop-down list based on all registered contacts regardless of user

    Parameters:
    request
    """

    nationalities = Contact.objects.values_list('nationality', flat=True).distinct()
    nat_list = list(nationalities)

    return nat_list

def filterContacts(request):
    """
    Description: 
    Filters user's contacts by job, nationality, AND sex

    Parameters:
    request
    """

    # Get list of jobs and nationalities for filters
    jobs = Contact.objects.values_list('job', flat=True).distinct()
    job_list = list(jobs)
    nationalities = Contact.objects.values_list('nationality', flat=True).distinct()
    nat_list = list(nationalities)

    if request.method == 'POST': 
        # Query to run filter options
        job_filter = request.POST.get('job')
        nat_filter = request.POST.get('nationality')
        sex_filter = request.POST.get('sex')
        
        # Get filtered list of contacts
        contacts = Contact.objects.filter(job = job_filter, nationality = nat_filter, sex = sex_filter, user = get_user(request))

        # Get filter options
        job_list = getJobFilerOptions
        nat_list = getNatFilterOptions
        
        template_name = 'contacts/webpages/all_contacts.html'

        context = {
            'jobs': job_list,
            'nationality': nat_list,
            'all_contacts': contacts,
            'filtered': True
        }
        return render(request, template_name, context)
    else:
        template_name = 'contacts/forms/filter_contacts.html'

        context = {
            'jobs': job_list,
            'nationality': nat_list
        }
        return render(request, template_name, context)
    
def filterBySex(request):
    """
    Description: 
    Filters user's contacts by sex

    Parameters:
    request
    """

    if request.method == 'POST':
        gender = request.POST['sex']

        contacts = Contact.objects.filter(sex = gender, user = get_user(request)).values()

        # Get list of jobs and nationalities for filters
        job_list = getJobFilerOptions
        nat_list = getNatFilterOptions

        template_name = 'contacts/webpages/all_contacts.html'

        context = {
            'jobs': job_list,
            'nationality': nat_list,
            'all_contacts': contacts,
            'filtered': True
        }
        return render(request, template_name, context)
    
def filterByJob(request):
    """
    Description: 
    Filters user's contacts by job

    Parameters:
    request
    """

    if request.method == 'POST':
        job_name = request.POST['job']

        contacts = Contact.objects.filter(job = job_name, user = get_user(request)).values()

        # Get list of jobs and nationalities for filters
        job_list = getJobFilerOptions
        nat_list = getNatFilterOptions

        template_name = 'contacts/webpages/all_contacts.html'

        context = {
            'jobs': job_list,
            'nationality': nat_list,
            'all_contacts': contacts,
            'filtered': True
        }
        return render(request, template_name, context)
    
def filterByNationality(request):
    """
    Description: 
    Filters user's contacts by nationality

    Parameters:
    request
    """

    if request.method == 'POST':
        nat_name = request.POST['nat']

        contacts = Contact.objects.filter(nationality = nat_name, user = get_user(request)).values()

        # Get list of jobs and nationalities for filters
        job_list = getJobFilerOptions
        nat_list = getNatFilterOptions

        template_name = 'contacts/webpages/all_contacts.html'

        context = {
            'jobs': job_list,
            'nationality': nat_list,
            'all_contacts': contacts,
            'filtered': True
        }
        return render(request, template_name, context)
    
def getActors(request):

    contacts = Contact.objects.filter(job = "Actor").values()

    template_name = 'contacts/webpages/all_contacts.html'

    context = {
        'all_contacts': contacts,
    }
    return render(request, template_name, context)