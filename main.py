class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name ,age ,tracks ,score):
        self.name = name
        self.age = age
        self.tracks =tracks
        self.score = score

    def change_name(self,new_name):
        self.name = new_name
        print('my name is ', self.name)


    def change_age(self,new_age):
        self.age = new_age
        print("i'm " , self.age ," years old")



    def add_track (self, new_tracks):
        self.tracks = new_tracks
        print('my tracks is', self.tracks)


    def get_score (self, new_score):
        self.score = new_score
        print('And i scored', self.score, 'out of '+ str(100))    



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)
# Expected methods
Bob.change_name("Lawal")
Bob.change_age(21)
Bob.add_track("BE")
Bob.get_score(78.5)
