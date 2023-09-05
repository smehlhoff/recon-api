from datetime import datetime

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from core.models.database import Base, engine, SessionLocal
from core.models.models import Mission, Storm
from core.schemas.schemas import MissionDetail, MissionList, StormDetail, StormsList

current_year = str(datetime.now().year)

Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url="/docs", redoc_url=None)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/storms", response_model=list[StormsList])
def get_storms(year: str = current_year, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    query = db.query(Storm).filter_by(year=year).offset(skip).limit(limit).all()

    return query


@app.get("/storms/{storm_id}", response_model=StormDetail)
def get_storm(storm_id: int, db: Session = Depends(get_db)):
    query = db.query(Storm).filter_by(id=storm_id).first()

    if query is None:
        raise HTTPException(status_code=404, detail="Not found")

    return query


@app.get("/missions", response_model=list[MissionList])
def get_missions(year: str = current_year, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    query = db.query(Mission).join(Storm).filter(Storm.year == year).offset(skip).limit(limit).all()

    mission_data = []

    for mission in query:
        mission_data.append({
            "id": mission.id,
            "callsign": mission.callsign,
            "mission_number": mission.mission_number,
            "storm": mission.storm.name,
            "year": mission.storm.year
        })

    return mission_data


@app.get("/missions/{mission_id}", response_model=MissionDetail)
def get_mission(mission_id: int, db: Session = Depends(get_db)):
    query = db.query(Mission).filter_by(id=mission_id).first()

    if query is None:
        raise HTTPException(status_code=404, detail="Not found")

    mission_data = {
        "id": query.id,
        "callsign": query.callsign,
        "mission_number": query.mission_number,
        "storm": query.storm.name,
        "year": query.storm.year,
        "high_density_observations": []
    }

    for hdob in query.high_density_observations:
        hdob_data = {
            "id": hdob.id,
            "observation_number": hdob.observation_number,
            "product": hdob.product,
            "transmitted": hdob.transmitted,
            "observations": []
        }

        for observation in hdob.observations:
            obs_data = {
                "id": observation.id,
                "hour": observation.hour,
                "minute": observation.minute,
                "second": observation.second,
                "coordinates": observation.coordinates,
                "aircraft_static_air_pressure": observation.aircraft_static_air_pressure,
                "aircraft_geopotential_height": observation.aircraft_geopotential_height,
                "extrapolated_surface_pressure": observation.extrapolated_surface_pressure,
                "air_temperature": observation.air_temperature,
                "dew_point": observation.dew_point,
                "wind_direction": observation.wind_direction,
                "wind_speed": observation.wind_speed,
                "peak_wind_speed": observation.peak_wind_speed,
                "sfmr_peak_surface_wind_speed": observation.sfmr_peak_surface_wind_speed,
                "sfmr_surface_rate_rate": observation.sfmr_surface_rate_rate,
                "quality_control_flags": observation.quality_control_flags
            }

            hdob_data["observations"].append(obs_data)

        mission_data["high_density_observations"].append(hdob_data)

    return mission_data
