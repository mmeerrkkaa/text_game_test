import pytest

from player.Inventory import Inventory

def tests_add_item():
	inventory = Inventory()
	inventory.add_item("Камень")
	assert inventory.get_item("Камень")['count'] == 1

	inventory.add_item("Камень", 2)
	assert inventory.get_item("Камень")['count'] == 3

	inventory.add_item("Камень", 2)
	assert inventory.get_item("Камень")['count'] == 5


def tests_remove_item():
	inventory = Inventory()
	inventory.add_item("Камень", 5)
	inventory.remove_item("Камень", 2)
	assert inventory.get_item("Камень") == {"count": 3}

	inventory.remove_item("Камень", 3)

	with pytest.raises(Exception):
		inventory.get_item("Камень")


def tests_get_item():
	inventory = Inventory()
	inventory.add_item("Камень", 5)
	assert inventory.get_item("Камень") == {"count": 5}


def tests_get_items():
	inventory = Inventory()
	inventory.add_item("Камень", 5)
	assert inventory.get_items() == {"Камень": {"count": 5}}

	inventory.add_item("Камень", 5)
	assert inventory.get_items() == {"Камень": {"count": 10}}

	inventory.add_item("Палка")
	assert inventory.get_items() == {"Камень": {"count": 10}, "Палка": {"count": 1}}


if __name__ == "__main__":
	tests_add_item()
	tests_remove_item()
	tests_get_item()
	tests_get_items()