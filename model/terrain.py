class Terrain:
    """Represente un type de terrain de circuit"""


    def __init__(self, name, color):
        self.name = name
        self.color = color


class Road(Terrain):
    """Represente la route."""

    def __init__(self):
        Terrain.__init__(self, "road", (80, 80, 80))


class Grass(Terrain):
    """Represente l'herbe."""

    def __init__(self):
        Terrain.__init__(self, "grass", (89, 147, 70))


class Dirt(Terrain):
    """Represente la terre."""

    def __init__(self):
        Terrain.__init__(self, "dirt", (164, 119, 77))


class Ice(Terrain):
    """Represente la glace."""

    def __init__(self):
        Terrain.__init__(self, "ice", (165, 220, 232))


class Void(Terrain):
    """Represente le vide."""

    def __init__(self):
        Terrain.__init__(self, "void", (25, 25, 35))