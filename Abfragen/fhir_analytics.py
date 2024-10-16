import requests

base_uri = "http://127.0.0.1:8000/"
headers = {'Connection': 'close'}


# Abfrage 1
def olap_abfrage1():
    try:
        res = requests.get(base_uri + "analytics/MedicationPatient",
                           params={"medication_code": "764073002"},
                           headers=headers)
        print('request successful')
        return res
    except ConnectionError as ce:
        print(
            f"Error connecting to the FHIR Server - Please check: {base_uri}", ce)
    except Exception as e:
        print(f"Unexpected error while sending a request - log: {e}")


def olap_abfrage2():
    try:
        res = requests.get(base_uri + "analytics/OrganizationContact",
                           params={"organization_id": "1258458"},
                           headers=headers)
        print('request successful')
        return res
    except ConnectionError as ce:
        print(
            f"Error connecting to the FHIR Server - Please check: {base_uri}", ce)
    except Exception as e:
        print(f"Unexpected error while sending a request - log: {e}")


def olap_abfrage3():
    try:
        res = requests.get(base_uri + "analytics/EncounterTimespan",
                           params={"start": "2023-01-01", "end": "2023-12-31"},
                           headers=headers)
        print('request successful')
        return res
    except ConnectionError as ce:
        print(
            f"Error connecting to the FHIR Server - Please check: {base_uri}", ce)
    except Exception as e:
        print(f"Unexpected error while sending a request - log: {e}")


def olap_abfrage4():
    try:
        res = requests.get(base_uri + "analytics/MedicationManufacturer",
                           params={"medication_code": "387471000", "manufacturer_id": "1218407"},
                           headers=headers)
        print('request successful')
        return res
    except ConnectionError as ce:
        print(
            f"Error connecting to the FHIR Server - Please check: {base_uri}", ce)
    except Exception as e:
        print(f"Unexpected error while sending a request - log: {e}")
