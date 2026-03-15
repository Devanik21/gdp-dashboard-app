# GDP Dashboard APP

![Language](https://img.shields.io/badge/Language-Python-3776AB?style=flat-square) ![Stars](https://img.shields.io/github/stars/Devanik21/gdp-dashboard-app?style=flat-square&color=yellow) ![Forks](https://img.shields.io/github/forks/Devanik21/gdp-dashboard-app?style=flat-square&color=blue) ![Author](https://img.shields.io/badge/Author-Devanik21-black?style=flat-square&logo=github) ![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

> Global economic intelligence — explore GDP trends, per-capita output, and growth dynamics across 200+ countries.

---

**Topics:** `data-science` · `data-visualization` · `economic-analysis` · `gdp-forecasting` · `machine-learning` · `macroeconomic-indicators` · `pandas` · `plotly` · `python` · `streamlit`

## Overview

This GDP Dashboard is a multi-country economic analysis tool built with Streamlit and Plotly, powered by World Bank Open Data. It provides an interactive environment for exploring national and regional GDP metrics across multiple dimensions: total GDP (nominal and PPP-adjusted), GDP per capita, annual growth rates, and decade-level trend analysis — all with configurable country and year range selections.

The application is designed for economists, policy researchers, students, and anyone interested in understanding the dynamics of global economic output. It supports multi-country comparison, allowing users to overlay growth curves for selected economies on a single chart — revealing patterns like the 2008 financial crisis, the COVID-19 shock, and differential recovery trajectories across income groups.

A regional aggregation view groups countries by World Bank income classification (Low, Lower-Middle, Upper-Middle, High) and plots aggregate GDP dynamics for each group, making structural development patterns immediately visible.

---

## Motivation

Economic data is publicly available but rarely presented in a form that invites exploration. Existing tools like the World Bank DataBank are powerful but not designed for fluid, interactive storytelling. This project was built to create a data journalism-style interface that makes macroeconomic data as engaging to explore as it is informative.

---

## Architecture

```
World Bank API (wbdata) or local CSV
        │
  pandas: reshaping, pivot tables, growth rate computation
        │
  Plotly: choropleth, line charts, bar charts
        │
  Streamlit: multi-select widgets, year range slider
        │
  Optional: statsmodels ARIMA trend projection
```

---

## Features

### Multi-Country GDP Comparison
Overlay GDP trend lines for any combination of countries on a single Plotly chart, with log-scale toggle for comparing economies of vastly different sizes.

### Per-Capita GDP Choropleth
World map with countries coloured by GDP per capita (current USD or PPP-adjusted), with year slider animation and hover-to-detail tooltips.

### Annual Growth Rate Analysis
Bar chart of year-on-year GDP growth rates with recession years highlighted in red, supporting configurable time windows and multi-country comparison.

### Regional Income Group Aggregation
Line charts of aggregate GDP for World Bank income groups (Low / Lower-Middle / Upper-Middle / High), showing structural development divergence over decades.

### PPP vs. Nominal Toggle
Switch between nominal GDP (current USD) and Purchasing Power Parity-adjusted GDP, with a side-by-side comparison mode to illustrate the difference.

### Decade Summary Statistics
Statistical summary table: mean, median, min, max, and CAGR for each selected country across configurable decade windows.

### Data Export
Download the filtered, reshaped GDP DataFrame as a CSV file with all computed indicators for use in external analysis.

### Trend Projection (Optional)
Short-term GDP growth projection using ARIMA or simple linear extrapolation, clearly marked as modelled estimates with confidence bands.

---

## Tech Stack

| Library / Tool | Role | Why This Choice |
|---|---|---|
| **Streamlit** | Dashboard UI | Multi-select widgets, sliders, layout |
| **pandas** | Data reshaping | Pivot tables, growth rate computation, filtering |
| **Plotly** | Interactive charts | Choropleth, multi-line, bar charts |
| **wbdata (optional)** | World Bank API | Live GDP data fetching |
| **NumPy** | Statistical computation | CAGR, growth rate arrays |
| **statsmodels (optional)** | Trend projection | ARIMA GDP forecasting |

> **Key packages detected in this repo:** `scikit-learn` · `numpy` · `pandas` · `matplotlib` · `seaborn` · `scipy` · `xgboost` · `lightgbm` · `catboost` · `tensorflow`

---

## Getting Started

### Prerequisites

- Python 3.9+ (or Node.js 18+ for TypeScript/JS projects)
- `pip` or `npm` package manager
- Relevant API keys (see Configuration section)

### Installation

```bash
git clone https://github.com/Devanik21/gdp-dashboard-app.git
cd gdp-dashboard-app
python -m venv venv && source venv/bin/activate
pip install streamlit pandas plotly numpy wbdata
streamlit run app.py
```

---

## Usage

```bash
streamlit run app.py

# Fetch fresh World Bank data
python fetch_data.py --indicators NY.GDP.MKTP.CD NY.GDP.PCAP.CD

# Export analysis
python export_report.py --countries IND,CHN,USA --years 2000-2023
```

---

## Configuration

| Variable | Default | Description |
|---|---|---|
| `DATA_SOURCE` | `world_bank_gdp.csv` | Local CSV or 'api' for live World Bank fetch |
| `DEFAULT_COUNTRIES` | `IND,CHN,USA,DEU` | Pre-selected countries on load |
| `DEFAULT_YEAR_RANGE` | `2000-2023` | Default year range for charts |
| `PPP_DEFAULT` | `False` | Use PPP-adjusted GDP by default |

> Copy `.env.example` to `.env` and populate all required values before running.

---

## Project Structure

```
gdp-dashboard-app/
├── README.md
├── requirements.txt
├── gdp_dashboard.py
├── GDP.csv
└── ...
```

---

## Roadmap

- [ ] Animated bubble chart (GDP vs. per-capita vs. population) in the style of Hans Rosling's Gapminder
- [ ] Sectoral GDP breakdown (agriculture, industry, services) per country
- [ ] Correlation analysis between GDP growth and HDI, Gini coefficient, trade openness
- [ ] News event overlay: annotate major economic shocks (GFC, COVID, oil crises) on the timeline
- [ ] Prediction competition mode: guess the growth rate before revealing the actual

---

## Contributing

Contributions, issues, and feature requests are welcome. Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'feat: add your feature'`)
4. Push to your branch (`git push origin feature/your-feature`)
5. Open a Pull Request

Please follow conventional commit messages and ensure any new code is documented.

---

## Notes

GDP data is sourced from the World Bank Open Data platform. Values are in current USD unless PPP mode is selected. Data availability varies by country and year.

---

## Author

**Devanik Debnath**  
B.Tech, Electronics & Communication Engineering  
National Institute of Technology Agartala

[![GitHub](https://img.shields.io/badge/GitHub-Devanik21-black?style=flat-square&logo=github)](https://github.com/Devanik21)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-devanik-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/devanik/)

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

*Crafted with curiosity, precision, and a belief that good software is worth building well.*
