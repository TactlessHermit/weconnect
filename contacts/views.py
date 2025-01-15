from django.shortcuts import render
from django.views import generic
from .models import Contact

# GENERIC VIEWS
class all_contacts(generic.ListView):
    model = Contact
    context_object_name = 'all_contacts'
    template_name = 'contacts/webpages/all_contacts.html'

class add_contact(generic.CreateView):
    model = Contact
    fields = ['first_name', 'last_name', 'sex', 'nationality',
              'email', 'job', 'experience', 'birthday', 'bio']
    template_name = 'contacts/forms/create_contact.html'

class contact_details(generic.DetailView):
    model = Contact
    context_object_name = 'contact'
    template_name = 'contacts/webpages/contact_details.html'

class update_contact(generic.UpdateView):
    model = Contact
    fields = ['first_name', 'last_name', 'sex', 'nationality',
              'email', 'job', 'experience', 'birthday', 'bio']
    template_name = 'contacts/forms/update_contact.html'

class delete_contact(generic.DeleteView):
    model = Contact
    template_name = 'contacts/forms/contact_confirm_delete.html'
    success_url = '/contacts/'


# CUSTOM VIEWS
def ViewContacts(request):
    # Get all contacts
    contacts = Contact.objects.all()

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
    jobs = Contact.objects.values_list('job', flat=True).distinct()
    job_list = list(jobs)

    return job_list

def getNatFilterOptions():
    nationalities = Contact.objects.values_list('nationality', flat=True).distinct()
    nat_list = list(nationalities)

    return nat_list

def filterContacts(request):

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
        contacts = Contact.objects.filter(job = job_filter, nationality = nat_filter, sex = sex_filter)

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

    if request.method == 'POST':
        gender = request.POST['sex']

        contacts = Contact.objects.filter(sex = gender).values()

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

    if request.method == 'POST':
        job_name = request.POST['job']

        contacts = Contact.objects.filter(job = job_name).values()

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

    if request.method == 'POST':
        nat_name = request.POST['nat']

        contacts = Contact.objects.filter(nationality = nat_name).values()

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