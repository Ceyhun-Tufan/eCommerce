from rest_framework import serializers
from django.contrib.auth.models import User
from customers.models import Customer


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    phone_number = serializers.CharField(required=False)  # Customer alanı

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'phone_number']

    def create(self, validated_data):
        # Kullanıcı bilgilerini ayıkla
        user_data = {
            'username': validated_data['username'],
            'email': validated_data['email'],
            'password': validated_data['password']
        }
        # Customer bilgilerini ayıkla
        customer_data = {
            'phone_number': validated_data.get('phone_number', ''),
        }

        # Kullanıcı oluştur
        user = User(
            username=user_data['username'],
            email=user_data['email']
        )
        user.set_password(user_data['password'])
        user.save()

        # Customer oluştur
        Customer.objects.create(user=user, **customer_data)

        return user

