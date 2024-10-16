import requests

base_uri = "http://localhost:8080/fhir/"
headers = {'Connection': 'close'}


def oltp_abfrage1():
    try:
        patient_ids = []
        res = requests.get(base_uri + "/Medication",
                           params={"code": "764073002", "_count": "1000000"},
                           headers=headers)
        medications = res.json()
        if medications.get('entry', None) is not None:
            for entry in medications['entry']:
                med_id = entry['resource']['id']
                res = requests.get(base_uri + "/MedicationStatement",
                                   params={"medication": med_id,
                                           "_count": "1000000"},
                                   headers=headers)
                res_json = res.json()
                if res_json.get('total', 0) != 0:
                    for e in res_json['entry']:
                        patient_id = e['resource']['subject'].get('reference', "").split('/')[1]
                        patient_ids.append(patient_id)

            print('requests successful')
        return patient_ids
    except ConnectionError as ce:
        print(
            f"Error connecting to the FHIR Server - Please check: {base_uri}", ce)
    except Exception as e:
        print(f"Unexpected error while sending a request - log: {e}")


def oltp_abfrage2():
    try:
        patient_ids = []
        encounter_ids = []
        res = requests.get(base_uri + "/Encounter",
                           params={"service-provider": "1258458",
                                   "_count": "1000000"},
                           headers=headers)
        encounter = res.json()
        if encounter.get('entry', None) is not None:
            for entry in encounter['entry']:
                e_id = entry['resource']['id']
                encounter_ids.append(e_id)
                patient_id = entry['resource']['subject'].get('reference', "").split('/')[1]
                patient_ids.append(patient_id)

        print('request successful')
        return patient_ids
    except ConnectionError as ce:
        print(
            f"Error connecting to the FHIR Server - Please check: {base_uri}", ce)
    except Exception as e:
        print(f"Unexpected error while sending a request - log: {e}")


def oltp_abfrage3():
    try:
        encounter_ids = []
        patient_ids = []
        res = requests.get(base_uri + "/Encounter",
                           params={"date": "ge2023-01-01",
                                   "date": "le2023-12-31",
                                   "_count": "1000000"},
                           headers=headers)
        encounter = res.json()
        if encounter.get('entry', None) is not None:
            for entry in encounter['entry']:
                e_id = entry['resource']['id']
                encounter_ids.append(e_id)
                p_id = entry['resource']['subject'].get('reference', "").split('/')[1]
                res = requests.get(base_uri + "/Patient",
                                   params={"_id": p_id,
                                           "active": "true"},
                                   headers=headers)
                res_json = res.json()
                if res_json['total'] != 0:
                    for e in res_json['entry']:
                        patient_id = e['resource']['id']
                        patient_ids.append(patient_id)
        print('request successful')
        return patient_ids
    except ConnectionError as ce:
        print(
            f"Error connecting to the FHIR Server - Please check: {base_uri}", ce)
    except Exception as e:
        print(f"Unexpected error while sending a request - log: {e}")


def oltp_abfrage4():
    try:
        medication_ids = []
        res = requests.get(base_uri + "/Medication",
                           params={"_content": "387471000",
                                   "manufacturer": "1218407",
                                   "_count": "1000000"},
                           headers=headers)
        medications = res.json()
        if medications.get('entry', None) is not None:
            for entry in medications['entry']:
                e_id = entry['resource']['id']
                medication_ids.append(e_id)

        med_statement_string = ""
        for med_id in medication_ids:
            med_statement_string = med_statement_string + str(med_id) + ","

        med_statement_string = med_statement_string[:-1]

        medication_statement_ids = []
        res = requests.get(base_uri + "/MedicationStatement",
                           params={"_content:contains": med_statement_string,
                                   "_count": "1000000"},
                           headers=headers)
        medication_statements = res.json()
        if medication_statements.get('entry', None) is not None:
            for entry in medication_statements['entry']:
                e_id = entry['resource']['id']
                medication_statement_ids.append(e_id)

        return medication_statement_ids
    except ConnectionError as ce:
        print(
            f"Error connecting to the FHIR Server - Please check: {base_uri}", ce)
    except Exception as e:
        print(f"Unexpected error while sending a request - log: {e}")
