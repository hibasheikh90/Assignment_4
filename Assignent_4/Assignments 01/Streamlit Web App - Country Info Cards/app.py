
import streamlit as st
import requests

def fetch_country_data(country):
    url = f'https://restcountries.com/v3.1/name/{country}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        country_data = data[0]

        # Extracting data safely
        name = country_data['name']['official']
        capital = country_data.get('capital', ['N/A'])[0]  # Handle missing capital
        population = f"{country_data['population']:,}"  # Format population with commas
        area = f"{country_data.get('area', 'N/A')} km²"  # Handle missing area
        currency_data = country_data.get('currencies', {})
        currency = ', '.join([f"{v['name']} ({k})" for k, v in currency_data.items()]) if currency_data else "N/A"
        region = country_data.get('region', 'N/A')

        return name, capital, population, area, currency, region
    else:
        return None

def main():
    st.title("🌍 Country Information App")

    country = st.text_input("Enter a country name:")

    if country:  # Corrected condition
        country_info = fetch_country_data(country)
        if country_info:
            name, capital, population, area, currency, region = country_info
            st.subheader("📌 Country Information")
            st.write(f"**Name:** {name}")
            st.write(f"**Capital:** {capital}")
            st.write(f"**Population:** {population}")
            st.write(f"**Area:** {area}")
            st.write(f"**Currency:** {currency}")
            st.write(f"**Region:** {region}")
        else:
            st.error("❌ Country not found. Please check the spelling.")

if __name__ == "__main__":  # Fixed function call
    main()
