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
  "id": 1,
  "callsign": "NOAA2",
  "mission_number": "09",
  "ocean_basin": "Atlantic",
  "storm": "Lee",
  "year": "2023",
  "high_density_observations": [
    {
      "id": 1,
      "observation_number": "38",
      "product": "URNT15 KWBC",
      "transmitted": "100244",
      "observations": [
        {
          "id": 1,
          "observation_time": "023430",
          "hour": "02",
          "minute": "34",
          "second": "30",
          "coordinates": "1806N06358W",
          "latitude": "1806N",
          "longitude": "06358W",
          "aircraft_static_air_pressure": "350.1",
          "aircraft_static_air_pressure_inhg": "10.34",
          "aircraft_geopotential_height": "5163",
          "aircraft_geopotential_height_ft": "16939",
          "extrapolated_surface_pressure": null,
          "extrapolated_surface_pressure_inhg": null,
          "d_value": "121",
          "d_value_ft": "397",
          "air_temperature": "-0.6",
          "air_temperature_f": "30.9",
          "dew_point": "-12.3",
          "dew_point_f": "9.9",
          "wind_direction": "20",
          "wind_cardinal_direction": "NNE",
          "wind_speed": "15",
          "wind_speed_mph": "17",
          "peak_wind_speed": "17",
          "peak_wind_speed_mph": "20",
          "sfmr_peak_surface_wind_speed": null,
          "sfmr_peak_surface_wind_speed_mph": null,
          "sfmr_surface_rain_rate": null,
          "sfmr_surface_rain_rate_in": null,
          "quality_control_flags": "03",
          "first_flag_decoded": "All parameters of nominal accuracy",
          "second_flag_decoded": "SFMR parameter(s) questionable"
        },
        {
          "id": 2,
          "observation_time": "023500",
          "hour": "02",
          "minute": "35",
          "second": "00",
          "coordinates": "1805N06400W",
          "latitude": "1805N",
          "longitude": "06400W",
          "aircraft_static_air_pressure": "569.0",
          "aircraft_static_air_pressure_inhg": "16.8",
          "aircraft_geopotential_height": "4888",
          "aircraft_geopotential_height_ft": "16037",
          "extrapolated_surface_pressure": "1012.8",
          "extrapolated_surface_pressure_inhg": "29.91",
          "d_value": null,
          "d_value_ft": null,
          "air_temperature": "0.5",
          "air_temperature_f": "32.9",
          "dew_point": "-9.7",
          "dew_point_f": "14.5",
          "wind_direction": "26",
          "wind_cardinal_direction": "NNE",
          "wind_speed": "16",
          "wind_speed_mph": "18",
          "peak_wind_speed": "17",
          "peak_wind_speed_mph": "20",
          "sfmr_peak_surface_wind_speed": null,
          "sfmr_peak_surface_wind_speed_mph": null,
          "sfmr_surface_rain_rate": null,
          "sfmr_surface_rain_rate_in": null,
          "quality_control_flags": "03",
          "first_flag_decoded": "All parameters of nominal accuracy",
          "second_flag_decoded": "SFMR parameter(s) questionable"
        },
        {
          "id": 3,
          "observation_time": "023530",
          "hour": "02",
          "minute": "35",
          "second": "30",
          "coordinates": "1804N06403W",
          "latitude": "1804N",
          "longitude": "06403W",
          "aircraft_static_air_pressure": "584.3",
          "aircraft_static_air_pressure_inhg": "17.25",
          "aircraft_geopotential_height": "4676",
          "aircraft_geopotential_height_ft": "15341",
          "extrapolated_surface_pressure": "1012.1",
          "extrapolated_surface_pressure_inhg": "29.89",
          "d_value": null,
          "d_value_ft": null,
          "air_temperature": "2.2",
          "air_temperature_f": "36.0",
          "dew_point": "-8.2",
          "dew_point_f": "17.2",
          "wind_direction": "27",
          "wind_cardinal_direction": "NNE",
          "wind_speed": "15",
          "wind_speed_mph": "17",
          "peak_wind_speed": "16",
          "peak_wind_speed_mph": "18",
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
