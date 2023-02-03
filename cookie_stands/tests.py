from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import CookieStand


class CookieStandsTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass"
        )

        self.cookie_stand = CookieStand.objects.create(
            location="Austin",
            owner=self.user,
            description="Texas location",
            hourly_sales=[23],
            minimum_customers_per_hour=3,
            maximum_customers_per_hour=7,
            average_cookies_per_sale=9,
        )

    def test_string_representation(self):
        self.assertEqual(str(self.cookie_stand), "Austin")

    def test_cookie_stand_content(self):
        self.assertEqual(f"{self.cookie_stand.location}", "Austin")
        self.assertEqual(f"{self.cookie_stand.owner}", "tester")
        self.assertEqual(self.cookie_stand.description, "Texas location")

    def test_cookie_stand_list_view(self):
        response = self.client.get(reverse("cookie_stand_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Austin")
        self.assertTemplateUsed(response, "cookie_stand_list.html")

    def test_cookie_stand_detail_view(self):
        response = self.client.get(reverse("cookie_stand_detail", args="1"))
        no_response = self.client.get("/1/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Owner: tester")
        self.assertTemplateUsed(response, "cookie_stand_detail.html")

    def test_cookie_stand_create_view(self):
        response = self.client.post(
            reverse("cookie_stand_create"),
            {
                "location": "Dallas",
                "owner": self.user.id,
                "description": "Dallas Location",
                "hourly_sales": [24],
                "minimum_customers_per_hour": 4,
                "maximum_customers_per_hour": 8,
                "average_cookies_per_sale": 10,
            }, follow=True
        )

        self.assertRedirects(response, reverse("cookie_stand_detail", args="2"))
        self.assertContains(response, "Dallas")

    def test_cookie_stand_update_view_redirect(self):
        response = self.client.post(
            reverse("cookie_stand_update", args="1"),
            {
                "location": "Chicago",
                "owner": self.user.id,
                "description": "Chicago Location",
                "hourly_sales": [25],
                "minimum_customers_per_hour": 5,
                "maximum_customers_per_hour": 9,
                "average_cookies_per_sale": 11,
            }
        )

        self.assertRedirects(response, reverse("cookie_stand_detail", args="1"), target_status_code=200)

    def test_cookie_stand_update_bad_url(self):
        response = self.client.post(
            reverse("cookie_stand_update", args="1"),
            {
                "location": "Chicago",
                "owner": self.user.id,
                "description": "Chicago Location",
                "hourly_sales": [25],
                "minimum_customers_per_hour": 5,
                "maximum_customers_per_hour": 9,
                "average_cookies_per_sale": 11,
            }
        )

        self.assertEqual(response.status_code, 200)

    def test_cookie_stand_delete_view(self):
        response = self.client.get(reverse("cookie_stand_delete", args="1"))
        self.assertEqual(response.status_code, 200)

    # you can also tests models directly
    def test_model(self):
        cookie_stand = CookieStand.objects.create(location="Austin", owner=self.user)
        self.assertEqual(cookie_stand.location, "Austin")
