# Geocode Tool

This is a python tool to geocode addresses provided through a csv file. The project was initally designed for a client in healthcare domain but can be used by anyone. The tool provides an option to use both Google API (user needs to have their own Google API key) and Nomanitum (free) geocoding services. The csv file being uplaoded needs to have "patient address1", "patient city", "patient state", and "patient zip" columns in order to correctly geocode the address. The code can be modified to have different columns as per the input file. Once the addresses are geocoded, latitude and longitude columns are added to the upload file and are visible after refreshing the file. 

To launch this tool run command <python geocode_tool.py> in command prompt. This tool can also be distributed as an executable (exe). Run the command <pyinstaller --onefile geocode_tool.py> to generate the exe. 

This tool uses Python 3.9.13 for its functionality and PyQt6 for its UI design. 
