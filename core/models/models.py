from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Storm(Base):
    __tablename__ = "storms"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    number = Column(String)
    ocean_basin = Column(String)
    year = Column(String)
    missions = relationship("Mission", back_populates="storm")


class Mission(Base):
    __tablename__ = "missions"

    id = Column(Integer, primary_key=True)
    callsign = Column(String)
    mission_number = Column(String)
    storm_id = Column(Integer, ForeignKey("storms.id"))
    high_density_observations = relationship("HighDensityObservation", back_populates="mission")
    storm = relationship("Storm", back_populates="missions")


class HighDensityObservation(Base):
    __tablename__ = "high_density_observations"

    id = Column(Integer, primary_key=True)
    date = Column(String)
    file = Column(String)
    observation_number = Column(String)
    product = Column(String)
    transmitted = Column(String)
    mission_id = Column(Integer, ForeignKey("missions.id"))
    mission = relationship("Mission", back_populates="high_density_observations")
    observations = relationship("Observation", back_populates="high_density_observation")


class Observation(Base):
    __tablename__ = "observations"

    id = Column(Integer, primary_key=True)
    observation_time = Column(String)
    hour = Column(String)
    minute = Column(String)
    second = Column(String)
    coordinates = Column(String)
    latitude = Column(String)
    longitude = Column(String)
    aircraft_static_air_pressure = Column(String)
    aircraft_static_air_pressure_inhg = Column(String)
    aircraft_geopotential_height = Column(String)
    aircraft_geopotential_height_ft = Column(String)
    extrapolated_surface_pressure = Column(String)
    extrapolated_surface_pressure_inhg = Column(String)
    d_value = Column(String)
    d_value_ft = Column(String)
    air_temperature = Column(String)
    air_temperature_f = Column(String)
    dew_point = Column(String)
    dew_point_f = Column(String)
    wind_direction = Column(String)
    wind_cardinal_direction = Column(String)
    wind_speed = Column(String)
    wind_speed_mph = Column(String)
    peak_wind_speed = Column(String)
    peak_wind_speed_mph = Column(String)
    sfmr_peak_surface_wind_speed = Column(String)
    sfmr_peak_surface_wind_speed_mph = Column(String)
    sfmr_surface_rain_rate = Column(String)
    sfmr_surface_rain_rate_in = Column(String)
    quality_control_flags = Column(String)
    first_flag_decoded = Column(String)
    second_flag_decoded = Column(String)
    high_density_observation_id = Column(Integer, ForeignKey("high_density_observations.id"))
    high_density_observation = relationship("HighDensityObservation", back_populates="observations")
