# to use with django-import-export

from import_export import resources, fields

from .models import Contact


class ContactResource(resources.ModelResource):
    class Meta:
        model = Contact
        fields = (
            'name',
            'email',
            'created_at'
        )


