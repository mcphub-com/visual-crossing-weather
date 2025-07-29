markdown
# Visual Crossing Weather MCP Server

## Overview

The Visual Crossing Weather MCP Server is a powerful tool for accessing both historical weather data and weather forecasts on a global scale. It provides high-performance, cost-effective access to a wide range of weather metrics, including temperature, rainfall, wind speed (including gusts), snow, perceived temperature, humidity, and pressure.

This server is designed to cater to a variety of needs, from occasional use to enterprise-level public deployments, offering a comprehensive solution for all weather data requirements. With the ability to handle multiple locations in a single request, it maximizes efficiency and minimizes cost for users.

## Features

- **Global Weather Data**: Access both historical and forecast weather data from around the world.
- **Detailed Weather Metrics**: Retrieve information on temperature, rainfall, wind speed, snow, perceived temperature, humidity, and pressure.
- **Flexible Time Intervals**: Historical data is available at hourly and daily levels, while forecasts can be accessed at hourly, daily, and 12-hour intervals.
- **Multi-location Requests**: Make API calls that include multiple locations to enhance efficiency.
- **Enterprise-ready**: Suitable for both small-scale and large-scale deployments.

## Tool List

The server provides several tools that can be used to access different types of weather data:

1. **Weather Forecast Data**:
   - Provides access to weather forecast information.
   - Forecasts are available for up to seven days at hourly, 12-hour, and daily summary levels.

2. **Historical Weather Record**:
   - Suitable for retrieving hourly or daily historical weather records.

## Tool Details

- **Weather Forecast Data Tool**:
  - **Parameters**:
    - `contentType`: Choose between JSON or CSV output (optional).
    - `unitGroup`: Select the system of units for the output data (e.g., US, UK, metric).
    - `aggregateHours`: Define the interval between weather forecast data in the output (e.g., 1 for hourly, 12 for 12-hour periods, 24 for daily).
    - `location`: Specify the address or latitude/longitude of the location. Supports partial addresses and decimal degrees format.
    - `shortColumnNames`: Toggle between descriptive and abbreviated column names (optional).

- **Historical Weather Record Tool**:
  - **Parameters**:
    - `startDateTime`: Define the start date and time for the data request in ISO format.
    - `aggregateHours`: Set the interval for weather history data (e.g., 1 for hourly, 24 for daily).
    - `location`: Specify the address or latitude/longitude of the location. Supports partial addresses and decimal degrees format.
    - `endDateTime`: Define the end date and time for the data request in ISO format.
    - `unitGroup`: Select the system of units for the output data (e.g., US, UK, metric).
    - `dayStartTime`: Filter the output to records between specific day times for business hours (optional).
    - `contentType`: Choose between JSON or CSV output (optional).
    - `dayEndTime`: Specify the end time for the day filter (optional).
    - `shortColumnNames`: Toggle between descriptive and abbreviated column names (optional).

The Visual Crossing Weather MCP Server simplifies the integration of weather and climate information into applications and backend systems. It is an essential tool for developers looking to enhance their projects with robust weather data capabilities.