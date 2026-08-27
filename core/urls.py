from django.urls import path
from . import views


urlpatterns = [

    # Home Page
    path(
        '',
        views.home,
        name='home'
    ),

    # Services Page
    path(
        'services/',
        views.services,
        name='services'
    ),

    # Service Details Page
    path(
        'services/<int:service_id>/',
        views.service_detail,
        name='service_detail'
    ),

    # Courses Page
    path(
        'courses/',
        views.courses,
        name='courses'
    ),

    # Course Details Page
    path(
        'courses/<int:course_id>/',
        views.course_detail,
        name='course_detail'
    ),

    # Contact Page
    path(
        'contact/',
        views.contact,
        name='contact'
    ),
]