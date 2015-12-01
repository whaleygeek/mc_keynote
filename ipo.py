# ipo.py (Input, Process, Output)  26/11/2015  D.J.Whale

mc     = None
prompt = None

def init(presenter):
    global mc, prompt
    mc     = presenter.mc
    prompt = presenter.prompt


def build_input():
    pass
    # TODO build a square box with I inside it


def build_output():
    pass
    # TODO build a square box, with O inside it


def build_process():
    pass
    #NOTE: Need a font builder (5x5)
    # TODO build a square box, with P inside it
    # TODO draw arrow from I to P
    # TODO draw arrow from P to O


def run(presenter)
    init(presenter)

    build_input()

    prompt.wait()
    prompt.say("keyboard...")
    prompt.wait()
    prompt.say("mouse...")
    prompt.wait()
    prompt.say("hardware buttons...")
    prompt.wait()
    prompt.say("minecraft sensing.")
    prompt.wait()

    build_output()

    prompt.wait()
    prompt.say("text screen...")
    prompt.wait()
    prompt.say("hardware LEDs...")
    prompt.wait()
    prompt.say("build inside minecraft.")
    prompt.wait()

    build_process()
    prompt.wait()




    