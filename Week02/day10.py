#-- This list shows my top 5 favourite movies --
favourite_movies = ["Iruvar", "Thalapathi", "Guru", "Soodhu Kavvum", "Saarpatta Parambarai"]

print("My favourite movies are:")
print(favourite_movies)

print(f"My absolute favourite movie is: {favourite_movies[1]}")
print(f"The movie i should at bottom in this list is: {favourite_movies[4
]}")

print("\noops i forgot one")
favourite_movies.append("Muthalvan")

print("My updated movie list:")
print(favourite_movies)

num_movies = len(favourite_movies)
print(f"\nI now have {num_movies} movies in my favourite list")