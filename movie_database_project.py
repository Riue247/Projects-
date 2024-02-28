## Please read instructions from Instructions.md and write your code below

import sys
##this import is to impliment way to terminate the program on command in the code

def data():
  my_dict={
    Movie_A: ['The Godfather',1972,"Francis Ford Coppola", "Crime, Drama",9.2],
    Movie_B:["The Shawshank Redemption",1994, "Frank Darabont","Drama",9.3],
    Movie_C:["The Dark Knight",2008,"Christopher Nolan","Action,Crime,Drama",9.0],
    Movie_D:["Forrest Gump",1994,"Robert Zemeckis","Comedy, Drama, Romance",8.8],
    Movie_E:["The Matrix",1999,"Lana Wachowski, Lilly Wachowski","Action, Sci-Fi",8.7]
  }
  ##data that was given for the project, decided to make a dictionary for it
  ##(just a idea refrence. i didn't end up using this) make a list for all movies and other categories just in case i need a better way of accessing all the data. 

def placement():
  data_placement=['title', 'year of release', 'director', 'genre', 'rating(out of 10)']
##Again a refrence. This wasn't used


def menu():
  menu_input=input(
  """"
  Menu:
  1.Search a Movie
  2.Add a New Movie
  3.Update a Movie
  4.Delete a Movie
  5.Exit the program
  """)
  if menu_input==1:
    print(search(data()))
  elif menu_input==2:
    print(add_new_Movie(data()))
  elif menu_input==3:
    print(update_movie(data()))
  elif menu_input==4:
    print(delete_movie(data()))
  elif menu_input==5:
    print(exit())
  ##this is the menu function. This uses all of the functions created and made a way to give the user a way to choose which function they want to access.



def search():
  while true:
    search_answer=input('what movie would you like to search for:')
    if search_answer=='The Godfather':
      print(data(my_dict[Movie_A]))
    elif search_answer=='The Shawshank Redemptiom':
      print(data(my_dict[Movie_B]))
    elif search_answer=='The Dark Knight':
      print(data(my_dict[Movie_C]))
    elif search_answer=='Forrest Gump':
      print(data(my_dict[Movie_D]))
    elif search_answer=='The Matrix':
      print(data(my_dict[Movie_E]))
    elif search_answer!= data(my_dict):
      answerback=input('movie not found. would you like to add it to the list?(y/n)')
      if answerback==y:
        data(my_dict[Move_F]==search_answer)
    continue_on=input('would you like to search again?(y/n)')
    if continue_on=='n':
      break
##this search fucntion was used with simple if statements to see if the user would type in the movie they are looking for and then printing all the information about the movie.and then if there is a movie that isn't in the data base, add that into a new key and value into our dictionary.and then lastly asks the user if they want to search again. if not then the while loop will break.



def add_new_Movie():
  new_movie=[]
  print('enter the following information in the following order to add a movie(title,Year of release, Director, Genre, rating (out of 10)')
for this in range(4):
  movie_unknown=input('enter the information in the correct order here.(once you enter each piece of information, press enter):')
  new_movie.append(movie_unknown)
print('Movie added!')
##this add new movie funciton allows you to consectively enter all the details and put it into a list and enter this information into the data base.





def update_movie():
  print('welcome to updating a movie!')
  movie_ID=input('enter the movie that you would like to update:')
  if movie_ID=='The Godfather':
    for elements in data(my_dict[Movie_A]):
      print(elements)
    movie_change=input('what numbered place of information would you like to change?(from number0-4) ')
    if movie_change==0:
      title=input('what would you change the title of "the Godfather" to?')
      data(my_dict[Movie_A][0]=title)
    elif movie_change==1:
      year=input('what would you change the year of this movie to?:')
      data(my_dict[Movie_A][1]=year)
    elif movie_change=2:
      director=input('what director name do you want to change?:')
      data(my_dict[Movie_A][2]=director)
    elif movie_change=3:
      genre=input('what genre would you like to change it to?:')
      data(my_dict[Movie_A][3]=genre)
    elif movie_change=4:
      rating=input('what rating would you change this movie to?:')
      data(my_dict[Movie_A][4]=rating)
  if movie_ID=='The Shawshank Redemption':
    for elements in data(my_dict[Movie_B]):
      print(elements)
    movie_change=input('what numbered place of information would you like to change?(from number0-4) ')
    if movie_change==0:
      title=input('what would you change the title of "The Shawshank Redemption" to?')
      data(my_dict[Movie_B][0]=title)
    elif movie_change==1:
      year=input('what would you change the year of this movie to?:')
      data(my_dict[Movie_B][1]=year)
    elif movie_change=2:
      director=input('what director name do you want to change?:')
      data(my_dict[Movie_B][2]=director)
    elif movie_change=3:
      genre=input('what genre would you like to change it to?:')
      data(my_dict[Movie_B][3]=genre)
    elif movie_change=4:
      rating=input('what rating would you change this movie to?:')
      data(my_dict[Movie_B][4]=rating)
  if movie_ID=='The Dark Knight':
    for elements in data(my_dict[Movie_C]):
      print(elements)
    movie_change=input('what numbered place of information would you like to change?(from number0-4) ')
    if movie_change==0:
      title=input('what would you change the title of "The Dark Knight" to?')
      data(my_dict[Movie_C][0]=title)
    elif movie_change==1:
      year=input('what would you change the year of this movie to?:')
      data(my_dict[Movie_C][1]=year)
    elif movie_change=2:
      director=input('what director name do you want to change?:')
      data(my_dict[Movie_C][2]=director)
    elif movie_change=3:
      genre=input('what genre would you like to change it to?:')
      data(my_dict[Movie_C][3]=genre)
    elif movie_change=4:
      rating=input('what rating would you change this movie to?:')
      data(my_dict[Movie_C][4]=rating)
  if movie_ID=='Forrest Gump':
    for elements in data(my_dict[Movie_D]):
      print(elements)
    movie_change=input('what numbered place of information would you like to change?(from number0-4) ')
    if movie_change==0:
      title=input('what would you change the title of "Forrest Gump" to?')
      data(my_dict[Movie_D][0]=title)
    elif movie_change==1:
      year=input('what would you change the year of this movie to?:')
      data(my_dict[Movie_D][1]=year)
    elif movie_change=2:
      director=input('what director name do you want to change?:')
      data(my_dict[Movie_D][2]=director)
    elif movie_change=3:
      genre=input('what genre would you like to change it to?:')
      data(my_dict[Movie_D][3]=genre)
    elif movie_change=4:
      rating=input('what rating would you change this movie to?:')
      data(my_dict[Movie_D][4]=rating)
  if movie_ID=='The Matrix':
    for elements in data(my_dict[Movie_E]):
      print(elements)
    movie_change=input('what numbered place of information would you like to change?(from number0-4) ')
    if movie_change==0:
      title=input('what would you change the title of "The Matrix" to?')
      data(my_dict[Movie_E][0]=title)
    elif movie_change==1:
      year=input('what would you change the year of this movie to?:')
      data(my_dict[Movie_E][1]=year)
    elif movie_change=2:
      director=input('what director name do you want to change?:')
      data(my_dict[Movie_E][2]=director)
    elif movie_change=3:
      genre=input('what genre would you like to change it to?:')
      data(my_dict[Movie_E][3]=genre)
    elif movie_change=4:
      rating=input('what rating would you change this movie to?:')
      data(my_dict[Movie_E][4]=rating) 
## the update function is a long function but it allows you to change any data element in the given dictionary we created.





def delete_movie():
  movie_target=input('what movie would you like to delete?:')
  if movie_target=='The Godfather':
    choice=input('are you sure you want to delete The Godfather?(y/n)')
    if choice=="y":
      data(my_dict.pop(Movie_A))
  elif movie_target=="The Shawshank Redemption":
    choice=input('are you sure you want to delete The Shawshank Redemption?(y/n)')
    if choice=='y':
      data(my_dict.pop(Movie_B))
  elif movie_target=="The Dark Knight":
    choice=input('are you sure you want to delete The Dark Knight?(y/n)')
    if choice=='y':
      data(my_dict.pop(Movie_C))
  elif movie_target=="Forrest Gump":
    choice=input('are you sure you want to delete The Dark Knight?(y/n)')
    if choice=='y':
      data(my_dict.pop(Movie_D))
  elif movie_target=="Forrest Gump":
    choice=input('are you sure you want to delete Forrest Gump?(y/n)')
    if choice=='y':
      data(my_dict.pop(Movie_E))
  elif movie_target!= data(my_dict):
    print(menu())
##this function will delete the selected movie out of the data base and if the movie doesn't exist then it will redirect you to the menu.


def exit():
  sys.exit(0)
## this is the exit the program function. so this can be called anywhere in the program

  
  
def main():
	starting_input=input('welcome to our data base,would you like to access it?(y/n)')
  if starting_input=='y':
    print(menu())
## main function. so just call this functiont to start the whole program.