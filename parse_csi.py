import re
from math import sqrt, atan2

if __name__ == "__main__":
    """
    This script file demonstrates how to transform raw CSI out from the ESP32 into CSI-amplitude and CSI-phase.
    """

    FILE_NAME = "data/202208041845_link1.csv"

    f = open(FILE_NAME)

    data = []
    for j, l in enumerate(f.readlines()):
        imaginary = []
        real = []
        amplitudes = []
        phases = []

        # Parse string to create integer list
        try: 
            csi_string = re.findall(r"\[(.*)\]", l)[0]
        except:
            continue
        try:
            csi_raw = [int(x) for x in csi_string.split(" ") if x != '']
        except:
            continue


        # Create list of imaginary and real numbers from CSI
        for i in range(len(csi_raw)):
            if i % 2 == 0:
                imaginary.append(csi_raw[i])
            else:
                real.append(csi_raw[i])

        # Transform imaginary and real into amplitude and phase
        for i in range(int(len(csi_raw) / 2)):
            amplitudes.append(sqrt(imaginary[i] ** 2 + real[i] ** 2))
            phases.append(atan2(imaginary[i], real[i]))
        print(amplitudes)

        # print("-------------------")
        # print("csi_amplitude#{}:".format(j), amplitudes)
        # print("csi_phase#{}:    ".format(j), phases)
        # print("-------------------")