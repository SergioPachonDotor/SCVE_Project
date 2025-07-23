from GPS import GPS

class ChunkArea:
    def __init__(self) -> None:
        self.__chunk_id: str  # Unique identifier for the chunk area
        self.__gps: GPS  # GPS coordinates (latitude, longitude)
        self.__x: float  # X coordinate in the chunk area (width)
        self.__y: float  # Y coordinate in the chunk area (height)
    
    def set_chunk_id(self, chunk_id: str) -> None:
        """Set the unique identifier for the chunk area."""
        self.__chunk_id = chunk_id
    
    def set_gps(self, latitude: float, longitude: float) -> None:
        """Set the GPS coordinates for the chunk area."""
        self.__gps = GPS(latitude, longitude)
    
    def set_coordinates(self, x: float, y: float) -> None:
        """Set the X and Y coordinates for the chunk area."""
        self.__x = x
        self.__y = y
    
    def get_chunk_id(self) -> str:
        """Get the unique identifier for the chunk area."""
        return self.__chunk_id
    
    def get_gps(self) -> GPS:
        """Get the GPS coordinates for the chunk area."""
        return self.__gps
    
    def get_coordinates(self) -> tuple[float, float]:
        """Get the X and Y coordinates for the chunk area."""
        return self.__x, self.__y
    
    def calculate_area(self) -> float:
        """Calculate the area of the chunk based on its coordinates."""
        X:float
        Y:float
        X, Y = self.get_coordinates()
        return X * Y