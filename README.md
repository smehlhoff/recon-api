# recon-api

API backend for interacting with high density observations from hurricane reconnaissance aircraft.

You can read more [here](https://www.nhc.noaa.gov/abouthdobs_2007.shtml) from National Hurricane Center.

Note: This is a work in progress. See [recon](https://github.com/smehlhoff/recon) for collecting and inserting the data into Postgres.

## Install

## Usage

Read the API docs here: `http://localhost:8000/docs`

## Example

```json
{
  "id": 25,
  "callsign": "NOAA3",
  "mission_number": "07",
  "ocean_basin": "Atlantic",
  "storm": "Lee",
  "year": "2023",
  "high_density_observations": [
    {
      "id": 910,
      "observation_number": "01",
      "product": "URNT15 KWBC",
      "transmitted": "090843",
      "observations": [
        {
          "id": 18181,
          "observation_time": "083330",
          "hour": "08",
          "minute": "33",
          "second": "30",
          "coordinates": "1742N06448W",
          "latitude": "1742N",
          "longitude": "06448W",
          "aircraft_static_air_pressure": "9.0",
          "aircraft_static_air_pressure_inhg": "0.27",
          "aircraft_geopotential_height": "21",
          "aircraft_geopotential_height_ft": "68",
          "extrapolated_surface_pressure": "11.3",
          "extrapolated_surface_pressure_inhg": "0.33",
          "air_temperature": "26.8",
          "air_temperature_f": "80.2",
          "dew_point": "25.5",
          "dew_point_f": "77.9",
          "wind_direction": "343",
          "wind_cardinal_direction": "NNW",
          "wind_speed": "4",
          "wind_speed_mph": "4",
          "peak_wind_speed": "8",
          "peak_wind_speed_mph": "9",
          "sfmr_peak_surface_wind_speed": null,
          "sfmr_peak_surface_wind_speed_mph": null,
          "sfmr_surface_rain_rate": null,
          "sfmr_surface_rain_rate_in": null,
          "quality_control_flags": "03",
          "first_flag_decoded": "All parameters of nominal accuracy",
          "second_flag_decoded": "SFMR parameter(s) questionable"
        },
        {
          "id": 18182,
          "observation_time": "083400",
          "hour": "08",
          "minute": "34",
          "second": "00",
          "coordinates": "1742N06447W",
          "latitude": "1742N",
          "longitude": "06447W",
          "aircraft_static_air_pressure": "6.0",
          "aircraft_static_air_pressure_inhg": "0.18",
          "aircraft_geopotential_height": "44",
          "aircraft_geopotential_height_ft": "144",
          "extrapolated_surface_pressure": "11.3",
          "extrapolated_surface_pressure_inhg": "0.33",
          "air_temperature": "28.1",
          "air_temperature_f": "82.6",
          "dew_point": "25.6",
          "dew_point_f": "78.1",
          "wind_direction": "47",
          "wind_cardinal_direction": "NE",
          "wind_speed": "5",
          "wind_speed_mph": "5",
          "peak_wind_speed": "10",
          "peak_wind_speed_mph": "11",
          "sfmr_peak_surface_wind_speed": null,
          "sfmr_peak_surface_wind_speed_mph": null,
          "sfmr_surface_rain_rate": null,
          "sfmr_surface_rain_rate_in": null,
          "quality_control_flags": "03",
          "first_flag_decoded": "All parameters of nominal accuracy",
          "second_flag_decoded": "SFMR parameter(s) questionable"
        },
        {
          "id": 18183,
          "observation_time": "083430",
          "hour": "08",
          "minute": "34",
          "second": "30",
          "coordinates": "1742N06446W",
          "latitude": "1742N",
          "longitude": "06446W",
          "aircraft_static_air_pressure": "992.6",
          "aircraft_static_air_pressure_inhg": "29.31",
          "aircraft_geopotential_height": "166",
          "aircraft_geopotential_height_ft": "544",
          "extrapolated_surface_pressure": "11.3",
          "extrapolated_surface_pressure_inhg": "0.33",
          "air_temperature": "28.5",
          "air_temperature_f": "83.3",
          "dew_point": "25.1",
          "dew_point_f": "77.2",
          "wind_direction": "63",
          "wind_cardinal_direction": "ENE",
          "wind_speed": "12",
          "wind_speed_mph": "13",
          "peak_wind_speed": "13",
          "peak_wind_speed_mph": "14",
          "sfmr_peak_surface_wind_speed": null,
          "sfmr_peak_surface_wind_speed_mph": null,
          "sfmr_surface_rain_rate": null,
          "sfmr_surface_rain_rate_in": null,
          "quality_control_flags": "03",
          "first_flag_decoded": "All parameters of nominal accuracy",
          "second_flag_decoded": "SFMR parameter(s) questionable"
        }
      ]
    }
  ]
}
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://github.com/smehlhoff/recon-api/blob/master/LICENSE)
