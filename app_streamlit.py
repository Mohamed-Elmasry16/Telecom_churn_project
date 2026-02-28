import streamlit as st
import requests
import pandas as pd

# Page Config
st.set_page_config(page_title="Telecom Churn AI Assistant", layout="wide")

# Custom Styling
st.title("📡 AI-Powered Churn Assistant")
st.markdown("""
    This assistant helps the **Marketing Team** identify customers at risk of leaving. 
    You can ask questions in natural language.
""")

# Sidebar for Project Info
with st.sidebar:
    st.header("Project Overview")
    st.info("Model: XGBoost Classifier")
    st.info("LLM: Qwen/Qwen2.5-1.5B-Instruct")
    st.markdown("---")
    st.write("### Sample Queries:")
    st.caption("- 'Find senior citizens with Fiber optic'")
    st.caption("- 'Customers with month-to-month contracts'")
    st.caption("- 'High charges and no tech support'")

# Main Chat Interface
user_query = st.chat_input("Ask about your customer base...")

if user_query:
    with st.chat_message("user"):
        st.write(user_query)

    with st.spinner("Analyzing data..."):
        try:
            # Connect to your FastAPI /chat endpoint
            response = requests.post("http://localhost:8000/chat", json={"message": user_query})
            
            if response.status_code == 200:
                data = response.json()
                result_text = data["response"]
                
                with st.chat_message("assistant"):
                    st.write(result_text)
                    
                    # Logic to extract numbers for visual metrics
                    # If "There are 598 customers likely to churn out of 806"
                    import re
                    nums = re.findall(r'\d+', result_text)
                    if len(nums) >= 2:
                        churn_risk = int(nums[0])
                        total = int(nums[1])
                        
                        col1, col2, col3 = st.columns(3)
                        col1.metric("Total Matched", total)
                        col2.metric("At Risk", churn_risk, delta=f"{(churn_risk/total)*100:.1f}%", delta_color="inverse")
                                          
            else:
                st.error("API error. Please check if the FastAPI server is running.")
        except Exception as e:
            st.error(f"Connection failed: {e}")