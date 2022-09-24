import pytest

from floors.events.chest_events import ChestEvents


def tests_get_resourses():
	chest = ChestEvents({"Камень": 5})
	assert chest.get_resourses() == {"Камень": 5}

	chest = ChestEvents({"Камень": 5, "Палка": 1})
	assert chest.get_resourses() == {"Камень": 5, "Палка": 1}


def tests_open_chest():
	chest = ChestEvents({"Камень": 5})
	assert chest.open_chest() == {"Камень": 5}
	assert chest.open is True

	chest = ChestEvents({"Камень": 5, "Палка": 1})
	assert chest.open_chest() == {"Камень": 5, "Палка": 1}
	assert chest.open is True


if __name__ == "__main__":
	tests_get_resourses()
	tests_open_chest()
