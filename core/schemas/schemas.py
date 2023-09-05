from pydantic import BaseModel


class ObservationBase(BaseModel):
    id: int
    hour: str
    minute: str
    second: str
    coordinates: str
    aircraft_static_air_pressure: str
    aircraft_geopotential_height: str
    extrapolated_surface_pressure: str | None
    air_temperature: str | None
    dew_point: str | None
    wind_direction: str | None
    wind_speed: str | None
    peak_wind_speed: str | None
    sfmr_peak_surface_wind_speed: str | None
    sfmr_surface_rate_rate: str | None
    quality_control_flags: str


class HighDensityObservationBase(BaseModel):
    id: int
    observation_number: str
    product: str
    transmitted: str
    observations: list[ObservationBase] = []


class MissionBase(BaseModel):
    id: int
    callsign: str
    mission_number: str

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
