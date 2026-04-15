# Formula 1 Race Strategy Intelligence
### National School of Technology | DVA Capstone Project | Gate 1

---

## Project Overview
This repository contains the comprehensive data analysis and visualization for the Formula 1 Race Strategy Intelligence project. This study examines the multi-faceted determinants of race outcomes, moving beyond raw car performance to evaluate how strategic execution—including qualifying precision, pit stop efficiency, and circuit-specific tactics—influences a constructor's position in the Championship standings.

---

## Master Documentation
The following documents serve as the primary references for the project's conceptual framework, methodology, and formal proposals:

| Document Title | Access Link | Description |
| :--- | :--- | :--- |
| **Master Project Document** | [View Document](https://docs.google.com/document/d/1rMlTm188s5ELVhODmY1sF_PMzNEJwIwD1xeBISw3xlI/edit?tab=t.0) | Centralized repository for project progress and deep analysis notes. |
| **Gate 1 Project Proposal** | [View Document](https://docs.google.com/document/d/1hgF-8RlZUbNi2d4QI_K483mzBwbZpYF8/edit?usp=sharing&ouid=103256623304686024418&rtpof=true&sd=true) | Formal submission for Gate 1, outlining the problem statement and dataset quality. |

---

## Technical Problem Statement

### Sector Analysis
**Motorsport & Predictive Analytics**

### Contextual Background
Formula 1 constructors inhabit a hyper-competitive, data-saturated environment. For mid-field teams (typically finishing between 4th and 7th in the Constructors' Championship), technical development budgets are often dwarfed by front-running teams. Consequently, tactical optimization—specifically regarding pit stop strategy and circuit-specific maneuvers—becomes the primary differentiator for maximizing season points and associated prize allocations.

### Core Business Question
*What is the measurable impact of starting grid position, pit stop efficiency (duration and frequency), and circuit topography on a driver's final classification? Furthermore, which controllable strategic variables should a mid-field constructor prioritize to optimize point accumulation across a diverse racing calendar?*

### Strategic Decision Support
This analysis is designed to empower Race Strategists to:
1.  **Optimize Pit Strategy:** Determine the statistical efficacy of one-stop vs. two-stop strategies across various circuit categories.
2.  **Resource Allocation:** Quantify the "Points Dividend" of pit crew efficiency improvements versus marginal gains in qualifying pace.
3.  **Benchmarking:** Evaluate the "Grid-to-Finish" performance delta against direct competitors to identify operational strengths and weaknesses.

---

## Team Composition | Section A, Team ID: 4

| Role | Name | GitHub Profile |
| :--- | :--- | :--- |
| **Project Lead** | Mitul Bhatia | [mitul-bhatia](https://github.com/mitul-bhatia) |
| **Data Lead** | Ramani Dhruv Dineshbhai | [DhruvR-16](https://github.com/DhruvR-16) |
| **ETL Lead** | Vetriselvan R | [Vetri-78640](https://github.com/Vetri-78640) |
| **Analysis Lead** | Agrim Kumar Malhotra | [Agrim-2007](https://github.com/Agrim-2007) |
| **Visualization Lead** | Kushal Sarkar | [Kushal425](https://github.com/Kushal425) |
| **Strategy Lead** | Ritik Ranjan | [ritik-beep](https://github.com/ritik-beep) |
| **PPT & Quality Lead** | Palaparthi Harshakarthikeya | [HARSHAKARTHIKEYA1510](https://github.com/HARSHAKARTHIKEYA1510) |

---

## Dataset Methodology
**Primary Source:** [Ergast Formula 1 Motor Racing Database (via Kaggle)](https://www.kaggle.com/datasets/jtrotman/formula-1-race-data)

### Data Analytics Profile
*   **Total Observations:** 726,600+ records across 14 relational entities.
*   **Temporal Coverage:** 1950 – 2026 (76 full seasons).
*   **Dimensionality:** 111 unique attributes.
*   **Key Variables:** `grid` (qualifying position), `position`/`points` (outcomes), `milliseconds` (pit duration), and `circuitId` (spatial grouping).

---

## Preliminary Analytical Framework

### Key Performance Indicators (KPIs)
1.  **Grid-to-Finish Excellence Delta:** A metric calculated as `(Grid Position − Final Finishing Position)`. This isolates race-day execution from pure qualifying pace.
2.  **Operational Efficiency Score:** A seasonally aggregated measure of average pit stop duration per constructor, used to test the correlation between mechanical speed and championship points.

### Hypothesized Insights
We anticipate that qualifying position will remain the dominant predictor of outcome on high-downforce, low-overtaking circuits. Conversely, on power-sensitive circuits with high overtaking frequency, pit stop strategy and efficiency will play a disproportionately larger role in determining final classification.

---

## Project Architecture
```text
├── data/
│   ├── raw/                    # Original Ergast F1 dataset files
│   └── processed/              # Cleaned and engineered feature sets
├── notebooks/
│   ├── 01_extraction.ipynb     # API/CSV data ingestion workflows
│   ├── 02_cleaning.ipynb       # Handling missing values and schema alignment
│   ├── 03_eda.ipynb            # Exploratory analysis and pit stop benchmarking
│   ├── 04_statistical_analysis.ipynb # Hypothesis testing and predictive modeling
│   └── 05_final_load_prep.ipynb # Final prep for Tableau integration
├── scripts/
│   └── etl_pipeline.py         # Automated data processing scripts
├── tableau/
│   ├── screenshots/            # Visual previews of dashboard components
│   └── dashboard_links.md      # Access URLs for interactive Tableau workbooks
├── docs/
│   └── data_dictionary.md      # Detailed mapping of relational variables
├── reports/
│   ├── project_report.pdf      # Comprehensive technical documentation
│   └── presentation.pdf        # Stakeholder presentation deck
├── DVA-focused-Portfolio/       # Project-specific portfolio assets
├── DVA-oriented-Resume/          # Resume tailored for Data Analytics roles
└── README.md                   # Primary project documentation
```

---
© 2026 Formula 1 Race Strategy Intelligence Team. All Rights Reserved.
