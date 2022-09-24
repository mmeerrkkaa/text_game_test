import pytest

from player.Player import Player

def tests_add_exp():
	player = Player("Test")
	player.add_exp(100)
	assert player.lvl == 2

	player.add_exp(100)
	assert player.lvl == 2


def tests_add_lvl():
	player = Player("Test")
	player.add_lvl(2)
	assert player.lvl == 3
	assert player.max_exp == 300.0
	assert player.max_health == 120

	player.add_lvl(2)
	assert player.lvl == 5


def tests_remove_lvl():
	player = Player("Test")
	player.add_lvl(5)
	player.remove_lvl(2)
	assert player.lvl == 4

	player.remove_lvl(2)
	assert player.lvl == 2

def tests_add_money():
	player = Player("Test")
	player.add_money(100)
	assert player.money == 100

	player.add_money(100)
	assert player.money == 200

def tests_remove_money():
	player = Player("Test")
	player.add_money(200)
	player.remove_money(100)
	assert player.money == 100

	player.remove_money(100)
	assert player.money == 0

if __name__ == "__main__":
	tests_add_exp()
	tests_add_lvl()
	tests_remove_lvl()
	tests_add_money()
	tests_remove_money()