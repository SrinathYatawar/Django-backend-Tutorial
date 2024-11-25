from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from .serializers import CreatorSerializer, questionSerializer, AuthSerializer

from .models import Creator, Question

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,AllowAny

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class CustomToken(APIView):
    '''
     APi view for the authentication token we are generated.
    '''
    permission_classes = [AllowAny]
    
    
    # Define the request body schema for Swagger
    auth_request_body = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['username', 'password'],
        properties={
            'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username of the user'),
            'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password of the user'),
        },
    )

    # Define the response schema
    auth_response = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'refresh': openapi.Schema(type=openapi.TYPE_STRING, description='Refresh token'),
            'access': openapi.Schema(type=openapi.TYPE_STRING, description='Access token'),
            'error': openapi.Schema(type=openapi.TYPE_STRING, description='Error message'),
        },
    )

    @swagger_auto_schema(
        request_body=auth_request_body,  # Define the expected request body
        responses={
            200: openapi.Response('Successful authentication', auth_response),
            400: openapi.Response('Bad Request', openapi.Schema(type=openapi.TYPE_OBJECT, properties={'error': openapi.Schema(type=openapi.TYPE_STRING)})),
            401: openapi.Response('Unauthorized', openapi.Schema(type=openapi.TYPE_OBJECT, properties={'error': openapi.Schema(type=openapi.TYPE_STRING)})),
        }
    )
    
    
    def post(self, request):
        
      serialized_data = AuthSerializer(data=request.data)
      
      if serialized_data.is_valid():
          username = serialized_data.validated_data['username']
          password = serialized_data.validated_data['password']
          
          user = authenticate(username = username,password = password)
          
          if user is None:
              return Response(
                  {
                      "error":"the user is invalid",
                      
                  },
                  status=status.HTTP_401_UNAUTHORIZED,
              )
        
          refresh = RefreshToken.for_user(user)
        
          return Response(
             {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                },
                status=status.HTTP_200_OK,   
        )
      
      return Response(status=status.HTTP_400_BAD_REQUEST)    
        
        


class CreatorListView(ListAPIView):
    queryset = Creator.objects.all()
    serializer_class = CreatorSerializer
    permission_classes  = [IsAuthenticatedOrReadOnly,IsAuthenticated]


class CreatorCreateView(CreateAPIView):
    queryset = Creator.objects.all()
    serializer_class = CreatorSerializer
    permission_classes  = [IsAuthenticatedOrReadOnly,IsAuthenticated]
    
    

class CreatorRetriveView(RetrieveAPIView):
    queryset = Creator.objects.all()
    serializer_class = CreatorSerializer
    lookup_field = 'pk'
    permission_classes  = [IsAuthenticatedOrReadOnly,IsAuthenticated]
    
    
class questionCreateView(CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = questionSerializer   
    permission_classes  = [IsAuthenticatedOrReadOnly,IsAuthenticated] 
    
    
    
    

class questionRetriveView(RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = questionSerializer
    lookup_field = 'pk'    
    permission_classes  = [IsAuthenticatedOrReadOnly,IsAuthenticated]




class questionListView(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = questionSerializer
    permission_classes  = [IsAuthenticatedOrReadOnly,IsAuthenticated]