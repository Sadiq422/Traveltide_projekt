import os  # Importiert das 'os'-Modul, das Funktionen zur Interaktion mit dem Betriebssystem bereitstellt (z.B. Dateipfade verwalten, Umgebungsvariablen lesen).

import sys  # Importiert das 'sys'-Modul, das Zugriff auf Systemparameter und -funktionen bietet (z.B. Beenden des Skripts, Zugriff auf Kommandozeilenargumente).

import pandas as pd  # type: ignore  # Importiert die beliebte 'pandas'-Bibliothek zur Datenanalyse und -manipulation. Sie wird unter dem Alias 'pd' verwendet. 
# Der Kommentar '# type: ignore' unterdrückt mögliche Typisierungswarnungen des Linters für diese Zeile.

from IPython.display import display  # type: ignore  # Importiert die 'display'-Funktion speziell aus 'IPython.display'. Diese Funktion ist nützlich, 
# um Pandas DataFrames oder andere Objekte in interaktiven Umgebungen (z.B. Jupyter Notebooks) formatiert anzuzeigen. Der Kommentar 
# '# type: ignore' unterdrückt erneut Typisierungswarnungen.
from core.utils import init_connection, execute_query, execute_sql_file  # Importiert spezifische Funktionen aus einem lokalen Modul namens 
# 'core.utils'. Es handelt sich dabei um Hilfsfunktionen, vermutlich für die Datenbankinteraktion:
# init_connection: Initialisiert eine Datenbankverbindung.
# execute_query: Führt eine SQL-Abfrage aus.
# execute_sql_file: Führt SQL-Befehle aus einer Datei aus.


# === PATH CONFIGURATION ===
# Füge core module zum Python-Pfad hinzu, damit Importe funktionieren
core_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)
sys.path.insert(0, core_path)

# === DATABASE INITIALIZATION ===
# Stellt Verbindung zur TravelTide PostgreSQL-Datenbank her
init_connection()

# === DIRECTORY SETUP ===
# Definiere Basis-Pfade für verschiedene Daten-Typen
base_path = os.path.dirname(__file__)
raw_data_path = os.path.join(base_path, '..', 'data', 'raw')             # Rohdaten: users.csv, flights.csv etc.
processed_data_path = os.path.join(base_path, '..', 'data', 'processed') # Verarbeitete Daten
sql_path = os.path.join(base_path, '..', 'sql')                          # SQL Query Dateien
reports_path = os.path.join(base_path, '..', 'reports')                  # Analyse Reports
feature_path = os.path.join(processed_data_path, 'feature_metrics')      # Feature Engineering Ergebnisse
segments_path = os.path.join(processed_data_path, 'segmentation')        # Kundensegmentierung
pca_path = os.path.join(processed_data_path, 'pca')                      # PCA Analyse Ergebnisse
kmeans_path = os.path.join(processed_data_path, 'kmean')                 # KMeans Clustering Ergebnisse
non_ml_patj = os.path.join(processed_data_path, 'non_ml')                # Manuelle Segmentierung Ergebnisse


def get_path(data_type: str, table_name: str) -> tuple[str, str]:
    """
    ### Funktion: get_path
    **Purpose:**
    Erzeugt den vollständigen Dateipfad basierend auf Daten-Typ und Tabellennamen.
    
    **Arguments:**
    - `data_type` (str): Typ der Daten ('raw', 'processed', 'sql', 'feature', 'segment', 'pca', 'kmean')
    - `table_name` (str): Name der Tabelle/Datei ohne Erweiterung
    
    **Returns:**
    - tuple[str, str]: Vollständiger Pfad und aufgelöster Daten-Typ
    
    **Example:**
    ```python
    path, dtype = get_path("raw", "users")
    # → ("../data/raw/users.csv", "raw")
    ```
    """
    # Mapping von Daten-Typen zu entsprechenden Verzeichnissen
    if data_type == "raw":
        path = os.path.join(raw_data_path, f"{table_name}.csv")
    elif data_type == "processed":
        path = os.path.join(processed_data_path, f"{table_name}.csv")
    elif data_type == "sql":
        path = os.path.join(sql_path, f"{table_name}.sql")
    elif data_type == "feature":
        path = os.path.join(feature_path, f"{table_name}.csv")
    elif data_type == "segment":
        path = os.path.join(segments_path, f"{table_name}.csv")
    elif data_type == "pca":
        path = os.path.join(pca_path, f"{table_name}.csv")
    elif data_type == "kmean":
        path = os.path.join(kmeans_path, f"{table_name}.csv")
    elif data_type == "non_ml":
        path = os.path.join(non_ml_patj, f"{table_name}.csv")
    
    else:
        raise ValueError(
            f":x: Ungültiger Datentyp: '{data_type}'. "
            f"Erlaubt sind 'raw', 'processed', 'sql'."
        )
    return path, data_type


def load_table(
    data_type: str,
    table_name: str,
    show_table_display: bool = False,
) -> pd.DataFrame:
    """
    ### Funktion: load_table
    **Purpose:**
    Lädt Daten aus verschiedenen Quellen (CSV, SQL, Datenbank) in einen DataFrame.
    
    **Workflow:**
    1. Prüft ob lokale CSV/SQL Datei existiert
    2. Falls nicht: Lädt direkt aus der Datenbank
    3. Speichert geladene Daten für zukünftige Verwendung
    
    **Arguments:**
    - `data_type` (str): Quelle der Daten ('raw', 'processed', 'sql')
    - `table_name` (str): Name der Tabelle
    - `show_table_display` (bool): Zeige Vorschau der Daten (default: False)
    
    **Returns:**
    - pd.DataFrame: Geladene Daten
    
    **Example:**
    ```python
    users_df = load_table("raw", "users", show_table_display=True)
    ```
    """
    # Ermittle den vollständigen Dateipfad
    file_path, resolved_type = get_path(data_type, table_name)
    
    # === SQL FILE HANDLING ===
    if resolved_type == "sql" and os.path.exists(file_path):
        print(
            f":blatt_oben: Lade Tabelle '{table_name}' aus SQL-Datei: "
            f"{file_path}"
        )
        df = execute_sql_file(file_path)  # Führt SQL aus Datei aus
        print(f":weißes_häkchen: SQL-Abfrage erfolgreich. Zeilen: {len(df)}")
        
        # Speichere Ergebnis als CSV für zukünftige Verwendung
        new_csv_path = os.path.join(processed_data_path, f"{table_name}.csv")
        df.to_csv(new_csv_path, index=False)
        print(f":diskette: Gespeichert unter: {new_csv_path}")
    
    # === CSV FILE HANDLING ===
    elif resolved_type in ["raw", "processed", "feature", "segment", "pca", "kmean", "non_ml"] and os.path.exists(file_path):
        print(
            f":aktenordner: Lade Tabelle '{table_name}' aus CSV: "
            f"{file_path}"
        )
        df = pd.read_csv(file_path)  # Lade Daten aus CSV
        print(f":weißes_häkchen: CSV geladen. Zeilen: {len(df)}")
    
    # === DATABASE FALLBACK ===
    else:
        print(
            f":globus_mit_meridianen: Lade Tabelle '{table_name}' "
            f"direkt aus der Datenbank..."
        )
        df = execute_query(f"SELECT * FROM {table_name};")  # Direkter DB Query
        print(
            f":weißes_häkchen: Datenbankabfrage erfolgreich. "
            f"Zeilen: {len(df)}"
        )
        
        # Speichere geladene Daten für zukünftige Verwendung
        if not df.empty and resolved_type in ["raw", "processed"]:
            df.to_csv(file_path, index=False)
            print(f":diskette: Gespeichert unter: {file_path}")
        elif df.empty:
            print(f":warnung: Keine Daten gefunden für Tabelle '{table_name}'")
    
    # === DATA PREVIEW ===
    # Zeige zufällige Stichprobe der Daten falls gewünscht
    if not df.empty and show_table_display:
        display(df.sample(min(100, len(df))))
    
    return df


def load_custom_query(query: str) -> pd.DataFrame:
    """
    ### Funktion: load_custom_query
    **Purpose:**
    Führt eine benutzerdefinierte SQL-Abfrage aus und gibt Ergebnisse zurück.
    
    **Arguments:**
    - `query` (str): SQL Query String
    
    **Returns:**
    - pd.DataFrame: Ergebnisse der Query
    
    **Example:**
    ```python
    query = "SELECT * FROM users WHERE has_children = true"
    families_df = load_custom_query(query)
    ```
    """
    print(":gehirn: Führe benutzerdefinierte SQL-Abfrage aus...")
    df = execute_query(query)
    
    if not df.empty:
        display(df.sample(min(100, len(df))))  # Zeige Stichprobe
    else:
        print(":warnung: Keine Ergebnisse für diese Abfrage.")
    
    return df


if __name__ == "__main__":
    """
    TEST MODUS: Lädt Beispiel-Datensätze beim direkten Ausführen der Datei
    """
    # Lade alle Haupttabellen für Testing
    flights = load_table(data_type="raw", table_name="flights",
                         show_table_display=False)
    users = load_table(data_type="processed", table_name="users",
                       show_table_display=False)
    sessions = load_table(data_type="processed", table_name="sessions",
                          show_table_display=False)
    hotels = load_table(data_type="raw", table_name="hotels",
                        show_table_display=False)