import streamlit as st
import pandas as pd

# Sample well data
def get_well_data():
    return pd.DataFrame({
        'Well ID': ['W001', 'W002', 'W003', 'W004', 'W005'],
        'State': ['Uttar Pradesh', 'Maharashtra', 'Karnataka', 'Gujarat', 'Punjab'],
        'District': ['Agra', 'Mumbai', 'Bangalore', 'Ahmedabad', 'Ludhiana'],
        'Battery Level (%)': [100, 45, 0, 75, 30],
        'Water Level (m)': [10, 5, 0, 8, 4],
        'Status': ['Normal', 'Low Battery', 'No Data', 'Normal', 'Normal'],
        'Latitude': [27.1767, 19.0760, 12.9716, 23.0225, 30.9009],
        'Longitude': [78.0081, 72.8777, 77.5946, 72.5714, 75.8573]
    })

# List of states and their districts in India
states_and_districts = {
    'Uttar Pradesh': [
        'Agra', 'Aligarh', 'Allahabad', 'Ambedkar Nagar', 'Auraiya',
        'Azamgarh', 'Badaun', 'Baghpat', 'Bahraich', 'Ballia',
        'Banda', 'Barabanki', 'Bareilly', 'Bijnor', 'Budaun',
        'Bulandshahr', 'Chandauli', 'Chitrakoot', 'Deoria', 'Etah',
        'Etawah', 'Farrukhabad', 'Fatehpur', 'Firozabad', 'Gautam Buddha Nagar',
        'Ghaziabad', 'Ghazipur', 'Gonda', 'Hamirpur', 'Hapurr',
        'Hardoi', 'Hathras', 'Jaunpur', 'Jhansi', 'Kannauj',
        'Kanpur Dehat', 'Kanpur Nagar', 'Kushinagar', 'Lakhimpur Kheri', 'Lalitpur',
        'Lucknow', 'Maharajganj', 'Mahoba', 'Mainpuri', 'Mathura',
        'Mau', 'Meerut', 'Mirzapur', 'Moradabad', 'Muzaffarnagar',
        'Pilibhit', 'Pratapgarh', 'Raebareli', 'Rampur', 'Saharanpur',
        'Sambhal', 'Shahjahanpur', 'Shrawasti', 'Sitapur', 'Sonbhadra',
        'Sultanpur', 'Unnao', 'Varanasi'
    ],
    'Maharashtra': [
        'Ahmednagar', 'Akola', 'Aurangabad', 'Beed', 'Bhandara',
        'Buldhana', 'Chandrapur', 'Dhule', 'Gadchiroli', 'Gondia',
        'Jalna', 'Kolhapur', 'Mumbai', 'Nagpur', 'Nanded',
        'Nasik', 'Osmanabad', 'Parbhani', 'Pune', 'Raigad',
        'Ratnagiri', 'Sindhudurg', 'Solapur', 'Thane', 'Wardha',
        'Washim', 'Yavatmal'
    ],
    'Karnataka': [
        'Bagalkot', 'Bangalore', 'Belgaum', 'Bellary', 'Bidar',
        'Chamarajanagar', 'Chikballapur', 'Chikkamagaluru', 'Chitradurga', 'Dakshina Kannada',
        'Davanagere', 'Dharwad', 'Gadag', 'Hassan', 'Haveri',
        'Kodagu', 'Kolar', 'Mandya', 'Mysore', 'Raichur',
        'Ramanagara', 'Shivamogga', 'Tumakuru', 'Udupi', 'Uttara Kannada',
        'Yadgir'
    ],
    'Gujarat': [
        'Ahmedabad', 'Amreli', 'Anand', 'Banaskantha', 'Bharuch',
        'Bhavnagar', 'Dahod', 'Dang', 'Gandhinagar', 'Kutch',
        'Mahisagar', 'Mehsana', 'Narmada', 'Navsari', 'Panchmahal',
        'Patan', 'Rajkot', 'Sabarkantha', 'Surat', 'Surendranagar',
        'Tapi', 'Vadodara', 'Valsad'
    ],
    'Punjab': [
        'Amritsar', 'Barnala', 'Bathinda', 'Fatehgarh Sahib', 'Firozpur',
        'Gurdaspur', 'Hoshiarpur', 'Jalandhar', 'Kapurthala', 'Ludhiana',
        'Mansa', 'Moga', 'Muktsar', 'Patiala', 'Rupnagar',
        'Sahibzada Ajit Singh Nagar', 'Sangrur', 'Tarn Taran'
    ],
    # Add more states and their districts here as needed
}

# Fetching the well data
well_data = get_well_data()

# Title of the application
st.title("Groundwater Monitoring System")
st.markdown('<style>h1 {font-family: Arial, sans-serif;}</style>', unsafe_allow_html=True)

# Displaying the map image
st.subheader("Well Locations Map")
st.image("/workspaces/blank-app2/monitoringstations_india_jpg_300.jpg", caption="Map showing well locations", use_column_width=True)

# Select State
selected_state = st.selectbox("Select State", list(states_and_districts.keys()))

# Select District based on State
district_filter = st.selectbox("Select District", states_and_districts[selected_state])

# Data table display
st.subheader("Well Data")
st.dataframe(well_data)

# Filtering the data based on user selection
filtered_data = well_data[(well_data['State'] == selected_state) & (well_data['District'] == district_filter)]

# Display filtered data
st.subheader("Filtered Well Data")
st.dataframe(filtered_data)

# Alert section for anomalies
st.subheader("Alerts")
alerts = filtered_data[filtered_data['Status'] != 'Normal']
if not alerts.empty:
    for index, row in alerts.iterrows():
        st.warning(f"Alert: Well {row['Well ID']} has status '{row['Status']}'")
else:
    st.success("All wells are functioning normally.")

# Footer with some information
st.markdown("""
---
**Ministry of Water Resources, Government of India**  
For any inquiries, please contact the helpline at +91-XXXXXXXXXX.
""")
