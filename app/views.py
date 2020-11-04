from django.shortcuts import render
from django.http import Http404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from app.models import Report
from app.serializers import ReportSerializer, ReportGetSerializer

# Create your views here.
class ReportApiView(APIView):

    def post(self, request):
        serializer = ReportSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return Response(ReportSerializer(instance).data)

    def get(self, request):
        if request.GET.get('pk') == None:
            print('im here')
            return Response(ReportSerializer(Report.objects.all(), many=True).data)
        else:
            pk_serializer = ReportGetSerializer(data=request.GET)
            if pk_serializer.is_valid():
                queryset = Report.objects.get(pk=request.GET.get('pk'))
                return Response(ReportSerializer(queryset).data)

            return Response(pk_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        pk_serializer = ReportGetSerializer(data=request.GET)
        if pk_serializer.is_valid():
            instance = Report.objects.get(pk=request.GET.get('pk'))
            serializer = ReportSerializer(instance=instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            instance_update = serializer.save()
            return Response(ReportSerializer(instance_update).data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
