from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view()
def welcome(request):
    return Response(f"Welcome to SafeWallet")


def greeting(request, name):
    return render(request,'hello.html',{'name':name})