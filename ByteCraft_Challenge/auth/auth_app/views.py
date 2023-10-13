from django.shortcuts import render
from .models import customuser, task
from .serializer import TaskSerializer, UserSerializer
from rest_framework import generics, permissions, status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from django.http import JsonResponse
import jwt, datetime
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import authentication_classes, permission_classes


@authentication_classes([])
@permission_classes([])
class register(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_instance = serializer.create(serializer.validated_data)
        return Response(
            UserSerializer(user_instance).data, status=status.HTTP_201_CREATED
        )


@permission_classes([])
@authentication_classes([])
class login(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        userr = customuser.objects.filter(email=email).first()

        if userr is None:
            raise AuthenticationFailed("User not found")

        if not userr.check_password(password):
            raise AuthenticationFailed("Wrong Password")

        refresh = RefreshToken.for_user(userr)
        access_token = str(refresh.access_token)

        response = Response()
        response.set_cookie(key="jwt", value=access_token, httponly=True)
        response.data = {"jwt": access_token}

        return response


class userv(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response(UserSerializer(request.user).data)


class lout(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie(key="jwt")
        response.data = {"message": "success"}
        return response


class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return task.objects.all()
        return task.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return task.objects.all()
        return task.objects.filter(user=user)


class taskDeleteView(generics.DestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return task.objects.all()
        return task.objects.filter(user=user)


class TaskListView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return task.objects.all()
        return task.objects.filter(user=user)
