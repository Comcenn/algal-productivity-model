from decimal import Decimal

STATIC_DATA = {
    "topt": Decimal(32.6),
    "tmin": Decimal(5),
    "tmax": Decimal(38.9),
    "umax": Decimal(),
    "iloc": Decimal(),
    "o": Decimal(),
    "iopt": Decimal(275),
    "ea": Decimal(141),
    "es": Decimal(0.4),
    "b": Decimal()
}





def proportional_effect_of_temperature(temperature, static_data):
    """This is circle T; equation 2.5 units: degrees C"""
    tmax = static_data["tmax"]
    tmin = static_data["tmin"]
    topt = static_data["topt"]
    return ((temperature - tmax) - (temperature - tmin)**2) / ((topt - tmin) * ((topt - tmin) * (temperature - topt) * (topt - tmax) * (topt + tmin - 2 * temperature)))


def specific_growth_rate_per_hour(temperature, irradiance, static_data):
    """Equation 2.4"""
    umax = static_data["umax"]
    iloc = static_data["iloc"]
    iopt = static_data["iopt"]
    o = static_data["o"]
    return umax * (iloc / (umax / o ((iloc / iopt) - 1)**2)) * proportional_effect_of_temperature(temperature, static_data)


def linear_scattering_modulus(static_data):
    """equation 2.30"""
    return 




if __name__ == "__main__":
    print(proportional_effect_of_temperature(Decimal(33), STATIC_DATA))
