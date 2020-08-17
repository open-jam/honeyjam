from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):
    actions = []

    def get_actions(self, request):
        actions = super().get_actions(request)

        if 'delete_selected' in actions:
            del actions['delete_selected']

        return actions

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    list_select_related = ()
    list_prefetch_related = ()

    def get_queryset(self, request):
        return super().get_queryset(request).select_related(*self.list_select_related).prefetch_related(*self.list_prefetch_related)

    readonly_fields_when_create = None

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields

        if self.readonly_fields_when_create is None:
            return self.readonly_fields

        return self.readonly_fields_when_create


class BaseTabularInline(admin.TabularInline):
    list_select_related = ()
    list_prefetch_related = ()

    def get_queryset(self, request):
        return super().get_queryset(request).select_related(*self.list_select_related).prefetch_related(*self.list_prefetch_related)

    readonly_fields_when_create = None

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields

        if self.readonly_fields_when_create is None:
            return self.readonly_fields

        return self.readonly_fields_when_create
