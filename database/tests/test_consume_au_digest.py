from django.test import TestCase

from database.consumer_au_digest import consumer


class ConsumerAuDigestTestCase(TestCase):
    def test_consumer_should_update_all_digests_when_a_valid_list_is_given(self):

        data = [
            {
                "lotId": "71499",
                "itemName": "Hunter dagger",
                "sellerName": "E them Up",
                "quality": "Fine",
                "sellerCastle": "🦌",
                "condition": "Reinforced",
                "endAt": "2018-07-15T20:23:38.217Z",
                "startedAt": "2018-07-15T16:20:16.851Z",
                "buyerCastle": "🦌",
                "status": "Active",  # one of Active / Finished / Cancelled
                "finishedAt": "2018-07-15T16:20:16.851Z",  # only for ended auctions
                "buyerName": "Shortspear",  # only for finished auctions
                "price": 9,
                "stats": {"⚔": 4, "🛡": 3},
            },
            {
                "lotId": "71500",
                "itemName": "📗Scroll of Peace",
                "sellerName": "kritik",
                "sellerCastle": "🌑",
                "endAt": "2018-07-16T04:36:15.183Z",
                "startedAt": "2018-07-15T16:34:50.722Z",
                "buyerCastle": "🌑",
                "price": 1,
            },
            {
                "lotId": "71501",
                "itemName": "📘Scroll of Peace",
                "sellerName": "BandYlly",
                "sellerCastle": "🦌",
                "endAt": "2018-07-15T20:36:10.675Z",
                "startedAt": "2018-07-15T16:35:53.257Z",
                "price": 0,
            },
        ]

        result = consumer(data)

        self.assertEqual(len(result), 3, "Should return 3 AuDigest objects")
