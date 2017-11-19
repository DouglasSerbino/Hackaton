# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from app.gamificacion.models import User
from app.gamificacion.serializers import UserSerializer

from rest_framework import generics
from rest_framework.response import Response

# Create your views here.
class UserList(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

	def list(self, *args, **kwargs):
		self.object_list = self.filter_queryset(self.get_queryset())
		serializer = self.get_serializer(self.object_list, many = True)
		return Response({ 'Usuarios': serializer.data })

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer