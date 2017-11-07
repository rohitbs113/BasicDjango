from django.conf.urls import url, include

from django.views.generic import ListView, DetailView
from blog.models import MyPost

urlpatterns = [

    url(r'^$', ListView.as_view(queryset=MyPost.objects.all().order_by("-date"), template_name="blog/blog.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model= MyPost, template_name="blog/post.html"))

]
