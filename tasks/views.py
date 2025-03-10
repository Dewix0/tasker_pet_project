from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.shortcuts import get_object_or_404
from .models import Task
from .serializers import TaskSerializer, UserRegisterSerializer, UserLoginSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes


class TaskListView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        description="Получить список задач для текущего пользователя.",
        responses={200: TaskSerializer(many=True)},
    )
    def get(self, request):
        tasks = Task.objects.filter(User_ID=request.user)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        description="Создать новую задачу для текущего пользователя.",
        request=TaskSerializer,
        responses={201: TaskSerializer},
    )
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(User_ID=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        description="Получить детали задачи по её ID.",
        parameters=[
            OpenApiParameter(
                name="pk",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                description="ID задачи",
            ),
        ],
        responses={200: TaskSerializer},
    )
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk, User_ID=request.user)
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        description="Обновить задачу по её ID.",
        parameters=[
            OpenApiParameter(
                name="pk",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                description="ID задачи",
            ),
        ],
        request=TaskSerializer,
        responses={200: TaskSerializer},
    )
    def put(self, request, pk):
        task = get_object_or_404(Task, pk=pk, User_ID=request.user)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        description="Частично обновить задачу по её ID.",
        parameters=[
            OpenApiParameter(
                name="pk",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                description="ID задачи",
            ),
        ],
        request=TaskSerializer,
        responses={200: TaskSerializer},
    )
    def patch(self, request, pk):
        task = get_object_or_404(Task, pk=pk, User_ID=request.user)
        serializer = TaskSerializer(
            task, data=request.data, partial=True
        )  # partial - значит частичное
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        description="Удалить задачу по её ID.",
        parameters=[
            OpenApiParameter(
                name="pk",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                description="ID задачи",
            ),
        ],
        responses={204: None},
    )
    def delete(self, request, pk):
        task = get_object_or_404(Task, pk=pk, User_ID=request.user)
        task.delete()
        return Response(
            {"message": "Вы удалили задачу, без возможности восстановления"},
            status=status.HTTP_204_NO_CONTENT,
        )


class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserLoginView(APIView):
    @extend_schema(
        description="Аутентификация пользователя и получение токенов.",
        request=UserLoginSerializer,
        responses={
            200: OpenApiTypes.OBJECT,
            401: OpenApiTypes.OBJECT,
        },
    )
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]
            user = authenticate(username=username, password=password)

            if user is not None:
                refresh = RefreshToken.for_user(user)
                return Response(
                    {
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),
                    },
                    status=status.HTTP_200_OK,
                )

            return Response(
                {"detail": "Данные для входа неверны, либо пользователь не найден"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
