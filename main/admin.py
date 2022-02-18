from django.contrib import admin

from main.models import Message, Ticket


class MessagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'ticket', 'author',)
    list_display_links = ('ticket', 'author',)
    search_fields = ('ticket', 'author',)
    ordering = ('ticket',)


class TicketsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'creator', 'status', 'created_at', 'updated_at')
    list_display_links = ('name', 'creator', 'status')
    search_fields = ('name', 'creator')
    ordering = ('creator',)


admin.site.register(Message, MessagesAdmin)
admin.site.register(Ticket, TicketsAdmin)