from vaisseau import Vaisseau
from interface import Interface
import core
from asteroid import Asteroid


def setup():
    print("Setup START---------")
    core.fps = 150
    core.memory("xWin", 1920)
    core.memory("yWin", 1080)
    core.WINDOW_SIZE = [core.memory("xWin"), core.memory("yWin")]
    core.memoryCentre = 0

    core.memory("v", Vaisseau())
    core.memory("a", Asteroid())
    core.memory("i", Interface())

    core.memory("listast", [])
    core.memory("nbrast", 200)

    for a in range(0, core.memory("nbrast")):
        core.memory("listast").append(Asteroid(1920, 1080))

    print("Setup END-----------")


def run():
    core.memory("v").bord(core.screen)

    core.cleanScreen()
    for a in core.memory("listast"):
        a.show(core.screen)
        a.deplacement()
        a.bord(core.screen)

    core.memory("v").deplacement(core.getMouseLeftClick())

    core.memory("v").show(core.screen)

    for c in core.memory("listast"):
        core.memory("v").eat(c)

        #   appuyé sur Q pour quitté la partie et affiché votre score:
    if core.getKeyPressList("q"):
        core.memory("i").show(core.screen)
        quit()

    if core.getKeyPressList("r"):
        for a in range(0, core.memory("nbrast")):
            core.memory("listast").append(Asteroid(1920, 1080))


core.main(setup, run)
