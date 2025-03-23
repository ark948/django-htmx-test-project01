import django_filters
from contacts.models import Contact


class ContactFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name='name',
        lookup_expr='icontains'
    )
    class Meta:
        model = Contact
        fields = ['email']