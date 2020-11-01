class Song:

    def __init__(self,name,artist,duration):
        self.name = name
        self.artist = artist
        self.duration = duration

    def __eq__(self,other):

      if not isinstance(other,Song):
        return False
      
      if(self.name==other.name and self.artist == other.artist and self.duration == other.duration):
        return True
      
      return False