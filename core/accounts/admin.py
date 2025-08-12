#django files
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


#your files
from .models import User, ContactInfo, SocialLink



class UserPanelAdmin(UserAdmin):
    list_display = ('username', 'email','is_superuser','is_active')
    list_filter = ('username',)
    search_fields = ('username', 'email')
    ordering = ('username',)
    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        fieldsets = list(fieldsets)
        for i, (title, options) in enumerate(fieldsets):
            if title == "Personal info":
                fields = list(options['fields'])
                if 'phone_number' not in fields:
                    fields.append('phone_number')
                    fieldsets[i] = (title, {'fields': fields})
        return fieldsets

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('phone_number',)}),
    )
admin.site.register(User, UserPanelAdmin)

class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'address', 'description')
admin.site.register(ContactInfo, ContactInfoAdmin)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
admin.site.register(SocialLink, SocialLinkAdmin)