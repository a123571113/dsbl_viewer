TEAMS = ['ASVW', 'BYC (BA)', 'BYC (BE)', 'BYCÜ', 'DYC', 'FSC', 'JSC', 'KYC (BW)', 'KYC (SH)', 'MSC', 'MYC', 'NRV', 'RSN',
         'SMCÜ', 'SV03', 'SVI', 'VSaW', 'WYC']

data = [
        # 1 Berlin
        """Flight Race Boat 1 Boat 2 Boat 3 Boat 4 Boat 5 Boat 6
1 BYC(BA) RSN SMCÜ WYC KYC(SH) DYC
2 BYCÜ VSaW SVI NRV JSC KYC(BW)
3 SV03 MSC BYC(BE) MYC FSC ASVW
4 NRV BYC(BA) BYC(BE) MYC KYC(BW) RSN
5 KYC(SH) JSC FSC DYC SVI SV03
6 MSC WYC ASVW BYCÜ SMCÜ VSaW
7 MSC DYC SV03 BYCÜ RSN NRV
8 ASVW SMCÜ JSC KYC(BW) BYC(BE) KYC(SH)
9 FSC MYC VSaW SVI BYC(BA) WYC
10 JSC MYC NRV ASVW DYC WYC
11 RSN KYC(BW) MSC KYC(SH) VSaW FSC
12 SVI BYCÜ BYC(BA) SMCÜ SV03 BYC(BE)
13 SVI KYC(SH) WYC MSC NRV BYC(BE)
14 VSaW SV03 MYC JSC RSN SMCÜ
15 KYC(BW) ASVW DYC FSC BYCÜ BYC(BA)
16 SMCÜ NRV KYC(SH) FSC BYCÜ MYC
17 DYC BYC(BE) RSN VSaW ASVW SVI
18 JSC BYC(BA) KYC(BW) SV03 WYC MSC
19 KYC(SH) BYC(BA) NRV SV03 VSaW ASVW
20 MYC SVI DYC KYC(BW) MSC SMCÜ
21 WYC FSC BYCÜ BYC(BE) JSC RSN
22 SMCÜ FSC VSaW BYC(BE) NRV DYC
23 SV03 BYCÜ WYC KYC(SH) MYC KYC(BW)
24 BYC(BA) MSC SVI RSN ASVW JSC
25 BYC(BE) DYC KYC(SH) VSaW MYC BYCÜ
26 NRV SMCÜ JSC BYC(BA) MSC FSC
27 ASVW RSN KYC(BW) WYC SVI SV03
28 DYC BYC(BE) MYC JSC BYC(BA) MSC
29 KYC(BW) NRV SV03 SMCÜ WYC VSaW
30 BYCÜ SVI RSN ASVW FSC KYC(SH)
31 VSaW WYC RSN MSC BYC(BE) KYC(SH)
32 FSC JSC ASVW DYC SV03 NRV
33 MYC SMCÜ BYCÜ BYC(BA) KYC(BW) SVI
34 WYC SV03 FSC DYC KYC(BW) BYC(BE)
35 RSN ASVW SVI NRV SMCÜ MYC
36 BYCÜ VSaW BYC(BA) MSC KYC(SH) JSC
37 FSC VSaW BYC(BA) RSN MYC SV03
38 MSC ASVW SMCÜ WYC DYC BYCÜ
39 BYC(BE) KYC(BW) NRV SVI KYC(SH) JSC
40 WYC DYC NRV SVI VSaW BYC(BA)
41 KYC(BW) KYC(SH) MSC FSC ASVW MYC
42 BYC(BE) JSC SV03 BYCÜ SMCÜ RSN
43 VSaW JSC WYC MYC FSC SVI
44 SV03 BYC(BE) KYC(SH) ASVW BYC(BA) SMCÜ
45 DYC BYCÜ MSC NRV RSN KYC(BW)
46 SMCÜ SVI MSC NRV SV03 FSC
47 KYC(SH) MYC JSC RSN WYC DYC
48 ASVW KYC(BW) BYCÜ VSaW BYC(BE) BYC(BA)
    """,
    # 2 - Warnemünde
    """Flight Race Boat 1 Boat 2 Boat 3 Boat 4 Boat 5 Boat 6
        1 KYC(SH) BYCÜ SV03 NRV MSC SVI
        2 VSaW FSC DYC BYC(BE) WYC JSC
        3 KYC(BW) RSN MYC SMCÜ BYC(BA) ASVW
        4 KYC(BW) SV03 MYC JSC SVI BYC(BE)
        5 RSN BYC(BA) MSC FSC DYC NRV
        6 ASVW KYC(SH) SMCÜ WYC BYCÜ VSaW
        7 SV03 KYC(SH) FSC BYC(BA) MYC VSaW
        8 SVI MSC BYC(BE) RSN ASVW WYC
        9 SMCÜ JSC NRV DYC KYC(BW) BYCÜ
        10 BYC(BE) ASVW NRV KYC(SH) KYC(BW) FSC
        11 BYCÜ DYC RSN SVI VSaW MYC
        12 WYC SMCÜ BYC(BA) MSC JSC SV03
        13 BYC(BE) SMCÜ VSaW RSN NRV SV03
        14 FSC MYC BYCÜ ASVW JSC MSC
        15 BYC(BA) KYC(BW) SVI WYC KYC(SH) DYC
        16 MSC KYC(BW) ASVW VSaW SV03 DYC
        17 JSC BYC(BE) KYC(SH) BYCÜ RSN BYC(BA)
        18 MYC NRV WYC SVI FSC SMCÜ
        19 SV03 RSN WYC BYCÜ FSC KYC(BW)
        20 NRV SVI JSC BYC(BA) VSaW ASVW
        21 DYC BYC(BE) MSC MYC SMCÜ KYC(SH)
        22 DYC SV03 RSN JSC ASVW KYC(SH)
        23 FSC BYC(BA) SVI SMCÜ BYC(BE) BYCÜ
        24 MSC VSaW KYC(BW) NRV WYC MYC
        25 SMCÜ ASVW DYC SV03 SVI FSC
        26 WYC BYCÜ BYC(BA) MYC BYC(BE) NRV
        27 JSC MSC KYC(BW) VSaW KYC(SH) RSN
        28 NRV WYC SV03 ASVW MYC RSN
        29 SVI JSC KYC(SH) KYC(BW) SMCÜ FSC
        30 BYC(BA) DYC VSaW MSC BYCÜ BYC(BE)
        31 BYC(BA) NRV FSC MSC RSN JSC
        32 MYC VSaW BYC(BE) KYC(BW) SV03 SVI
        33 BYCÜ WYC ASVW KYC(SH) DYC SMCÜ
        34 BYCÜ BYC(BE) ASVW SV03 BYC(BA) KYC(BW)
        35 VSaW SVI SMCÜ FSC RSN MSC
        36 KYC(SH) MYC JSC DYC NRV WYC
        37 SMCÜ MYC JSC BYCÜ MSC SV03
        38 ASVW NRV SVI KYC(SH) VSaW BYC(BA)
        39 RSN FSC DYC BYC(BE) KYC(BW) WYC
        40 MSC FSC KYC(SH) BYC(BE) ASVW MYC
        41 JSC VSaW BYC(BA) WYC SMCÜ KYC(BW)
        42 SV03 RSN BYCÜ DYC NRV SVI
        43 WYC JSC BYC(BE) ASVW MSC SVI
        44 DYC BYC(BA) KYC(BW) RSN MYC SMCÜ
        45 FSC KYC(SH) SV03 VSaW BYCÜ NRV
        46 RSN KYC(SH) SV03 SVI WYC BYC(BA)
        47 KYC(BW) BYCÜ SMCÜ NRV BYC(BE) MSC
        48 MYC ASVW VSaW JSC FSC DYC
    """,
    # 3 - Hotel Kieler Yacht Club
    """Flight Race Boat 1 Boat 2 Boat 3 Boat 4 Boat 5 Boat 6
        1 MYC ASVW DYC SMCÜ NRV BYCÜ
        2 MSC KYC(BW) WYC FSC KYC(SH) BYC(BE)
        3 VSaW JSC BYC(BA) RSN SVI SV03
        4 VSaW DYC BYC(BA) BYC(BE) BYCÜ FSC
        5 JSC SVI NRV KYC(BW) WYC SMCÜ
        6 SV03 MYC RSN KYC(SH) ASVW MSC
        7 DYC MYC KYC(BW) SVI BYC(BA) MSC
        8 BYCÜ NRV FSC JSC SV03 KYC(SH)
        9 RSN BYC(BE) SMCÜ WYC VSaW ASVW
        10 FSC SV03 SMCÜ MYC VSaW KYC(BW)
        11 ASVW WYC JSC BYCÜ MSC BYC(BA)
        12 KYC(SH) RSN SVI NRV BYC(BE) DYC
        13 FSC RSN MSC JSC SMCÜ DYC
        14 KYC(BW) BYC(BA) ASVW SV03 BYC(BE) NRV
        15 SVI VSaW BYCÜ KYC(SH) MYC WYC
        16 NRV VSaW SV03 MSC DYC WYC
        17 BYC(BE) FSC MYC ASVW JSC SVI
        18 BYC(BA) SMCÜ KYC(SH) BYCÜ KYC(BW) RSN
        19 DYC JSC KYC(SH) ASVW KYC(BW) VSaW
        20 SMCÜ BYCÜ BYC(BE) SVI MSC SV03
        21 WYC FSC NRV BYC(BA) RSN MYC
        22 WYC DYC JSC BYC(BE) SV03 MYC
        23 KYC(BW) SVI BYCÜ RSN FSC ASVW
        24 NRV MSC VSaW SMCÜ KYC(SH) BYC(BA)
        25 RSN SV03 WYC DYC BYCÜ KYC(BW)
        26 KYC(SH) ASVW SVI BYC(BA) FSC SMCÜ
        27 BYC(BE) NRV VSaW MSC MYC JSC
        28 SMCÜ KYC(SH) DYC SV03 BYC(BA) JSC
        29 BYCÜ BYC(BE) MYC VSaW RSN KYC(BW)
        30 SVI WYC MSC NRV ASVW FSC
        31 SVI SMCÜ KYC(BW) NRV JSC BYC(BE)
        32 BYC(BA) MSC FSC VSaW DYC BYCÜ
        33 ASVW KYC(SH) SV03 MYC WYC RSN
        34 ASVW FSC SV03 DYC SVI VSaW
        35 MSC BYCÜ RSN KYC(BW) JSC NRV
        36 MYC BYC(BA) BYC(BE) WYC SMCÜ KYC(SH)
        37 RSN BYC(BA) BYC(BE) ASVW NRV DYC
        38 SV03 SMCÜ BYCÜ MYC MSC SVI
        39 JSC KYC(BW) WYC FSC VSaW KYC(SH)
        40 NRV KYC(BW) MYC FSC SV03 BYC(BA)
        41 BYC(BE) MSC SVI KYC(SH) RSN VSaW
        42 DYC JSC ASVW WYC SMCÜ BYCÜ
        43 KYC(SH) BYC(BE) FSC SV03 NRV BYCÜ
        44 WYC SVI VSaW JSC BYC(BA) RSN
        45 KYC(BW) MYC DYC MSC ASVW SMCÜ
        46 JSC MYC DYC BYCÜ KYC(SH) SVI
        47 VSaW ASVW RSN SMCÜ FSC NRV
        48 BYC(BA) SV03 MSC BYC(BE) KYC(BW) WYC
    """,
        # 4 - Camp 24/7
    """Flight Race Boat 1 Boat 2 Boat 3 Boat 4 Boat 5 Boat 6
        1 SMCÜ FSC VSaW BYC(BA) MYC BYC(BE)
        2 KYC(SH) DYC MSC SV03 NRV ASVW
        3 WYC BYCÜ RSN SVI JSC KYC(BW)
        4 WYC VSaW RSN ASVW BYC(BE) SV03
        5 BYCÜ JSC MYC DYC MSC BYC(BA)
        6 KYC(BW) SMCÜ SVI NRV FSC KYC(SH)
        7 VSaW SMCÜ DYC JSC RSN KYC(SH)
        8 BYC(BE) MYC SV03 BYCÜ KYC(BW) NRV
        9 SVI ASVW BYC(BA) MSC WYC FSC
        10 SV03 KYC(BW) BYC(BA) SMCÜ WYC DYC
        11 FSC MSC BYCÜ BYC(BE) KYC(SH) RSN
        12 NRV SVI JSC MYC ASVW VSaW
        13 SV03 SVI KYC(SH) BYCÜ BYC(BA) VSaW
        14 DYC RSN FSC KYC(BW) ASVW MYC
        15 JSC WYC BYC(BE) NRV SMCÜ MSC
        16 MYC WYC KYC(BW) KYC(SH) VSaW MSC
        17 ASVW SV03 SMCÜ FSC BYCÜ JSC
        18 RSN BYC(BA) NRV BYC(BE) DYC SVI
        19 VSaW BYCÜ NRV FSC DYC WYC
        20 BYC(BA) BYC(BE) ASVW JSC KYC(SH) KYC(BW)
        21 MSC SV03 MYC RSN SVI SMCÜ
        22 MSC VSaW BYCÜ ASVW KYC(BW) SMCÜ
        23 DYC JSC BYC(BE) SVI SV03 FSC
        24 MYC KYC(SH) WYC BYC(BA) NRV RSN
        25 SVI KYC(BW) MSC VSaW BYC(BE) DYC
        26 NRV FSC JSC RSN SV03 BYC(BA)
        27 ASVW MYC WYC KYC(SH) SMCÜ BYCÜ
        28 BYC(BA) NRV VSaW KYC(BW) RSN BYCÜ
        29 BYC(BE) ASVW SMCÜ WYC SVI DYC
        30 JSC MSC KYC(SH) MYC FSC SV03
        31 JSC BYC(BA) DYC MYC BYCÜ ASVW
        32 RSN KYC(SH) SV03 WYC VSaW BYC(BE)
        33 FSC NRV KYC(BW) SMCÜ MSC SVI
        34 FSC SV03 KYC(BW) VSaW JSC WYC
        35 KYC(SH) BYC(BE) SVI DYC BYCÜ MYC
        36 SMCÜ RSN ASVW MSC BYC(BA) NRV
        37 SVI RSN ASVW FSC MYC VSaW
        38 KYC(BW) BYC(BA) BYC(BE) SMCÜ KYC(SH) JSC
        39 BYCÜ DYC MSC SV03 WYC NRV
        40 MYC DYC SMCÜ SV03 KYC(BW) RSN
        41 ASVW KYC(SH) JSC NRV SVI WYC
        42 VSaW BYCÜ FSC MSC BYC(BA) BYC(BE)
        43 NRV ASVW SV03 KYC(BW) MYC BYC(BE)
        44 MSC JSC WYC BYCÜ RSN SVI
        45 DYC SMCÜ VSaW KYC(SH) FSC BYC(BA)
        46 BYCÜ SMCÜ VSaW BYC(BE) NRV JSC
        47 WYC FSC SVI BYC(BA) SV03 MYC
        48 RSN KYC(BW) KYC(SH) ASVW DYC MSC
        """,
        # - 5 Münchner Yacht-Club
    """Flight Race Boat 1 Boat 2 Boat 3 Boat 4 Boat 5 Boat 6
        1 NRV BYC(BE) KYC(BW) MYC KYC(SH) JSC
        2 WYC SV03 VSaW ASVW MSC BYCÜ
        3 DYC SVI SMCÜ BYC(BA) RSN FSC
        4 DYC KYC(BW) SMCÜ BYCÜ JSC ASVW
        5 SVI RSN KYC(SH) SV03 VSaW MYC
        6 FSC NRV BYC(BA) MSC BYC(BE) WYC
        7 KYC(BW) NRV SV03 RSN SMCÜ WYC
        8 JSC KYC(SH) ASVW SVI FSC MSC
        9 BYC(BA) BYCÜ MYC VSaW DYC BYC(BE)
        10 ASVW FSC MYC NRV DYC SV03
        11 BYC(BE) VSaW SVI JSC WYC SMCÜ
        12 MSC BYC(BA) RSN KYC(SH) BYCÜ KYC(BW)
        13 ASVW BYC(BA) WYC SVI MYC KYC(BW)
        14 SV03 SMCÜ BYC(BE) FSC BYCÜ KYC(SH)
        15 RSN DYC JSC MSC NRV VSaW
        16 KYC(SH) DYC FSC WYC KYC(BW) VSaW
        17 BYCÜ ASVW NRV BYC(BE) SVI RSN
        18 SMCÜ MYC MSC JSC SV03 BYC(BA)
        19 KYC(BW) SVI MSC BYC(BE) SV03 DYC
        20 MYC JSC BYCÜ RSN WYC FSC
        21 VSaW ASVW KYC(SH) SMCÜ BYC(BA) NRV
        22 VSaW KYC(BW) SVI BYCÜ FSC NRV
        23 SV03 RSN JSC BYC(BA) ASVW BYC(BE)
        24 KYC(SH) WYC DYC MYC MSC SMCÜ
        25 BYC(BA) FSC VSaW KYC(BW) JSC SV03
        26 MSC BYC(BE) RSN SMCÜ ASVW MYC
        27 BYCÜ KYC(SH) DYC WYC NRV SVI
        28 MYC MSC KYC(BW) FSC SMCÜ SVI
        29 JSC BYCÜ NRV DYC BYC(BA) SV03
        30 RSN VSaW WYC KYC(SH) BYC(BE) ASVW
        31 RSN MYC SV03 KYC(SH) SVI BYCÜ
        32 SMCÜ WYC ASVW DYC KYC(BW) JSC
        33 BYC(BE) MSC FSC NRV VSaW BYC(BA)
        34 BYC(BE) ASVW FSC KYC(BW) RSN DYC
        35 WYC JSC BYC(BA) SV03 SVI KYC(SH)
        36 NRV SMCÜ BYCÜ VSaW MYC MSC
        37 BYC(BA) SMCÜ BYCÜ BYC(BE) KYC(SH) KYC(BW)
        38 FSC MYC JSC NRV WYC RSN
        39 SVI SV03 VSaW ASVW DYC MSC
        40 KYC(SH) SV03 NRV ASVW FSC SMCÜ
        41 BYCÜ WYC RSN MSC BYC(BA) DYC
        42 KYC(BW) SVI BYC(BE) VSaW MYC JSC
        43 MSC BYCÜ ASVW FSC KYC(SH) JSC
        44 VSaW RSN DYC SVI SMCÜ BYC(BA)
        45 SV03 NRV KYC(BW) WYC BYC(BE) MYC
        46 SVI NRV KYC(BW) JSC MSC RSN
        47 DYC BYC(BE) BYC(BA) MYC ASVW KYC(SH)
        48 SMCÜ FSC WYC BYCÜ SV03 VSaW
    """,
        # 6 - Bayerischer Yacht-Club
    """Flight Race Boat 1 Boat 2 Boat 3 Boat 4 Boat 5 Boat 6
        1 KYC(SH) BYCÜ SV03 NRV MSC SVI
        2 VSaW FSC DYC BYC(BE) WYC JSC
        3 KYC(BW) RSN MYC SMCÜ BYC(BA) ASVW
        4 KYC(BW) SV03 MYC JSC SVI BYC(BE)
        5 RSN BYC(BA) MSC FSC DYC NRV
        6 ASVW KYC(SH) SMCÜ WYC BYCÜ VSaW
        7 SV03 KYC(SH) FSC BYC(BA) MYC VSaW
        8 SVI MSC BYC(BE) RSN ASVW WYC
        9 SMCÜ JSC NRV DYC KYC(BW) BYCÜ
        10 BYC(BE) ASVW NRV KYC(SH) KYC(BW) FSC
        11 BYCÜ DYC RSN SVI VSaW MYC
        12 WYC SMCÜ BYC(BA) MSC JSC SV03
        13 BYC(BE) SMCÜ VSaW RSN NRV SV03
        14 FSC MYC BYCÜ ASVW JSC MSC
        15 BYC(BA) KYC(BW) SVI WYC KYC(SH) DYC
        16 MSC KYC(BW) ASVW VSaW SV03 DYC
        17 JSC BYC(BE) KYC(SH) BYCÜ RSN BYC(BA)
        18 MYC NRV WYC SVI FSC SMCÜ
        19 SV03 RSN WYC BYCÜ FSC KYC(BW)
        20 NRV SVI JSC BYC(BA) VSaW ASVW
        21 DYC BYC(BE) MSC MYC SMCÜ KYC(SH)
        22 DYC SV03 RSN JSC ASVW KYC(SH)
        23 FSC BYC(BA) SVI SMCÜ BYC(BE) BYCÜ
        24 MSC VSaW KYC(BW) NRV WYC MYC
        25 SMCÜ ASVW DYC SV03 SVI FSC
        26 WYC BYCÜ BYC(BA) MYC BYC(BE) NRV
        27 JSC MSC KYC(BW) VSaW KYC(SH) RSN
        28 NRV WYC SV03 ASVW MYC RSN
        29 SVI JSC KYC(SH) KYC(BW) SMCÜ FSC
        30 BYC(BA) DYC VSaW MSC BYCÜ BYC(BE)
        31 BYC(BA) NRV FSC MSC RSN JSC
        32 MYC VSaW BYC(BE) KYC(BW) SV03 SVI
        33 BYCÜ WYC ASVW KYC(SH) DYC SMCÜ
        34 BYCÜ BYC(BE) ASVW SV03 BYC(BA) KYC(BW)
        35 VSaW SVI SMCÜ FSC RSN MSC
        36 KYC(SH) MYC JSC DYC NRV WYC
        37 SMCÜ MYC JSC BYCÜ MSC SV03
        38 ASVW NRV SVI KYC(SH) VSaW BYC(BA)
        39 RSN FSC DYC BYC(BE) KYC(BW) WYC
        40 MSC FSC KYC(SH) BYC(BE) ASVW MYC
        41 JSC VSaW BYC(BA) WYC SMCÜ KYC(BW)
        42 SV03 RSN BYCÜ DYC NRV SVI
        43 WYC JSC BYC(BE) ASVW MSC SVI
        44 DYC BYC(BA) KYC(BW) RSN MYC SMCÜ
        45 FSC KYC(SH) SV03 VSaW BYCÜ NRV
        46 RSN KYC(SH) SV03 SVI WYC BYC(BA)
        47 KYC(BW) BYCÜ SMCÜ NRV BYC(BE) MSC
        48 MYC ASVW VSaW JSC FSC DYC
    """
    ]
