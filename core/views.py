from django.shortcuts import render, get_object_or_404

from .models import (
    Course,
    Service,
    ContactMessage,
    Statistic,
)

from .forms import ContactMessageForm


def home(request):

    courses_count = Course.objects.filter(
        is_active=True
    ).count()

    services_count = Service.objects.filter(
        is_active=True
    ).count()

    messages_count = ContactMessage.objects.count()

    featured_courses = Course.objects.filter(
        is_active=True,
        is_featured=True
    )[:3]

    featured_services = Service.objects.filter(
        is_active=True,
        is_featured=True
    )[:3]

    statistics = Statistic.objects.filter(
        is_active=True
    ).order_by('order')

    context = {
        'courses_count': courses_count,
        'services_count': services_count,
        'messages_count': messages_count,
        'featured_courses': featured_courses,
        'featured_services': featured_services,
        'statistics': statistics,
    }

    return render(
        request,
        'home.html',
        context
    )


def services(request):

    services = Service.objects.filter(
        is_active=True
    )

    context = {
        'services': services
    }

    return render(
        request,
        'services.html',
        context
    )


def service_detail(request, service_id):

    service = get_object_or_404(
        Service,
        id=service_id,
        is_active=True
    )

    context = {
        'service': service
    }

    return render(
        request,
        'service_detail.html',
        context
    )


def courses(request):

    courses = Course.objects.filter(
        is_active=True
    )

    context = {
        'courses': courses
    }

    return render(
        request,
        'courses.html',
        context
    )


def contact(request):

    if request.method == 'POST':

        form = ContactMessageForm(request.POST)

        if form.is_valid():

            form.save()

            return render(
                request,
                'contact.html',
                {
                    'form': ContactMessageForm(),
                    'success': True
                }
            )

    else:

        form = ContactMessageForm()

    context = {
        'form': form
    }

    return render(
        request,
        'contact.html',
        context
    )


def course_detail(request, course_id):

    course = get_object_or_404(
        Course,
        id=course_id,
        is_active=True
    )

    context = {
        'course': course
    }

    return render(
        request,
        'course_detail.html',
        context
    )