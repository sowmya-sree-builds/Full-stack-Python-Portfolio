# Create 4 Classes of your own choice

# class movie:
#     def __init__(self,movie,timeline):
#         self.movie = movie
#         self.timeline = timeline

#     def movieyear(self):
#         print(f'{self.movie} is released in the year {self.timeline}')

#     def hitmov(self):
#         print(f'{self.movie} is a hit')

# mov1=movie('bahubali',2017)
# mov1.movieyear()
# mov1.hitmov()
# mov2=movie('ninnukori',2019)
# mov2.hitmov()
# mov3=movie('anthariksham',2015)


# class cafe:
#     freedish='brownie'
#     def __init__(self,book,food,drinks):
#         self.book = book
#         self.food = food
#         self.drinks = drinks
    
#     def booktype(self):
#         print(f'lets get the genre of the book {self.book} heres your freedish {self.freedish}')

#     def foodcusine(self):
#         print(f'lets get the genre of the book {self.food}')

#     def drinkies(self):
#         print(f'lets get the genre of the book {self.drinks}')

# carla = cafe('death note','mushroom 65 ',' blueberry mojito')
# carla.booktype()


# class dog:
#     species='mammal'
#     area='hyderabad'
#     def __init__(self,name,breed):
#         self.name=name
#         self.breed=breed

#     def details(self):
#         print(f'the {self.name} of breed {self.breed} is {self.species} belongs to {self.area}')
    

# dog1=dog('bunty','indie')
# dog1.details()

# dog2=dog('chimtu','Pomerian')
# dog2.details()


# class Favi:
#     def __init__(self, char1, char2, movie_name):
#         self.char1 = char1
#         self.char2 = char2
#         self.movie_name = movie_name

#     def page(self):
#         print(f"Welcome to Disney's {self.movie_name}!")
#         print(f"Hey people, this is the crew from {self.movie_name}.")
#         print(f"I am {self.char1} and I am {self.char2}.")
#         print("-" * 40)

#     def plot_summary(self, summary):
#         print(f"Storyline of {self.movie_name}:")
#         print(summary)
#         print("-" * 40)

#     def fun_fact(self, fact):
#         print(f"Fun Fact about {self.movie_name}: {fact}")
#         print("-" * 40)

#     def cast_list(self, *members):
#         print(f"Cast of {self.movie_name}:")
#         for m in members:
#             print(f" - {m}")
#         print("-" * 40)


# movie = Favi("Rapunzel", "Flynn Rider", "Tangled")

# movie.page()
# movie.plot_summary("A lost princess with magical hair escapes her tower to discover the real world.")
# movie.fun_fact("Rapunzel’s hair is said to be around 70 feet long in the movie!")
# movie.cast_list("Rapunzel", "Flynn Rider", "Mother Gothel", "Pascal", "Maximus")
