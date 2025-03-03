import streamlit as st

# Set up Streamlit app
st.set_page_config(page_title="Unit Converter", layout="wide")
st.title("Unit Converter with LLM Integration")
st.write("Convert between different units and get explanations!")


# Conversion functions
def convert_units(value, from_unit, to_unit, conversion_type):
    conversion_factors = {
        "Temperature": {
            "Celsius": {"Fahrenheit": lambda x: x * 9/5 + 32, "Kelvin": lambda x: x + 273.15},
            "Fahrenheit": {"Celsius": lambda x: (x - 32) * 5/9, "Kelvin": lambda x: (x - 32) * 5/9 + 273.15},
            "Kelvin": {"Celsius": lambda x: x - 273.15, "Fahrenheit": lambda x: (x - 273.15) * 9/5 + 32}
        },
        "Length": {
            "Meters": {"Kilometers": lambda x: x / 1000, "Feet": lambda x: x * 3.281, "Miles": lambda x: x / 1609},
            "Kilometers": {"Meters": lambda x: x * 1000, "Miles": lambda x: x / 1.609},
            "Miles": {"Meters": lambda x: x * 1609, "Kilometers": lambda x: x * 1.609},
            "Feet": {"Meters": lambda x: x / 3.281}
        },
        "Weight": {
            "Kilograms": {"Pounds": lambda x: x * 2.205, "Grams": lambda x: x * 1000},
            "Pounds": {"Kilograms": lambda x: x / 2.205},
            "Grams": {"Kilograms": lambda x: x / 1000}
        },
        "Volume": {
            "Liters": {"Cups": lambda x: x * 4.227, "Ounces": lambda x: x * 33.814},
            "Cups": {"Liters": lambda x: x / 4.227},
            "Ounces": {"Liters": lambda x: x / 33.814}
        }
    }

    if conversion_type in conversion_factors and from_unit in conversion_factors[conversion_type]:
        if to_unit in conversion_factors[conversion_type][from_unit]:
            return round(conversion_factors[conversion_type][from_unit][to_unit](value), 2)
    
    return None

# Unit Categories
unit_types = {
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Length": ["Meters", "Kilometers", "Feet", "Miles"],
    "Weight": ["Kilograms", "Pounds", "Grams"],
    "Volume": ["Liters", "Cups", "Ounces"],
}

# Select conversion type
conversion_type = st.selectbox("Choose a category", list(unit_types.keys()))

# Select units
from_unit = st.selectbox("From", unit_types[conversion_type])
to_unit = st.selectbox("To", unit_types[conversion_type])

# Input value
value = st.number_input(f"Enter value in {from_unit}", min_value=0.0)

# Convert button
if st.button("Convert"): 
    result = convert_units(value, from_unit, to_unit, conversion_type)
    if result is not None: 
        st.success(f"{value} {from_unit} = {result} {to_unit}")
    else: 
        st.error("Conversion not available.")

