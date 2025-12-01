"""
TravelTide Data Analysis Package - Master Projekt
__init__.py - Package Initialisierung und Modul-Imports
Dieses File macht den Ordner zu einem Python-Package und definiert die öffentliche API.
"""

# === IMPORTE aus den Modulen ===

# Importiert Funktionen aus utils.py Modul
from .utils import (
    init_connection,      # Stellt Verbindung zur PostgreSQL TravelTide Datenbank her
    execute_query,        # Führt SQL-Queries aus und gibt Resultate als DataFrame zurück
    execute_sql_file,     # Liest SQL-Code aus einer .sql Datei und führt ihn aus
    to_datetime,          # Konvertiert Strings zu datetime Objekten für Zeitreihen-Analysen
    group_summary,        # Erstellt statistische Zusammenfassungen nach Gruppen (z.B. nach Geschlecht)
    calculate_duration,   # Berechnet Zeitdauern zwischen zwei Timestamps (z.B. Session-Dauer)
)

# Importiert Funktionen aus load_data.py Modul  
from .load_data import (
    get_path,            # Hilfsfunktion für relative Pfade zu Datenfiles
    load_table,          # Lädt komplette Tabellen aus der Datenbank (users, sessions, flights, hotels)
    load_custom_query,   # Lädt Daten basierend auf einer benutzerdefinierten SQL-Abfrage
)

# Importiert Funktionen aus eda.py Modul (Exploratory Data Analysis)
from .eda import (
    missing_values_summary,  # Analysiert fehlende Werte - zeigt Missing Count und Prozent pro Spalte
)

from .advance_metrics import (
    prepare_features, # Bereitet Rohdaten für Feature-Engineering vor
    BEHAVIOR_FEATURES, # Definiert Verhaltensbezogene Features
    MINIMAL_FEATURES, # Definiert Minimale Features
    COMPREHENSIVE_FEATURES, # Definiert Umfassende Features
    evaluate_feature_sets, # Bewertet verschiedene Feature-Sets anhand von Modellmetriken
    analyze_feature_importance_pca, # Analysiert Feature-Wichtigkeit mittels PCA
    correlation_analysis, # Führt Korrelationsanalyse zwischen Features und Zielvariable durch
    plot_pca_component_heatmap, # Visualisiert PCA-Komponenten als Heatmap
    plot_2d, # Erstellt 2D Visualisierungen der Daten
    plot_3d # Erstellt 3D Visualisierungen der Daten
)
from .perk_assignment import PerkAssignment
from .segment_analyse import SegmentAnalyzer


# === ÖFFENTLICHE API DEFINITION ===
# __all__ listet alle Funktionen auf, die von außen importiert werden können
# Wenn jemand schreibt: "from traveltide_analysis import *" - nur diese Funktionen werden importiert
__all__ = [
    # === Database Utility Functions ===
    "init_connection",      # 📡 Verbindet mit: postgres://Test:bQNxVzJL4g6u@ep-noisy-flower-846766.us-east-2.aws.neon.tech/TravelTide
    "execute_query",        # 🗃️ Führt beliebige SQL-Queries aus, z.B. SELECT * FROM users LIMIT 10
    "execute_sql_file",     # 📄 Führt SQL aus Files aus - nützlich für komplexe, gespeicherte Queries
    "to_datetime",          # 📅 Konvertiert z.B. "2023-01-01" zu Python datetime Objekt
    "group_summary",        # 📊 Erstellt GroupBy-Statistiken, z.B. Durchschnittsalter nach Geschlecht
    "calculate_duration",   # ⏱️ Berechnet z.B. Session-Länge: session_end - session_start
    
    # === Data Loading Functions ===
    "load_table",          # 📂 Lädt komplette Tabellen: users (1M+ Zeilen), sessions (5M+ Zeilen), etc.
    "get_path",            # 🗺️ Gibt korrekte Pfade zurück, z.B. für CSV-Exporte
    "load_custom_query",   # 🔍 Lädt Daten mit custom SQL, z.B. JOINs zwischen users und sessions
    
    # === Exploratory Data Analysis Functions ===
    "missing_values_summary",  # 🔎 Analysiert Data Quality: Zeigt Missing Values pro Spalte für Data Cleaning


    # Advance Metrics
    'prepare_features', # Bereitet Rohdaten für Feature-Engineering vor
    'BEHAVIOR_FEATURES', # Definiert Verhaltensbezogene Features
    'MINIMAL_FEATURES', # Definiert Minimale Features
    'COMPREHENSIVE_FEATURES', # Definiert Umfassende Features
    'evaluate_feature_sets', # Bewertet verschiedene Feature-Sets anhand von Modellmetriken
    'analyze_feature_importance_pca', # Analysiert Feature-Wichtigkeit mittels PCA
    'correlation_analysis', # Führt Korrelationsanalyse zwischen Features und Zielvariable durch
    'plot_pca_component_heatmap', # Visualisiert PCA-Komponenten als Heatmap
    'plot_2d', # Erstellt 2D Visualisierungen der Daten
    'plot_3d', # Erstellt 3D Visualisierungen der Daten
    # Perks Assignmant Pipeline
    'PerkAssignment', # Klasse zur Durchführung der Perk-Zuweisung basierend auf Nutzersegmenten
    # Segment Analyse
    'SegmentAnalyzer', # Klasse zur Analyse und Visualisierung von Nutzersegmenten
]






"""
VERWENDUNGSBEISPIEL in VS Code:

# Package importieren
from traveltide_analysis import init_connection, load_table, missing_values_summary

# 1. Datenbankverbindung herstellen
conn = init_connection()

# 2. Users-Tabelle laden (1.020.926 Nutzer)
users_df = load_table("users")

# 3. Datenqualität prüfen
missing_summary = missing_values_summary(users_df)
print(missing_summary)  # Zeigt: user_id: 0 missing, birthdate: 0 missing, etc.

# 4. Eigene Query ausführen
query = "SELECT * FROM sessions WHERE flight_booked = true LIMIT 100"
bookings_df = execute_query(query)

STRUCTURE DES PACKAGES in VS Code:
traveltide_analysis/       # Root Package Folder
├── __init__.py           # Dieses File - definiert die öffentliche Schnittstelle
├── utils.py              # Enthält init_connection(), execute_query(), etc.
├── load_data.py          # Enthält load_table(), load_custom_query(), etc.  
├── eda.py                # Enthält missing_values_summary() und andere EDA Tools
└── requirements.txt      # Liste der benötigten Packages (pandas, sqlalchemy, etc.)

VS CODE FEATURES die hier helfen:
• Ctrl+Click auf Funktionen springt zur Definition
• Mouse-over zeigt die Docstrings
• IntelliSense schlägt verfügbare Funktionen vor
• Auto-Import erkennt benötigte Imports
"""