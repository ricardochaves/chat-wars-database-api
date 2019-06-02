from typing import Optional

from database.models import AuDigest
from database.models import Item
from database.models import Player

STATS_MAP = {"⚔": "attack", "💧": "mana", "🛡": "defense"}


def extract_bonus(item_name: str) -> Optional[int]:
    if item_name[0] == "⚡":
        return int(item_name.split(" ")[0][2:])

    return None


def extract_name(item_name: str) -> str:
    if item_name[0] == "⚡":
        return " ".join(str(x) for x in item_name.split(" ")[1:])
    return item_name


def get_item(item_name: str, stats: Optional[dict] = None) -> Item:

    name = extract_name(item_name)

    defaults = {"name": name}
    if stats:
        defaults["attack"] = stats.get("⚔")  # type: ignore
        defaults["defense"] = stats.get("🛡")  # type: ignore
        defaults["mana"] = stats.get("💧")  # type: ignore

    item, created = Item.objects.get_or_create(name=name, defaults=defaults)
    return item


def get_player(player_name: str) -> Optional[Player]:

    if player_name:
        item, created = Player.objects.get_or_create(name=player_name, defaults={"name": player_name})
        return item

    return None


def get_quality(quality_name: str) -> Optional[int]:

    if quality_name:
        values = {"Fine": AuDigest.FINE, "High": AuDigest.FINE, "Great": AuDigest.HIGH, "Excellent": AuDigest.EXCELLENT}

        return values[quality_name]

    return None


def get_status(status_name: str) -> Optional[int]:

    if status_name:
        values = {"Active": AuDigest.ACTIVE, "Finished": AuDigest.FINISHED, "Cancelled": AuDigest.CANCELLED}

        return values[status_name]

    return None


def get_condition(condition_name: str) -> Optional[int]:

    if condition_name:
        values = {"Regular": AuDigest.REGULAR, "Broken": AuDigest.BROKEN, "Reinforced": AuDigest.REINFORCED}

        return values[condition_name]

    return None
