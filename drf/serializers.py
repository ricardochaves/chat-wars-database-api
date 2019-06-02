from database.models import AuDigest
from database.models import Item
from database.models import Player
from rest_framework import serializers


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ("name", "attack", "defense", "mana")


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ("name",)


class AuDigestSerializer(serializers.ModelSerializer):
    item = ItemSerializer()
    seller = PlayerSerializer()
    buyer = PlayerSerializer()

    class Meta:
        model = AuDigest
        fields = (
            "lot_id",
            "item",
            "item_bonus",
            "seller",
            "quality",
            "seller_castle",
            "condition",
            "end_at",
            "started_at",
            "buyer_castle",
            "status",
            "finished_at",
            "buyer",
            "prince",
        )
