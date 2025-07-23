from GPS import GPS
from Terrain import Terrain
from Species import Species
from ChunkArea import ChunkArea

class SCVEchunk:
    def __init__(self):
        self.__gps:GPS
        self.__terrain:Terrain
        self.__species:Species
        self.__area:ChunkArea
        
    def set_gps(self, gps: GPS) -> None:
        """Set the GPS coordinates for the chunk."""
        self.__gps = gps
        
    def set_terrain(self, terrain: Terrain) -> None:
        """Set the terrain type for the chunk."""
        self.__terrain = terrain
        
    def set_species(self, species: Species) -> None:
        """Set the species associated with the chunk."""
        self.__species = species
    
    def set_area(self, area: ChunkArea) -> None:
        """Set the area of the chunk."""
        self.__area = area
    
    def get_gps(self) -> GPS:
        """Get the GPS coordinates for the chunk."""
        return self.__gps
    
    def get_terrain(self) -> Terrain:
        """Get the terrain type for the chunk."""
        return self.__terrain
    
    def get_species(self) -> Species:
        """Get the species associated with the chunk."""
        return self.__species
    
    def get_area(self) -> ChunkArea:
        """Get the area of the chunk."""
        return self.__area