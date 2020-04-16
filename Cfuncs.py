def hub(where, *args):
    if where == "Tconv":
        ret = temperature_conversion(*args)
        return verify(ret)
    if where == "Mconv":
        ret = meters_conversion(*args)
        return verify(ret)
    if where == "Wconv":
        ret = weight_conversion(*args)
        return verify(ret)

def verify(ret):
    if ret == "Error":
        return ret
    else:
        return "%0.2f" % ret

def temperature_conversion(value, ubox, bbox):
    if ubox == "Celsius":
        if bbox == "Fahrenheit":
            return from_c_to_f(value)
        elif bbox == "Kelvin":
            return from_c_to_k(value)
        else:
            try:
                return float(value)
            except:
                return "Error"
    elif ubox == "Kelvin":
        if bbox == "Celsius":
            return from_k_to_c(value)
        elif bbox == "Fahrenheit":
            return from_c_to_f(from_k_to_c(value))
        else:
            try:
                return float(value)
            except:
                return "Error"
    elif ubox == "Fahrenheit":
        if bbox == "Celsius":
            return from_f_to_c(value)
        elif bbox == "Kelvin":
            return from_c_to_k(from_f_to_c(value))
        else:
            try:
                return float(value)
            except:
                return "Error"


def from_c_to_f(value):
    try:
        return float(value) * 9 / 5 + 32
    except:
        return "Error"


def from_c_to_k(value):
    try:
        return float(value) + 273.15
    except:
        return "Error"


def from_k_to_c(value):
    try:
        return float(value) - 273.15
    except:
        return "Error"


def from_f_to_c(value):
    try:
        return (float(value) - 32) * 5 / 9
    except:
        return "Error"


def meters_conversion(value, ubox, bbox):
    try:
        ret = float(value)
    except:
        return "Error"

    if ubox == bbox:
        return ret
    elif ubox != "Feet" and ubox != "Inch":
        if bbox != "Feet" and bbox != "Inch":
            return ret * meters_units[ubox] / meters_units[bbox]
        else:
            return ret * meters_units[bbox]
    elif ubox == "Feet":
        if bbox != "Inch":
            return ret / meters_units[ubox] / meters_units[bbox]
        else:
            return ret / meters_units[ubox] * meters_units[bbox]
    elif ubox == "Inch":
        if bbox != "Feet":
            return ret / meters_units[ubox] / meters_units[bbox]
        else:
            return ret / meters_units[ubox] * meters_units[bbox]


def weight_conversion(value, ubox, bbox):
    try:
        ret = float(value)
    except:
        return "Error"
    if ubox == bbox:
        return ret
    elif ubox == "Kilograms":
        return ret * weight_units[bbox]
    else:
        return ret / weight_units[ubox] * weight_units[bbox]

meters_units = {
    'Kilometers': 1000,
    'Hectometres': 100,
    'Decameters': 10,
    'Meters': 1,
    'Decimeters': 0.1,
    'Centimeters': 0.01,
    'Millimeters': 0.001,
    'Inch': 39.37,
    'Feet': 3.28084,
}
weight_units = {
    'Kilograms': 1,
    'Grams': 1000,
    'Pound': 2.2,
    'Ounces': 35.27
}
