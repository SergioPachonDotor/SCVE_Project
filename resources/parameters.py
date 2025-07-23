# Variables
# Species_Data
Nest_ID:str # Location,Name Sector Initials, Common Name Initials, Eggs Number.
Species_Common_Name:str
Species_Scientific_Name:str # Genus, Species.
Start_Date:str # Date Format: Month, Day, Year.
End_Date:str # Date Format: Month, Day, Year.
Location:str # Name of the beach where the survey is done.
GPS:list[float] # Decimal Degrees: Latitude, Longitude.

# Nesting Biology and Ecology
Number_of_Eggs:int # Number of eggs per nest.
Nest_Status:list[str] # Active, depredated, flooded, hatched, abandoned.
Nest_Status_Date:str # Date of nest discovery and date of failure or hatching.
Nest_Fate:list[str] # Nest Fate (successful or failed) is crucial, and criteria such as the presence of eggshell fragments can be used as evidence of hatching.
Hatching_Rate:float # Refers to the proportion of eggs that hatch in the overall proportion of eggs laid in a population or study area that successfully hatch.
Fledging_Rate:float # Represents the number of chicks that successfully survive from hatching to the point of fledging (becoming capable of flight) per nesting attempt or per successful nest.

# Nesting Habitat and Protection
Sustrata_Type:list[str] # refers to where the nest placement is lay, for example, sand, gravel, mud, shell hash, vegetation (specify type, e.g., grass, sedge, forbs), mixed.
Litter_Cover:float # Litter Cover refers to the percentage of ground covered by dead vegetation (leaf litter, thatch) within a defined radius (1 meter radius). It can be measure by a photograph.
Precense_Camouflage:list[str] # Low, medium, and high camoflage of the nest; Camouflage refers of how well the nest blends with its surroundings.
Nearest_Neighbor_Distance:float # Distance to other shorebird nests (if colonial or semi-colonial) refers to the measure of the distance to the nearest neighboring shorebird nests of the same or different species.
Nest_Density:float # Refers to the density measure of the surrounding area if the species nests in aggregations (e.g., number of nests per hectare). Eggs number/square meter.
Position_Colony:float # Refers to the distance to the closest conspecific nest.
Distance_Water:float # Refers to the measure of the linear distance from the nest to the high tide.
Proportion_Habitat_Type:float # refers to a defined radius (e.g., 100m, 500m, 1km) around the nest, estimate or map the percentage cover of different habitat types (e.g., grassland, wetland, forest, agriculture, developed).
Edge_Effects:float # Measure the length of habitat edges (e.g., where grassland meets forest) within a defined area around nest). Edge Effects, where different habitat types meet, have been shown to negatively affect nesting success in some bird groups, highlighting the importance of considering habitat edges in shorebird nesting environments as well.

# Nesting Human Disturbing
Distance_Human_Disturbance:float # Refers to the measure of the nest distance to the nearest disturbance area (e.g., trails, roads, buildings, parking lots, boardwalk or areas of high human activity).

# Nesting Atmospheric and Oceanic Variables
Temperature:float # Eggs can suffer mortality due to overheating if left exposed in high temperatures, or chilling if parental incubation is disrupted. Young chicks, being less able to regulate their body temperature, are also vulnerable to both heat and cold stress. It's measure in centigrades.
Wind:float # High winds can directly destroy nests and lead to the loss of eggs or young chicks. It's measure in kilometer per hour.
Precipitation:float # Intense Precipitation events poses a direct threat to shorebird nesting success. Altered precipitation patterns can directly impact nesting success through nest flooding, particularly in low-lying coastal areas or regions experiencing increased rainfall or storm events. It's measure in milimeters.
Tide_Level:float # Tide Level leads to nest flooding and is the most direct and often catastrophic impact is the inundation of nests by high tides, especially during spring tides (the highest high tides) or storm surges. Eggs and young chicks are particularly vulnerable and can be washed away or succumb to cold and exposure after flooding. It's measured in meters.
Sea_Level_Rise:float # It translates to the inundation and erosion of critical breeding grounds, including beaches areas where shorebirds nest. It's measured in meters.
Extreme_Weather_Events:float # Refers to the increase in the frequency and intensity of events such as storms, hurricanes, and cyclones, they pose a direct and immediate threat to shorebird nesting efforts. Predictions of more frequent and intense storms suggest a heightened risk of nest destruction and chick mortality.
Storm_Surge:float # Storm Surges can directly destroy nests and lead to the loss of eggs or young chicks. It's measured in meters.
Temperature_Fluctuation:float # Fluctuations in Temperature, particularly extreme heat or cold, can lead to egg mortality if parents are forced to leave the nest due to thermal stress or disturbance. It's measured in centigrades.
Topography:float # Topography, refers to the measuring of the nest sites elevation relative to a known datum, by characterizing microtopography surrounding the nest site (e.g., slope, presence of hummocks or depressions) to analyze nest placement in relation to topographic features (e.g., LiDAR-derived elevation models). The data can be help to compare nest success across different topographic settings, whether nests located at different elevations or on different topographic features (e.g., dune crests vs. beach flats) have different hatching or fledging success rates, it also can be used to do Modeling Inundation Risk based on topography and Tide Levels by combining topographic data with tidal predictions to assess the potential for flooding at different nesting elevations, lastly it can document whether nesting birds show a preference for specific topographic features.
Water_Quality:None