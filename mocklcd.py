OFF = 0x00

def message(message):
    for line in message.split("\n"):
        print "LCD: %s" % line


def clear():
    pass


def noDisplay():
    print "LCD OFF"


def backlight(color):
    pass
