from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers, status
from bangazonapi.models import Category,User,Product


class ProductView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type
        Returns:
            Response -- JSON serialized game type
        """
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
          return Response({'message': 'Product does not exist'}, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def create(self, request):
 
       
        UserId = User.objects.get(pk=request.data["sellerId"])
        catId = Category.objects.get(pk=request.data["categoryId"])

        product = Product.objects.create(
            name=request.data["name"],
            product_image_url=request.data["productImageUrl"],
            description=request.data["description"],
            quantity=request.data["quantity"],
            price=request.data["price"],
            added_on=request.data["addedOn"],
            category_id=catId,
            seller_id = UserId
            
        )
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk):

        product = Product.objects.get(pk=pk)
        product.name = request.data["name"]
        product.product_image_url=request.data["productImageUrl"]
        product.description=request.data["description"]
        product.quantity=request.data["quantity"]
        product.price=request.data["price"]
        product.added_on=request.data["addedOn"]
        product.category_id= Category.objects.get(pk=request.data["categoryId"])
        product.seller_id= User.objects.get(pk=request.data["sellerId"])

        product.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)   
    
    def destroy(self, request, pk):
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class ProductSerializer(serializers.ModelSerializer):
    """JSON serializer for events
    """
    class Meta:
        model = Product
        fields = ('id', 'name', 'product_image_url', 'description','price','added_on', 'category_id', 'seller_id','quantity')
        depth = 1