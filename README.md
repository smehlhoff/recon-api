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
  "id": 14,
  "callsign": "NOAA3",
  "mission_number": "14",
  "ocean_basin": "Atlantic",
  "storm": "Lee",
  "year": "2023",
  "high_density_observations": [
    {
      "id": 485,
      "date": "20230910",
      "observation_number": "01",
      "product": "URNT15 KWBC",
      "transmitted": "102037",
      "observations": [
        {
          "id": 9680,
          "observation_time": "202800",
          "hour": "20",
          "minute": "28",
          "second": "00",
          "coordinates": "1742N06448W",
          "latitude": "1742N",
          "longitude": "06448W",
          "aircraft_static_air_pressure": "1008.4",
          "aircraft_static_air_pressure_inhg": "29.78",
          "aircraft_geopotential_height": "30",
          "aircraft_geopotential_height_ft": "98",
          "extrapolated_surface_pressure": "1012.1",
          "extrapolated_surface_pressure_inhg": "29.89",
          "d_value": null,
          "d_value_ft": null,
          "air_temperature": "33.0",
          "air_temperature_f": "91.4",
          "dew_point": null,
          "dew_point_f": null,
          "wind_direction": "316",
          "wind_cardinal_direction": "NW",
          "wind_speed": "8",
          "wind_speed_mph": "9",
          "peak_wind_speed": "10",
          "peak_wind_speed_mph": "12",
          "sfmr_peak_surface_wind_speed": null,
          "sfmr_peak_surface_wind_speed_mph": null,
          "sfmr_surface_rain_rate": null,
          "sfmr_surface_rain_rate_in": null,
          "quality_control_flags": "05",
          "first_flag_decoded": "All parameters of nominal accuracy",
          "second_flag_decoded": "T/TD and SFMR questionable"
        },
        {
          "id": 9681,
          "observation_time": "202830",
          "hour": "20",
          "minute": "28",
          "second": "30",
          "coordinates": "1742N06447W",
          "latitude": "1742N",
          "longitude": "06447W",
          "aircraft_static_air_pressure": "1005.2",
          "aircraft_static_air_pressure_inhg": "29.68",
          "aircraft_geopotential_height": "56",
          "aircraft_geopotential_height_ft": "184",
          "extrapolated_surface_pressure": "1012.3",
          "extrapolated_surface_pressure_inhg": "29.89",
          "d_value": null,
          "d_value_ft": null,
          "air_temperature": "31.8",
          "air_temperature_f": "89.2",
          "dew_point": null,
          "dew_point_f": null,
          "wind_direction": "329",
          "wind_cardinal_direction": "NNW",
          "wind_speed": "8",
          "wind_speed_mph": "9",
          "peak_wind_speed": "9",
          "peak_wind_speed_mph": "10",
          "sfmr_peak_surface_wind_speed": null,
          "sfmr_peak_surface_wind_speed_mph": null,
          "sfmr_surface_rain_rate": null,
          "sfmr_surface_rain_rate_in": null,
          "quality_control_flags": "05",
          "first_flag_decoded": "All parameters of nominal accuracy",
          "second_flag_decoded": "T/TD and SFMR questionable"
        },
        {
          "id": 9682,
          "observation_time": "202900",
          "hour": "20",
          "minute": "29",
          "second": "00",
          "coordinates": "1742N06446W",
          "latitude": "1742N",
          "longitude": "06446W",
          "aircraft_static_air_pressure": "987.1",
          "aircraft_static_air_pressure_inhg": "29.15",
          "aircraft_geopotential_height": "217",
          "aircraft_geopotential_height_ft": "712",
          "extrapolated_surface_pressure": "1011.5",
          "extrapolated_surface_pressure_inhg": "29.87",
          "d_value": null,
          "d_value_ft": null,
          "air_temperature": "30.1",
          "air_temperature_f": "86.2",
          "dew_point": null,
          "dew_point_f": null,
          "wind_direction": "323",
          "wind_cardinal_direction": "NW",
          "wind_speed": "8",
          "wind_speed_mph": "9",
          "peak_wind_speed": "9",
          "peak_wind_speed_mph": "10",
          "sfmr_peak_surface_wind_speed": null,
          "sfmr_peak_surface_wind_speed_mph": null,
          "sfmr_surface_rain_rate": null,
          "sfmr_surface_rain_rate_in": null,
          "quality_control_flags": "05",
          "first_flag_decoded": "All parameters of nominal accuracy",
          "second_flag_decoded": "T/TD and SFMR questionable"
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
