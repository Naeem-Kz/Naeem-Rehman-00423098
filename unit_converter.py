import streamlit as st

st.set_page_config(page_title="Unit Converter", page_icon="🔁")

st.title("🔁 Unit Converter")
st.write("Convert between Length, Weight, and Temperature units.")

conversion_type = st.selectbox("Choose a conversion type", ["Length", "Weight", "Temperature"])

# Define units for each type
unit_options = {
    "Length": ["Meters", "Kilometers", "Miles", "Feet"],
    "Weight": ["Kilograms", "Grams", "Pounds", "Ounces"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"]
}

from_unit = st.selectbox("From Unit", unit_options[conversion_type])
to_unit = st.selectbox("To Unit", unit_options[conversion_type])
value = st.number_input("Enter value to convert", format="%.4f")

def convert_length(val, from_u, to_u):
    conversions = {
        "Meters": 1,
        "Kilometers": 1000,
        "Miles": 1609.34,
        "Feet": 0.3048
    }
    return val * conversions[from_u] / conversions[to_u]

def convert_weight(val, from_u, to_u):
    conversions = {
        "Kilograms": 1,
        "Grams": 0.001,
        "Pounds": 0.453592,
        "Ounces": 0.0283495
    }
    return val * conversions[from_u] / conversions[to_u]

def convert_temperature(val, from_u, to_u):
    if from_u == to_u:
        return val
    # Convert to Celsius first
    if from_u == "Fahrenheit":
        val = (val - 32) * 5 / 9
    elif from_u == "Kelvin":
        val = val - 273.15

    # Convert from Celsius to target unit
    if to_u == "Fahrenheit":
        return (val * 9 / 5) + 32
    elif to_u == "Kelvin":
        return val + 273.15
    else:
        return val

if st.button("Convert"):
    if conversion_type == "Length":
        result = convert_length(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = convert_weight(value, from_unit, to_unit)
    else:
        result = convert_temperature(value, from_unit, to_unit)

    st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
