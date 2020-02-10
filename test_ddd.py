def test_hello_world():
    assert "A" == "A"


class Factory:
    def __init__(self, map):
        self.map = map

    def deliver(self, warehouse):
        pass

    def get_delivery_time(self):
        return self.map.road.time_travel


class Warehouse:
    def __init__(self, warehouse_id):
        self.id = warehouse_id


class TimeTravel:
    def __init__(self, time):
        self.time = time

    def __eq__(self, other):
        return self.time == other.time


class WorldMap:
    def __init__(self):
        self.road = None

    def add_road(self, road):
        self.road = road


def test_should_calculate_travel_time_between_two_points():
    assert_travel_time_for_one_road(5, 5)
    assert_travel_time_for_one_road(4, 4)


class Road:
    def __init__(self, time_travel):
        self.time_travel = time_travel


def assert_travel_time_for_one_road(road_time_travel, expected_time_travel):
    world_map = WorldMap()
    world_map.add_road(Road(TimeTravel(road_time_travel)))
    factory = Factory(world_map)
    factory.deliver(Warehouse("B"))
    assert factory.get_delivery_time() == TimeTravel(expected_time_travel)
