from Nest import Nest
import numpy as np

class MathTools:
    def __init__(self):
        self.__absolute_abundance: dict[str, int]
        self.__relative_abundance: dict[str, float]
    
    def calculate_eclidian_distance(self, point1: tuple[float, float], point2: tuple[float, float]) -> float:
        """
        Calculate the Euclidean distance between two points.
        :param point1: Tuple containing (latitude, longitude) of the first point.
        :param point2: Tuple containing (latitude, longitude) of the second point.
        :return: Distance in meters.
        """
        lat1, lon1 = point1
        lat2, lon2 = point2
        
        return np.sqrt((lat2 - lat1) ** 2 + (lon2 - lon1) ** 2)

    def calculate_nest_density(self, nests:int, chunkarea:float) -> float:
        """
        Calculate the density of nests in a given area.
        :param nests: List of nest objects.
        :return: Nest density (nests per square meter).
        """
        return nests / chunkarea if chunkarea > 0 else 0.0
        
    def calculate_nearest_neighbor_distances(self, nests: list[Nest]) -> dict[dict[str, float]]:
        """
        Calculate the distances to the nearest neighboring nests.
        :param nests: List of nest objects. 
        :return: Dictionary with distances to other nests.
        """
        current_nest_lattitude:float
        current_nest_longitude:float
        other_nest_lattitude:float
        other_nest_longitude:float
        
        distances:dict[dict[str, float]] = {}
        
        for current_nest in nests:
            calculated_distances:dict[str, float] = {}
            current_nest_lattitude, current_nest_longitude = current_nest.get_gps_location().get_coordinates()
            current_nest_id:str = current_nest.get_nest_id()
            
            for other_nest in nests:
                if other_nest != current_nest:
                    other_nest_lattitude, other_nest_longitude = other_nest.get_gps_location().get_coordinates()
                    point1: tuple[float, float] = tuple(current_nest_lattitude, other_nest_lattitude)
                    point2: tuple[float, float] = tuple(current_nest_longitude, other_nest_longitude)
                    calculated_distances[other_nest.get_nest_id()] = self.calculate_eclidian_distance(point1, point2)
                    
            distances[current_nest_id] = calculated_distances
            
        return distances
        # Riqueza, Diversidad
        
    def calculate_absolute_abundance(self, nests: list[Nest]) -> dict[str, int]:
        """
        Calculate the absolute abundance of nests.
        :param nests: List of nest objects.
        :return: Absolute abundance (number of nests per species).
        """
        species_count:dict[str, int] = {}
        for nest in nests:
            if not isinstance(nest, Nest):
                raise TypeError("All items in nests must be of type Nest.")
            
            scientific_name:str = nest.get_species().get_scientific_name()
            species_count[scientific_name] = species_count.get(scientific_name, 0) + 1
            
        return species_count
    
    def calculate_relative_abundance(self, nests: list[Nest]) -> dict[str, float]:
        """
        Calculate the relative abundance of nests in a given area.
        :param nests: List of nest objects.
        :param chunkarea: ChunkArea object representing the area.
        :return: Relative abundance (nests per square meter).
        """
        species_count:dict[str, int] = self.calculate_absolute_abundance(nests)
        total_nests:int = len(nests)
        relative_abundance:dict[str, float] = {species: (count/(total_nests) if total_nests > 0 else 0.0) for species, count in species_count.items()}        
        
        return relative_abundance
    
    def calculate_species_richness(self, nests: list[Nest]) -> int:
        """
        Calculate the species richness from a list of nests.
        :param nests: List of nest objects.
        :return: Number of unique species.
        """
        unique_species:set[str] = set(nest.get_species().get_scientific_name() for nest in nests)
        return len(unique_species)
    
    def calculate_shannon_weiner_index(self, nests: list[Nest]) -> float:
        """
        Calculate the Shannon-Wiener index for species diversity.
        :param nests: List of nest objects.
        :return: Shannon-Wiener index value.
        """
        species_count:dict[str, int] = self.calculate_absolute_abundance(nests)
        total_nests:int = sum(species_count.values())
        shannon_index:float = 0.0
        
        if total_nests == 0:
            return shannon_index
        
        elif total_nests > 0 and len(species_count.keys()) > 1:
            for count in species_count.values():
                proportion = count / total_nests
                
                if proportion > 0:
                    shannon_index -= proportion * np.log(proportion)
                    
            return shannon_index
        
        
    def calculate_simpson_index_dominance(self, nests: list[Nest]) -> float:
        """_summary_

        Args:
            nests (list[Nest]): _description_

        Returns:
            float: _description_
        """
        relative_abundance:dict[str, float] = self.calculate_relative_abundance(nests)
        dominance:float = 0.0
        for ra in relative_abundance.values():
            dominance += ra ** 2

        return dominance
        
    def calculate_simpson_index_diversity(self, nests: list[Nest]) -> float:
        """ Calculate the Simpson index of diversity for a list of nests.
        Args:
            nests (list[Nest]): List of nest objects.
        Returns:
            float: Simpson index of diversity.
        """
        dominance:float = self.calculate_simpson_index_dominance(nests)
        return (1 - dominance) if dominance > 0 else 0.0
    
    def calculate_pielou_equiuitability_index(self, nests: list[Nest]) -> float:
        """ Calculate the Pielou's evenness index for a list of nests.
        Args:
            nests (list[Nest]): List of nest objects.
        Returns:
            float: Pielou's evenness index.
        """
        shannon_index:float = self.calculate_shannon_weiner_index(nests)
        species_richness:int = self.calculate_species_richness(nests)
        
        return (shannon_index / np.log(species_richness)) if shannon_index > 0 else 0.0