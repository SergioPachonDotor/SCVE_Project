from ChunkArea import ChunkArea
from GPS import GPS
from Nest import Nest

class NestRecord:
    def __init__(self):
        self.nest: Nest # Nest details
        self.recorded_date: str  # Date when the nest was recorded
        self.recorded_time: str  # Time when the nest was recorded
        self.observer: str  # Name of the
        self.gps_location: GPS  # GPS coordinates (latitude, longitude)
        
    def calculate_nest_density(self, nests:int) -> float:
        """
        Calculate the density of nests in a given area.
        :param nests: List of nest objects.
        :return: Nest density (nests per square meter).
        """
        area:float
        # nests/area
        current_chunk_area:ChunkArea = ChunkArea()
        current_chunk_area.set_coordinates(100, 100)  # Example coordinates
        area = current_chunk_area.calculate_area()
        return len(nests) / area if area > 0 else 0.0
        
    def calculate_nearest_neighbor_distance(self, nests: list) -> float:
        """
        Calculate the distance to the nearest neighboring nest.
        :param nests: List of nest objects.
        :return: Nearest neighbor distance (in meters).
        """
        
        # Method: self.nearest_neighbor_distance: float  # Distance to other shorebird nests (if colonial
        # Method: self.nest_density: float  # Refers to the density measure of the surrounding area if the species nests in aggregations (e.g., number of nests per hectare). Eggs number/square meter.
        # Method: self.position_colony: float  # Refers to the distance to the closest conspecific
        # Method: self.distance_water: float  # Refers to the measure of the linear distance from the nest to the high tide.
        # Method: self.proportion_habitat_type: float  # refers to a defined radius (e.g., 100m, 500m, 1km) around the nest, estimate or map the percentage cover of different habitat types (e.g., grassland, wetland, forest, agriculture, developed).
        # Method: self.edge_effects: float  # Measure the length of habitat edges (e.g., where grassland meets forest) within a defined area around nest). Edge Effects, where different habitat types meet, have been shown to negatively affect nesting success in some bird groups, highlighting the importance of considering habitat edges in shorebird nesting environments as well.