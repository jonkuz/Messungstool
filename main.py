import time
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from Abfragen.fhir_analytics import olap_abfrage1, olap_abfrage2, olap_abfrage3, olap_abfrage4
from Abfragen.hapi_fhir_server import oltp_abfrage1, oltp_abfrage2, oltp_abfrage3, oltp_abfrage4

if __name__ == '__main__':
    # Liste zur Speicherung der Laufzeiten
    times = []

    # API-Abfragen durchführen und die Laufzeiten messen
    for i in range(30):
        start_time = time.time()
        response = oltp_abfrage1()  # Ersetzen durch die gewünschte Abfrage
        end_time = time.time()

        # Laufzeit in Sekunden berechnen
        elapsed_time = (end_time - start_time)
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
    plt.title("HAPI FHIR Server Antwortzeiten")
    plt.ylabel("Zeit in Sekunden")
    plt.show()




