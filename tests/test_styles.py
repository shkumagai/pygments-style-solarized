from pygments.style import Style


def _get_darkstyle():
    from pygments_style_solarized import DarkStyle
    return DarkStyle


def _get_lightstyle():
    from pygments_style_solarized import LightStyle
    return LightStyle


def test_module():
    DarkStyle = _get_darkstyle()
    LightStyle = _get_lightstyle()

    assert issubclass(DarkStyle, Style)
    assert issubclass(LightStyle, Style)


def test_color_pallet():
    from pygments_style_solarized import (
        BASE03,
        BASE02,
        BASE01,
        BASE00,
        BASE0,
        BASE1,
        BASE2,
        BASE3,
        YELLOW,
        ORANGE,
        RED,
        MAGENTA,
        VIOLET,
        BLUE,
        CYAN,
        GREEN,
    )

    assert BASE03 == "#002b36"
    assert BASE02 == "#073642"
    assert BASE01 == "#586e75"
    assert BASE00 == "#657b83"
    assert BASE0 == "#839496"
    assert BASE1 == "#93a1a1"
    assert BASE2 == "#eee8d5"
    assert BASE3 == "#fdf6e3"
    assert YELLOW == "#b58900"
    assert ORANGE == "#cb4b16"
    assert RED == "#dc322f"
    assert MAGENTA == "#d33682"
    assert VIOLET == "#6c71c4"
    assert BLUE == "#268bd2"
    assert CYAN == "#2aa198"
    assert GREEN == "#859900"
