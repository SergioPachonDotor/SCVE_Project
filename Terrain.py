class Terrain:
    def __init__(self):
        self.substrata_type: list[str]  # refers to where the nest placement is lay, for example, sand, gravel, mud, shell hash, vegetation (specify type, e.g., grass, sedge, forbs), mixed.
        self.sand:float
        self.gravel:float
        self.grass:float
        self.shell_hash:float
        self.wood:float

        # Method: self.nearest_neighbor_distance: float  # Distance to other shorebird nests (if colonial
        # Method:  self.nest_density: float  # Refers to the density measure of the surrounding area if the species nests in aggregations (e.g., number of nests per hectare). Eggs number/square meter.
        # Method: self.position_colony: float  # Refers to the distance to the closest conspecific
        # Method: self.distance_water: float  # Refers to the measure of the linear distance from the nest to the high tide.
        # Method: self.proportion_habitat_type: float  # refers to a defined radius (e.g., 100m, 500m, 1km) around the nest, estimate or map the percentage cover of different habitat types (e.g., grassland, wetland, forest, agriculture, developed).
        # Method: self.edge_effects: float  # Measure the length of habitat edges (e.g., where grassland meets forest) within a defined area around nest). Edge Effects, where different habitat types meet, have been shown to negatively affect nesting success in some bird groups, highlighting the importance of considering habitat edges in shorebird nesting environments as well.
        