from django.urls import path
from .views import ShoppingCart, GetProductById

urlpatterns = [
    path('twee-mf-clone/', ShoppingCart.as_view()),
    path('twee-mf-clone/<str:id>', GetProductById.as_view()),
    # path('cart-items/update', update),
]
