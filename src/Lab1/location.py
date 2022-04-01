# CPE 202 Location Class, Lab 1

# represents a location using name, latitude and longitude
class Location:
    def __init__(self, name, lat, lon):
        self.name = name    # string for name of location
        self.lat = lat      # latitude in degrees (-90 to 90)
        self.lon = lon      # longitude in degrees (-180 to 180)
        
    def __val(self) -> tuple: # value private method for use in repr and eq
        return (self.name, self.lat, self.lon)
        
    def __repr__(self) -> str:
        return 'Location' + str(self.__val())# add location onto the string representation of a tuple containing its attributes
    
    def __eq__(self, __o: object) -> bool:
        return True if self.__val() == __o.__val() else False #compares the value of each location with another Location 
    
def main():
    loc1 = Location("SLO", 35.3, -120.7)
    loc2 = Location("Paris", 48.9, 2.4)
    loc3 = Location("SLO", 35.3, -120.7)
    loc4 = loc1

    print("Location 1:",loc1)
    print("Location 2:",loc2)
    print("Location 3:",loc3)
    print("Location 4:",loc4)

    print("\nLocation 1 equals Location 2:",loc1==loc2)
    print("Location 1 equals Location 3:",loc1==loc3)
    print("Location 1 equals Location 4:",loc1==loc4)

    locations = [loc1, loc2]
    print(loc1 in locations)
    print(loc2 in locations)
    print(loc3 in locations)
    print(loc4 in locations)

if __name__ == "__main__":
    main()