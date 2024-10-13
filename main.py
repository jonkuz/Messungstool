import time
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

base_uri = "http://127.0.0.1:8000/"


# Abfrage 1
def abfrage1():
    try:
        res = requests.get(base_uri + "analytics/MedicationPatient",
                           params={"medication_id": "111355001"})
        print(res.content)
        return res
    except ConnectionError as ce:
        print(
            f"Error connecting to the FHIR Server - Please check: {base_uri}", ce)
    except Exception as e:
        print(f"Unexpected error while sending a request - log: {e}")


def abfrage2():
    try:
        res = requests.get(base_uri + "analytics/PatientOrganizationContact",
                           params={"patient_id": "451254", "organization_id": "5034"})
        print(res.content)
        return res
    except ConnectionError as ce:
        print(
            f"Error connecting to the FHIR Server - Please check: {base_uri}", ce)
    except Exception as e:
        print(f"Unexpected error while sending a request - log: {e}")


def abfrage3():
    try:
        res = requests.get(base_uri + "analytics/EncounterTimespan",
                           params={"start": "2023-01-01", "end": "2023-12-31"})
        print(res.content)
        return res
    except ConnectionError as ce:
        print(
            f"Error connecting to the FHIR Server - Please check: {base_uri}", ce)
    except Exception as e:
        print(f"Unexpected error while sending a request - log: {e}")


def abfrage4():
    try:
        res = requests.get(base_uri + "analytics/MedicationManufacturer",
                           params={"medication_code": "111355001", "manufacturer_id": "4947"})
        print(res.content)
        return res
    except ConnectionError as ce:
        print(
            f"Error connecting to the FHIR Server - Please check: {base_uri}", ce)
    except Exception as e:
        print(f"Unexpected error while sending a request - log: {e}")


if __name__ == '__main__':
    # Liste zur Speicherung der Laufzeiten
    times = []

    # 6 API-Abfragen durchführen und die Laufzeiten messen
    for i in range(30):
        start_time = time.time()
        response = abfrage1()
        end_time = time.time()

        # Laufzeit in Sekunden berechnen
        elapsed_time = end_time - start_time
        times.append(elapsed_time)

    # Daten in ein Pandas DataFrame übertragen
    df = pd.DataFrame(times, columns=["Response Time"])

    # Berechnung von Median, Mittelwert und Standardabweichung
    median_time = df["Response Time"].median()
    mean_time = df["Response Time"].mean()
    std_dev_time = df["Response Time"].std()

    # Ergebnisse ausgeben
    print(f"Median der Laufzeiten: {median_time:.4f} Sekunden")
    print(f"Mittelwert der Laufzeiten: {mean_time:.4f} Sekunden")
    print(f"Standardabweichung der Laufzeiten: {std_dev_time:.4f} Sekunden")

    # Boxplot der Laufzeiten erstellen
    sns.boxplot(data=df, y="Response Time")
    plt.title("FHIRAnalytics Antwortzeiten")
    plt.ylabel("Zeit in Sekunden")
    plt.show()




