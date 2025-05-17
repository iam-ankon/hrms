from django.urls import path, include
from .views import * 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('buyer', BuyerViewSet)
router.register('agent', AgentViewSet)
router.register('supplier', SupplierViewSet)
router.register('customer', CustomerViewSet)
router.register('style', StyleViewSet)
router.register('repeat_of', RepeatOfViewSet)
router.register('item', ItemViewSet)
router.register('fabrication', FabricationViewSet)
router.register('size_range', SizeRangeViewSet)
router.register('total_accessories', TotalAccessoriesViewSet)
router.register('inquiry', InquiryViewSet)


urlpatterns = [
    path('api/', include(router.urls)),

]