from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
    attack = models.IntegerField(null=True, blank=True, verbose_name="Attack")
    defense = models.IntegerField(null=True, blank=True, verbose_name="Defense")
    mana = models.IntegerField(null=True, blank=True, verbose_name="Mana")

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")

    def __str__(self):
        return self.name


class AuDigest(models.Model):

    ACTIVE = 0
    FINISHED = 1
    CANCELLED = 2
    STATUS_CHOICES = ((ACTIVE, "Active"), (FINISHED, "Finished"), (CANCELLED, "Cancelled"))

    REGULAR = 0
    BROKEN = 1
    REINFORCED = 2
    CONDITION_CHOICES = ((REGULAR, "Regular"), (BROKEN, "Broken"), (REINFORCED, "Reinforced"))

    FINE = 0
    HIGH = 1
    GREAT = 2
    EXCELLENT = 3
    QUALITY_CHOICES = ((FINE, "Fine"), (HIGH, "High"), (GREAT, "Great"), (EXCELLENT, "Excellent"))

    lot_id = models.IntegerField(verbose_name="lotId")

    item = models.ForeignKey(Item, related_name="item", verbose_name="Item", on_delete=models.CASCADE)
    seller = models.ForeignKey(
        Player, null=True, blank=True, related_name="seller", verbose_name="Seller", on_delete=models.CASCADE
    )
    buyer = models.ForeignKey(
        Player, null=True, blank=True, related_name="buyer", verbose_name="Buyer", on_delete=models.CASCADE
    )

    condition = models.IntegerField(null=True, blank=True, choices=CONDITION_CHOICES, verbose_name="Condition")
    status = models.IntegerField(null=True, blank=True, choices=STATUS_CHOICES, verbose_name="Status")
    quality = models.IntegerField(null=True, blank=True, choices=QUALITY_CHOICES, verbose_name="quality")

    end_at = models.DateTimeField(verbose_name="endAt")
    started_at = models.DateTimeField(verbose_name="startedAt")
    finished_at = models.DateTimeField(null=True, blank=True, verbose_name="finishedAt")

    seller_castle = models.CharField(max_length=2, verbose_name="sellerCastle")
    buyer_castle = models.CharField(null=True, blank=True, max_length=2, verbose_name="buyerCastle")
    prince = models.IntegerField(verbose_name="price")
    item_bonus = models.IntegerField(null=True, blank=True, verbose_name="Item Plus Bonus")

    def __str__(self):
        return self.item.name
