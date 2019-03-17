from faction_assets.faction import Faction

class NpcFaction(Faction):
    def __init__(self, species, name):
        super().__init__(name)
        self.species = species