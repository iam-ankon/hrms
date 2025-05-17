from rest_framework import serializers
from .models import *

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = "__all__"

class SupplierSerializer(serializers.ModelSerializer):
    agreement_contract_file = serializers.FileField(required=False, allow_null=True)
    agreement_vendor_signing_copy = serializers.FileField(required=False, allow_null=True)

    class Meta:
        model = Supplier
        fields = "__all__"

class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = "__all__"       


class InquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = '__all__'

class StyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Style
        fields = "__all__"

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"
class RepeatOfSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepeatOf
        fields = "__all__"
class FabricationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fabrication
        fields = "__all__"

class SizeRangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizeRange
        fields = "__all__"     


class TotalAccessoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TotalAccessories
        fields = "__all__"           