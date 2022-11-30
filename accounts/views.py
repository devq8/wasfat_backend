from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from accounts.serializer import UserCreateSerializer, UserLoginSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = UserLoginSerializer(data= request.data)
        
        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.data
            print('Logged in successfully.')
            return Response(valid_data, status=HTTP_200_OK)
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)