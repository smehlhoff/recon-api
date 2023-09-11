from pydantic import BaseModel


class ObservationBase(BaseModel):
    id: int
    observation_time: str
    hour: str
    minute: str
    second: str
    coordinates: str
    latitude: str
    longitude: str
    aircraft_static_air_pressure: str | None
    aircraft_static_air_pressure_inhg: str | None
    aircraft_geopotential_height: str | None
    aircraft_geopotential_height_ft: str | None
    extrapolated_surface_pressure: str | None
    extrapolated_surface_pressure_inhg: str | None
    d_value: str | None
    d_value_ft: str | None
    air_temperature: str | None
    air_temperature_f: str | None
    dew_point: str | None
    dew_point_f: str | None
    wind_direction: str | None
    wind_cardinal_direction: str | None
    wind_speed: str | None
    wind_speed_mph: str | None
    peak_wind_speed: str | None
    peak_wind_speed_mph: str | None
    sfmr_peak_surface_wind_speed: str | None
    sfmr_peak_surface_wind_speed_mph: str | None
    sfmr_surface_rain_rate: str | None
    sfmr_surface_rain_rate_in: str | None
    quality_control_flags: str
    first_flag_decoded: str
    second_flag_decoded: str


class HighDensityObservationBase(BaseModel):
    id: int
    date: str
    observation_number: str
    product: str
    transmitted: str
    observations: list[ObservationBase] = []


class MissionBase(BaseModel):
    id: int
    callsign: str
    mission_number: str
    ocean_basin: str

    class Config:
        from_attributes = True


class MissionList(MissionBase):
    storm: str
    year: str


class MissionDetail(MissionBase):
    storm: str
    year: str
    high_density_observations: list[HighDensityObservationBase] = []


class StormsList(BaseModel):
    id: int
    name: str
    number: str
    ocean_basin: str
    year: str

    class Config:
        from_attributes = True


class StormDetail(StormsList):
    missions: list[MissionBase] = []
