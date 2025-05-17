from rest_framework import viewsets
from .models import *
from .serializers import *

# Customer Views
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# Agent Views
class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

# Supplier Views
class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

# Buyer Views
class BuyerViewSet(viewsets.ModelViewSet):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer

# Inquiry Views   
class InquiryViewSet(viewsets.ModelViewSet):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer


class StyleViewSet(viewsets.ModelViewSet):
    queryset = Style.objects.all()
    serializer_class = StyleSerializer

class RepeatOfViewSet(viewsets.ModelViewSet):
    queryset = RepeatOf.objects.all()
    serializer_class = RepeatOfSerializer  

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class FabricationViewSet(viewsets.ModelViewSet):
    queryset = Fabrication.objects.all()
    serializer_class = FabricationSerializer

class SizeRangeViewSet(viewsets.ModelViewSet):
    queryset = SizeRange.objects.all()
    serializer_class = SizeRangeSerializer      

class TotalAccessoriesViewSet(viewsets.ModelViewSet):
    queryset = TotalAccessories.objects.all()
    serializer_class = TotalAccessoriesSerializer       