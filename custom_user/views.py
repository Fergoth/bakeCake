from sqlite3 import IntegrityError
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import login, logout

from .models import User


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    try:
        phonenumber = request.data.get('phonenumber')
        name = request.data.get('name')

        if not phonenumber or not name:
            return Response(
                {'error': 'Телефон и имя обязательны'},
                status=status.HTTP_400_BAD_REQUEST
            )

        user, created = User.objects.get_or_create(
            phonenumber=phonenumber,
            defaults={
                'name': name
            }
        )
        backend = 'custom_user.authentication.NoPasswordBackend'
        login(request, user, backend=backend)

        return Response({
            'message': 'Пользователь успешно зарегистрирован',
            'user_id': user.id
        }, status=status.HTTP_201_CREATED)

    except IntegrityError:
        return Response(
            {'error': 'Пользователь с таким номером уже существует'},
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request):
    user = request.user
    return Response({
        'name': user.name,
        'phonenumber': user.phonenumber,
        'email': user.email if hasattr(user, 'email') else '',
        'address': user.address if hasattr(user, 'address') else ''
    })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_profile(request):
    user = request.user

    name = request.data.get('name')
    phonenumber = request.data.get('phonenumber')
    email = request.data.get('email')
    address = request.data.get('address')

    if phonenumber and User.objects.exclude(id=user.id).filter(phonenumber=phonenumber).exists():
        return Response(
            {'error': 'Пользователь с таким номером уже существует'},
            status=status.HTTP_400_BAD_REQUEST
        )

    if name:
        user.name = name
    if phonenumber:
        user.phonenumber = phonenumber
    if email:
        user.email = email
    if address:
        user.address = address

    try:
        user.save()
        return Response({
            'message': 'Профиль успешно обновлен',
            'name': user.name,
            'phonenumber': user.phonenumber,
            'email': user.email,
            'address': user.address
        })
    except IntegrityError:
        return Response(
            {'error': 'Пользователь с таким номером уже существует'},
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    logout(request)
    return Response({
        'message': 'Пользователь успешно вышел из системы'
    }, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def check_user_exists(request):
    phonenumber = request.data.get('phonenumber')

    if not phonenumber:
        return Response(
            {'error': 'Телефон обязателен'},
            status=status.HTTP_400_BAD_REQUEST
        )

    exists = User.objects.filter(phonenumber=phonenumber).exists()

    return Response({
        'exists': exists,
        'phonenumber': phonenumber
    }, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    phonenumber = request.data.get('phonenumber')

    if not phonenumber:
        return Response(
            {'error': 'Телефон обязателен'},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        user = User.objects.get(phonenumber=phonenumber)
        backend = 'custom_user.authentication.NoPasswordBackend'
        login(request, user, backend=backend)

        return Response({
            'message': 'Вход выполнен успешно',
            'user_id': user.id
        }, status=status.HTTP_200_OK)

    except User.DoesNotExist:
        return Response(
            {'error': 'Пользователь не найден'},
            status=status.HTTP_404_NOT_FOUND
        )
