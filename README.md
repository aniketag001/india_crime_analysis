# **Caste-Based Crime Insights in India**

## **Introduction**  
This project provides a comprehensive platform for analyzing caste-based hate crimes across India. It visualizes crime patterns over the years, highlights correlations, and allows users to explore state-wise and category-wise data through an interactive and user-friendly interface. The platform aims to help identify areas requiring intervention to combat caste-based discrimination effectively.

---

## **Project Type**  
**Fullstack**  

---

## **Deployed App**  
- **Frontend:** [Website](https://crimeinsight.streamlit.app)  
- **Backend:** Not Applicable (handled via Streamlit)  
- **Database:** CSV files used as the primary data source  

---

## **Directory Structure**  
```
project/
├─ data/
│  ├─ crime_by_state_rt.csv
│  ├─ india_literacy_rate.csv
│  ├─ population_of_india.csv
├─ src/
│  ├─ app.py
│  ├─ dashboard_visualization.py (Interactive dashboard enabler code via Streamlit)
|  ├─ kpi_visualization.py (Key Performance Indicators metrics calculation code)
|  ├─ utils.py (Data handeling functions)
```

## Video Walkthrough of the Project
Attach a very short video walkthrough of all features (1–3 minutes).

## Video Walkthrough of the Codebase
Attach a very short video walkthrough of the codebase (1–5 minutes).

## Features
List out the key features of your application:
- Feature 1
- Feature 2
- Feature 3

## Design Decisions or Assumptions
List your design decisions and assumptions.

## Installation & Getting Started | Setup the project in VS Code from Github
Detailed instructions on how to install, configure, and get the project running. For Backend/Fullstack projects, guide the reviewer on how to check the MongoDB schema, etc.

### How to clone a github repository
```
git clone https://github.com/sakshitechworld/india_crime_analysis.git
```

### How to publish your changes to Github
```
git add .
git commit -m "[Message]"
git push
```
<br>

## Streamlit
### How to test your code with Streamlit Locally?
```
conda activate .conda/
streamlit run src/app.py
```
<br>

### Deployment | How does the code get deployed to Streamlit cloud?
Streamlit cloud is connected with `main` branch of github, hence as soon as the code is committed in the `main` branch, it will be deployed to the cloud and the app will be available at https://crimeinsight.streamlit.app
<br>
