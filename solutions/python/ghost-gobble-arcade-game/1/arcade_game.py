def eat_ghost(power_pellet_active, touching_ghost):
    return power_pellet_active and touching_ghost

def score(touching_power_pellet, touching_dot):
    return touching_power_pellet or touching_dot

def lose(power_pellet_active1, touching_ghost1):
    return not power_pellet_active1 and touching_ghost1

def win(eaten_dots, power_pellet_active2, touching_ghost2):
    return eaten_dots and not lose(power_pellet_active2, touching_ghost2)
    