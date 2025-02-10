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

app_name = 'contacts'

urlpatterns = [
    path('new', views.new_contact, name='new_contact'),
    path('<int:pk>', views.contact_details.as_view(), name='view_contact'),
    path('', views.ViewContacts, name='all_contacts'),
    path('update/<int:pk>', views.update_contact.as_view(), name='update_contact'),
    path('delete/<int:pk>', views.delete_contact.as_view(), name='delete_contact'),
    path('search', views.getActors, name='search'),
    path('filtered', views.filterContacts, name='filter'),
    path('bysex', views.filterBySex, name='filter_sex'),
    path('byjob', views.filterByJob, name='filter_job'),
    path('bynat', views.filterByNationality, name='filter_nationality')

]