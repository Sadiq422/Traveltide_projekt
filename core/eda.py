# core/eda.py
import pandas as pd  # type: ignore
import numpy as np  # type: ignore  # noqa: F401
from datetime import datetime  # type: ignore  # noqa: F401
from IPython.display import display  # type: ignore


def missing_values_summary(df: pd.DataFrame):
    """
    ### Funktion: missing_values_summary
    **Purpose:**
    Zeigt eine Tabelle mit der Anzahl und dem Prozentsatz fehlender
    Werte (NaN) pro Spalte in einem DataFrame.
    **Arguments:**
    - `df` *(pd.DataFrame)* - Eingabe-DataFrame zur Analyse.
    **Returns:**
    - Gibt nichts zurück, zeigt aber eine formatierte Tabelle mit den Spalten:
      - `column`: Name der Spalte
      - `missing_count`: Anzahl fehlender Werte
      - `missing_percent`: Anteil fehlender Werte in Prozent
    **Example:**
    ```python
    missing_values_summary(my_dataframe)
    ```
    """
    # Anzahl fehlender Werte berechnen
    # df.isnull() gibt Boolean DataFrame zurück (True = fehlender Wert)
    # .sum() zählt True-Werte pro Spalte (= Anzahl missing values)
    missing_count = df.isnull().sum()
    
    # Prozentualer Anteil fehlender Werte
    # (Anzahl missing / Gesamtanzahl Zeilen) * 100 für Prozent
    missing_percent = (missing_count / len(df)) * 100
    
    # DataFrame für die Anzeige erstellen
    # Kombiniert Spaltennamen mit missing counts und percentages
    missing_df = pd.DataFrame({
        'column': df.columns,           # Spaltennamen des Original-DataFrames
        'missing_count': missing_count,  # Absolute Anzahl fehlender Werte
        'missing_percent': missing_percent.round(2)  # Prozent auf 2 Dezimalstellen gerundet
    })

    # AUSKOMMENTIERT: Filter für nur Spalten mit fehlenden Werten
    # Diese Zeile würde nur Spalten anzeigen, die mindestens 1 missing value haben
    # missing_df = missing_df[
    # missing_df['missing_count'] > 0
    # ].reset_index(drop=True)
    
    # Tabelle im Jupyter Notebook anzeigen
    # display() zeigt den DataFrame formatiert an statt print()
    display(missing_df)

# Beispiel wie die Ausgabe aussieht:
"""
     column  missing_count  missing_percent
0    user_id              0             0.00
1  birthdate              0             0.00
2     gender              0             0.00
3    married              0             0.00
4     trip_id         3072218           56.81  ← z.B. 56.81% fehlende trip_ids
"""