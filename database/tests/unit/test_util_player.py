from django.test import TestCase

from database.models import Player
from database.util import get_player


class TestUtilPlayerFunctions(TestCase):
    def test_get_player_should_create_new_player_when_new_player_is_passed(self):

        Player.objects.all().delete()
        get_player("ricardobchaves")

        player = Player.objects.first()
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "ricardobchaves")
