def sim_arrivals(self, distances, p):
    """Simulate end state of the game for given planet.

        distances: List of tuples of objects are going to this planet.
        p: planet for simulation
    """
    history = []
    prev_distance = 0
    history.append((p.owner, p.num_ships, 0))
    for dist_group in distances:
        diff_distance = dist_group[0][1] - prev_distance
        if p.owner != 0:
            p.num_ships += p.growth_rate * diff_distance #next group came
        prev_distance = dist_group[0][1]

        participants = {p.owner:p.num_ships}
        for obj in dist_group:
            if not obj[0] in participants:
                participants[obj[0]] = obj[2]
            else:
                participants[obj[0]] += obj[2]

        winner = (0, 0)
        second = (0, 0)
        for k, v in participants.items():
            if v > second[1]:
                if v > winner[1]:
                    second = winner
                    winner = (k, v)
                else:
                    second = (k, v)

        if winner[1] > second[1]:
            p.num_ships = winner[1] - second[1]
            p.owner = winner[0]
        else:
            p.num_ships = 0
        history.append((p.owner, p.num_ships, dist_group[0][1]))
    return history
