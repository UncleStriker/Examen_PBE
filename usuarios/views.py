from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer, TopicoSerializer, PostSerializer
from .models import User, Topico, Post


# Create your views here.


def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password'] == request.POST['password-confirm']:
            # register user
            try:
                user = User.objects.create_user(
                    username=request.POST['password'], password=request.POST[['password']])
                user.save()
                return HttpResponse('User create successfully')
            except:
                return HttpResponse('Username already exists')
        return HttpResponse('Password do not match')


def homepage(request):
    return render(request, 'home.html', {

    })


# viewSet de las clases

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TopicoViewSet(viewsets.ModelViewSet):
    queryset = Topico.objects.all()
    serializer_class = TopicoSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# CRUD USUARIO
@api_view(['GET'])
def getUsuarios(request):
    usuarios = User.objects.all()
    serializer = UserSerializer(usuarios, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addUsuarios(request):
    data = request.data
    User = User.objects.create(

        username=data['Username'],
        password=data['password']
    )
    serializer = UserSerializer(User, many=False)
    return Response(serializer.data)


@api_view(['UPDATE'])
def updateUsuarios(request):
    data = request.data
    usuarios = User.objects.get(id=data['id'])
    serializer = UserSerializer(instance=usuarios, data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteUsuarios(request):
    data = request.data
    usuarios = User.objects.filter(id=data['id'])
    usuarios.delete()
    respuesta = {'message': 'Eliminación exitosa'}
    return Response(respuesta, status=status.HTTP_204_NO_CONTENT)


# CRUD TOPICO
@api_view(['GET'])
def getTopico(request):
    topicos = Topico.objects.all()
    serializer = TopicoSerializer(topicos, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def postTopicos(request):
    data = request.data
    topico = Topico.objects.create(
        noticias=data['noticias']
    )
    serializer = TopicoSerializer(topico, many=False)
    return Response(serializer.data)


@api_view(['UPDATE'])
def updateTopicos(request):
    data = request.data
    topicos = Topico.objects.get(id=data['id'])
    serializer = TopicoSerializer(instance=topicos, data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteTopicos(request):
    data = request.data
    topicos = Topico.objects.filter(id=data['id'])
    topicos.delete()
    respuesta = {'message': 'Eliminación exitosa'}
    return Response(respuesta, status=status.HTTP_204_NO_CONTENT)


# CRUD POST


@api_view(['GET'])
def getPost(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addPost(request):
    data = request.data
    post = Post.objects.create(
        title=data['titulo'],
        content=data['contenido']
    )
    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)


@api_view(['UPDATE'])
def updatePost(request):
    data = request.data
    post = Post.objects.get(id=data['id'])
    serializer = PostSerializer(instance=post, data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deletePost(request, id):
    if request.method == 'GET':
        return Response({'error': 'Method not allowed'})
    else:
        post = Post.objects.get(id=id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
