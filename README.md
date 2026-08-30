# 🌍 GreenCloud-AI: Intelligent Sustainable Cloud Resource Management

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-Active-lightgrey.svg)
![Machine Learning](https://img.shields.io/badge/ML-Scikit--Learn-orange.svg)
![Status](https://img.shields.io/badge/Status-Beta_V1-emerald.svg)

## 📌 Project Overview
**GreenCloud-AI** is designed to drastically reduce the carbon footprint and energy consumption of cloud data centers. By leveraging predictive machine learning models, the system dynamically forecasts workloads, seamlessly consolidates Virtual Machines (VMs), and intelligently scales cooling systems.

Data centers currently waste massive amounts of electricity powering and cooling underutilized servers. GreenCloud-AI acts as an intelligent load balancer—forecasting compute needs, packing active tasks onto the minimum required physical servers, and securely powering down idle nodes.

---

## ⚙️ System Architecture & Workflow

1. **Data Ingestion (Telemetry):** Continuous collection of real-time metrics (CPU utilization, memory allocation, thermal output, power draw).
2. **AI-Driven Forecasting:** Machine Learning models analyze historical traffic to predict impending workload spikes or drops.
3. **Dynamic Resource Optimization:**
   * **VM Consolidation:** Migrating active VMs to high-density nodes.
   * **Idle Node Shutdown:** Transitioning empty servers into deep-sleep states.
   * **Cooling Adjustments:** Scaling CRAC units based on predictive heat maps.
4. **Live SOC Dashboard:** Real-time visualization of automated decisions, PUE metrics, and carbon savings.

---

## 🛠️ Technology Stack & Team Structure

This project is divided into three core functional pillars:

* **UI/UX & Machine Learning Core (Ishant Thakur):** 
  * *Tech:* Scikit-learn (Random Forest Regressor), Flask, JavaScript, Tailwind CSS, Chart.js.
  * *Focus:* Predictive modeling, real-time API endpoints, and the interactive Security/System Operations Center (SOC) dashboard.
* **Backend & Data Pipeline (Sheetal):** 
  * *Tech:* PostgreSQL / SQLite, Python Data Routing.
  * *Focus:* Storing telemetry data influx and maintaining the data cleaning pipeline.
* **Cloud Mechanics & Research (Arohi):** 
  * *Focus:* Mathematical modeling for energy consumption, VM migration protocols, and academic documentation for ICITCBT'26.

---

## 🚀 Running the Local MVP Demo

This repository currently contains the **V1 Interactive Prototype**, which utilizes synthetic telemetry generation and a live ML model to simulate data center optimization.

### Prerequisites
* Python 3.8+
* `pip` package manager

### Quick Start
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Ishant1821/GreenCloud_Beta_V1.git](https://github.com/Ishant1821/GreenCloud_Beta_V1.git)
   cd GreenCloud_Beta_V1