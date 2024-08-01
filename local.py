from geopy.geocoders import Nominatim  # Vou utilizar um metodo do geopy para me retornar a localização

class Local:
    geolocator = Nominatim(user_agent="my_app") # A biblioteca exirge uma instancia para acessar o banco de dados
    
    # O construtor recebe os paremetros x(latitude) e y(longetude),
    # Os parametros já são definidos para converter qualquer tipo para (float) para evitar erro
    def __init__(self, latitude:float, longitude:float):
            self.latitude   = latitude 
            self.longitude  = longitude
    
    
    def __str__(self) -> str:
         return f'{self.latitude}, {self.longitude}'
            
    # Esta função sera usada para retornar a localização do banco de dados
    def pesquisa(self):
        # Caso a localização exista ele retorna todos os dados do local
        try:
            location = self.geolocator.reverse(f"{self.latitude}, {self.longitude}")
            return location.address
        except:
            return None