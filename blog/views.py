from rest_auth.views import LogoutView
from rest_framework import permissions

from blog_api import serializers
from blog_api.models import PostImage


class CustomLogoutView(LogoutView):
    permission_classes = (permissions.IsAuthenticated, )


from rest_framework import mixins, viewsets


class PostImagesViewSet(mixins.CreateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    serializer_class = serializers.PostImageSerializer
    queryset = PostImage.objects.all()