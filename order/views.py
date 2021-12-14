from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from order.models import Order
from order.serializers import OrderSerializer


class CreateOrderView(CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


# TODO: Обновление заказа
# TODO: список заказов пользователя
