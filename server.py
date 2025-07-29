import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/visual-crossing-corporation-visual-crossing-corporation-default/api/visual-crossing-weather'

mcp = FastMCP('visual-crossing-weather')

@mcp.tool()
def weather_forecast_data(aggregateHours: Annotated[Union[int, float], Field(description='The interval between weather forecast data in the output. 1 represents an hourly forecast, 24 represents a daily forecast. As the source data is calculated at the hourly level, records calculated at 12 or 24 hours are aggregated to indicate the predominant weather condition during that time period. For example the maximum temperature, total precipitation, maximum windspeed etc. Supported values 1,12 or 24. Default: 24')],
                          location: Annotated[str, Field(description='he address or latitude or longitude of the location. Addresses can be specified as full addresses. The system will also attempt to match partial addresses such as city, state, zip code, postal code and other common formats. When specify a point based on longitude, latitude, the format must be specifed as latitude,longitude where both latitude and longitude are in decimal degrees. latitude should run from -90 to 90 and longitude from -180 to 180 (with 0 being at the prime meridian through London, UK).')],
                          contentType: Annotated[Union[str, None], Field(description='When present, choose between json or csv output')] = None,
                          unitGroup: Annotated[Union[str, None], Field(description='unitGroup - The system of units used for the output data. Supported values are us,uk,metric.')] = None,
                          shortColumnNames: Annotated[Union[bool, None], Field(description='When false, the returned dataset includes descriptive column names. When true, returns shorter, abbreviated column names with only alphanumeric characters. The short names are useful for programmatic use of the data.')] = None) -> dict: 
    '''Provides access to weather forecast information. The forecast is available for up to seven days at the hourly, 12 hour and daily summary level.'''
    url = 'https://visual-crossing-weather.p.rapidapi.com/forecast'
    headers = {'x-rapidapi-host': 'visual-crossing-weather.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'aggregateHours': aggregateHours,
        'location': location,
        'contentType': contentType,
        'unitGroup': unitGroup,
        'shortColumnNames': shortColumnNames,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def historical_weather_record(startDateTime: Annotated[str, Field(description='The date time for the start of the data request using the time zone of the location. In the ISO format: yyyy-MM-ddTHH:mm:ss. Hours should be specified in 24 hour clock format.')],
                              aggregateHours: Annotated[Union[int, float], Field(description='The interval between weather history data in the output. 1 represent hourly records, 24 represents a daily forecast. As the source data is recorded at the hourly level, 24 hour records are aggregated to indicate the predominant weather conditions during that time period. Supported values 1 or 24. Default: 24')],
                              location: Annotated[str, Field(description='The address or latitude or longitude of the location. Addresses can be specified as full addresses. The system will also attempt to match partial addresses such as city, state, zip code, postal code and other common formats. When specify a point based on longitude, latitude, the format must be specifed as latitude,longitude where both latitude and longitude are in decimal degrees. latitude should run from -90 to 90 and longitude from -180 to 180 (with 0 being at the prime meridian through London, UK).')],
                              endDateTime: Annotated[str, Field(description='The date time for the start of the data request using the time zone of the location. In the ISO format: yyyy-MM-ddTHH:mm:ss. Hours should be specified in 24 hour clock format.')],
                              unitGroup: Annotated[str, Field(description='The system of units used for the output data. Supported values are us,uk,metric')],
                              dayStartTime: Annotated[Union[str, None], Field(description='When present and not set to the same as the dayEndTime, filters the output to records that between the specified day times. This is useful for setting filters for business hours. Format h:m:ss (eg 9:00:00 woudl be 9am).')] = None,
                              contentType: Annotated[Union[str, None], Field(description='When present, choose between json or csv output')] = None,
                              dayEndTime: Annotated[Union[str, None], Field(description='When present and not set to the same as the dayEndTime, filters the output to records that between the specified day times.')] = None,
                              shortColumnNames: Annotated[Union[bool, None], Field(description='When false, the returned dataset includes descriptive column names. When true, returns shorter, abbreviated column names with only alphanumeric characters. The short names are useful for programmatic use of the data.')] = None) -> dict: 
    '''The weather history data is suitable for retrieving hourly or daily historical weather records.'''
    url = 'https://visual-crossing-weather.p.rapidapi.com/history'
    headers = {'x-rapidapi-host': 'visual-crossing-weather.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'startDateTime': startDateTime,
        'aggregateHours': aggregateHours,
        'location': location,
        'endDateTime': endDateTime,
        'unitGroup': unitGroup,
        'dayStartTime': dayStartTime,
        'contentType': contentType,
        'dayEndTime': dayEndTime,
        'shortColumnNames': shortColumnNames,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
