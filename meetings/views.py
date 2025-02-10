import logging
from django.contrib.auth import get_user
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Meeting
from .forms import MeetingForm
from contacts.models import Contact


logger = logging.getLogger(__name__)

# Create your views here.

# GENERIC VIEWS
class new_meeting(generic.CreateView):
    """
    Description: 
    (Incomplete) Creates new meeting for request.user
    """

    model = Meeting
    fields = ['date', 'time', 'title', 'location', 'contact']
    template = ''

    # Overrides form_valid() to set contact.user to request.user
    def form_valid(self, form):
        form.instance.user = get_user(self.request)
        return super().form_valid(form)

class all_meetings(generic.ListView):
    """
    Description: 
    Lists all meetings of request.user
    """

    model = Meeting
    context_object_name = 'all_meetings'
    template_name = 'meetings/webpages/all_meetings.html'

class meeting_details(generic.DetailView):
    """
    Description: 
    Shows details of specified meeting
    """

    model = Meeting
    context_object_name = 'meeting'
    template_name = 'meetings/webpages/meeting_details.html'

class delete_meeting(generic.DeleteView):
    """
    Description: 
    Deletes meeting of request.user
    """

    model = Meeting
    template_name = 'meetings/forms/contact_confirm_delete.html'
    success_url = '/meetings/'


# CUSTOM VIEWS
def create_meeting(request):
    """
    Description: 
    Creates new meeting for the user

    Parameters:
    request
    """
    
    if request.method == 'POST':
        form = MeetingForm(request.POST)

        if form.is_valid:
            meeting = form.save(commit=False)
            # Set meeting user to request.user
            meeting.user = request.user
            meeting.save()
            return redirect(reverse('meetings:all_meetings'))
        else:
            return HttpResponse('<h4> MEETING CREATION FAILED </h4>')

    else:
        logger.error(request.user)
        form = MeetingForm()

        # Restrict contact choices to request.user contacts
        form.fields['contact'].queryset = Contact.objects.filter(user = request.user)

    template = 'meetings/forms/create_meeting.html'

    return render(request, template, {'form': form})

def get_upcoming_meetings(request):
    """
    Description: 
    Gets user's upcoming meetings
    """

    current_date = timezone.localdate()

    upcoming_meetings = Meeting.objects.filter(user = request.user, date__gte = current_date)

    context = {
        'all_meetings': upcoming_meetings
    }

    template = 'meetings/webpages/all_meetings.html'

    return render(request, template, context)

def get_past_meetings(request):
    """
    Description: 
    Gets user's previous meetings
    """

    current_date = timezone.localdate()

    upcoming_meetings = Meeting.objects.filter(user = request.user, date__lt = current_date)

    context = {
        'all_meetings': upcoming_meetings
    }

    template = 'meetings/webpages/all_meetings.html'

    return render(request, template, context)
