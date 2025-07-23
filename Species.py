class Species:
    def __init__(self):
        self.Species_Common_Name: str
        self.Species_Scientific_Name: str
    
    def set_common_name(self, common_name: str) -> None:
        """Set the common name of the species."""
        self.Species_Common_Name = common_name
        
    def set_scientific_name(self, scientific_name: str) -> None:
        """Set the scientific name of the species."""
        self.Species_Scientific_Name = scientific_name
        
    def get_common_name(self) -> str:
        """Get the common name of the species."""
        return self.Species_Common_Name
    
    def get_scientific_name(self) -> str:
        """Get the scientific name of the species."""
        return self.Species_Scientific_Name