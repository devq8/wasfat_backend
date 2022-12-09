from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.models import Profile

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'token']

    
    def create(self, validated_data):
        print('Start creating new account process ...')
        print(validated_data)
        username = validated_data['username']
        password = validated_data['password']
        new_user = User(username = username)
        new_user.set_password(password)
        new_user.save()

        #Create profile after creating user account
        Profile.objects.create(user=new_user, image='')


        print('User account created successfully')
        payload = RefreshToken.for_user(new_user)
        payload['username'] = str(username)
        validated_data['token'] = str(payload.access_token)
        print('Token created successfully')
        
        return validated_data
        
        

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only = True)
    token = serializers.CharField(allow_blank = True, read_only = True)

    def validate(self, data):
        print(data)
        my_username = data.get('username')
        my_password = data.get('password')

        try:
            user_obj = User.objects.get(username = my_username)
            profile = Profile.objects.get(user=user_obj)
        except User.DoesNotExist:
            raise serializers.ValidationError('Username does not exist!!')
        if not user_obj.check_password(my_password):
            raise serializers.ValidationError('Incorrect password!')

        payload = RefreshToken.for_user(user_obj)
        payload['username'] = user_obj.username
        token = str(payload.access_token)

        data['username'] = str(user_obj.username)
        data['token'] = token

        return data