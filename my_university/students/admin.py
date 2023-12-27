from django.contrib import admin

from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "full_name",
        "email",
        "age",
        "gpa",
        "course_str",
        "faculty",
        "education_form",
    )
    list_filter = (
        "course",
        "faculty",
        "education_form",
    )
    search_fields = (
        "username",
        "name",
        "surname",
        "patronymic",
    )
    readonly_fields = ("full_name",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "password",
                )
            },
        ),
        (
            "Personal info",
            {
                "fields": (
                    "name",
                    "surname",
                    "patronymic",
                    "email",
                    "age",
                    "gpa",
                    "course",
                    "faculty",
                    "education_form",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    filter_horizontal = (
        "groups",
        "user_permissions",
    )
    actions = ["make_active", "make_inactive"]

    def make_active(self, request, queryset):
        queryset.update(is_active=True)

    make_active.short_description = "Mark selected students as active"

    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)

    make_inactive.short_description = "Mark selected students as inactive"
