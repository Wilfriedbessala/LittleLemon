from django.test import TestCase
from reservation.models import BookingTable, MenuList

class MenuListTest(TestCase):
    def test_get_item(self):
        item = MenuList.objects.create(title='Pizza', price=10.99, inventory=5)
        itemstr = item.get_item()
        self.assertEqual(itemstr,"Pizza : $10.99 (Inventory: 5)")

# Create your tests here.
