# TravelTide: Customer Segmentation & Perk Assignment Platform

## 📋 Overview

TravelTide is a comprehensive data analysis platform designed to transform raw travel service data into actionable business intelligence. The project analyzes user behavior, segments customers into meaningful clusters, and assigns targeted perks to optimize user engagement and business outcomes. Through a combination of data processing, machine learning, and visualization, TravelTide provides insights into customer value, preferences, and interaction patterns.

## 🏗️ Project Architecture

´´´
TravelTide/
├── core/                          # Core Python modules
│   ├── load_data.py               # Data loading and preprocessing
│   ├── eda.py                     # Exploratory data analysis tools
│   ├── advance_metrics.py         # Advanced feature engineering
│   ├── segment_analyse.py         # Segmentation analysis
│   ├── perk_assignment.py         # Perk allocation logic
│   ├── visualization.py           # Visualization utilities
│   └── utils.py                   # Helper functions
│
├── data/                          # Data management
│   ├── raw/                       # Source data (CSV files)
│   │   ├── flights.csv
│   │   ├── hotels.csv
│   │   ├── sessions.csv
│   │   └── users.csv
│   │
│   └── processed/                 # Transformed datasets
│       ├── feature_metrics/       # Calculated user metrics
│       ├── kmean/                 # K-means clustering results
│       ├── non_ml/                # Rule-based segmentation
│       └── pca/                   # Dimensionality reduction outputs
│
├── notebooks/                      # Interactive analysis
│   ├── eda.ipynb                  # Initial data exploration
│   ├── kmean_cluster.ipynb        # ML-based clustering
│   ├── segment_analyse.ipynb      # Segment evaluation
│   ├── perk_assignment.ipynb      # Perk strategy design
│   └── pca_processing.ipynb       # Feature space optimization
│
├── reports/                       # Outputs and visualizations
│   ├── eda/viz/                   # Exploratory analysis charts
│   └── viz/                       # Final presentation graphics
│
├── sql/                           # Database scripts
│   └── session_base.sql
│
├── requirements.txt               # Python dependencies
└── README.md                      # This documentation
´´´

## 🎯 Key Features

### 🔍 **Data Intelligence**
- Automated data cleaning and preprocessing pipelines
- Comprehensive exploratory data analysis (EDA)
- Advanced feature engineering and metric calculation
- Outlier detection and statistical validation

### 👥 **Customer Segmentation**
- **Machine Learning Approach**: K-means clustering with PCA optimization
- **Business Rules Approach**: Manual segmentation based on key metrics
- Segment profiling and comparative analysis
- Business impact assessment for each segment

### 🎁 **Personalized Perk Assignment**
- Data-driven perk allocation strategies
- ROI analysis for perk assignment
- Segment-specific reward optimization
- Automated perk assignment pipelines

### 📊 **Visual Analytics**
- Interactive dashboards and visualizations
- Demographic and behavioral analysis charts
- Segment comparison visualizations
- Business impact reporting

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Jupyter Notebook/Lab

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd TravelTide
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare your data**
   - Place raw data files in `data/raw/`
   - Files required: `flights.csv`, `hotels.csv`, `sessions.csv`, `users.csv`

### Usage Workflow

1. **Data Preparation**
   ```bash
   # Run data processing pipeline
   python -m core.load_data
   ```

2. **Exploratory Analysis**
   ```bash
   # Launch Jupyter and open notebooks/eda.ipynb
   jupyter notebook
   ```

3. **Customer Segmentation**
   - For ML-based segmentation: `notebooks/kmean_cluster.ipynb`
   - For rule-based segmentation: `notebooks/segment_analyse.ipynb`

4. **Perk Assignment**
   ```bash
   # Review and execute perk assignment logic
   python -m core.perk_assignment
   ```

5. **Generate Reports**
   ```bash
   # Create visualizations and summaries
   python -m core.visualization
   ```

## 📈 Analytical Methodologies

### Data Processing
- Session data aggregation and cleaning
- User feature engineering (engagement, spending, frequency metrics)
- Missing value imputation and outlier handling
- Data normalization and standardization

### Segmentation Approaches
1. **K-means Clustering**
   - Elbow method for optimal cluster determination
   - PCA for dimensionality reduction
   - Silhouette analysis for cluster quality

2. **Business Rule Segmentation**
   - RFM (Recency, Frequency, Monetary) analysis
   - Engagement scoring
   - Demographic-based grouping

### Perk Assignment Logic
- Segment-specific perk recommendations
- Cost-benefit analysis
- Implementation scenarios (free, paid, hybrid)
- Expected ROI calculations

## 📁 Data Structure

### Input Data
- **Users**: Demographic information and account details
- **Sessions**: User interaction logs and behavior tracking
- **Flights**: Booking history and travel patterns
- **Hotels**: Accommodation preferences and spending

### Output Data
- **User Segments**: Cluster assignments and profiles
- **Perk Recommendations**: Personalized reward suggestions
- **Analytical Reports**: Business insights and visualizations
- **Processed Features**: Engineered metrics for analysis

## 📊 Expected Outcomes

1. **Customer Insights**
   - Identify high-value user segments
   - Understand behavioral patterns
   - Predict user preferences and needs

2. **Business Impact**
   - Optimized marketing spend through targeted perks
   - Increased user engagement and retention
   - Data-driven decision making for product development

3. **Operational Efficiency**
   - Automated segmentation pipelines
   - Scalable perk assignment systems
   - Reusable analytical frameworks

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Sadiq Qais**  
*Data Scientist & Analytics Specialist*

## 🙏 Acknowledgments

- Data provided by TravelTide analytics team
- Inspiration from customer segmentation literature
- Open-source data science community

---

**TravelTide** – Transforming travel data into customer delight through intelligent segmentation and personalized experiences. ✈️🏨📊