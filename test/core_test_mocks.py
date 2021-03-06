core_mock_data = {
    'coordinates': [[32.41275, 20.74575], [-58.32833, -31.91], [-109.84817, 52.996], [-79.95756, -1.87089], [29.41822, 36.54194], [26.70972, 45.275], [-68.489444, -31.535556], [78.03333, 12.66667], [-7.015, 31.16333], [48.95937, 22.72192], [14.25528, 29.35944], [14.26972, 29.37972], [14.24833, 29.35833], [14.27611, 29.36583], [9.84069, 31.481], [10.28403, 31.93833], [9.87722, 31.49972], [10.19361, 31.87164], [10.19572, 31.89689], [10.19528, 31.89831], [10.1875, 31.92181], [10.18961, 31.92644], [10.18961, 31.92644], [-114.323, 34.685], [126.61667, -30.31667], [-117.45303, 35.31218], [-117.48305, 35.28528], [-117.48305, 35.28638], [-117.45817, 35.30455], [-117.472, 35.296], [-117.472, 35.296], [16.21867, 27.32833], [54.72362, 19.26397], [54.62077, 19.21303], [54.36783, 19.01602], [54.39382, 18.99865], [54.40382, 18.97655], [54.41825, 18.98797], [54.41623, 18.99842], [54.41775, 18.99225], [54.37352, 19.01882], [54.3723, 19.0182], [54.36903, 19.01935], [54.25013, 18.34955], [54.16155, 18.45278], [54.16808, 18.5689], [54.17113, 18.56905], [54.17105, 18.57128], [54.15795, 18.56615], [54.15795, 18.56615], [54.17217, 18.56177], [54.16967, 18.56672], [54.16038, 18.56668], [54.14937, 18.57433], [54.16885, 18.60507], [54.17155, 18.61057], [54.17775, 18.6031], [54.40313, 18.98865], [54.40437, 18.79783], [54.3769, 18.74325], [54.45433, 18.77583], [54.45017, 18.67378], [54.44203, 18.68517], [54.43487, 18.66703], [54.42, 18.68712], [54.39702, 18.73168], [54.38944, 18.33861], [54.61717, 18.52533], [54.59533, 18.40867], [54.41283, 18.92633], [54.3845, 18.732], [54.36633, 18.46117], [54.53967, 18.6845], [54.54717, 18.40167], [54.68167, 18.67133], [54.24056, 18.35167], [54.60783, 18.51133], [54.39633, 18.77633], [54.95415, 19.56755], [54.28133, 18.17417], [54.31783, 18.222], [54.56533, 18.36367], [54.59033, 18.5745], [54.64, 18.5345], [54.28, 18.585], [54.1755, 18.647], [54.23717, 18.43033], [54.543, 18.59083], [54.3475, 18.63333], [54.32217, 18.7645], [54.21367, 18.2735], [54.1065, 18.24233], [54.63597, 19.2872], [-101.938333, 32.788333], [-117.26658, 35.04568], [-107.67405, 44.33823], [132.08333, -30.85], [110.73333, -6.6], [55.8535, 19.78565], [56.43006, 19.97133], [56.43006, 19.97133], [56.42839, 19.97525], [56.41939, 19.97875], [56.43194, 19.97892], [56.42361, 19.97778], [56.42192, 19.97531], [56.418, 19.97567], [56.41514, 19.96825], [56.41678, 19.96886], [56.41108, 19.97683], [56.41206, 19.98056], [56.41744, 19.98147], [55.6748, 19.69418], [55.64743, 19.67495], [55.52115, 19.67897], [55.5124, 19.66977], [55.56237, 19.63783], [55.56403, 19.63498], [55.15273, 19.54188], [55.17998, 19.53085], [55.17978, 19.53098], [55.19542, 19.52662], [55.24668, 19.54963], [55.11403, 19.41078], [55.17292, 19.50153], [55.18007, 19.53042], [55.18097, 19.5306], [55.18135, 19.53048], [55.18157, 19.53048], [55.18148, 19.5317], [55.18183, 19.53182], [55.17975, 19.53122], [55.17502, 19.53323], [55.17557, 19.53333], [55.17553, 19.53373], [55.17403, 19.53428], [55.17403, 19.53428], [55.1749, 19.53348], [55.17548, 19.53415], [55.17478, 19.53378], [55.16707, 19.54055], [55.16965, 19.53848], [55.16712, 19.53602], [55.16508, 19.54402], [55.17385, 19.53667], [55.16248, 19.5453], [55.16233, 19.54527], [55.1625, 19.53575], [55.16298, 19.53657], [55.22913, 19.61122], [55.16788, 19.53807], [55.16568, 19.54752], [55.16277, 19.53665], [55.16012, 19.53663], [55.16833, 19.5382], [55.18237, 19.53102], [55.20168, 19.53858], [55.17742, 19.53697], [55.18165, 19.52913], [55.18333, 19.525], [55.18773, 19.5987], [55.18603, 19.59995], [55.48655, 19.57205], [55.58987, 19.65715], [55.64228, 19.64485], [56.11798, 19.76382], [56.10517, 19.83992], [56.10577, 19.85603], [56.17267, 19.8993], [56.21317, 19.83263], [56.19767, 19.6712], [56.14413, 19.68675], [56.48563, 19.83422], [9.72872, 32.681], [93.17306, 41.66889], [-114.455, 35.16867], [-116.96147, 34.48712], [-116.9592, 34.48657], [-116.9564, 34.48662], [-116.95673, 34.48565], [-116.95595, 34.48703], [-116.96055, 34.48733], [-116.96065, 34.48738], [-116.95593, 34.48598], [-99.704, 34.849], [-4.3, 30.51667], [-6.36, 32.37167], [-114.2917, 33.67248], [13.43333, 58.58333], [13.43333, 58.58333], [-114.34572, 34.7049], [125.51333, -30.68833], [49.53252, 23.14302], [56.15087, 20.5971], [56.1299, 20.58143], [56.12693, 20.57128], [56.12678, 20.5534], [56.12155, 20.5247], [56.1285, 20.50483], [56.12353, 20.51968], [56.10287, 20.58077], [56.10683, 20.5426], [56.11768, 20.5225], [56.13955, 20.61728], [56.15995, 20.63257], [56.20918, 20.59658], [-114.03285, 35.64], [-68.57217, -23.826], [-69.870333, -25.443833], [-69.870667, -25.445], [-69.867, -25.4445], [-69.8715, -25.444167], [-69.8745, -25.4435], [-69.875167, -25.443], [-69.874, -25.4425], [-69.876167, -25.4415], [-69.8735, -25.441667], [-69.872167, -25.4425], [-69.871833, -25.443], [-69.872333, -25.44], [-69.8995, -25.372], [-69.871167, -25.4425], [-69.871167, -25.442667], [-69.871167, -25.441167], [-69.871, -25.441833], [-69.870333, -25.441833], [-69.879, -25.440333], [-69.877167, -25.4425], [56.55805, 20.01585], [56.55827, 20.02557], [56.55787, 20.0136], [56.62447, 20.097], [56.64625, 20.15998], [57.14967, 20.78617], [57.11877, 21.27632], [57.178, 21.2921], [56.9719, 20.95935], [56.63413, 20.27317], [56.64225, 20.2926], [57.12872, 21.26845], [56.80917, 20.19867], [57.11117, 20.7025], [-102.67268, 32.70038], [53.3335, 18.33633], [53.914667, 18.604167], [53.96015, 18.6066], [53.97798, 18.54908], [116.90083, -23.25556], [-87.23, -85.348], [-90.351, -85.24067], [-90.326, -85.239], [-90.34483, -85.24417], [-87.11583, -85.387], [-94.74433, -85.16567], [-94.74517, -85.17567], [-114.45585, 35.16993], [131.55, -30.48333], [131.55, -30.48333], [48.73742, 23.34775], [48.72245, 23.35717], [48.62988, 23.31522]],
    'nasa_datum_archetype': {'geolocation': {'coordinates': []}},
    'googlemaps_datum_archetype': {
        u'status': "OK",
        u'results': [
            {
                u'address_components': [
                    {
                        u'long_name': "Unnamed Road",
                        u'short_name': "Unnamed Road",
                        u'types': ["route"]
                    },
                    {
                        u'long_name': "Al Marj",
                        u'short_name': "Al Marj",
                        u'types': ["administrative_area_level_1","political"]
                    },
                    {
                        u'long_name': "Libya",
                        u'short_name': "LY",
                        u'types': ["country","political"]
                    }
                ],
                u'formatted_address': "Unnamed Road, Libya",
                u'geometry': {
                    u'bounds': {
                        u'northeast': {
                            u'lat': 32.4250723,
                            u'lng': 20.7542258
                        },
                        u'southwest': {
                            u'lat': 32.4248411,
                            u'lng': 20.7457602
                        }
                    },
                    u'location': {
                        u'lat': 32.424969,
                        u'lng': 20.7499935
                    },
                    u'location_type': "GEOMETRIC_CENTER",
                    u'viewport': {
                        u'northeast': {
                            u'lat': 32.4263056802915,
                            u'lng': 20.7542258
                        },
                        u'southwest': {
                            u'lat': 32.4236077197085,
                            u'lng': 20.7457602
                        }
                    }
                },
                u'place_id': "ChIJGdkzEwUVghMRIh2pmfHK3hI",
                u'types': ["route"]
            },
            {
                u'address_components': [
                    {
                        u'long_name': "Al Marj",
                        u'short_name': "Al Marj",
                        u'types': ["administrative_area_level_1","political"]
                    },
                    {
                        u'long_name': "Libya",
                        u'short_name': "LY",
                        u'types': ["country","political"]
                    }
                ],
                u'formatted_address': "Al Marj, Libya",
                u'geometry': {
                    u'bounds': {
                        u'northeast': {
                            u'lat': 32.794605,
                            u'lng': 21.712295
                        },
                        u'southwest': {
                            u'lat': 31.173156,
                            u'lng': 20.5461772
                        }
                    },
                    u'location': {
                        u'lat': 32.0550363,
                        u'lng': 21.1891151
                    },
                    u'location_type': "APPROXIMATE",
                    u'viewport': {
                        u'northeast': {
                            u'lat': 32.794605,
                            u'lng': 21.712295
                        },
                        u'southwest': {
                            u'lat': 31.173156,
                            u'lng': 20.5461772
                        }
                    }
                },
                u'place_id': "ChIJ44AWRId9gRMRx-iIa1Rl0PY",
                u'types': ["administrative_area_level_1","political"]
            },
            {
                u'address_components': [
                    {
                        u'long_name': "Libya",
                        u'short_name': "LY",
                        u'types': ["country","political"]
                    }
                ],
                u'formatted_address': "Libya",
                u'geometry': {
                    u'bounds': {
                        u'northeast': {
                            u'lat': 33.16797930000001,
                            u'lng': 25.146954
                        },
                        u'southwest': {
                            u'lat': 19.5,
                            u'lng': 9.391466
                        }
                    },
                    u'location': {
                        u'lat': 26.3351,
                        u'lng': 17.228331
                    },
                    u'location_type': "APPROXIMATE",
                    u'viewport': {
                        u'northeast': {
                            u'lat': 33.16797930000001,
                            u'lng': 25.146954
                        },
                        u'southwest': {
                            u'lat': 19.5,
                            u'lng': 9.391466
                        }
                    }
                },
                u'place_id': "ChIJDQHOjtmSqBMRKsL5x0FgB_o",
                u'types': ["country","political"]
            }
        ],
    },
    u'worldbank_countries_datum_archetype': [
        {
            u'page': 1,
            u'pages': 1,
            u'per_page': "1000",
            u'total': 304
        },
        [
            {
                u'id': "LBY",
                u'iso2Code': "LY",
                u'name': "Libya",
                u'region': {
                    u'id': "MEA",
                    u'value': "Middle East & North Africa"
                },
                u'adminregion': {
                    u'id': "MNA",
                    u'value': "Middle East & North Africa (excluding high income)"
                },
                u'incomeLevel': {
                    u'id': "UMC",
                    u'value': "Upper middle income"
                },
                u'lendingType': {
                    u'id': "IBD",
                    u'value': "IBRD"
                },
                u'capitalCity': "Tripoli",
                u'longitude': "13.1072",
                u'latitude': "32.8578"
            }
        ]
    ],
    u'worldbank_article_datum_archetype': [
        {
            u'page': 1,
            u'pages': 1,
            u'per_page': "1000",
            u'total': 1
        },
        [
            {
                u'indicator': {
                    u'id': "IP.JRN.ARTC.SC",
                    u'value': "Scientific and technical journal articles"
                },
                u'country': {
                    u'id': "LY",
                    u'value': "Libya"
                },
                u'value': "139.7",
                u'decimal': "0",
                u'date': "2008"
            }
        ]
    ],
    u'worldbank_num_articles_datum_archetype': [{'country': u'Libya', 'num_articles': 139.7}],
    u'meteorite_countries_with_num_articles': [
        {
            u'num_articles': 140,
            u'country': "Libya"
        }
    ],
    u'countries_with_meteorite_landings': [
        "Libya",
        "Antarctica",
        "Saudi Arabia",
        "Saudi Arabia",
        "Svalbard and Jan Mayen",
        "Tanzania",
        "Ukraine",
        "Sudan",
        "Sudan",
        "South Sudan",
        "South Sudan",
        "South Sudan",
        "Poland",
        "Poland",
        "Poland",
        "Poland",
        "South Sudan",
        "Tanzania",
        "Latvia",
        "Latvia",
        "Antarctica",
        "Antarctica",
        "Ukraine",
        "Ukraine",
    ]
}
