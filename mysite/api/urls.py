from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [
    url(r'^get', views.GetPersonInfo, name='get'),

    path('', views.person_list, name='person_list'),
    path('view/<int:pk>', views.PersonView.as_view(), name='person_view'),
    path('new', views.PersonCreate.as_view(), name='person_new'),
    path('edit/<int:pk>', views.PersonUpdate.as_view(), name='person_edit'),
    path('delete/<int:pk>', views.PersonDelete.as_view(), name='person_delete'),
]