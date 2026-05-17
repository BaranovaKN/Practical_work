class NPC:
    def __init__(self, name, good):
        self.name = name
        self.good = good

        
class Merchant(NPC):
    def __init__(self, name, good):
        super().__init__(name, good)


npc = Merchant("Торговец", "Паучий глаз")
print(npc.name, npc.good)

