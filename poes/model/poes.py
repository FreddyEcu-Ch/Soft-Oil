def Poes(area, h, poro, swi, boi):
    """
    This function calculates the POES of any resevoir.
    Parameters
    ----------
    area: Area of the resevoir in ft2.
    h: Thickness of the formation in ft.
    poro: Rock porosity. Fraction.
    swi: Initial water saturation. Fraction.
    boi: Bubble oil point. rb/stb

    Returns: Poes in stb
    -------

    """
    poes = (7758 * area * poro * h * (1 - swi)) / boi

    return poes