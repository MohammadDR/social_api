import django_filters
from .models import Post

class PostFilter(django_filters.FilterSet):
    created_at = django_filters.DateFromToRangeFilter()
    class Meta:
        model = Post
        fields = ['owner','created_at']