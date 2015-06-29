from django.test import TestCase
from django.utils import six

from . import models


class ContributorPageTestCase(TestCase):
    def test_title_from_name(self):
        contributor = models.ContributorPage.objects.create(first_name="Bob", last_name="Smith", depth=1)
        contributor.save()

        self.assertEqual(contributor.title, "Bob Smith")

    def test_str_returns_name_and_email(self):
        contributor = models.ContributorPage(first_name="Bob", last_name="Smith", email="bob@example.com")

        self.assertEqual(str(contributor), "Bob Smith - bob@example.com")

    def test_full_name_returns_first_and_last_name(self):
        contributor = models.ContributorPage(first_name="Bob", last_name="Smith", email="bob@example.com")

        self.assertEqual(contributor.full_name, "Bob Smith")

    def test_last_comma_first_name_returns_last_name_and_first_name(self):
        contributor = models.ContributorPage(first_name="Bob", last_name="Smith", email="bob@example.com")

        self.assertEqual(contributor.last_comma_first_name, "Smith, Bob")


class ContributorListPageTestCase(TestCase):
    fixtures = ["people_test.json", ]

    def test_str_returns_title(self):
        contributor_list = models.ContributorListPage(title="This is the title.")
        self.assertEqual(str(contributor_list), "This is the title.")

    def test_list_of_contributors_contains_all_live_contributors(self):
        contributor_list = models.ContributorListPage.objects.all().first()
        all_live_contributors = models.ContributorPage.objects.live()

        six.assertCountEqual(
            self,
            all_live_contributors,
            contributor_list.contributors
        )

    def test_list_of_contributors_sorted_by_last_name(self):
        contributor_list = models.ContributorListPage.objects.all().first()
        contributors = contributor_list.contributors

        joe = models.ContributorPage.objects.get(slug="joe-sampson")
        beth = models.ContributorPage.objects.get(slug="beth-smith")
        bob = models.ContributorPage.objects.get(slug="bob-smith")
        mary = models.ContributorPage.objects.get(slug="mary-sue")

        self.assertSequenceEqual(contributors, [joe, beth, bob, mary])
