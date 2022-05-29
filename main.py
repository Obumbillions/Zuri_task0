class Student:
    def __init__(self):
        pass
    def __init__(self,name,age,tracks,score):
        self.name=str(name)
        self.age=int(age)
        self.tracks=list(tracks)
        self.score=float(score)
        print ( "My Name is ",name , "my age is age", age , "my tracks are", tracks, "my score is", score )


    
        

d =  Student ("naandam" ,24 ,["FE","BE"],30.50)
def speak(self):
    print("details of new students")
    def change_name(self, new_name):
        self.name = new_name
        print("name", new_name)
    def change_age(self, new_age):
        self.age= new_age
        print("age:", new_age)
    def change_tracks(self, new_tracks):
        self.tracks= new_tracks
        print("tracks:", self.tracks) 
    def get_scores(self,new_score):
         print("score:",self.score)
         return new_score   