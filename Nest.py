from Species import Species
from GPS import GPS

class Nest:
    def __init__(self):
        self.__Nest_ID: str
        self.__Species:Species
        self.__nest_location: str  # Name of the beach where the survey is done
        self.__number_of_eggs: int
        self.__gps_location: GPS  # GPS coordinates (latitude, longitude)
    
    def set_nest_id(self, nest_id: str) -> None:
        """Set the unique identifier for the nest."""
        self.__Nest_ID = nest_id
        
    def set_species(self, species: Species) -> None:
        """Set the species associated with the nest."""
        self.__Species = species
        
    def set_nest_location(self, location: str) -> None:
        """Set the location of the nest."""
        self.__nest_location = location
        
    def set_number_of_eggs(self, number_of_eggs: int) -> None:
        """Set the number of eggs in the nest."""
        self.__number_of_eggs = number_of_eggs
        
    def set_gps_location(self, latitude: float, longitude: float) -> None:
        """Set the GPS coordinates for the nest."""
        self.__gps_location = GPS(latitude, longitude)
        
    def get_nest_id(self) -> str:
        """Get the unique identifier for the nest."""
        return self.__Nest_ID
    
    def get_species(self) -> Species:
        """Get the species associated with the nest."""
        return self.__Species
    
    def get_nest_location(self) -> str:
        """Get the location of the nest."""
        return self.__nest_location
    
    def get_number_of_eggs(self) -> int:
        """Get the number of eggs in the nest."""
        return self.__number_of_eggs
    
    def get_gps_location(self) -> GPS:
        """Get the GPS coordinates for the nest."""
        return self.__gps_location
        