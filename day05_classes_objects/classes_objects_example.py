print("Classes & Objects")


# Classes are blueprints
# Objects are the actual things you built
# variables => attributes
# functions => methods

# class names always starts with capital letter, CamelCase is conventional
class Movie:
    # __init__ is used to create an instance from the class
    # it's like a constructor in Java
    # We can also give default values to each attribute
    def __init__(self, title="SOME FILM", year=2020, imdb_score=5.0, have_seen=False):
        self.title = title
        self.year = year
        self.imdb_score = imdb_score
        self.have_seen = have_seen

    def nice_print(self):
        print(f"Title: {self.title}")
        print(f"Year:  {self.year}")
        print(f"IMDB score: {self.imdb_score}")
        print(f"I have seen it: {self.have_seen}")


film_1 = Movie("Life of Brian", 1979, 8.1, True)
film_2 = Movie("The Holy Grail", 1975, 8.2, False)

# print(film_1) will print some hash code
print(film_1.title)
print("----------------\n")

# multiple ways to use methods
Movie.nice_print(film_1) # or
print("----------------")
film_2.nice_print()


print("----------------")
# we can also create list of films
films = [film_1, film_2]

for each in films:
    print(f"Movie: {each.title}")


print("----------------")
# Creating a film using default constructor
film_3 = Movie()

film_3.nice_print()
