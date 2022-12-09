"""Models for Open Data Platform of Gent."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass
class Garage:
    """Object representing a garage."""

    garage_id: str
    name: str
    parking_type: str
    url: str

    is_open: bool
    free_parking: bool
    temporary_closed: bool

    free_space: int
    total_capacity: int
    availability_pct: float
    occupation_pct: int

    longitude: float
    latitude: float
    updated_at: datetime

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Garage:
        """Return a Garage object from a dictionary.

        Args:
            data: The data from the API.

        Returns:
            A Garage object.
        """

        attr = data["fields"]
        geo = data["geometry"]["coordinates"]
        return cls(
            garage_id=str(data.get("recordid")),
            name=attr.get("name"),
            parking_type=attr.get("type"),
            url=attr.get("urllinkaddress"),
            is_open=bool(attr.get("isopennow")),
            free_parking=bool(attr.get("freeparking")),
            temporary_closed=bool(attr.get("temporaryclosed")),
            free_space=attr.get("availablecapacity"),
            total_capacity=attr.get("totalcapacity"),
            availability_pct=round(
                (
                    float(attr.get("availablecapacity"))
                    / float(attr.get("totalcapacity"))
                )
                * 100,
                1,
            ),
            occupation_pct=attr.get("occupation"),
            longitude=geo[0],
            latitude=geo[1],
            updated_at=datetime.strptime(attr.get("lastupdate"), "%Y-%m-%dT%H:%M:%S%z"),
        )


@dataclass
class ParkAndRide:
    """Object representing a park and ride spot."""

    spot_id: str
    name: str
    parking_type: str
    url: str

    is_open: bool
    free_parking: bool
    temporary_closed: bool
    gentse_feesten: bool

    free_space: int
    total_capacity: int
    availability_pct: float
    occupation_pct: int

    longitude: float
    latitude: float
    updated_at: datetime

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ParkAndRide:
        """Return a ParkAndRide object from a dictionary.

        Args:
            data: The data from the API.

        Returns:
            A ParkAndRide object.
        """

        def convert_bool(value: str) -> bool:
            """Convert a string to a boolean.

            Args:
                value: The string to convert.

            Returns:
                A boolean.
            """
            if value == "True":
                return True
            return False

        attr = data["fields"]
        geo = data["geometry"]["coordinates"]
        return cls(
            spot_id=str(data.get("recordid")),
            name=attr.get("name"),
            parking_type=attr.get("type"),
            url=attr.get("urllinkaddress"),
            is_open=bool(attr.get("isopennow")),
            free_parking=bool(attr.get("freeparking")),
            temporary_closed=bool(attr.get("temporaryclosed")),
            gentse_feesten=convert_bool(attr.get("gentse_feesten")),
            free_space=attr.get("availablespaces"),
            total_capacity=attr.get("numberofspaces"),
            availability_pct=round(
                (float(attr.get("availablespaces")) / float(attr.get("numberofspaces")))
                * 100,
                1,
            ),
            occupation_pct=attr.get("occupation"),
            longitude=geo[0],
            latitude=geo[1],
            updated_at=datetime.strptime(attr.get("lastupdate"), "%Y-%m-%dT%H:%M:%S%z"),
        )

   
@dataclass
class Bluebike:
    """Object representing a Bluebike location."""

    spot_id: str
    name: str
    type: str

    last_seen: datetime
    bikes_in_use: int
    bikes_available: int

    longitude: float
    latitude: float


    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Bluebike:
        """Return a Bluebike object from a dictionary.

        Args:
            data: The data from the API.

        Returns:
            A Bluebike object.
        """

        attr = data["fields"]
        return cls(
            spot_id=str(data.get("recordid")),
            name=attr.get("name"),
            type=attr.get("type"),
            last_seen=datetime.strptime(attr.get("last_seen"), "%Y-%m-%dT%H:%M:%S%z"),
            bikes_in_use=attr.get("bikes_in_use"),
            bikes_available=attr.get("bikes_available"),
            longitude=attr.get("longitude"),
            latitude=attr.get("latitude"),
        )

