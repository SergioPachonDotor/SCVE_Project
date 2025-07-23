class GPS:
    def __init__(self):
        self.lattitude: float
        self.longitude: float
        self.location: str  # Name of the beach where the survey is done
        
    def set_coordinates(self, latitude: float, longitude: float) -> None:
        """Set the GPS coordinates for the location."""
        self.lattitude = latitude
        self.longitude = longitude
        
    def get_coordinates(self) -> tuple[float, float]:
        """Get the GPS coordinates for the location."""
        return self.lattitude, self.longitude