class CodingTable(object):
    kStopFrameIndex = 15

    k1 = ( -0.97850, -0.97270, -0.97070, -0.96680, -0.96290, -0.95900,
    -0.95310, -0.94140, -0.93360, -0.92580, -0.91600, -0.90620, -0.89650,
    -0.88280, -0.86910, -0.85350, -0.80420, -0.74058, -0.66019, -0.56116,
    -0.44296, -0.30706, -0.15735, -0.00005, 0.15725, 0.30696, 0.44288,
    0.56109, 0.66013, 0.74054, 0.80416, 0.85350 )

    k2 = ( -0.64000, -0.58999, -0.53500, -0.47507, -0.41039, -0.34129, -0.26830, -0.19209, -0.11350, -0.03345, 0.04702, 0.12690, 0.20515, 0.28087, 0.35325, 0.42163, 0.48553, 0.54464, 0.59878, 0.64796, 0.69227, 0.73190, 0.76714, 0.79828, 0.82567, 0.84965, 0.87057, 0.88875, 0.90451, 0.91813, 0.92988, 0.98830)

    k3 = ( -0.86000, -0.75467, -0.64933, -0.54400, -0.43867, -0.33333, -0.22800, -0.12267, -0.01733, 0.08800, 0.19333, 0.29867, 0.40400, 0.50933, 0.61467, 0.72000)

    k4 = ( -0.64000, -0.53145, -0.42289, -0.31434, -0.20579, -0.09723, 0.01132, 0.11987, 0.22843, 0.33698, 0.44553, 0.55409, 0.66264, 0.77119, 0.87975, 0.98830)

    k5 = ( -0.64000, -0.54933, -0.45867, -0.36800, -0.27733, -0.18667, -0.09600, -0.00533, 0.08533, 0.17600, 0.26667, 0.35733, 0.44800, 0.53867, 0.62933, 0.72000)

    k6 = ( -0.50000, -0.41333, -0.32667, -0.24000, -0.15333, -0.06667, 0.02000, 0.10667, 0.19333, 0.28000, 0.36667, 0.45333, 0.54000, 0.62667, 0.71333, 0.80000)

    k7 = ( -0.60000, -0.50667, -0.41333, -0.32000, -0.22667, -0.13333, -0.04000, 0.05333, 0.14667, 0.24000, 0.33333, 0.42667, 0.52000, 0.61333, 0.70667, 0.80000)

    k8 = ( -0.50000, -0.31429, -0.12857, 0.05714, 0.24286, 0.42857, 0.61429, 0.80000)

    k9 = ( -0.50000, -0.34286, -0.18571, -0.02857, 0.12857, 0.28571, 0.44286, 0.60000)

    k10 = ( -0.40000, -0.25714, -0.11429, 0.02857, 0.17143, 0.31429, 0.45714, 0.60000)

    rms = ( 0.0, 52.0, 87.0, 123.0, 174.0, 246.0, 348.0, 491.0, 694.0, 981.0, 1385.0, 1957.0, 2764.0, 3904.0, 5514.0, 7789.0)

    pitch = ( 0.0, 1.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0, 30.0, 31.0, 32.0, 33.0, 34.0, 35.0, 36.0, 36.0, 38.0, 39.0, 40.0, 41.0, 42.0, 44.0, 46.0, 48.0, 50.0, 52.0, 53.0, 56.0, 58.0, 60.0, 62.0, 65.0, 67.0, 70.0, 72.0, 75.0, 78.0, 80.0, 83.0, 86.0, 89.0, 93.0, 97.0, 100.0, 104.0, 108.0, 113.0, 117.0, 121.0, 126.0, 131.0, 135.0, 140.0, 146.0, 151.0, 157)


    @classmethod
    def kSizeFor(cls, k):
        if k>10:
            raise Exception("RangeError")
        return 1 << cls.bits[k+2]

    @classmethod
    def rmsSize(cls):
        return 1 << cls.bits[0]

    @classmethod
    def pitchSize(cls):
        return 1 << cls.bits[2]

    @classmethod
    def kBinFor(cls, k):
        mapping = { 1:cls.k1, 2:cls.k2, 3:cls.k3, 4:cls.k4, 5:cls.k5, 6:cls.k6, 7:cls.k7, 8:cls.k8, 9:cls.k9, 10:cls.k10}
        return mapping[k]

    @classmethod
    def parameters(cls):
        return [
             'kParameterGain',
             'kParameterRepeat',
             'kParameterPitch',
             'kParameterK1',
             'kParameterK2',
             'kParameterK3',
             'kParameterK4',
             'kParameterK5',
             'kParameterK6',
             'kParameterK7',
             'kParameterK8',
             'kParameterK9',
             'kParameterK10'
              ]

    bits = ( 4, 1, 6, 5, 5, 4, 4, 4, 4, 4, 3, 3, 3)

