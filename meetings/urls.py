"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views

app_name = 'meetings'

urlpatterns = [
    # path('new/<int:pk>', views.create_meeting, name='new_meeting-pk'),
    path('new', views.create_meeting, name='new_meeting'),
    # path('', views.all_meetings.as_view(), name='all_meetings'),
    path('', views.get_upcoming_meetings, name='all_meetings'),
    path('<int:pk>', views.meeting_details.as_view(), name='meeting_details'),
    path('delete/<int:pk>', views.delete_meeting.as_view(), name='delete_meeting')

]