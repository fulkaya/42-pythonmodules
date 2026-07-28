from typing import List
from pydantic import BaseModel, Field, ValidationError, model_validator
from enum import Enum
from datetime import datetime


class CrewRanks(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: CrewRanks
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission_rules(self) -> 'SpaceMission':
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        for member in self.crew:
            if not member.is_active:
                raise ValueError(
                    f"Crew member {member.name} is not active"
                )

        has_leadership = any(
            member.rank in (CrewRanks.COMMANDER, CrewRanks.CAPTAIN)
            for member in self.crew
        )
        if not has_leadership:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        if self.duration_days > 365:
            experienced_count = sum(
                1 for m in self.crew if m.years_experience >= 5
            )
            if experienced_count / len(self.crew) < 0.5:
                raise ValueError(
                    "Long missions (> 365 days) need at least 50% "
                    "experienced crew (5+ years)"
                )

        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 40)

    crew1 = [
        CrewMember(
            member_id="M01",
            name="Sarah Connor",
            rank=CrewRanks.COMMANDER,
            age=40,
            specialization="Mission Command",
            years_experience=15
        ),
        CrewMember(
            member_id="M02",
            name="John Smith",
            rank=CrewRanks.LIEUTENANT,
            age=32,
            specialization="Navigation",
            years_experience=6
        ),
        CrewMember(
            member_id="M03",
            name="Alice Johnson",
            rank=CrewRanks.OFFICER,
            age=28,
            specialization="Engineering",
            years_experience=3
        )
    ]

    try:
        valid_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=crew1,
            budget_millions=2500.0
        )
        print("Valid mission created:")
        print(f"Mission: {valid_mission.mission_name}")
        print(f"ID: {valid_mission.mission_id}")
        print(f"Destination: {valid_mission.destination}")
        print(f"Duration: {valid_mission.duration_days} days")
        print(f"Budget: ${valid_mission.budget_millions}M")
        print(f"Crew size: {len(valid_mission.crew)}")
        print("Crew members:")
        for member in valid_mission.crew:
            print(
                f"- {member.name} ({member.rank.value}) - "
                f"{member.specialization}"
            )
    except ValidationError as e:
        print(f"Unexpected error: {e}")

    print()
    print("=" * 40)
    print("Expected validation error:")

    crew2 = [
        CrewMember(
            member_id="M04",
            name="Bob Brown",
            rank=CrewRanks.LIEUTENANT,
            age=30,
            specialization="Piloting",
            years_experience=4
        ),
        CrewMember(
            member_id="M05",
            name="Charlie Green",
            rank=CrewRanks.CADET,
            age=22,
            specialization="Medical",
            years_experience=1
        ),
    ]

    try:
        SpaceMission(
            mission_id="M2024_LUNAR",
            mission_name="Lunar Base Alpha",
            destination="Moon",
            launch_date=datetime.now(),
            duration_days=180,
            crew=crew2,
            budget_millions=500.0
        )
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"][13:])


if __name__ == "__main__":
    main()
