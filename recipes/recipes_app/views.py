from django.shortcuts import render
from rest_framework import APIView
from rest_framework.response import Response

# Create your views here.


class HomeView(APIView):

    def get(self, request):
        return Response({'status' : '200'})