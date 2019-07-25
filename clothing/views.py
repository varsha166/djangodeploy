from django.shortcuts import render
from clothing.models import *
from clothing.serializer import *
from rest_framework import serializers, response, status, renderers
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import list_route
from rest_framework.decorators import action

# Create your views here.

class ProdVset(ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProdSer


    # def highlight(self, request, *args, **kwargs):
    #     queryset = models.objects.all()
    #
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

    # @list_route(renderer_classes=[renderers.StaticHTMLRenderer])


    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #
    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)
    #
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

    # @action(detail=False, methods=['GET'], name='Get Highlight')
    # def highlight(self, request, *args, **kwargs):
    #     queryset = models.Highlight.objects.all()
    #
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

#---------------------------------Final Delete
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # print(instance.__dict__)
        # instance.price=500
        # if instance.active==1:
        instance.active = 0
        instance.save()


        return Response(status=status.HTTP_204_NO_CONTENT)

#--------------------------------Final Get all

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        print(queryset)
        my_list=[]
        for item in queryset:
            if item.active==1:
                my_list.append(item)
                item.__dict__.pop('_state')
                print(item.__dict__)
                print(item.active)


        page = self.paginate_queryset(my_list)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


#
# class SnippetViewSet(ModelViewSet):
#     pass
#
#     @action(detail=False, methods=['GET'], name='Get Highlight')
#     def highlight(self, request, *args, **kwargs):
#         queryset = models.Highlight.objects.all()
#
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)
#

    # --------------------------------Final Get all








class VendVset(ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendSer

    # ---------------------------------Final Delete
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # print(instance.__dict__)
        # instance.price=500
        # if instance.active==1:
        instance.active = 0
        instance.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        print(queryset)
        my_list = []
        for item in queryset:
            if item.active == 1:
                my_list.append(item)
                item.__dict__.pop('_state')
                print(item.__dict__)
                print(item.active)

        page = self.paginate_queryset(my_list)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)







