import math

#####Thermistor Code#####
#Thermistor Circuit Settings
VDD = 5
resistor = 10000
#offset = 7.6
A_CONST = (1.125498266) * (10**-3)
B_CONST = (2.346771694) * (10**-4)
C_CONST = (8.579674698) * (10**-8)

#####Watermark Code########
volt_to_ohm_lookup = {2: "ERROR",
                      1.707: 0,
                      1.704: 1,
                      1.702: 2,
                      1.699: 3,
                      1.697: 4,
                      1.691: 6,
                      1.686: 8,
                      1.676: 12,
                      1.666: 16,
                      1.645: 24,
                      1.625: 32,
                      1.588: 48,
                      1.552: 64,
                      1.485: 96,
                      1.426: 128,
                      1.320: 192,
                      1.230: 256,
                      1.089: 384,
                      0.98: 512,
                      0.828: 768,
                      0.726: 1024,
                      0.596: 1536,
                      0.517: 2048,
                      0.427: 3072,
                      0.377: 4096,
                      0.323: 6144,
                      0.295: 8192,
                      0.265: 12288,
                      0.25: 16384,
                      0.234: 24576,
                      0.230: 28672,
                      0.226: 32768,
                      0.218: 49152,
                      0.214: 65536,
                      0.21: 98304,
                      0.208: 131072,
                      0.206: 196608,
                      0.205: 262144,
                      0.201: 1000000,
                      0.180: "ERROR"}

ohm_to_kpa_lookup = {550: 0,
                     1000: 9,
                     1100: 10,
                     2000: 15,
                     6000: 35,
                     9200: 55,
                     12200: 75,
                     15575: 100,
                     28075: 200}

def convert_to_temperature(millivoltage):
    thermistor_voltage = float(millivoltage)/1000
    thermistor_resistance = (resistor * thermistor_voltage)/(VDD - thermistor_voltage)
    if (thermistor_resistance > 0):
        temperature_kelvin = (A_CONST + (B_CONST * (math.log(thermistor_resistance))) + (C_CONST * ((math.log(thermistor_resistance))**3)))**-1
        temperature_fahrenheit = (((temperature_kelvin - 273.15) * 1.8) + 32) #- offset
        temperature_fahrenheit = round(temperature_fahrenheit,1)
        return round(temperature_fahrenheit,1)
    else:
        return "ERROR"

def convert_to_vwc(volt, temperature):
    volt = (volt/1000)
    result = min(volt_to_ohm_lookup, key=lambda x:abs(x-volt))
    r_raw = volt_to_ohm_lookup[result]
    if (r_raw != "ERROR"):
        r_comp = r_raw * (1 + (0.01 * (temperature - 75)))
        #VWC_lookup = min(ohm_to_kpa_lookup, key=lambda x:abs(x-r_comp))
        #print VWC_lookup
        if ((r_comp>550) and (r_comp<=1000)):
            VWC = (r_comp - 547.53)/53.022
        elif ((r_comp>1000) and (r_comp<=4096)):
            VWC = (r_comp * 0.0052) + 3.8
        elif ((r_comp>4096) and (r_comp<28075)):
            VWC = (r_comp - 1153.8)/137.76
        elif ((r_comp>=28075) and (r_comp<32678)):
            VWC = (r_comp * 0.0086) - 40.712
        else:
            return "RANGE ERROR"
    else:
        VWC = -99
        return "RANGE ERROR"
