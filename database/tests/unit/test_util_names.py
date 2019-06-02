from django.test import TestCase

from database.models import Item
from database.util import extract_bonus
from database.util import extract_name
from database.util import get_item


class TestUtilItemNameFunctions(TestCase):
    def test_extract_name_remove_update_from_name_when_update_exists(self):
        self.assertEqual(extract_name("⚡️+5 Lion Helmet +8⚔️ +22🛡"), "Lion Helmet +8⚔️ +22🛡")

    def test_extract_name_should_return_same_nam_when_update_dont_exists(self):
        self.assertEqual(extract_name("Ghost Boots +5⚔️ +10🛡"), "Ghost Boots +5⚔️ +10🛡")

    def test_get_item_should_create_new_item_when_new_item_is_passed(self):

        Item.objects.all().delete()
        get_item("⚡️+5 Lion Helmet +8⚔️ +22🛡")

        item = Item.objects.first()
        self.assertIsNotNone(item)
        self.assertEqual(item.name, "Lion Helmet +8⚔️ +22🛡")

    def test_extract_bonus_should_return_a_int_value_when_bonus_exists(self):
        self.assertEqual(extract_bonus("⚡️+5 Lion Helmet +8⚔️ +22🛡"), 5)

    def test_extract_bonus_should_return_none_when_bonus_dont_exists(self):
        self.assertIsNone(extract_bonus("Lion Helmet +8⚔️ +22🛡"))
