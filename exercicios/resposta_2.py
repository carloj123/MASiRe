def generate_events(self) -> list:
    """Generate all the events based on probabilities.

    If the probability of a flood to occur is bigger than the drawn number, an event is created. Except the first
    step which will always have a flood.

    :return list: All the steps containing either a dictionary with the event or a dictionary with a None flood."""

    steps_number: int = self.general_map_variables['steps']
    events = [0] * steps_number

    flood, propagation = self.generate_flood()
    nodes: list = flood.list_of_nodes
    event: dict = {
        'flood': flood,
        'victims': self.generate_victims(nodes),
        'water_samples': self.generate_water_samples(nodes),
        'photos': self.generate_photos(nodes),
        'propagation': propagation
    }

    events[0] = event

    flood_probability: int = self.generate_variables['flood']['probability']
    i: int = 1
    while i < steps_number:
        event: dict = {'flood': None, 'victims': [], 'water_samples': [], 'photos': [], 'propagation': []}

        if random.randint(1, 100) <= flood_probability:
            event['flood'], propagation = self.generate_flood()
            nodes: list = event['flood'].list_of_nodes
            event['victims']: list = self.generate_victims(nodes)
            event['water_samples']: list = self.generate_water_samples(nodes)
            event['photos']: list = self.generate_photos(nodes)
            event['propagation']: list = propagation

        events[i] = event
        i += 1

    return events