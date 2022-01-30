from django.views import View
from django.http import JsonResponse
import json

from .models import CartItem
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from .serializer import CarItemSerializer


@method_decorator(csrf_exempt, name='dispatch')
class ShoppingCart(View):
    def post(self, request):
        product_data = getDataFromRequest(request)

        cart_item = CartItem.objects.create(**product_data)

        data = {
            "message": f"New item added to Cart with id: {cart_item.id}"
        }
        return JsonResponse(data, status=201)


@method_decorator(csrf_exempt, name='dispatch')
class GetProductById(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarItemSerializer

    def put(self, request, id):
        product_data = getDataFromRequest(request)
        print(request.body)
        CartItem.objects.filter(id=id).update(**product_data)
        data = {
            "message": f"Item was updated to Cart with id: {id}"
        }

        return JsonResponse(json.dumps(list([""])), status=204, safe=False)

    def get(self, request, id):
        print("here")
        if id == "all":
            return JsonResponse(json.dumps(list(CartItem
                                .objects
                                .values('product_quantity', 'product_name', 'product_price'))),
                                safe=False)
        else:
            return JsonResponse(json.dumps(list(CartItem
                                .objects
                                .filter(id=int(self.kwargs['id']))
                                .values('product_quantity', 'product_name', 'product_price'))),
                                safe=False)

    def delete(self, request, id):
        CartItem.objects.filter(id=id).delete()
        data = {
            "message": f"Item was updated to Cart with id: {id}"
        }
        return JsonResponse(data, status=204, safe=False)



# def put(self, request, idk):
#     update(self, request, id)
#     return JsonResponse(CartItem.objects.all(), status=201)


def getDataFromRequest(request):
    data = json.loads(request.body.decode("utf-8"))
    p_name = data.get('product_name')
    p_price = data.get('product_price')
    p_quantity = data.get('product_quantity')

    product_data = {
        'product_name': p_name,
        'product_price': p_price,
        'product_quantity': p_quantity,
    }
    return product_data

# @api_view(["PUT"])
# def update(request):
#     product_data = getDataFromRequest(request)
#     print(request.body)
#     cart_item = request
#     CartItem.objects.update(**product_data)
#     data = {
#         "message": f"Item was updated to Cart with id: {cart_item}"
#     }
#
#     return JsonResponse(data, status=204)
