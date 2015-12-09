class Character():
    def __init__(self, health = 20, armor = 10):
        self._health = health
        self._armor = armor
        self._isAlive = True

    def sufferDamage(self, damage):
        sufferedDamage = self._health + self._armor - damage

        if sufferedDamage < 1:
            self._isAlive = False

    def heal(self, heal):
        self._health += heal

    def isAlive(self):
        return self._isAlive

    def getHealth(self):
        return self._health

def handleEvents(events):
    list(map(handleEvent, events))

def handleEvent(event):
    eventHandlers[event["type"]](event)

def applyHeal(event):
    event["character"].heal(event["size"])

def applyDamage(event):
    event["character"].sufferDamage(event["size"])

eventHandlers = {
    "damage": applyDamage,
    "heal": applyHeal
}


# def handleEvents(events):
#     eventHandlers = {
#         "damage": applyDamage,
#         "heal": applyHeal
#     }
#
#     list(map(lambda event: eventHandlers[event["type"]](event), events))
#
# def applyHeal(event):
#     event["character"].sufferDamage(event["size"])
#
# def applyDamage(event):
#     event["character"].heal(event["size"])
