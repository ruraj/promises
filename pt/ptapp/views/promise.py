from rest_framework import serializers, mixins, generics
from ..models import PromiseUser


class PromiseUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PromiseUser
        fields = ('user',)


class PromiseUserList(mixins.ListModelMixin,
                          mixins.CreateModelMixin,
                          generics.GenericAPIView):


    queryset = PromiseUser.objects.all()
    serializer_class = PromiseUserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
