#!/usr/bin/env python3
# Created By: Finn Kitor
# Date: December 5th, 2023
# this program tells the user to input their address and
# it will tell them their address in uppercase


# Function: format address, Parameters: apartment_number, street_number
# street_name, city, province, and postal code
def format_address(
    apartment_number: str = "",
    street_number: str = "",
    street_name: str = "",
    city: str = "",
    province: str = "",
    postal_code: str = "",
) -> str:
    # Checking if any of the required address components are missing
    if (
        not street_number
        or not street_name
        or not city
        or not province
        or not postal_code
    ):
        raise ValueError("Missing required address components.")

    # Formatting the address with named parameters

    formatted_address += f"STREET NUMBER: {street_number.upper()}\n"
    formatted_address += f"APARTMENT NUMBER: {apartment_number.upper()}\n"
    formatted_address += f"STREET NAME: {street_name.upper()}\n"
    formatted_address += f"CITY: {city.upper()}\n"
    formatted_address += f"PROVINCE: {province.upper()}\n"
    formatted_address += f"POSTAL CODE: {postal_code.upper()}"

    return formatted_address


def main():
    # Getting user input for the address components
    street_number = input("Enter the street number: ")
    apartment_number = input("Enter the apartment number (optional): ")
    street_name = input("Enter the street name: ")
    city = input("Enter the city: ")
    province = input("Enter the province: ")
    postal_code = input("Enter the postal code: ")

    try:
        # Formatting the address using the format_address function
        formatted_address = format_address(
            apartment_number=apartment_number,
            street_number=street_number,
            street_name=street_name,
            city=city,
            province=province,
            postal_code=postal_code,
        )

        # Displaying the formatted address
        print(formatted_address)
    except ValueError as e:
        print(f"Error: {e}")


# Running the main function
if __name__ == "__main__":
    main()
