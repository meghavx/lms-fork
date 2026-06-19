from django.contrib import admin
from .models import User, Student, Parent, RegistrationRequest


class UserAdmin(admin.ModelAdmin):
    list_display = [
        "get_full_name",
        "username",
        "email",
        "is_active",
        "is_student",
        "is_lecturer",
        "is_parent",
        "is_staff",
    ]
    search_fields = [
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "is_lecturer",
        "is_parent",
        "is_staff",
    ]

    class Meta:
        managed = True
        verbose_name = "User"
        verbose_name_plural = "Users"


admin.site.register(User, UserAdmin)
admin.site.register(Student)
admin.site.register(Parent)

class RegistrationRequestAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "email",
        "role",
        "status",
        "email_verified",
        "created_at",
    )

    list_filter = (
        "role",
        "status",
        "email_verified",
    )

    search_fields = (
        "first_name",
        "last_name",
        "email",
    )

admin.site.register(
    RegistrationRequest,
    RegistrationRequestAdmin,
)