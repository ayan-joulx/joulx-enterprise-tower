import streamlit as st
from pydantic import BaseModel
import numpy as np

# Page configuration
st.set_page_config(
    page_title="JouleX Enterprise Control Tower",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ JouleX Enterprise Control Tower")
st.markdown("### Enterprise AI Model Optimization & Registration Portal")

# Tabs for different functionalities
tab1, tab2 = st.tabs(["🏢 Enterprise Signup", "⚙️ AI Optimization"])

with tab1:
    st.subheader("Client Registration")
    company_name = st.text_input("Company Name")
    work_email = st.text_input("Work Email")
    industry = st.selectbox("Industry", ["Autonomous Vehicles", "Robotics", "Cloud Hyperscalers", "Edge Computing"])
    
    if st.button("Register Enterprise Account"):
        if company_name and work_email:
            mock_api_key = "jx_live_" + np.random.bytes(8).hex()
            st.success(f"Welcome {company_name}! Account created successfully.")
            st.json({
                "status": "success",
                "message": f"Welcome {company_name}! Account created successfully.",
                "assigned_industry": industry,
                "api_key": mock_api_key,
                "deployment_ready": True
            })
        else:
            st.warning("Please fill in all the required fields.")

with tab2:
    st.subheader("Thermodynamic Weight Optimization")
    api_key_input = st.text_input("Enter Enterprise API Key", type="password")
    target_sparsity = st.slider("Target Sparsity Ratio", min_value=0.1, max_value=0.9, value=0.5, step=0.1)
    
    if st.button("Run Optimization Pipeline"):
        if api_key_input:
            # Dummy AI weights calculation using NumPy
            arr = np.array([1.2, -2.5, 0.3, 0.7, -1.9, 0.4])
            threshold = np.percentile(np.abs(arr), target_sparsity * 100)
            mask = np.abs(arr) >= threshold
            optimized_weights = arr * mask
            saved_energy_kwh = float(np.sum(np.abs(arr)) * 0.075)
            
            st.success("Optimization completed successfully!")
            st.json({
                "status": "success",
                "target_sparsity": f"{target_sparsity * 100}%",
                "active_weights_count": int(np.sum(mask)),
                "optimized_weights": optimized_weights.tolist(),
                "estimated_energy_saved_kwh": round(saved_energy_kwh, 4),
                "cost_reduction_percent": 50.0
            })
        else:
            st.error("Please enter a valid API Key to run optimization.")