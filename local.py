from geopy.geocoders import Nominatim  # Vou utilizar um metodo do geopy para me retornar a localização

geolocator = Nominatim(user_agent="my_app")


class Local:
    # O construtor recebe os paremetros x(latitude) e y(longetude)
    def __init__(self, latitude:float, longitude:float):
            self.latitude   = latitude 
            self.longitude  = longitude
    
    
    def __str__(self) -> str:
         return f'{self.latitude}, {self.longitude}'
            
    # Esta função sera usada para retornar a localização do banco de dados
    def pesquisa(self):
        
        try:
            location = geolocator.reverse(f"{self.latitude}, {self.longitude}")
            return location.address
        except:
            return None