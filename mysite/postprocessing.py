def getNamesForYieldPred(crop, season, state):
    state_correlation = {
        "Assam": 0,
        "Karnataka": 1,
        "Meghalaya": 2,
        "West Bengal": 3,
        "Puducherry": 4,
        "Goa": 5,
        "Kerala": 6,
        "Andhra Pradesh": 7,
        "Tamil Nadu": 8,
        "Bihar": 9,
        "Gujarat": 10,
        "Maharashtra": 11,
        "Mizoram": 12,
        "Punjab": 13,
        "Uttar Pradesh": 14,
        "Haryana": 15,
        "Himachal Pradesh": 16,
        "Madhya Pradesh": 17,
        "Tripura": 18,
        "Nagaland": 19,
        "Odisha": 20,
        "Chhattisgarh": 21,
        "Uttarakhand": 22,
        "Jharkhand": 23,
        "Delhi": 24,
        "Manipur": 25,
        "Jammu and Kashmir": 26,
        "Telangana": 27,
        "Arunachal Pradesh": 28,
        "Sikkim": 29,
    }

    season_correlation = {
        "Autumn": 0,
        "Summer": 1,
        "Winter": 2,
        "Kharif": 3,
        "Rabi": 4,
        "Whole Year": 5,
    }

    crop_correlation = {
        "Arecanut": 0,
        "Arhar/Tur": 1,
        "Castor seed": 2,
        "Coconut ": 3,
        "Cotton(lint)": 4,
        "Dry chillies": 5,
        "Gram": 6,
        "Jute": 7,
        "Linseed": 8,
        "Maize": 9,
        "Mesta": 10,
        "Niger seed": 11,
        "Onion": 12,
        "Other  Rabi pulses": 13,
        "Potato": 14,
        "Rapeseed &Mustard": 15,
        "Rice": 16,
        "Sesamum": 17,
        "Small millets": 18,
        "Sugarcane": 19,
        "Sweet potato": 20,
        "Tapioca": 21,
        "Tobacco": 22,
        "Turmeric": 23,
        "Wheat": 24,
        "Bajra": 25,
        "Black pepper": 26,
        "Cardamom": 27,
        "Coriander": 28,
        "Garlic": 29,
        "Ginger": 30,
        "Groundnut": 31,
        "Horse-gram": 32,
        "Jowar": 33,
        "Ragi": 34,
        "Cashewnut": 35,
        "Banana": 36,
        "Soyabean": 37,
        "Barley": 38,
        "Khesari": 39,
        "Masoor": 40,
        "Moong(Green Gram)": 41,
        "Other Kharif pulses": 42,
        "Safflower": 43,
        "Sannhamp": 44,
        "Sunflower": 45,
        "Urad": 46,
        "Peas & beans (Pulses)": 47,
        "other oilseeds": 48,
        "Other Cereals": 49,
        "Cowpea(Lobia)": 50,
        "Oilseeds total": 51,
        "Guar seed": 52,
        "Other Summer Pulses": 53,
        "Moth": 54,
    }

    return {
        "crop": list(crop_correlation.keys())[
            list(crop_correlation.values()).index(crop - 1)
        ],
        "state": list(state_correlation.keys())[
            list(state_correlation.values()).index(state)
        ],
        "season": list(season_correlation.keys())[
            list(season_correlation.values()).index(season)
        ],
    }


def getNamesForCropReco(crop):
    crop_correlation = {
        "rice": 0,
        "maize": 1,
        "chickpea": 2,
        "kidneybeans": 3,
        "pigeonpeas": 4,
        "mothbeans": 5,
        "mungbean": 6,
        "blackgram": 7,
        "lentil": 8,
        "pomegranate": 9,
        "banana": 10,
        "mango": 11,
        "grapes": 12,
        "watermelon": 13,
        "muskmelon": 14,
        "apple": 15,
        "orange": 16,
        "papaya": 17,
        "coconut": 18,
        "cotton": 19,
        "jute": 20,
        "coffee": 21,
    }

    return list(crop_correlation.keys())[list(crop_correlation.values()).index(crop)]


def getNamesForFertReco(soil, crop, fertilizer):
    soil_correlation = {
        "Black": 0,
        "Red ": 1,
        "Medium Brown": 2,
        "Dark Brown": 3,
        "Red": 4,
        "Light Brown": 5,
        "Reddish Brown": 6,
    }
    crop_correlation = {
        "Sugarcane": 0,
        "Jowar": 1,
        "Cotton": 2,
        "Rice": 3,
        "Wheat": 4,
        "Groundnut": 5,
        "Maize": 6,
        "Tur": 7,
        "Urad": 8,
        "Moong": 9,
        "Gram": 10,
        "Masoor": 11,
        "Soybean": 12,
        "Ginger": 13,
        "Turmeric": 14,
        "Grapes": 15,
    }
    fertilizer_correlation = {
        "Urea": 0,
        "DAP": 1,
        "MOP": 2,
        "10:26:26 NPK": 3,
        "SSP": 4,
        "Magnesium Sulphate": 5,
        "13:32:26 NPK": 6,
        "12:32:16 NPK": 7,
        "50:26:26 NPK": 8,
        "19:19:19 NPK": 9,
        "Chilated Micronutrient": 10,
        "18:46:00 NPK": 11,
        "Sulphur": 12,
        "20:20:20 NPK": 13,
        "Ammonium Sulphate": 14,
        "Ferrous Sulphate": 15,
        "White Potash": 16,
        "10:10:10 NPK": 17,
        "Hydrated Lime": 18,
    }

    return {
        "soil": list(soil_correlation.keys())[
            list(soil_correlation.values()).index(soil)
        ],
        "crop": list(crop_correlation.keys())[
            list(crop_correlation.values()).index(crop)
        ],
        "fertilizer": list(fertilizer_correlation.keys())[
            list(fertilizer_correlation.values()).index(fertilizer)
        ],
    }
