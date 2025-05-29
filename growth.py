# import streamlit as st
# import numpy as np
# import matplotlib.pyplot as plt

# st.set_page_config(page_title="Child Growth Chart", layout="wide")

# def local_css():
#     st.markdown("""
#     <style>
#         @import url('https://fonts.googleapis.com/css2?family=Lexend:wght@500&display=swap');
#         html, body, [class*="stApp"] {
#             font-family: 'Lexend', Arial, sans-serif !important;
#             font-weight: 500 !important;
#             font-size: 1.08rem;
#             color: #22304a;
#         }
#         :root {
#             --primary: #2563eb;
#             --secondary: #38bdf8;
#             --accent: #22c55e;
#             --background: #f4faff;
#             --card: #ffffff;
#             --text: #22304a;
#             --text-light: #4A5568;
#             --warning: #ef4444;
#             --success: #22c55e;
#             --info: #2563eb;
#             --border-radius: 16px;
#             --box-shadow: 0 4px 24px rgba(37, 99, 235, 0.08);
#             --transition: all 0.2s cubic-bezier(.4,0,.2,1);
#         }
#         .stApp {
#             background-color: var(--background) !important;
#         }
#         .main .block-container {
#             background-color: var(--background);
#             padding-top: 2rem;
#             padding-bottom: 2rem;
#         }
#         .header-container {
#             background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
#             padding: 2.5rem 1.5rem;
#             border-radius: var(--border-radius);
#             margin-bottom: 2rem;
#             box-shadow: var(--box-shadow);
#             color: #fff;
#             text-align: center;
#             position: relative;
#             overflow: hidden;
#         }
#         .header-container h1, .header-container p {
#             color: #fff !important;
#             font-family: 'Lexend', Arial, sans-serif !important;
#             font-weight: 500 !important;
#         }
#         .card {
#             background: var(--card);
#             border-radius: var(--border-radius);
#             box-shadow: var(--box-shadow);
#             padding: 1.5rem 1.5rem 1.2rem 1.5rem;
#             margin-bottom: 1.2rem;
#             border: 1px solid #e3eaf3;
#             font-family: 'Lexend', Arial, sans-serif !important;
#             font-weight: 500 !important;
#         }
#         .info-box {
#             background-color: #e0f2fe;
#             border-left: 6px solid #38bdf8;
#             padding: 1rem;
#             border-radius: var(--border-radius);
#             margin-bottom: 1.5rem;
#         }
#         .info-box h3 {
#             margin-top: 0;
#             color: #0c4a6e;
#         }
#         .results-summary {
#             background: var(--card);
#             border-radius: var(--border-radius);
#             box-shadow: var(--box-shadow);
#             padding: 1.5rem;
#             margin-bottom: 2rem;
#             border: 1px solid #e3eaf3;
#         }
#         .results-summary h2 {
#             color: var(--primary);
#             margin-top: 0;
#             margin-bottom: 1.5rem;
#             font-size: 1.5rem;
#         }
#         .results-grid {
#             display: grid;
#             grid-template-columns: 1fr 1fr;
#             gap: 1.5rem;
#         }
#         .result-card {
#             background: #f8fafc;
#             border-radius: 12px;
#             padding: 1.2rem;
#             border: 1px solid #e2e8f0;
#         }
#         .result-card h3 {
#             margin-top: 0;
#             margin-bottom: 0.8rem;
#             font-size: 1.1rem;
#             color: var(--text);
#         }
#         .result-value {
#             font-size: 1.5rem;
#             font-weight: 700;
#             color: var(--primary);
#             margin-bottom: 0.5rem;
#         }
#         .result-range {
#             color: var(--text-light);
#             font-size: 0.95rem;
#             margin-bottom: 0.5rem;
#         }
#         .result-status {
#             display: inline-block;
#             padding: 0.3rem 0.8rem;
#             border-radius: 20px;
#             font-size: 0.9rem;
#             font-weight: 600;
#         }
#         .status-normal {
#             background-color: #dcfce7;
#             color: #166534;
#         }
#         .status-below {
#             background-color: #fee2e2;
#             color: #991b1b;
#         }
#         .status-above {
#             background-color: #dbeafe;
#             color: #1e40af;
#         }
#         .stButton>button {
#             background: linear-gradient(90deg, var(--primary) 60%, var(--secondary) 100%);
#             color: #fff !important;
#             font-size: 1.13rem;
#             font-weight: 700;
#             border-radius: var(--border-radius);
#             padding: 0.85rem 2.2rem;
#             border: none;
#             box-shadow: 0 2px 8px rgba(37, 99, 235, 0.10);
#             transition: var(--transition);
#             letter-spacing: 0.01em;
#             outline: none !important;
#             font-family: 'Lexend', Arial, sans-serif !important;
#         }
#         .stButton>button:hover, .stButton>button:focus {
#             background: linear-gradient(90deg, var(--secondary) 0%, var(--primary) 100%);
#             color: #fff !important;
#             box-shadow: 0 4px 16px rgba(37, 99, 235, 0.18);
#             transform: translateY(-2px) scale(1.03);
#         }
#         .stButton>button:active {
#             transform: scale(0.98);
#         }
#         .stSelectbox > div > div > select,
#         .stNumberInput > div > div > input {
#             border-radius: var(--border-radius) !important;
#             padding: 12px 14px !important;
#             border: 1.5px solid #dbeafe !important;
#             font-size: 1.15rem !important;
#             color: var(--text) !important;
#             background: #fff;
#             transition: var(--transition);
#             font-family: 'Lexend', Arial, sans-serif !important;
#             font-weight: 500 !important;
#             height: 3.5rem !important;
#         }
#         .stSelectbox > div > div > select option {
#             color: var(--text) !important;
#             background: #fff !important;
#         }
#         .stSelectbox > div > div > select:focus,
#         .stNumberInput > div > div > input:focus {
#             border-color: var(--primary) !important;
#             box-shadow: 0 0 0 2px rgba(37, 99, 235, 0.13) !important;
#             color: var(--text) !important;
#         }
#         .stPlotlyChart {
#             background: var(--card);
#             border-radius: var(--border-radius);
#             box-shadow: var(--box-shadow);
#             padding: 1rem;
#             margin-bottom: 1.2rem;
#         }
#         @media (max-width: 768px) {
#             .header-container {
#                 padding: 1.5rem 0.5rem;
#             }
#             .card {
#                 padding: 1rem;
#             }
#             .results-grid {
#                 grid-template-columns: 1fr;
#             }
#             .stButton>button {
#                 padding: 0.7rem 1.2rem;
#                 font-size: 1rem;
#             }
#         }
#     </style>
#     """, unsafe_allow_html=True)

# # Dummy percentile curves (simplified WHO-like format)
# def get_weight_for_age_curves(gender):
#     months = np.arange(0, 61)
#     base = 3.2 if gender == "Male" else 3.0
#     return {
#         "months": months,
#         "3rd": base + 0.3 * months + 0.001 * months**2,
#         "15th": base + 0.35 * months + 0.0015 * months**2,
#         "50th": base + 0.42 * months + 0.002 * months**2,
#         "85th": base + 0.49 * months + 0.0025 * months**2,
#         "97th": base + 0.55 * months + 0.003 * months**2,
#     }

# def get_height_for_age_curves(gender):
#     months = np.arange(0, 61)
#     base = 49.9 if gender == "Male" else 49.1
#     return {
#         "months": months,
#         "3rd": base + 0.7 * months + 0.01 * months**2,
#         "15th": base + 0.75 * months + 0.015 * months**2,
#         "50th": base + 0.8 * months + 0.02 * months**2,
#         "85th": base + 0.85 * months + 0.025 * months**2,
#         "97th": base + 0.9 * months + 0.03 * months**2,
#     }

# def get_weight_for_height_curves(gender):
#     heights = np.arange(45, 120)
#     base = 2.5 if gender == "Male" else 2.3
#     return {
#         "heights": heights,
#         "3rd": base + 0.1 * (heights - 45) + 0.001 * (heights - 45)**2,
#         "15th": base + 0.13 * (heights - 45) + 0.0015 * (heights - 45)**2,
#         "50th": base + 0.15 * (heights - 45) + 0.002 * (heights - 45)**2,
#         "85th": base + 0.18 * (heights - 45) + 0.0025 * (heights - 45)**2,
#         "97th": base + 0.20 * (heights - 45) + 0.003 * (heights - 45)**2,
#     }

# # Function to get normal ranges based on age and gender
# def get_normal_ranges(age, gender):
#     # These are simplified examples - in a real app you would use actual growth chart data
#     if gender == "Male":
#         if age < 12:
#             weight_range = "3.5 - 10.5 kg"
#             height_range = "55 - 75 cm"
#         elif age < 24:
#             weight_range = "8.5 - 13.5 kg"
#             height_range = "73 - 88 cm"
#         elif age < 36:
#             weight_range = "10.5 - 16.0 kg"
#             height_range = "83 - 97 cm"
#         elif age < 48:
#             weight_range = "12.0 - 18.5 kg"
#             height_range = "90 - 105 cm"
#         else:
#             weight_range = "14.0 - 21.0 kg"
#             height_range = "97 - 112 cm"
#     else:  # Female
#         if age < 12:
#             weight_range = "3.2 - 9.8 kg"
#             height_range = "54 - 73 cm"
#         elif age < 24:
#             weight_range = "7.8 - 12.8 kg"
#             height_range = "71 - 86 cm"
#         elif age < 36:
#             weight_range = "9.8 - 15.5 kg"
#             height_range = "81 - 96 cm"
#         elif age < 48:
#             weight_range = "11.5 - 17.5 kg"
#             height_range = "88 - 104 cm"
#         else:
#             weight_range = "13.5 - 20.5 kg"
#             height_range = "95 - 111 cm"
    
#     return weight_range, height_range

# # Function to determine status (simplified for demo)
# def get_status(value, low, high):
#     if value < low:
#         return "Below normal range", "status-below"
#     elif value > high:
#         return "Above normal range", "status-above"
#     else:
#         return "Within normal range", "status-normal"

# # Apply custom CSS
# local_css()

# # Header with gradient
# st.markdown("""
# <div class="header-container">
#     <h1 style="margin:0;padding:0;">👶 Child Growth Chart Visualizer</h1>
#     <p style="margin:0;padding-top:0.5rem;font-size:1.1rem;">Track your child's growth and development</p>
# </div>
# """, unsafe_allow_html=True)

# # Input section in a card
# st.markdown('<div class="card">', unsafe_allow_html=True)
# st.markdown('<h2 style="color: var(--primary); margin-bottom: 1.5rem;">Enter Child\'s Information</h2>', unsafe_allow_html=True)

# col1, col2 = st.columns(2)
# with col1:
#     gender = st.radio("Gender", ["Male", "Female"])
#     age = st.number_input("Age (months)", min_value=0, max_value=60, step=1)
# with col2:
#     weight = st.number_input("Weight (kg)", min_value=2.0, max_value=30.0, step=0.1)
#     height = st.number_input("Height (cm)", min_value=45.0, max_value=120.0, step=0.1)

# show = st.button("Plot Growth Charts", use_container_width=True)
# st.markdown('</div>', unsafe_allow_html=True)

# if show:
#     color = "blue" if gender == "Male" else "deeppink"
    
#     # Get normal ranges
#     weight_range, height_range = get_normal_ranges(age, gender)
    
#     # Parse the ranges to get low and high values (simplified for demo)
#     try:
#         weight_low, weight_high = map(float, weight_range.split(" - "))
#         height_low, height_high = map(float, height_range.split(" - "))
#     except:
#         weight_low, weight_high = 3.0, 10.0
#         height_low, height_high = 50.0, 80.0
    
#     # Get status for each measurement
#     weight_status, weight_status_class = get_status(weight, weight_low, weight_high)
#     height_status, height_status_class = get_status(height, height_low, height_high)
    
#     # Display the results summary in a visually appealing card
#     st.markdown("""
#     <div class="results-summary">
#         <h2>📊 Your Child's Growth Summary</h2>
#         <div class="results-grid">
#             <div class="result-card">
#                 <h3>Weight</h3>
#                 <div class="result-value">{weight:.1f} kg</div>
#                 <div class="result-range">Normal range for {gender}, {age} months: {weight_range}</div>
#                 <div class="result-status {weight_status_class}">{weight_status}</div>
#             </div>
#             <div class="result-card">
#                 <h3>Height</h3>
#                 <div class="result-value">{height:.1f} cm</div>
#                 <div class="result-range">Normal range for {gender}, {age} months: {height_range}</div>
#                 <div class="result-status {height_status_class}">{height_status}</div>
#             </div>
#         </div>
#         <p style="margin-top: 1.5rem; font-size: 0.95rem; color: var(--text-light);">
#         Note: These ranges are approximate based on WHO growth standards. Individual growth patterns may vary. 
#         Consult your pediatrician for a professional assessment.
#         </p>
#     </div>
#     """.format(
#         weight=weight, 
#         height=height, 
#         gender=gender.lower(), 
#         age=age, 
#         weight_range=weight_range, 
#         height_range=height_range,
#         weight_status=weight_status,
#         weight_status_class=weight_status_class,
#         height_status=height_status,
#         height_status_class=height_status_class
#     ), unsafe_allow_html=True)

#     # --- Plot Charts ---
#     data_weight_age = get_weight_for_age_curves(gender)
#     data_height_age = get_height_for_age_curves(gender)
#     data_weight_height = get_weight_for_height_curves(gender)

#     # Plot Weight-for-Age
#     fig1, ax1 = plt.subplots(figsize=(8, 5))
#     for key in ['3rd', '15th', '50th', '85th', '97th']:
#         ax1.plot(data_weight_age["months"], data_weight_age[key], label=f"{key} percentile", linestyle='--' if key != "50th" else '-', color='gray' if key != "50th" else 'orange')
#     ax1.scatter(age, weight, color=color, label="Your child", zorder=5, s=100)
#     ax1.set_title("Weight-for-Age", fontsize=14, fontweight='bold', pad=20)
#     ax1.set_xlabel("Age (months)", fontsize=12)
#     ax1.set_ylabel("Weight (kg)", fontsize=12)
#     ax1.legend(fontsize=10)
#     ax1.grid(True, alpha=0.3)
#     plt.tight_layout()

#     # Plot Height-for-Age
#     fig2, ax2 = plt.subplots(figsize=(8, 5))
#     for key in ['3rd', '15th', '50th', '85th', '97th']:
#         ax2.plot(data_height_age["months"], data_height_age[key], label=f"{key} percentile", linestyle='--' if key != "50th" else '-', color='gray' if key != "50th" else 'orange')
#     ax2.scatter(age, height, color=color, label="Your child", zorder=5, s=100)
#     ax2.set_title("Height-for-Age", fontsize=14, fontweight='bold', pad=20)
#     ax2.set_xlabel("Age (months)", fontsize=12)
#     ax2.set_ylabel("Height (cm)", fontsize=12)
#     ax2.legend(fontsize=10)
#     ax2.grid(True, alpha=0.3)
#     plt.tight_layout()

#     # Plot Weight-for-Height
#     fig3, ax3 = plt.subplots(figsize=(8, 5))
#     for key in ['3rd', '15th', '50th', '85th', '97th']:
#         ax3.plot(data_weight_height["heights"], data_weight_height[key], label=f"{key} percentile", linestyle='--' if key != "50th" else '-', color='gray' if key != "50th" else 'orange')
#     ax3.scatter(height, weight, color=color, label="Your child", zorder=5, s=100)
#     ax3.set_title("Weight-for-Height", fontsize=14, fontweight='bold', pad=20)
#     ax3.set_xlabel("Height (cm)", fontsize=12)
#     ax3.set_ylabel("Weight (kg)", fontsize=12)
#     ax3.legend(fontsize=10)
#     ax3.grid(True, alpha=0.3)
#     plt.tight_layout()

#     # Display in two columns
#     st.markdown('<h2 style="color: var(--primary); margin-top: 2rem;">Growth Charts</h2>', unsafe_allow_html=True)
#     col1, col2 = st.columns(2)
#     with col1:
#         st.pyplot(fig1)
#         st.pyplot(fig3)
#     with col2:
#         st.pyplot(fig2)

# # Footer
# st.markdown("""
# <div class="footer">
#     <p>Child Growth Chart Visualizer | Based on WHO Growth Standards</p>
#     <p>For informational purposes only. Consult your healthcare provider for medical advice.</p>
# </div>
# """, unsafe_allow_html=True)

# import streamlit as st
# import numpy as np
# import matplotlib.pyplot as plt

# st.set_page_config(page_title="Child Growth Chart", layout="wide")

# def local_css():
#     st.markdown("""
#     <style>
#         @import url('https://fonts.googleapis.com/css2?family=Lexend:wght@500&display=swap');
#         html, body, [class*="stApp"] {
#             font-family: 'Lexend', Arial, sans-serif !important;
#             font-weight: 500 !important;
#             font-size: 1.08rem;
#             color: #22304a;
#         }
#         :root {
#             --primary: #2563eb;
#             --secondary: #38bdf8;
#             --accent: #22c55e;
#             --background: #f4faff;
#             --card: #ffffff;
#             --text: #22304a;
#             --text-light: #4A5568;
#             --warning: #ef4444;
#             --success: #22c55e;
#             --info: #2563eb;
#             --border-radius: 16px;
#             --box-shadow: 0 4px 24px rgba(37, 99, 235, 0.08);
#             --transition: all 0.2s cubic-bezier(.4,0,.2,1);
#         }
#         .stApp {
#             background-color: var(--background) !important;
#         }
#         .main .block-container {
#             background-color: var(--background);
#             padding-top: 2rem;
#             padding-bottom: 2rem;
#         }
#         .header-container {
#             background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
#             padding: 2.5rem 1.5rem;
#             border-radius: var(--border-radius);
#             margin-bottom: 2rem;
#             box-shadow: var(--box-shadow);
#             color: #fff;
#             text-align: center;
#             position: relative;
#             overflow: hidden;
#         }
#         .header-container h1, .header-container p {
#             color: #fff !important;
#             font-family: 'Lexend', Arial, sans-serif !important;
#             font-weight: 500 !important;
#         }
#         .card {
#             background: var(--card);
#             border-radius: var(--border-radius);
#             box-shadow: var(--box-shadow);
#             padding: 1.5rem 1.5rem 1.2rem 1.5rem;
#             margin-bottom: 1.2rem;
#             border: 1px solid #e3eaf3;
#             font-family: 'Lexend', Arial, sans-serif !important;
#             font-weight: 500 !important;
#         }
#         .info-box {
#             background-color: #e0f2fe;
#             border-left: 6px solid #38bdf8;
#             padding: 1rem;
#             border-radius: var(--border-radius);
#             margin-bottom: 1.5rem;
#         }
#         .info-box h3 {
#             margin-top: 0;
#             color: #0c4a6e;
#         }
#         .results-summary {
#             background: var(--card);
#             border-radius: var(--border-radius);
#             box-shadow: var(--box-shadow);
#             padding: 1.5rem;
#             margin-bottom: 2rem;
#             border: 1px solid #e3eaf3;
#         }
#         .results-summary h2 {
#             color: var(--primary);
#             margin-top: 0;
#             margin-bottom: 1.5rem;
#             font-size: 1.5rem;
#         }
#         .results-grid {
#             display: grid;
#             grid-template-columns: 1fr 1fr;
#             gap: 1.5rem;
#         }
#         .result-card {
#             background: #f8fafc;
#             border-radius: 12px;
#             padding: 1.2rem;
#             border: 1px solid #e2e8f0;
#         }
#         .result-card h3 {
#             margin-top: 0;
#             margin-bottom: 0.8rem;
#             font-size: 1.1rem;
#             color: var(--text);
#         }
#         .result-value {
#             font-size: 1.5rem;
#             font-weight: 700;
#             color: var(--primary);
#             margin-bottom: 0.5rem;
#         }
#         .result-range {
#             color: var(--text-light);
#             font-size: 0.95rem;
#             margin-bottom: 0.5rem;
#         }
#         .result-status {
#             display: inline-block;
#             padding: 0.3rem 0.8rem;
#             border-radius: 20px;
#             font-size: 0.9rem;
#             font-weight: 600;
#         }
#         .status-normal {
#             background-color: #dcfce7;
#             color: #166534;
#         }
#         .status-below {
#             background-color: #fee2e2;
#             color: #991b1b;
#         }
#         .status-above {
#             background-color: #dbeafe;
#             color: #1e40af;
#         }
#         .stButton>button {
#             background: linear-gradient(90deg, var(--primary) 60%, var(--secondary) 100%);
#             color: #fff !important;
#             font-size: 1.13rem;
#             font-weight: 700;
#             border-radius: var(--border-radius);
#             padding: 0.85rem 2.2rem;
#             border: none;
#             box-shadow: 0 2px 8px rgba(37, 99, 235, 0.10);
#             transition: var(--transition);
#             letter-spacing: 0.01em;
#             outline: none !important;
#             font-family: 'Lexend', Arial, sans-serif !important;
#         }
#         .stButton>button:hover, .stButton>button:focus {
#             background: linear-gradient(90deg, var(--secondary) 0%, var(--primary) 100%);
#             color: #fff !important;
#             box-shadow: 0 4px 16px rgba(37, 99, 235, 0.18);
#             transform: translateY(-2px) scale(1.03);
#         }
#         .stButton>button:active {
#             transform: scale(0.98);
#         }
#         .stSelectbox > div > div > select,
#         .stNumberInput > div > div > input {
#             border-radius: var(--border-radius) !important;
#             padding: 12px 14px !important;
#             border: 1.5px solid #dbeafe !important;
#             font-size: 1.15rem !important;
#             color: var(--text) !important;
#             background: #fff;
#             transition: var(--transition);
#             font-family: 'Lexend', Arial, sans-serif !important;
#             font-weight: 500 !important;
#             height: 3.5rem !important;
#         }
#         .stSelectbox > div > div > select option {
#             color: var(--text) !important;
#             background: #fff !important;
#         }
#         .stSelectbox > div > div > select:focus,
#         .stNumberInput > div > div > input:focus {
#             border-color: var(--primary) !important;
#             box-shadow: 0 0 0 2px rgba(37, 99, 235, 0.13) !important;
#             color: var(--text) !important;
#         }
#         .stPlotlyChart {
#             background: var(--card);
#             border-radius: var(--border-radius);
#             box-shadow: var(--box-shadow);
#             padding: 1rem;
#             margin-bottom: 1.2rem;
#         }
#         @media (max-width: 768px) {
#             .header-container {
#                 padding: 1.5rem 0.5rem;
#             }
#             .card {
#                 padding: 1rem;
#             }
#             .results-grid {
#                 grid-template-columns: 1fr;
#             }
#             .stButton>button {
#                 padding: 0.7rem 1.2rem;
#                 font-size: 1rem;
#             }
#         }
#     </style>
#     """, unsafe_allow_html=True)

# # Dummy percentile curves (simplified WHO-like format)
# def get_weight_for_age_curves(gender):
#     months = np.arange(0, 61)
#     base = 3.2 if gender == "Male" else 3.0
#     return {
#         "months": months,
#         "3rd": base + 0.3 * months + 0.001 * months**2,
#         "15th": base + 0.35 * months + 0.0015 * months**2,
#         "50th": base + 0.42 * months + 0.002 * months**2,
#         "85th": base + 0.49 * months + 0.0025 * months**2,
#         "97th": base + 0.55 * months + 0.003 * months**2,
#     }

# def get_height_for_age_curves(gender):
#     months = np.arange(0, 61)
#     base = 49.9 if gender == "Male" else 49.1
#     return {
#         "months": months,
#         "3rd": base + 0.7 * months + 0.01 * months**2,
#         "15th": base + 0.75 * months + 0.015 * months**2,
#         "50th": base + 0.8 * months + 0.02 * months**2,
#         "85th": base + 0.85 * months + 0.025 * months**2,
#         "97th": base + 0.9 * months + 0.03 * months**2,
#     }

# def get_weight_for_height_curves(gender):
#     heights = np.arange(45, 120)
#     base = 2.5 if gender == "Male" else 2.3
#     return {
#         "heights": heights,
#         "3rd": base + 0.1 * (heights - 45) + 0.001 * (heights - 45)**2,
#         "15th": base + 0.13 * (heights - 45) + 0.0015 * (heights - 45)**2,
#         "50th": base + 0.15 * (heights - 45) + 0.002 * (heights - 45)**2,
#         "85th": base + 0.18 * (heights - 45) + 0.0025 * (heights - 45)**2,
#         "97th": base + 0.20 * (heights - 45) + 0.003 * (heights - 45)**2,
#     }

# # Function to get normal ranges based on age and gender (returns numerical values)
# def get_normal_ranges(age, gender):
#     # These are simplified examples - in a real app you would use actual growth chart data
#     if gender == "Male":
#         if age < 12:
#             return (3.5, 10.5), (55, 75)  # (weight_low, weight_high), (height_low, height_high)
#         elif age < 24:
#             return (8.5, 13.5), (73, 88)
#         elif age < 36:
#             return (10.5, 16.0), (83, 97)
#         elif age < 48:
#             return (12.0, 18.5), (90, 105)
#         else:
#             return (14.0, 21.0), (97, 112)
#     else:  # Female
#         if age < 12:
#             return (3.2, 9.8), (54, 73)
#         elif age < 24:
#             return (7.8, 12.8), (71, 86)
#         elif age < 36:
#             return (9.8, 15.5), (81, 96)
#         elif age < 48:
#             return (11.5, 17.5), (88, 104)
#         else:
#             return (13.5, 20.5), (95, 111)

# # Function to determine status
# def get_status(value, low, high):
#     if value < low:
#         return "Below normal range", "status-below"
#     elif value > high:
#         return "Above normal range", "status-above"
#     else:
#         return "Within normal range", "status-normal"

# # Apply custom CSS
# local_css()

# # Header with gradient
# st.markdown("""
# <div class="header-container">
#     <h1 style="margin:0;padding:0;">👶 Child Growth Chart Visualizer</h1>
#     <p style="margin:0;padding-top:0.5rem;font-size:1.1rem;">Track your child's growth and development</p>
# </div>
# """, unsafe_allow_html=True)

# # Input section in a card
# st.markdown('<div class="card">', unsafe_allow_html=True)
# st.markdown('<h2 style="color: var(--primary); margin-bottom: 1.5rem;">Enter Child\'s Information</h2>', unsafe_allow_html=True)

# col1, col2 = st.columns(2)
# with col1:
#     gender = st.radio("Gender", ["Male", "Female"])
#     age = st.number_input("Age (months)", min_value=0, max_value=60, step=1)
# with col2:
#     weight = st.number_input("Weight (kg)", min_value=2.0, max_value=30.0, step=0.1)
#     height = st.number_input("Height (cm)", min_value=45.0, max_value=120.0, step=0.1)

# show = st.button("Plot Growth Charts", use_container_width=True)
# st.markdown('</div>', unsafe_allow_html=True)

# if show:
#     color = "blue" if gender == "Male" else "deeppink"
    
#     # Get normal ranges as numerical values
#     (weight_low, weight_high), (height_low, height_high) = get_normal_ranges(age, gender)
    
#     # Format ranges for display
#     weight_range = f"{weight_low} - {weight_high} kg"
#     height_range = f"{height_low} - {height_high} cm"
    
#     # Get status for each measurement
#     weight_status, weight_status_class = get_status(weight, weight_low, weight_high)
#     height_status, height_status_class = get_status(height, height_low, height_high)
    
#     # Display the results summary in a visually appealing card
#     st.markdown("""
#     <div class="results-summary">
#         <h2>📊 Your Child's Growth Summary</h2>
#         <div class="results-grid">
#             <div class="result-card">
#                 <h3>Weight</h3>
#                 <div class="result-value">{weight:.1f} kg</div>
#                 <div class="result-range">Normal range for {gender}, {age} months: {weight_range}</div>
#                 <div class="result-status {weight_status_class}">{weight_status}</div>
#             </div>
#             <div class="result-card">
#                 <h3>Height</h3>
#                 <div class="result-value">{height:.1f} cm</div>
#                 <div class="result-range">Normal range for {gender}, {age} months: {height_range}</div>
#                 <div class="result-status {height_status_class}">{height_status}</div>
#             </div>
#         </div>
#         <p style="margin-top: 1.5rem; font-size: 0.95rem; color: var(--text-light);">
#         Note: These ranges are approximate based on WHO growth standards. Individual growth patterns may vary. 
#         Consult your pediatrician for a professional assessment.
#         </p>
#     </div>
#     """.format(
#         weight=weight, 
#         height=height, 
#         gender=gender.lower(), 
#         age=age, 
#         weight_range=weight_range, 
#         height_range=height_range,
#         weight_status=weight_status,
#         weight_status_class=weight_status_class,
#         height_status=height_status,
#         height_status_class=height_status_class
#     ), unsafe_allow_html=True)

#     # --- Plot Charts ---
#     data_weight_age = get_weight_for_age_curves(gender)
#     data_height_age = get_height_for_age_curves(gender)
#     data_weight_height = get_weight_for_height_curves(gender)

#     # Plot Weight-for-Age
#     fig1, ax1 = plt.subplots(figsize=(8, 5))
#     for key in ['3rd', '15th', '50th', '85th', '97th']:
#         ax1.plot(data_weight_age["months"], data_weight_age[key], label=f"{key} percentile", linestyle='--' if key != "50th" else '-', color='gray' if key != "50th" else 'orange')
#     ax1.scatter(age, weight, color=color, label="Your child", zorder=5, s=100)
#     ax1.set_title("Weight-for-Age", fontsize=14, fontweight='bold', pad=20)
#     ax1.set_xlabel("Age (months)", fontsize=12)
#     ax1.set_ylabel("Weight (kg)", fontsize=12)
#     ax1.legend(fontsize=10)
#     ax1.grid(True, alpha=0.3)
#     plt.tight_layout()

#     # Plot Height-for-Age
#     fig2, ax2 = plt.subplots(figsize=(8, 5))
#     for key in ['3rd', '15th', '50th', '85th', '97th']:
#         ax2.plot(data_height_age["months"], data_height_age[key], label=f"{key} percentile", linestyle='--' if key != "50th" else '-', color='gray' if key != "50th" else 'orange')
#     ax2.scatter(age, height, color=color, label="Your child", zorder=5, s=100)
#     ax2.set_title("Height-for-Age", fontsize=14, fontweight='bold', pad=20)
#     ax2.set_xlabel("Age (months)", fontsize=12)
#     ax2.set_ylabel("Height (cm)", fontsize=12)
#     ax2.legend(fontsize=10)
#     ax2.grid(True, alpha=0.3)
#     plt.tight_layout()

#     # Plot Weight-for-Height
#     fig3, ax3 = plt.subplots(figsize=(8, 5))
#     for key in ['3rd', '15th', '50th', '85th', '97th']:
#         ax3.plot(data_weight_height["heights"], data_weight_height[key], label=f"{key} percentile", linestyle='--' if key != "50th" else '-', color='gray' if key != "50th" else 'orange')
#     ax3.scatter(height, weight, color=color, label="Your child", zorder=5, s=100)
#     ax3.set_title("Weight-for-Height", fontsize=14, fontweight='bold', pad=20)
#     ax3.set_xlabel("Height (cm)", fontsize=12)
#     ax3.set_ylabel("Weight (kg)", fontsize=12)
#     ax3.legend(fontsize=10)
#     ax3.grid(True, alpha=0.3)
#     plt.tight_layout()

#     # Display in two columns
#     st.markdown('<h2 style="color: var(--primary); margin-top: 2rem;">Growth Charts</h2>', unsafe_allow_html=True)
#     col1, col2 = st.columns(2)
#     with col1:
#         st.pyplot(fig1)
#         st.pyplot(fig3)
#     with col2:
#         st.pyplot(fig2)

# # Footer
# st.markdown("""
# <div class="footer">
#     <p>Child Growth Chart Visualizer | Based on WHO Growth Standards</p>
#     <p>For informational purposes only. Consult your healthcare provider for medical advice.</p>
# </div>
# """, unsafe_allow_html=True)

import streamlit as st
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(page_title="Child Growth Chart", layout="wide")

def local_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Lexend:wght@500&display=swap');
        html, body, [class*="stApp"] {
            font-family: 'Lexend', Arial, sans-serif !important;
            font-weight: 500 !important;
            font-size: 1.08rem;
            color: #22304a;
        }
        :root {
            --primary: #2563eb;
            --secondary: #38bdf8;
            --accent: #22c55e;
            --background: #f4faff;
            --card: #ffffff;
            --text: #22304a;
            --text-light: #4A5568;
            --warning: #ef4444;
            --success: #22c55e;
            --info: #2563eb;
            --border-radius: 16px;
            --box-shadow: 0 4px 24px rgba(37, 99, 235, 0.08);
            --transition: all 0.2s cubic-bezier(.4,0,.2,1);
        }
        .stApp {
            background-color: var(--background) !important;
        }
        .main .block-container {
            background-color: var(--background);
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        .header-container {
            background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
            padding: 2.5rem 1.5rem;
            border-radius: var(--border-radius);
            margin-bottom: 2rem;
            box-shadow: var(--box-shadow);
            color: #fff;
            text-align: center;
            position: relative;
            overflow: hidden;
        }
        .header-container h1, .header-container p {
            color: #fff !important;
            font-family: 'Lexend', Arial, sans-serif !important;
            font-weight: 500 !important;
        }
        .card {
            background: var(--card);
            border-radius: var(--border-radius);
            box-shadow: var(--box-shadow);
            padding: 1.5rem 1.5rem 1.2rem 1.5rem;
            margin-bottom: 1.2rem;
            border: 1px solid #e3eaf3;
            font-family: 'Lexend', Arial, sans-serif !important;
            font-weight: 500 !important;
        }
        .info-box {
            background-color: #e0f2fe;
            border-left: 6px solid #38bdf8;
            padding: 1rem;
            border-radius: var(--border-radius);
            margin-bottom: 1.5rem;
        }
        .info-box h3 {
            margin-top: 0;
            color: #0c4a6e;
        }
        .results-summary {
            background: var(--card);
            border-radius: var(--border-radius);
            box-shadow: var(--box-shadow);
            padding: 1.5rem;
            margin-bottom: 2rem;
            border: 1px solid #e3eaf3;
        }
        .results-summary h2 {
            color: var(--primary);
            margin-top: 0;
            margin-bottom: 1.5rem;
            font-size: 1.5rem;
        }
        .results-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1.5rem;
        }
        .result-card {
            background: #f8fafc;
            border-radius: 12px;
            padding: 1.2rem;
            border: 1px solid #e2e8f0;
        }
        .result-card h3 {
            margin-top: 0;
            margin-bottom: 0.8rem;
            font-size: 1.1rem;
            color: var(--text);
        }
        .result-value {
            font-size: 1.5rem;
            font-weight: 700;
            color: var(--primary);
            margin-bottom: 0.5rem;
        }
        .result-range {
            color: var(--text-light);
            font-size: 0.95rem;
            margin-bottom: 0.5rem;
        }
        .result-status {
            display: inline-block;
            padding: 0.3rem 0.8rem;
            border-radius: 20px;
            font-size: 0.9rem;
            font-weight: 600;
        }
        .status-normal {
            background-color: #dcfce7;
            color: #166534;
        }
        .status-below {
            background-color: #fee2e2;
            color: #991b1b;
        }
        .status-above {
            background-color: #dbeafe;
            color: #1e40af;
        }
        .stButton>button {
            background: linear-gradient(90deg, var(--primary) 60%, var(--secondary) 100%);
            color: #fff !important;
            font-size: 1.13rem;
            font-weight: 700;
            border-radius: var(--border-radius);
            padding: 0.85rem 2.2rem;
            border: none;
            box-shadow: 0 2px 8px rgba(37, 99, 235, 0.10);
            transition: var(--transition);
            letter-spacing: 0.01em;
            outline: none !important;
            font-family: 'Lexend', Arial, sans-serif !important;
        }
        .stButton>button:hover, .stButton>button:focus {
            background: linear-gradient(90deg, var(--secondary) 0%, var(--primary) 100%);
            color: #fff !important;
            box-shadow: 0 4px 16px rgba(37, 99, 235, 0.18);
            transform: translateY(-2px) scale(1.03);
        }
        .stButton>button:active {
            transform: scale(0.98);
        }
        .stSelectbox > div > div > select,
        .stNumberInput > div > div > input {
            border-radius: var(--border-radius) !important;
            padding: 12px 14px !important;
            border: 1.5px solid #dbeafe !important;
            font-size: 1.15rem !important;
            color: var(--text) !important;
            background: #fff;
            transition: var(--transition);
            font-family: 'Lexend', Arial, sans-serif !important;
            font-weight: 500 !important;
            height: 3.5rem !important;
        }
        .stSelectbox > div > div > select option {
            color: var(--text) !important;
            background: #fff !important;
        }
        .stSelectbox > div > div > select:focus,
        .stNumberInput > div > div > input:focus {
            border-color: var(--primary) !important;
            box-shadow: 0 0 0 2px rgba(37, 99, 235, 0.13) !important;
            color: var(--text) !important;
        }
        .stPlotlyChart {
            background: var(--card);
            border-radius: var(--border-radius);
            box-shadow: var(--box-shadow);
            padding: 1rem;
            margin-bottom: 1.2rem;
            border: 1px solid #e3eaf3;
        }
        @media (max-width: 768px) {
            .header-container {
                padding: 1.5rem 0.5rem;
            }
            .card {
                padding: 1rem;
            }
            .results-grid {
                grid-template-columns: 1fr;
            }
            .stButton>button {
                padding: 0.7rem 1.2rem;
                font-size: 1rem;
            }
        }
    </style>
    """, unsafe_allow_html=True)

# Dummy percentile curves (simplified WHO-like format)
def get_weight_for_age_curves(gender):
    months = np.arange(0, 61)
    base = 3.2 if gender == "Male" else 3.0
    return {
        "months": months,
        "3rd": base + 0.3 * months + 0.001 * months**2,
        "15th": base + 0.35 * months + 0.0015 * months**2,
        "50th": base + 0.42 * months + 0.002 * months**2,
        "85th": base + 0.49 * months + 0.0025 * months**2,
        "97th": base + 0.55 * months + 0.003 * months**2,
    }

def get_height_for_age_curves(gender):
    months = np.arange(0, 61)
    base = 49.9 if gender == "Male" else 49.1
    return {
        "months": months,
        "3rd": base + 0.7 * months + 0.01 * months**2,
        "15th": base + 0.75 * months + 0.015 * months**2,
        "50th": base + 0.8 * months + 0.02 * months**2,
        "85th": base + 0.85 * months + 0.025 * months**2,
        "97th": base + 0.9 * months + 0.03 * months**2,
    }

def get_weight_for_height_curves(gender):
    heights = np.arange(45, 120)
    base = 2.5 if gender == "Male" else 2.3
    return {
        "heights": heights,
        "3rd": base + 0.1 * (heights - 45) + 0.001 * (heights - 45)**2,
        "15th": base + 0.13 * (heights - 45) + 0.0015 * (heights - 45)**2,
        "50th": base + 0.15 * (heights - 45) + 0.002 * (heights - 45)**2,
        "85th": base + 0.18 * (heights - 45) + 0.0025 * (heights - 45)**2,
        "97th": base + 0.20 * (heights - 45) + 0.003 * (heights - 45)**2,
    }

# Function to get normal ranges based on age and gender (returns numerical values)
def get_normal_ranges(age, gender):
    # These are simplified examples - in a real app you would use actual growth chart data
    if gender == "Male":
        if age < 12:
            return (3.5, 10.5), (55, 75)  # (weight_low, weight_high), (height_low, height_high)
        elif age < 24:
            return (8.5, 13.5), (73, 88)
        elif age < 36:
            return (10.5, 16.0), (83, 97)
        elif age < 48:
            return (12.0, 18.5), (90, 105)
        else:
            return (14.0, 21.0), (97, 112)
    else:  # Female
        if age < 12:
            return (3.2, 9.8), (54, 73)
        elif age < 24:
            return (7.8, 12.8), (71, 86)
        elif age < 36:
            return (9.8, 15.5), (81, 96)
        elif age < 48:
            return (11.5, 17.5), (88, 104)
        else:
            return (13.5, 20.5), (95, 111)

# Function to determine status
def get_status(value, low, high):
    if value < low:
        return "Below normal range", "status-below"
    elif value > high:
        return "Above normal range", "status-above"
    else:
        return "Within normal range", "status-normal"

# Apply custom CSS
local_css()

# Header with gradient
st.markdown("""
<div class="header-container">
    <h1 style="margin:0;padding:0;">👶 Child Growth Chart Visualizer</h1>
    <p style="margin:0;padding-top:0.5rem;font-size:1.1rem;">Track your child's growth and development</p>
</div>
""", unsafe_allow_html=True)

# Input section in a card
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<h2 style="color: var(--primary); margin-bottom: 1.5rem;">Enter Child\'s Information</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    gender = st.radio("Gender", ["Male", "Female"])
    age = st.number_input("Age (months)", min_value=0, max_value=60, step=1)
with col2:
    weight = st.number_input("Weight (kg)", min_value=2.0, max_value=30.0, step=0.1)
    height = st.number_input("Height (cm)", min_value=45.0, max_value=120.0, step=0.1)

show = st.button("Plot Growth Charts", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

if show:
    color = "#2563eb" if gender == "Male" else "#ec4899"
    
    # Get normal ranges as numerical values
    (weight_low, weight_high), (height_low, height_high) = get_normal_ranges(age, gender)
    
    # Format ranges for display
    weight_range = f"{weight_low} - {weight_high} kg"
    height_range = f"{height_low} - {height_high} cm"
    
    # Get status for each measurement
    weight_status, weight_status_class = get_status(weight, weight_low, weight_high)
    height_status, height_status_class = get_status(height, height_low, height_high)
    
    # Display the results summary in a visually appealing card
    st.markdown("""
    <div class="results-summary">
        <h2>📊 Your Child's Growth Summary</h2>
        <div class="results-grid">
            <div class="result-card">
                <h3>Weight</h3>
                <div class="result-value">{weight:.1f} kg</div>
                <div class="result-range">Normal range for {gender}, {age} months: {weight_range}</div>
                <div class="result-status {weight_status_class}">{weight_status}</div>
            </div>
            <div class="result-card">
                <h3>Height</h3>
                <div class="result-value">{height:.1f} cm</div>
                <div class="result-range">Normal range for {gender}, {age} months: {height_range}</div>
                <div class="result-status {height_status_class}">{height_status}</div>
            </div>
        </div>
        <p style="margin-top: 1.5rem; font-size: 0.95rem; color: var(--text-light);">
        Note: These ranges are approximate based on WHO growth standards. Individual growth patterns may vary. 
        Consult your pediatrician for a professional assessment.
        </p>
    </div>
    """.format(
        weight=weight, 
        height=height, 
        gender=gender.lower(), 
        age=age, 
        weight_range=weight_range, 
        height_range=height_range,
        weight_status=weight_status,
        weight_status_class=weight_status_class,
        height_status=height_status,
        height_status_class=height_status_class
    ), unsafe_allow_html=True)

    # --- Plot Charts with Plotly ---
    data_weight_age = get_weight_for_age_curves(gender)
    data_height_age = get_height_for_age_curves(gender)
    data_weight_height = get_weight_for_height_curves(gender)

    # Create Weight-for-Age chart
    fig1 = go.Figure()
    
    # Add percentile curves
    percentiles = ['3rd', '15th', '50th', '85th', '97th']
    colors = ['rgba(200, 200, 200, 0.7)', 'rgba(150, 150, 150, 0.7)', 
              'rgba(255, 165, 0, 0.8)', 'rgba(150, 150, 150, 0.7)', 
              'rgba(200, 200, 200, 0.7)']
    
    for i, p in enumerate(percentiles):
        fig1.add_trace(go.Scatter(
            x=data_weight_age["months"],
            y=data_weight_age[p],
            mode='lines',
            name=f'{p} percentile',
            line=dict(color=colors[i], width=2 if p != '50th' else 3, dash='dot' if p != '50th' else None),
            hoverinfo='x+y+name',
            fill=None if p == '97th' else 'tonexty' if p != '3rd' else None,
            fillcolor='rgba(200, 200, 200, 0.2)' if p != '3rd' else None
        ))
    
    # Add child's data point
    fig1.add_trace(go.Scatter(
        x=[age],
        y=[weight],
        mode='markers+text',
        name='Your Child',
        marker=dict(color=color, size=12, line=dict(width=2, color='white')),
        text=[f'Age: {age} months<br>Weight: {weight} kg'],
        textposition='top center',
        hoverinfo='text',
        textfont=dict(size=12)
    ))
    
    # Update layout
    fig1.update_layout(
        title='<b>Weight-for-Age</b>',
        title_x=0.5,
        xaxis_title='Age (months)',
        yaxis_title='Weight (kg)',
        hovermode='x unified',
        plot_bgcolor='rgba(244, 250, 255, 1)',
        paper_bgcolor='rgba(255, 255, 255, 1)',
        margin=dict(l=40, r=40, t=60, b=40),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        height=500
    )
    
    # Create Height-for-Age chart
    fig2 = go.Figure()
    
    for i, p in enumerate(percentiles):
        fig2.add_trace(go.Scatter(
            x=data_height_age["months"],
            y=data_height_age[p],
            mode='lines',
            name=f'{p} percentile',
            line=dict(color=colors[i], width=2 if p != '50th' else 3, dash='dot' if p != '50th' else None),
            hoverinfo='x+y+name',
            fill=None if p == '97th' else 'tonexty' if p != '3rd' else None,
            fillcolor='rgba(200, 200, 200, 0.2)' if p != '3rd' else None
        ))
    
    # Add child's data point
    fig2.add_trace(go.Scatter(
        x=[age],
        y=[height],
        mode='markers+text',
        name='Your Child',
        marker=dict(color=color, size=12, line=dict(width=2, color='white')),
        text=[f'Age: {age} months<br>Height: {height} cm'],
        textposition='top center',
        hoverinfo='text',
        textfont=dict(size=12)
    ))
    
    # Update layout
    fig2.update_layout(
        title='<b>Height-for-Age</b>',
        title_x=0.5,
        xaxis_title='Age (months)',
        yaxis_title='Height (cm)',
        hovermode='x unified',
        plot_bgcolor='rgba(244, 250, 255, 1)',
        paper_bgcolor='rgba(255, 255, 255, 1)',
        margin=dict(l=40, r=40, t=60, b=40),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        height=500
    )
    
    # Create Weight-for-Height chart
    fig3 = go.Figure()
    
    for i, p in enumerate(percentiles):
        fig3.add_trace(go.Scatter(
            x=data_weight_height["heights"],
            y=data_weight_height[p],
            mode='lines',
            name=f'{p} percentile',
            line=dict(color=colors[i], width=2 if p != '50th' else 3, dash='dot' if p != '50th' else None),
            hoverinfo='x+y+name',
            fill=None if p == '97th' else 'tonexty' if p != '3rd' else None,
            fillcolor='rgba(200, 200, 200, 0.2)' if p != '3rd' else None
        ))
    
    # Add child's data point
    fig3.add_trace(go.Scatter(
        x=[height],
        y=[weight],
        mode='markers+text',
        name='Your Child',
        marker=dict(color=color, size=12, line=dict(width=2, color='white')),
        text=[f'Height: {height} cm<br>Weight: {weight} kg'],
        textposition='top center',
        hoverinfo='text',
        textfont=dict(size=12)
    ))
    
    # Update layout
    fig3.update_layout(
        title='<b>Weight-for-Height</b>',
        title_x=0.5,
        xaxis_title='Height (cm)',
        yaxis_title='Weight (kg)',
        hovermode='x unified',
        plot_bgcolor='rgba(244, 250, 255, 1)',
        paper_bgcolor='rgba(255, 255, 255, 1)',
        margin=dict(l=40, r=40, t=60, b=40),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        height=500
    )

    # Display in two columns
    st.markdown('<h2 style="color: var(--primary); margin-top: 2rem;">Growth Charts</h2>', unsafe_allow_html=True)
    
    # First row with weight-for-age and height-for-age
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(fig1, use_container_width=True)
    with col2:
        st.plotly_chart(fig2, use_container_width=True)
    
    # Second row with weight-for-height (full width)
    st.plotly_chart(fig3, use_container_width=True)

# Footer
st.markdown("""
<div class="footer">
    <p>Child Growth Chart Visualizer | Based on WHO Growth Standards</p>
    <p>For informational purposes only. Consult your healthcare provider for medical advice.</p>
</div>
""", unsafe_allow_html=True)