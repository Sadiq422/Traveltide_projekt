# TravelTide: Kunden-Segmentierung & Vorteils-Zuteilungsplattform


# 📋 Übersicht

TravelTide ist eine umfassende Datenanalyseplattform, die entwickelt wurde, um Rohdaten von Reisediensten in umsetzbare Geschäftsinformationen zu verwandeln. Das Projekt analysiert das Nutzerverhalten, segmentiert Kunden in aussagekräftige Gruppen und weist gezielte Vorteile zu, um das Nutzerengagement und Geschäftsergebnisse zu optimieren. Durch eine Kombination aus Datenverarbeitung, maschinellem Lernen und Visualisierung liefert TravelTide Einblicke in Kund:innenwert, -präferenzen und Interaktionsmuster.

Präsentation und Berichtszusammenfassung befinden sich im Verzeichnis reports/docs.

# 🏗️ Projektarchitektur

````
TravelTide/
├── core/                          # Kern-Python-Module
│   ├── load_data.py               # Datenladen und Vorverarbeitung
│   ├── eda.py                     # Werkzeuge für explorative Datenanalyse (EDA)
│   ├── advance_metrics.py         # Erweiterte Feature-Engineering
│   ├── segment_analyse.py         # Segmentierungsanalyse
│   ├── perk_assignment.py         # Logik für Vorteilszuteilung
│   ├── visualization.py           # Visualisierungs-Hilfsfunktionen
│   └── utils.py                   # Hilfsfunktionen
│
├── data/                          # Datenverwaltung
│   ├── raw/                       # Quelldaten (CSV-Dateien)
│   │   ├── flights.csv
│   │   ├── hotels.csv
│   │   ├── sessions.csv
│   │   └── users.csv
│   │
│   └── processed/                 # Transformierte Datensätze
│       ├── feature_metrics/       # Berechnete Nutzerkennzahlen
│       ├── kmean/                 # K-Means-Clustering-Ergebnisse
│       ├── non_ml/                # Regelbasierte Segmentierung
│       └── pca/                   # Ergebnisse der Dimensionsreduktion
│
├── notebooks/                     # Interaktive Analyse
│   ├── eda.ipynb                  # Erste Datenexploration
│   ├── kmean_cluster.ipynb        # ML-basiertes Clustering
│   ├── segment_analyse.ipynb      # Segmentbewertung
│   ├── perk_assignment.ipynb      # Vorteilsstrategie-Design
│   └── pca_processing.ipynb       # Feature-Raum-Optimierung
│
├── reports/                       # Ausgaben und Visualisierungen
│   ├── eda/viz/                   # Diagramme zur explorativen Analyse
│   └── viz/                       # Grafiken für die finale Präsentation
│
├── sql/                           # Datenbank-Skripte
│   └── session_base.sql
│
├── requirements.txt               # Python-Abhängigkeiten
└── README.md                      # Diese Dokumentation
````

# 🎯 Hauptfunktionen

## Datenintelligenz

- Automatisierte Datenbereinigungs- und Vorverarbeitungspipelines
- Umfassende explorative Datenanalyse (EDA)
- Erweiterte Feature-Engineering und Kennzahlenberechnung
- Ausreißererkennung und statistische Validierung

## Kundensegmentierung

- Maschinelles Lernen Ansatz: K-Means-Clustering mit PCA-Optimierung
- Geschäftsregel-Ansatz: Manuelle Segmentierung basierend auf Kernkennzahlen
- Segmentprofilierung und vergleichende Analyse
- Bewertung der Geschäftsauswirkung für jedes Segment

## Personalisierte Vorteils-Zuteilung

- Datengetriebene Strategien zur Vorteilszuweisung
- ROI-Analyse für die Vorteilszuteilung
- Segment-spezifische Belohnungsoptimierung
- Automatisierte Vorteilszuteilungspipelines

## Visuelle Analytik

- Interaktive Dashboards und Visualisierungen
- Demografische und verhaltensbezogene Analyse-Diagramme
- Segmentvergleichsvisualisierungen
- Berichterstattung über Geschäftsauswirkungen

## Erste Schritte

Voraussetzungen
Python 3.8+

Jupyter Notebook/Lab

# 🛠️ Installation

- Repository klonen
  git clone <repository-url>
  cd TravelTide

- Abhängigkeiten installieren
  pip install -r requirements.txt

- Daten vorbereiten
  Platzieren Sie die Rohdatendateien in data/raw/
  Erforderliche Dateien: flights.csv, hotels.csv, sessions.csv, users.csv


# 🧰 Nutzungsworkflow

- Datenvorbereitung
  Datenverarbeitungspipeline ausführen
  python -m core.load_data

- Explorative Analyse
  Jupyter starten und notebooks/eda.ipynb öffnen
  jupyter notebook

- Kundensegmentierung
  Für ML-basierte Segmentierung: notebooks/kmean_cluster.ipynb
  Für regelbasierte Segmentierung: notebooks/segment_analyse.ipynb

- Vorteils-Zuteilung
  Logik zur Vorteilszuteilung prüfen und ausführen
  python -m core.perk_assignment

- Berichte erstellen
  Visualisierungen und Zusammenfassungen erstellen
  python -m core.visualization


# 📈 Analysemethoden

 Datenverarbeitung

- Sitzungsdatenaggregation und -bereinigung
- Nutzer-Feature-Engineering (Engagement, Ausgaben, Häufigkeitskennzahlen)
- Fehlende Werte-Imputation und Ausreißerbehandlung
- Daten-Normalisierung und Standardisierung

 Segmentierungsansätze

1. K-Means-Clustering
- Ellbogenmethode zur optimalen Clusterbestimmung
- PCA zur Dimensionsreduktion
- Silhouetten-Analyse für Clusterqualität

2. Geschäftsregel-Segmentierung
- RFM-Analyse (Recency, Frequency, Monetary)
- Engagement-Bewertung
- Demografie-basierte Gruppierung

 Logik zur Vorteils-Zuteilung

- Segment-spezifische Vorteilsempfehlungen
- Kosten-Nutzen-Analyse
- Implementierungsszenarien (kostenlos, kostenpflichtig, hybrid)
- Berechnungen der erwarteten Kapitalrendite (ROI)

# 📁 Datenstruktur

 Eingabedaten

- Nutzer:innen: Demografische Informationen und Kontodetails
- Sitzungen: Nutzerinteraktionslogs und Verhaltensverfolgung
- Flüge: Buchungshistorie und Reisemuster
- Hotels: Unterkunftspräferenzen und Ausgaben

 Ausgabedaten

- Nutzer:innensegmente: Clusterzuordnungen und Profile
- Vorteilsempfehlungen: Personalisierte Belohnungsvorschläge
- Analytische Berichte: Geschäftseinblicke und Visualisierungen
- Verarbeitete Features: Erzeugte Kennzahlen für die Analyse

# 📊 Erwartete Ergebnisse

1. Kunden:inneneinblicke
- Hochwertige Nutzer:innensegmente identifizieren
- Verhaltensmuster verstehen
- Nutzer:innenpräferenzen und -bedürfnisse vorhersagen

2. Geschäftsauswirkung

- Optimierte Marketingausgaben durch gezielte Vorteile
- Erhöhtes Nutzer:innenengagement und -bindung
- Datengetriebene Entscheidungsfindung für die Produktentwicklung

3. Operative Effizienz

- Automatisierte Segmentierungspipelines
- Skalierbare Systeme zur Vorteilszuteilung
- Wiederverwendbare analytische Frameworks

# 🤝 Mitwirkung

Wir freuen uns über Beiträge! Bitte folgen Sie diesen Schritten:

- Forken Sie das Repository
- Erstellen Sie einen Feature-Branch (git checkout -b feature/AmazingFeature)
- Committen Sie Ihre Änderungen (git commit -m 'Add AmazingFeature')
- Pushen Sie zum Branch (git push origin feature/AmazingFeature)
- Öffnen Sie einen Pull Request

# 📄 Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert - siehe die LICENSE-Datei für Details.

# 👤 Autor:
Sadiq Qais
<br>
Data Scientist & Analytics Specialist

Inspiration aus der Kundensegmentierungs-Literatur
Open-Source Data-Science-Community


**TravelTide** – Verwandelt Reisendaten durch intelligente Segmentierung und personalisierte Erfahrungen in Kund:innenbegeisterung. ✈️🏨📊




