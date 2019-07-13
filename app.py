"""

- Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, 'q' to quit:

- Add movies
- See movies
- Find movie
- Stop running the program

Tasks:
[]: Show the user the main interface and get their input
[]: Allow users to add movies
[]: Allow users to show all their movies
[]: Find a movie
[]: Stop running the program when they type 'q'

for testing
movies = [
    {
        'title': 'Avengers',
        'director': 'Russo',
        'year': '2018',
    },
    {
        'title': 'Transformers',
        'director': 'Michael',
        'year': '2017',
    },
    {
        'title': 'Avengers',
        'director': 'Seth',
        'year': '2015',
    }
]

"""

movies = []

def main():
    print('Enter "a" to add a movie, "l" to see your movies, "f" to find a movie, or "q" to quit')
    user_input = input("What would you like to do: ")
    # print(user_input)
    while user_input is not 'q':
        if user_input is 'a':
            # print('a')
            add()
        elif user_input is 'l':
            # print('l')
            list()
        elif user_input is 'f':
            # print('f')
            print('Enter "title" to search by title, "director" by director, or "year" by year.')
            key = input('Which category would you like to search by: ')
            value = input(f'Enter the {key} of the movie: ')
            result = find(key, value)
            print(result)
        else:
            print('You did not enter one of the options')
        print('Enter "a" to add a movie, "l" to see your movies, "f" to find a movie, or "q" to quit')
        user_input = input('What would you like to do: ')
    print('quitting program ... ')
    return

def add():
    movie_title = input('Add the title for your movie: ')
    movie_director = input('Add the director for your movie: ')
    movie_year = input('Add the year for your movie: ')
    new_movie = {
        'title': movie_title,
        'director': movie_director,
        'year': movie_year,
    }
    movies.append(new_movie)
    print('Movie Added!')

def list():
    print(movies)

def find(key, value):
    new_movie_list = [movie for movie in movies if movie[key] == value]
    print('Here is the result of the search')
    return new_movie_list

main()