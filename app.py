import streamlit as st
import google.generativeai as genai

# 🔹 Replace with your actual Google API Key
GOOGLE_API_KEY = "AIzaSyDejubChBeArtssNcboIgj0-kFW38AYS2Q"  

# Configure Google GenAI with API Key
genai.configure(api_key=GOOGLE_API_KEY)

# Function to get travel recommendations
def get_travel_recommendations(source, destination):
    """Fetch travel options using Google GenAI."""
    prompt = f"Suggest different travel options from {source} to {destination} with estimated costs for cab, train, bus, and flights."

    try:
        model = genai.GenerativeModel("gemini-1.5-pro")  # Ensure model name is correct
        response = model.generate_content(prompt)

        if response and hasattr(response, 'text'):
            return response.text.strip()
        else:
            return "Unable to fetch travel recommendations. Try again later."
    
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.title("🚀 AI-Powered Travel Planner")
st.markdown("Plan your journey with AI-generated travel options!")

source = st.text_input("📍 Enter Source Location")
destination = st.text_input("📍 Enter Destination Location")

if st.button("Find Travel Options"):
    if source and destination:
        travel_info = get_travel_recommendations(source, destination)
        st.text_area("📌 Recommended Travel Options:", travel_info, height=200)
    else:
        st.warning("⚠️ Please enter both source and destination.")
