import datetime
import json
from typing import Optional

from django.core.management.base import BaseCommand
from django.utils import timezone

from database.consumer_au_digest import consumer
from database.models import AuDigest
from database.models import Item
from database.util import extract_bonus
from database.util import get_condition
from database.util import get_item
from database.util import get_player
from database.util import get_quality
from database.util import get_status


def _build_date(dt: Optional[str]) -> Optional[datetime.datetime]:
    if dt:
        return datetime.datetime.strptime(dt, "%Y-%m-%dT%H:%M:%S.%fZ")

    return None


class Command(BaseCommand):
    help = "Seed database"

    def handle(self, *args, **options):

        with open("./CW2.Auction.json", "r") as json_file:
            for x in json_file:
                d = json.loads(x)

                fdt = d.get("finishedAt")
                if fdt:
                    fdt = fdt["$date"]

                AuDigest.objects.create(
                    lot_id=int(d["lotId"]),
                    item=get_item(d["itemName"], d.get("stats")),
                    item_bonus=extract_bonus(d["itemName"]),
                    seller=get_player(d["sellerName"]),
                    quality=get_quality(d.get("quality")),
                    seller_castle=d["sellerCastle"],
                    condition=get_condition(d.get("condition")),
                    end_at=_build_date(d["endAt"]["$date"]),
                    started_at=_build_date(d["startedAt"]["$date"]),
                    buyer_castle=d.get("buyerCastle"),
                    status=get_status(d.get("status")),
                    finished_at=fdt,
                    buyer=get_player(d.get("buyerName")),
                    prince=d["price"],
                )
