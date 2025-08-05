# 🧪 CTA Placement A/B Test – Productivity App

This A/B test simulates how CTA button placement affects user engagement and conversion for a productivity tool like Google Calendar or Calendly. Users were randomly assigned to two groups:
- **Inline CTA**: Button shown after time selection
- **Floating CTA**: Always-visible floating action button

## 📊 Features
- KPI Cards: CTR, Conversion Rate, Revenue per Session, Avg Scroll Depth
- Filters: Device Type, Variant Group
- Visuals:
  - CTR by Variant
  - Conversion Rate by Variant & Device
  - Revenue Distribution by Variant
  - Session Engagement: Scroll vs Duration

## 🧪 Use Cases
- Compare button visibility impacts on CTR and conversion
- Measure scroll & hover as proxy for intent
- Tie test results to business KPIs like revenue and conversion lift

## 🛠 Tools Used
- Python
- Streamlit
- Pandas
- Plotly

## 🚀 How to Run
1. Clone this repo
2. Install requirements: `pip install -r requirements.txt`
3. Run: `streamlit run app.py`

## 📁 Files
- `app.py`: Streamlit dashboard
- `cta_placement_test_data.csv`: Simulated test data
- `requirements.txt`: Dependencies
- `cta_case_study.docx`: Case study summary