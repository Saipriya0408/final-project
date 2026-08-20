"""
Haversine distance calculation utility.

Used by the doctor/hospital service to compute straight-line distances
between two GPS coordinates.
"""

import math


def haversine_km(lat1: float, lng1: float, lat2: float, lng2: float) -> float:
    """
    Calculate the great-circle distance in kilometres between two points
    on Earth specified by (latitude, longitude) in decimal degrees.

    Args:
        lat1, lng1: First point (user's location)
        lat2, lng2: Second point (doctor/hospital location)

    Returns:
        Distance in kilometres (float)
    """
    R = 6371.0  # Earth radius in km

    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    d_phi = math.radians(lat2 - lat1)
    d_lambda = math.radians(lng2 - lng1)

    a = (
        math.sin(d_phi / 2) ** 2
        + math.cos(phi1) * math.cos(phi2) * math.sin(d_lambda / 2) ** 2
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c
