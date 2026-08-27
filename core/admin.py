from django.contrib import admin

from .models import Course, Service, ContactMessage, Statistic


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'level',
        'price',
        'hours',
        'lectures',
        'is_featured',
        'is_active',
    )

    list_filter = (
        'is_featured',
        'is_active',
        'level',
    )

    search_fields = (
        'title',
        'description',
        'level',
    )

    list_editable = (
        'is_featured',
        'is_active',
    )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'icon',
        'is_featured',
        'is_active',
    )

    list_filter = (
        'is_featured',
        'is_active',
    )

    search_fields = (
        'title',
        'description',
    )

    list_editable = (
        'is_featured',
        'is_active',
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'email',
        'subject',
        'created_at',
        'is_read',
    )

    list_filter = (
        'is_read',
        'created_at',
    )

    search_fields = (
        'name',
        'email',
        'subject',
        'message',
    )

    list_editable = (
        'is_read',
    )

    ordering = (
        '-created_at',
    )


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'value',
        'icon',
        'order',
        'is_active',
    )

    list_filter = (
        'is_active',
    )

    search_fields = (
        'title',
        'value',
    )

    list_editable = (
        'value',
        'order',
        'is_active',
    )

    ordering = (
        'order',
    )