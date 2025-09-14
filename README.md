# 📊 Marketing Intelligence Dashboard  

An interactive **Streamlit dashboard** for analyzing **Business KPIs** and **Marketing Performance** with real-time date filtering and visualizations.  

This project helps track important metrics like revenue, profit, orders, and marketing spend. It provides **insights into trends and performance over time** with a simple and intuitive interface.  

---

## 🚀 Features:

### 🔹 Business Dashboard
- Displays **key metrics**:
  - Total Revenue  
  - Total Gross Profit  
  - Total COGS  
  - no. of Orders  
  - no. of New Orders  
  - New Customers  
- Interactive **date range filter** (Start Date & End Date).  
- **Line charts** for revenue and order trends over time.  

### 🔹 Marketing Dashboard
- Displays **key metrics**:
  - Total Spend  
  - Total Impressions  
  - Total Clicks  
  - Total Conversions  
- Interactive **date range filter** (Start Date & End Date).  
- **Line charts** for spend and conversion trends over time.  
- **Platform-level breakdown** (e.g., Facebook, Google, TikTok) to compare performance.  

### 🔹 Data Handling
- Data is loaded from **CSV files** (`business.csv`, `Google.csv`, `Facebook.csv`, `TikTok.csv`).  
- All the datasets are **date-filtered** between the selected start and end dates.  
- Uses **Plotly** for interactive visualizations and **Streamlit** for UI.  

---

## 🛠️ Tech Stack
- **Python 3.9+**  
- [Streamlit](https://streamlit.io/) – Web App Framework  
- [Pandas](https://pandas.pydata.org/) – Data Manipulation  
- [Plotly Express](https://plotly.com/python/plotly-express/) – Interactive Charts

## 📊 Example KPIs

**Business Dashboard (Example)**  
- 💰 Total Revenue: `$450,000`  
- 📈 Gross Profit: `$180,000`  
- 📦 Orders: `2,300`  

**Marketing Dashboard (Example)**  
- 💸 Total Spend: `$120,000`  
- 👁️ Impressions: `2,500,000`  
- 🖱️ Clicks: `320,000`  
- 🔄 Conversions: `15,000`

  
## ▶️ How to Run  

1. Clone this repository  
   ```bash
   git clone https://github.com/Shruti1Suman/Marketing-Intelligence.git
   cd Marketing-Intelligence
   ```
 2. Create & activate a virtual environment
  ```bash
    python -m venv venv
    venv\Scripts\activate    
```
  3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Run the Streamlit app
   ``` bash
   streamlit run app.py

5. Open the app in your browser at
👉 http://localhost:8501


# Dashboard Link

[Click here!](https://shruti-suman-marketing-intelligence.streamlit.app/)

- https://shruti-suman-marketing-intelligence.streamlit.app/


# 👨‍💻 Author
Shruti Suman ✨
