from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers, status
from bangazonapi.models import PaymentType,User, Order 


class OrderView(ViewSet):
  """Bangazon API order view"""
  
  def retrieve(self, request, pk):
    """Handle GET requests for a single order
    
    Returns:
        Response -- JSON serialized order
    """
    try:
        order = Order.objects.get(pk=pk)
        
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    except Order.DoesNotExist as ex:
        return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
      
  def list(self, request):
    """Handle GET requests to get all orders
    
    Returns:
        Response -- JSON serialized list of all orders
    """
    order = Order.objects.all()
    serializer = OrderSerializer(order, many=True)
    return Response(serializer.data, status = status.HTTP_200_OK)

  def create(self, request):
    """Handle POST operations for order
    
    Returns:
        Response -- JSON serialized order instance
    """
    
    customer_id = User.objects.get(pk=request.data["customerId"])
    payment_type = PaymentType.objects.get(pk=request.data["paymentType"])
    
    order = Order.objects.create(
    customer_id=customer_id,
    payment_type=payment_type,
    total=request.data["total"],
    is_completed=request.data["isCompleted"],
    date_placed=request.data["datePlaced"]
    )
    serializer = OrderSerializer(order)
    return Response(serializer.data, status=status.HTTP_201_CREATED) 
    
  def update(self, request, pk):

    order = Order.objects.get(pk=pk)
    order.total=request.data["total"]
    order.is_completed=request.data["isCompleted"]
    customer_id = User.objects.get(pk=request.data["customerId"])
    order.customer_id = customer_id
    payment_type = PaymentType.objects.get(pk=request.data["paymentType"])
    order.payment_type= payment_type


    order.save()

    return Response(None, status=status.HTTP_204_NO_CONTENT)   

  def destroy(self, request, pk):
    order = Order.objects.get(pk=pk)
    order.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)


class OrderSerializer(serializers.ModelSerializer):
    """JSON serializer for events
    """
    class Meta:
        model = Order
        fields = ('id', 'customer_id', 'date_placed', 'payment_type', 'total', 'is_completed')
        depth = 1