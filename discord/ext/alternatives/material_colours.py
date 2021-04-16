from discord.colour import Colour


MDIO_COLOURS = {
    "400": {
        "red": 0xef534e,
        "pink": 0xec407e,
        "purple": 0xab47bc,
        "deep_purple": 0x7e56c1,
        "indigo": 0x5c6bc0,
        "blue": 0x42a5f5,
        "light_blue": 0x29b6f6,
        "cyan": 0x26c6da,
        "teal": 0x26a69a,
        "green": 0x66bb6a,
        "light_green": 0x9ccc65,
        "lime": 0xd4e157,
        "yellow": 0xffee58,
        "amber": 0xffca28,
        "orange": 0xffa726,
        "deep_orange": 0xff7043,
    }
}

for shade, colours in MDIO_COLOURS.items():
    for name, value in colours.items():
        delegate = lambda cls, value=value: cls(value)
        setattr(Colour, "material_{0}_{1}".format(shade, name), classmethod(delegate))
