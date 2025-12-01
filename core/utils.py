# type: ignore
# Diese Zeile sagt Type-Checkern (wie mypy), dass sie diesen Code ignorieren sollen
# Nützlich wenn wir Bibliotheken ohne Type-Hints verwenden

import os  # Betriebssystem-Interaktion: Dateipfade, Verzeichnisse
import pandas as pd  # type: ignore # Datenmanipulation: DataFrames, Datenanalyse
import sqlalchemy as sa  # type: ignore # Datenbank-Interaktion: SQL Verbindungen, Abfragen
from sqlalchemy.exc import SQLAlchemyError  # type: ignore # Fehlerbehandlung für SQLAlchemy
from sqlalchemy.engine import URL
from dotenv import load_dotenv

# ============================================================
load_dotenv()  # Lade Umgebungsvariablen aus .env Datei
# ============================================================
# :zahnrad: Utility Functions (General-Purpose)
# Hilfsfunktionen für Datenbankverbindung und Datenverarbeitung
# ============================================================

# Globale Verbindungsobjekte - werden einmal initialisiert und wiederverwendet
_engine = None      # SQLAlchemy Engine: Verwaltet Datenbank-Verbindungspool
_connection = None  # Aktive Datenbankverbindung für Abfragen


def init_connection(db_url: str = None):
    """
    ### FUNKTION: init_connection
    **Zweck:**
    Stellt eine Verbindung zur TravelTide PostgreSQL-Datenbank her und initialisiert 
    die globalen _engine und _connection Objekte.
    
    **Funktionsweise:**
    1. Erstellt eine SQLAlchemy Engine mit Connection Pooling
    2. Öffnet eine persistente Verbindung zur Datenbank
    3. Setzt AUTOCOMMIT für automatische Transaktionsverwaltung
    
    **Parameter:**
    - db_url (str): PostgreSQL Connection URL mit Benutzername, Passwort, Host und Datenbankname
    
    **Beispiel:**
    ```python
    init_connection()  # Verbindung mit Default-URL
    ```
    """
    global _engine, _connection
    try:
        if not db_url:
        
            db_url = URL.create(
                    drivername="postgresql",
                    username=os.getenv("DB_USER"),
                    password=os.getenv("DB_PASSWORD"),
                    host=os.getenv("DB_HOST"),
                    database=os.getenv("DB_NAME"),
                    query={"sslmode": os.getenv("DB_SSLMODE", "require")}
                )
        # Erstelle Database Engine mit Connection Pool
        _engine = sa.create_engine(db_url, pool_pre_ping=True)
        # Öffne persistente Verbindung mit Auto-Commit
        _connection = _engine.connect().execution_options(isolation_level="AUTOCOMMIT")
        print(":weißes_häkchen: Connected to PostgreSQL database.")
    except SQLAlchemyError as e:
        print(f":x: Connection failed: {e}")
        _engine = None
        _connection = None


def execute_query(query: str) -> pd.DataFrame:
    """
    ### FUNKTION: execute_query
    **Zweck:**
    Führt eine SQL-Abfrage aus und gibt die Ergebnisse als pandas DataFrame zurück.
    
    **Funktionsweise:**
    1. Überprüft ob aktive Datenbankverbindung existiert
    2. Führt SQL-Query mit pandas read_sql() aus
    3. Gibt Ergebnisse als DataFrame für weitere Analyse zurück
    
    **Parameter:**
    - query (str): SQL SELECT Abfrage als String
    
    **Rückgabe:**
    - pd.DataFrame: Ergebnisse der Abfrage, oder leerer DataFrame bei Fehler
    
    **Beispiel:**
    ```python
    df = execute_query("SELECT * FROM users LIMIT 10")
    ```
    """
    if not _connection:
        raise ConnectionError(":warnung: No active database connection.")
    try:
        # Führe SQL aus und lese Ergebnisse direkt in DataFrame
        df = pd.read_sql(sa.text(query), _connection)
        print(f":weißes_häkchen: Query executed. {len(df)} rows retrieved.")
        return df
    except SQLAlchemyError as e:
        print(f":x: Query failed: {e}")
        return pd.DataFrame()  # Leerer DataFrame bei Fehler


def execute_sql_file(sql_file_path: str) -> pd.DataFrame:
    """
    ### FUNKTION: execute_sql_file  
    **Zweck:**
    Liest SQL-Code aus einer Datei und führt ihn aus.
    
    **Funktionsweise:**
    1. Überprüft ob SQL-Datei existiert
    2. Liest gesamten Dateiinhalt als String
    3. Übergibt SQL an execute_query() zur Ausführung
    
    **Parameter:**
    - sql_file_path (str): Pfad zur .sql Datei
    
    **Rückgabe:**
    - pd.DataFrame: Ergebnisse der SQL-Abfrage
    
    **Beispiel:**
    ```python
    df = execute_sql_file("../sql/complex_analysis.sql")
    ```
    """
    if not os.path.exists(sql_file_path):
        raise FileNotFoundError(f":warnung: SQL file not found: {sql_file_path}")
    
    # Lese gesamten SQL-Code aus Datei
    with open(sql_file_path, "r") as file:
        sql_query = file.read()
    
    print(f":blatt_oben: Executing SQL from file: {sql_file_path}")
    return execute_query(sql_query)


def to_datetime(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """
    ### FUNKTION: to_datetime
    **Zweck:**
    Konvertiert Spalten sicher in datetime-Format mit Fehlerbehandlung.
    
    **Funktionsweise:**
    - pd.to_datetime() mit errors="coerce" verwandelt ungültige Daten in NaT (Not a Time)
    - Schützt vor Abbruch bei fehlerhaften Datumswerten
    
    **Parameter:**
    - df (pd.DataFrame): Input DataFrame
    - columns (list[str]): Liste der zu konvertierenden Spaltennamen
    
    **Rückgabe:**
    - pd.DataFrame: DataFrame mit konvertierten datetime-Spalten
    
    **Beispiel:**
    ```python
    df = to_datetime(df, ['session_start', 'session_end'])
    ```
    """
    for col in columns:
        if col in df.columns:
            # Coerce: Ungültige Werte werden zu NaT statt Fehler
            df[col] = pd.to_datetime(df[col], errors="coerce")
    return df


def group_summary(
    df: pd.DataFrame, 
    group_cols: list[str], 
    metrics: dict, 
    sort_by: str = None, 
    top_n: int = None
) -> pd.DataFrame:
    """
    ### FUNKTION: group_summary
    **Zweck:**
    Erstellt aggregierte Zusammenfassungen nach Gruppen - wiederverwendbar für alle Tabellen.
    
    **Funktionsweise:**
    1. Gruppiert Daten nach group_cols
    2. Wendet Aggregationsfunktionen aus metrics an
    3. Optional: Sortiert und begrenzt Ergebnisse
    
    **Parameter:**
    - df (pd.DataFrame): Input DataFrame
    - group_cols (list[str]): Spalten zum Gruppieren (z.B. ['gender', 'has_children'])
    - metrics (dict): Aggregationen {'spaltenname': 'funktion'} (z.B. {'trip_id': 'count', 'base_fare_usd': 'mean'})
    - sort_by (str): Optional - Spalte zum Sortieren (absteigend)
    - top_n (int): Optional - Nur Top N Ergebnisse zurückgeben
    
    **Rückgabe:**
    - pd.DataFrame: Aggregierte und formatierte Ergebnisse
    
    **Beispiel:**
    ```python
    summary = group_summary(
        users_df, 
        ['gender'], 
        {'user_id': 'count', 'age': 'mean'}, 
        sort_by='user_id', 
        top_n=5
    )
    ```
    """
    # Führe Gruppierung und Aggregation durch
    result = df.groupby(group_cols).agg(metrics).reset_index()
    
    # Optional: Sortiere Ergebnisse
    if sort_by and sort_by in result.columns:
        result = result.sort_values(by=sort_by, ascending=False)
    
    # Optional: Begrenze auf Top N Ergebnisse
    if top_n:
        result = result.head(top_n)
    
    # Runde numerische Werte auf 2 Dezimalstellen
    return result.round(2)


def calculate_duration(
    df: pd.DataFrame, 
    start_col: str, 
    end_col: str, 
    new_col: str = "duration_days"
) -> pd.DataFrame:
    """
    ### FUNKTION: calculate_duration
    **Zweck:**
    Berechnet die Dauer in Tagen zwischen zwei datetime-Spalten.
    
    **Funktionsweise:**
    1. Konvertiert Start- und End-Spalten zu datetime
    2. Berechnet Differenz in Tagen
    3. Erstellt neue Spalte mit dem Ergebnis
    
    **Parameter:**
    - df (pd.DataFrame): Input DataFrame
    - start_col (str): Start-Zeitstempel Spalte
    - end_col (str): End-Zeitstempel Spalte  
    - new_col (str): Name der neuen Dauer-Spalte (default: "duration_days")
    
    **Rückgabe:**
    - pd.DataFrame: DataFrame mit neuer Dauer-Spalte
    
    **Beispiel:**
    ```python
    # Berechne Session-Dauer in Tagen
    sessions_df = calculate_duration(sessions_df, 'session_start', 'session_end', 'session_days')
    ```
    """
    # Stelle sicher dass beide Spalten datetime sind
    df = to_datetime(df, [start_col, end_col])
    
    # Berechne Differenz und extrahiere Tage
    df[new_col] = (df[end_col] - df[start_col]).dt.days
    
    return df