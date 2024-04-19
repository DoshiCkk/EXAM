import sqlite3


connection = sqlite3.connect('database.db')

cursor = connection.cursor()

def create_table():
    cursor.execute('CREATE TABLE IF NOT EXISTS cinema (id INTEGER PRIMARY KEY, name TEXT, address TEXT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS movie (id INTEGER PRIMARY KEY, name TEXT, genre TEXT, year INTEGER,  description TEXT, rating REAL)')
    cursor.execute('CREATE TABLE IF NOT EXISTS afisha (id INTEGER PRIMARY KEY, movie_id INTEGER, cinema_id INTEGER, price INTEGER, date DATE, time TIME, capacity INTEGER)')
    cursor.execute('CREATE TABLE IF NOT EXISTS place (id INTEGER PRIMARY KEY, afisha_id INTEGER, room INTEGER, row INTEGER, seat INTEGER)')
    cursor.execute('CREATE TABLE IF NOT EXISTS ticket (id INTEGER PRIMARY KEY, name TEXT, phone TEXT, place_id INTEGER)')
    
create_table()

final_result = []

class Cinema:
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address

    def cinema():
        try:
            print(f"Здравствуйте! какой кинотеатр вы хотите выбрать?\n1.Арман\n2.Chaplin cinemas\n3.Kinopark\n4.Евразия Cinema 7\n5.Арсенал")
            cinema_choise = int(input("Введите цифру от 1 до 5: "))
           
            if cinema_choise == 1:
                cursor.execute("SELECT name, address FROM cinema WHERE id == '1'")
                result = cursor.fetchone()
                for i in result:
                    print(i)
                final_result.append(result)


            elif cinema_choise == 2:
                cursor.execute("SELECT name, address FROM cinema WHERE id == '2'")
                result = cursor.fetchone()
                for i in result:
                    print(i)            
                final_result.append(result)

            

            elif cinema_choise == 3:
                cursor.execute("SELECT name, address FROM cinema WHERE id == '3'")
                result = cursor.fetchone()
                for i in result:
                    print(i)            
                final_result.append(result)
            

            elif cinema_choise == 4:
                cursor.execute("SELECT name, address FROM cinema WHERE id == '4'")
                result = cursor.fetchone()
                for i in result:
                    print(i)            
                final_result.append(result)
           

            elif cinema_choise == 5:
                cursor.execute("SELECT name, address FROM cinema WHERE id == '5'")
                result = cursor.fetchone()
                for i in result:
                    print(i)
                final_result.append(result)
            

            
            else:
                print("There's no that name")
        except ValueError:
            print("Пиши цифрами дуралей ")
        

class Movie:
    def __init__(self, id, name, genre,year,description,rating):
        self.id = id
        self.name = name
        self.genre = genre
        self.year = year
        self.description = description
        self.rating = rating

    def genre():
        try:
            print(f"Какой жанр предпочитаете?\n1.DRAMA\n2.CRIME\n3.ACTION\n4.BIOGRAPHY\n5.ADVENTURE\n6.ANIMATION\n7.COMEDY\n8.HORROR\n9.MYSTERY")
            genre = int(input("Введите цифру от 1 до 9: "))
           
            if genre == 1:
                drama_movie = ("SELECT name FROM movie WHERE genre == 'Drama'")
                drama_year = ("SELECT year FROM movie WHERE genre == 'Drama'")
                drama_rating = ("SELECT rating FROM movie WHERE genre == 'Drama'")
                for index, drama_movie,  in enumerate(cursor.execute(drama_movie)):
                    print(index + 1, drama_movie)
                drama_result = cursor.execute("SELECT name FROM movie WHERE genre == 'Drama'")
                connection.commit()
                final_result.append(drama_result)



            elif genre == 2:
                crime_movie = ("SELECT name FROM movie WHERE genre == 'Crime'")
                crime_year = ("SELECT year FROM movie WHERE genre == 'Crime'")
                crime_rating = ("SELECT rating FROM movie WHERE genre == 'Crime'")
                for index, crime_movie in enumerate(cursor.execute(crime_movie)):
                    print(index + 1, crime_movie)
                crime_result = cursor.execute("SELECT name FROM movie WHERE genre == 'Crime'")
                connection.commit()
                final_result.append(crime_result)
            

            elif genre == 3:
                action_movie = ("SELECT name FROM movie WHERE genre == 'Action'")
                action_year = ("SELECT year FROM movie WHERE genre == 'Action'")
                action_rating = ("SELECT rating FROM movie WHERE genre == 'Action'")
                for index, action_movie in enumerate(cursor.execute(action_movie)):
                    print(index + 1, action_movie)
                action_result = cursor.execute("SELECT name FROM movie WHERE genre == 'Action'")
                connection.commit()
                final_result.append(action_result)

            elif genre == 4:
                bio_movie = ("SELECT name FROM movie WHERE genre == 'Biography'")
                bio_year = ("SELECT year FROM movie WHERE genre == 'Biography'")
                bio_rating = ("SELECT rating FROM movie WHERE genre == 'Biography'")
                for index, bio_movie in enumerate(cursor.execute(bio_movie)):
                    print(index + 1, bio_movie)
                bio_result = cursor.execute("SELECT name FROM movie WHERE genre == 'Biography'")
                connection.commit()
                final_result.append(bio_result)
           

            elif genre == 5:
                adventure_movie = ("SELECT name FROM movie WHERE genre == 'Adventure'")
                adventure_year = ("SELECT year FROM movie WHERE genre == 'Adventure'")
                adventure_rating = ("SELECT rating FROM movie WHERE genre == 'Adventure'")
                for index, adventure_movie in enumerate(cursor.execute(adventure_movie)):
                    print(index + 1, adventure_movie)
                adventure_result = cursor.execute("SELECT name FROM movie WHERE genre == 'Drama'")
                connection.commit()
                final_result.append(adventure_result)
            
            elif genre == 6:
                animation_movie = ("SELECT name FROM movie WHERE genre == 'Animation'")
                animation_year = ("SELECT year FROM movie WHERE genre == 'Animation'")
                animation_rating = ("SELECT rating FROM movie WHERE genre == 'Animation'")
                for index, animation_movie in enumerate(cursor.execute(animation_movie)):
                    print(index + 1, animation_movie)
                animation_result = cursor.execute("SELECT name FROM movie WHERE genre == 'Animation'")
                connection.commit()
                final_result.append(animation_result)
            
            elif genre == 7:
                comedy_movie = ("SELECT name FROM movie WHERE genre == 'Comedy'")
                comedy_year = ("SELECT year FROM movie WHERE genre == 'Comedy'")
                comedy_rating = ("SELECT rating FROM movie WHERE genre == 'Comedy'")
                for index, comedy_movie in enumerate(cursor.execute(comedy_movie)):
                    print(index + 1, comedy_movie)
                comedy_result = cursor.execute("SELECT name FROM movie WHERE genre == 'Comedy'")
                connection.commit()
                final_result.append(comedy_result)

            elif genre == 8:
                horror_movie = ("SELECT name FROM movie WHERE genre == 'Horror'")
                horror_year = ("SELECT year FROM movie WHERE genre == 'Horror'")
                horror_rating = ("SELECT rating FROM movie WHERE genre == 'Horror'")
                for index, horror_movie in enumerate(cursor.execute(horror_movie)):
                    print(index + 1, horror_movie)
                horror_result = cursor.execute("SELECT name FROM movie WHERE genre == 'Horror'")
                connection.commit()
                final_result.append(horror_result)
            

            elif genre == 9:
                mystery_name = ("SELECT name FROM movie WHERE genre == 'Mystery'")
                mystery_year = ("SELECT year FROM movie WHERE genre == 'Mystery'")
                mystery_rating = ("SELECT rating FROM movie WHERE genre == 'Mystery'")
                for index, mystery_movie in enumerate(cursor.execute(mystery_movie)):
                    print(index + 1, mystery_movie)
                mystery_result = cursor.execute("SELECT name FROM movie WHERE genre == 'Mystery'")
                connection.commit()
                final_result.append(mystery_result)
            

            
            else:
                print("There's no that name")
        except ValueError:
            print("Пиши цифрами дуралей ")

    
    def movie():
        movie = input("Напишите какой фильм вы хотите выбрать:")
        final_result.append(movie)

class Afisha:
    def __init__(self, id, movie_id, cinema_id,price,date,time,capacity):
        self.id = id
        self.movie_id = movie_id
        self.cinema_id = cinema_id
        self.price = price
        self.date = date
        self.time = time
        self.capacity = capacity

    def afisha():
        pass

class Place:
    def __init__(self, id, afisha_id, room,row,seat):
        self.id = id
        self.afisha_id = afisha_id
        self.room = room
        self.row = row
        self.seat = seat

class Ticket:
    def __init__(self, id, name, phone,place_id):
        self.id = id
        self.name = name
        self.phone = phone
        self.place_id = place_id

class Order:
    def __init__(self):
        pass

    def start():
        pass


cinema = Cinema
cinema.cinema()
movie = Movie
movie.genre()
movie.movie()
print("Ваш выбор состоит из: ", final_result)