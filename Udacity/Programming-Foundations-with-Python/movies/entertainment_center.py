import media, fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://viverpararecordar.wordpress.com/files/2009/10/toystory.jpg",
                        "https://www.youtube.com/watch?v=v-PjgYDrg70")

#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A Marine on an Alien Planet",
                     "https://upload.wikimedia.org/wikipedia/pt/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

school_of_rock = media.Movie("School Of Rock",
                             "Using Rock to Learn Music",
                             "http://br.web.img3.acsta.net/medias/nmedia/18/91/90/98/20169244.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille",
                          "A Rat is a Chef in Paris",
                          "https://i.ytimg.com/vi/eh62Ri60lXI/movieposter.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

the_name_of_the_rose = media.Movie("The Name Of The Rose",
                               "They believe in God, but deal with the Devil",
                               "http://br.web.img2.acsta.net/medias/nmedia/18/90/19/35/20085225.jpg",
                               "https://www.youtube.com/watch?v=7-yYJgpQ-CE")
                            
the_count_of_monte_cristo = media.Movie("The COunt of Monte Cristo",
                                        "Prepare for Adventure, enjoy the vengeance",
                                        "http://fr.web.img2.acsta.net/medias/nmedia/00/02/43/26/affcristo.jpg",
                                        "https://www.youtube.com/watch?v=X9F6Ssb7GHo")

movies = [toy_story, avatar, school_of_rock,ratatouille, the_name_of_the_rose, the_count_of_monte_cristo]

fresh_tomatoes.open_movies_page(movies)