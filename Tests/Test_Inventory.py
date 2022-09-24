import pytest

from player.Player import Player

def tests_add_item():
	player = Player("Test")
	player.inventory.add_item("Камень")
	assert player.inventory.get_item("Камень")['count'] == 1

	player.inventory.add_item("Камень", 2)
	assert player.inventory.get_item("Камень")['count'] == 3

	player.inventory.add_item("Камень", 2)
	assert player.inventory.get_item("Камень")['count'] == 5


def tests_remove_item():
	player = Player("Test")
	player.inventory.add_item("Камень", 5)
	player.inventory.remove_item("Камень", 2)
	assert player.inventory.get_item("Камень") == {"count": 3}

	player.inventory.remove_item("Камень", 3)

	with pytest.raises(Exception):
		player.inventory.get_item("Камень")


def tests_get_item():
	player = Player("Test")
	player.inventory.add_item("Камень", 5)
	assert player.inventory.get_item("Камень") == {"count": 5}


def tests_get_items():
	player = Player("Test")
	player.inventory.add_item("Камень", 5)
	assert player.inventory.get_items() == {"Камень": {"count": 5}}

	player.inventory.add_item("Камень", 5)
	assert player.inventory.get_items() == {"Камень": {"count": 10}}

	player.inventory.add_item("Палка")
	assert player.inventory.get_items() == {"Камень": {"count": 10}, "Палка": {"count": 1}}


if __name__ == "__main__":
	tests_add_item()
	tests_remove_item()
	tests_get_item()
	tests_get_items()