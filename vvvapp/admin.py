from django.contrib import admin
from .models import AddUser, Ping

class AddUserAdmin(admin.ModelAdmin):
    list_display = ('ip', 'active', 'check', 'os', 'location')
    list_editable = ('check',)
    list_display_links = ('ip',)
    list_filter = ('location', 'active', 'check')
    search_fields = ('location', 'os', 'info')
    ordering = ('-created_at',)
    fieldsets = (
        (None, {
            'fields': ('ip', 'active', 'check', 'location', 'os', 'info')
        }),
        ('Timestamp', {
            'fields': ('created_at',),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('created_at', 'active')

class PingAdmin(admin.ModelAdmin):
    list_display = ('ip', 'created_at')
    search_fields = ('ip',)


# Register the model with the custom admin class
admin.site.register(AddUser, AddUserAdmin)
admin.site.register(Ping, PingAdmin)