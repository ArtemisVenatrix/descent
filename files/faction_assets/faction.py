from faction_assets.territory import Territory

class Faction:
    def __init__(self, name):
        self.name = name
        self.territory = Territory()