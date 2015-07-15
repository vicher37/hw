__author__ = 'vickyzhang'

from pandas import read_csv

def costars():
    df = read_csv('/Users/vickyzhang/Documents/MSBA/programming/hw1/movies.csv', header=None)

    # ask user for inputs
    movie1 = raw_input("Please input movie 1")
    movie2 = raw_input("Please input movie 2")

    # check inputs, make sure they are all strings before processing
    for movie in [movie1, movie2]:
        try:
            isinstance(int(movie), int)
        except:
            print("Input cannot be converted into int, which mean it must be a string. Valid.")
        else:
            print("Your input is actually an int, not a string, not valid!")
            movie1 = raw_input("Please input the correct name of this movie again")

    # find actors in movie 1 and movie 2, separately
    actors_movie1 = []
    actors_movie2 = []
    for i in range(len(df)):
        if movie1 in df.loc[i,].values:
            actors_movie1.append(df.loc[i,][0])
        if movie2 in df.loc[i,].values:
            actors_movie2.append(df.loc[i,][0])

    # find actors in both movies, save in same_actors, using nested for loop
    # find actors in movie 1 but not in movie 2, save in in_1_not_in_2
    same_actors = []
    in_1_not_in_2 = []
    not_in_movie2 = True
    for actor1 in actors_movie1:
        for actor2 in actors_movie2:
            if actor1 == actor2:
                same_actors.append(actor1)
                not_in_movie2 = False
        if not_in_movie2 == True:
            in_1_not_in_2.append(actor1)

    # find actors in movie 2 but not in movie 1, save in in_2_not_in_1
    in_2_not_in_1 = []
    not_in_movie1 = True
    for actor2 in actors_movie2:
        for actor1 in actors_movie1:
            if actor2 == actor1:
                not_in_movie1 = False
        if not_in_movie1 == True:
            in_2_not_in_1.append(actor2)

    print same_actors, in_1_not_in_2, in_2_not_in_1


if __name__ == '__main__':
    costars()