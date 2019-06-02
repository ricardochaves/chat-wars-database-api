import datetime
from typing import List
from typing import Optional

from database.models import AuDigest
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


def consumer(digests: List[dict]) -> List[AuDigest]:

    result: List[AuDigest] = []

    for d in digests:

        defaults = {  # type: ignore
            "lot_id": int(d["lotId"]),
            "item": get_item(d["itemName"], d.get("stats")),
            "item_bonus": extract_bonus(d["itemName"]),
            "seller": get_player(d["sellerName"]),
            "quality": get_quality(d.get("quality")),  # type: ignore
            "seller_castle": d["sellerCastle"],
            "condition": get_condition(d.get("condition")),  # type: ignore
            "end_at": _build_date(d["endAt"]),
            "started_at": _build_date(d["startedAt"]),
            "buyer_castle": d.get("buyerCastle"),
            "status": get_status(d.get("status")),  # type: ignore
            "finished_at": _build_date(d.get("finishedAt")),
            "buyer": get_player(d.get("buyerName")),  # type: ignore
            "prince": d["price"],
        }

        au_digest, created = AuDigest.objects.update_or_create(lot_id=int(d["lotId"]), defaults=defaults)
        result.append(au_digest)

    return result
