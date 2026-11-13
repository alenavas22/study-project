import pandas as pd


def data_types(data: pd.DataFrame) -> pd.DataFrame:
    print("Приведение типа данных")

    data["Has_OMS"] = data["Has_OMS"] == "Yes"
    data["FSR_overlap"] = data["FSR_overlap"] == "Y"
    data["from_CSD"] = data["from_CSD"] == "Y"
    data["public"] = data["public"] == "Y"
    data["CSD_overlap_inCoRE"] = data["CSD_overlap_inCoRE"] == "Y"
    data["CSD_overlap_inCCDC"] = data["CSD_overlap_inCCDC"] == "Y"

    data = data.astype(
        {
            "filename": "str",
            "Open_Metal_Sites": "str",
            "DISORDER": "str",
            "CSD_of_WoS_inCoRE": "str",
            "date_CSD": "str",
            "DOI_public": "str",
            "Note": "str",
            "LCD": "float32",
            "PLD": "float32",
            "LFPD": "float32",
            "cm3_g": "float32",
            "ASA_m2_cm3": "float32",
            "ASA_m2_g": "float32",
            "NASA_m2_cm3": "float32",
            "NASA_m2_g": "float32",
            "AV_VF": "float32",
            "AV_cm3_g": "float32",
            "NAV_cm3_g": "float32",
            "All_Metals": "category",
            "Matched_CSD_of_CoRE": "category",
            "Possible_List_CSD_of_CoRE": "category",
            "Extension": "category",
            "Has_OMS": "bool",
            "FSR_overlap": "bool",
            "from_CSD": "bool",
            "public": "bool",
            "CSD_overlap_inCoRE": "bool",
            "CSD_overlap_inCCDC": "bool",
        }
    )
    return data


def validate_data(data: pd.DataFrame) -> bool:
    return len(data) > 0
