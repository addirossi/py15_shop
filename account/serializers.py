from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    name = serializers.CharField(required=False)
    password = serializers.CharField(required=True, min_length=6)
    password_confirmation = serializers.CharField(required=True, min_length=6)

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Адрес почты уже занят')
        return email

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirmation = attrs.pop('password_confirmation')
        if password != password_confirmation:
            raise serializers.ValidationError('Пароли не совпадают')
        return attrs

    def create(self):
        attrs = self.validated_data
        user = User.objects.create_user(**attrs)
        code = user.generate_activation_code()
        user.send_activation_mail(user.email, code)
        return user


class ActivationSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    code = serializers.CharField(min_length=8, max_length=8)

    def validate_email(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Пользователь не зарегистрирован')
        return email

    def validate_code(self, code):
        if not User.objects.filter(activation_code=code).exists():
            raise serializers.ValidationError('Пользователь не зарегистрирован')
        return code

    def validate(self, attrs):
        email = attrs.get('email')
        code = attrs.get('code')
        if not User.objects.filter(email=email,
                                   activation_code=code).exists():
            raise serializers.ValidationError('Пользователь не найден')
        return attrs


class LoginSerializer(serializers.Serializer):
    pass


class ChangePasswordSerializer(serializers.Serializer):
    pass


class ForgotPasswordSerializer(serializers.Serializer):
    pass
