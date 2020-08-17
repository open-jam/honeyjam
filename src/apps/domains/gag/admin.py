from django.contrib import admin
from reversion.admin import VersionAdmin

from apps.domains.gag.models import Gag


@admin.register(Gag)
class GagAdmin(VersionAdmin):
    list_display = ('id', 'user', 'gag_type', 'question', 'answer', 'is_active', 'create_time', 'update_time')

    list_filter = ('is_active', 'gag_type',)
    search_fields = ('question',)
    ordering = ('-id',)
    readonly_fields = ('create_time', 'update_time',)

    fieldsets = (
        ('개그 정보', {'fields': ('user', 'gag_type', 'question', 'answer',)}),
        ('노출 정보', {'fields': ('is_active',)}),
        ('날짜정보', {'fields': ('create_time', 'update_time',)}),
    )

    def has_add_permission(self, request):
        return True
