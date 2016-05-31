import media
import fresh_tomatoes

# Create instances of my favorite movies
the_dark_knight = media.Movie("The Dark Knight", "The follow-up to Batman Begins, The Dark Knight reunites director Christopher Nolan and star Christian Bale, who reprises the role of Batman/Bruce Wayne in his continuing war on crime. With the help of Lt. Jim Gordon and District Attorney Harvey Dent, Batman sets out to destroy organized crime in Gotham for good.",
                              "https://upload.wikimedia.org/wikipedia/en/thumb/8/8a/Dark_Knight.jpg/220px-Dark_Knight.jpg", "https://www.youtube.com/watch?v=EXeTwQWrcwY")

dawn_planet_apes = media.Movie("Dawn of the Planet of the Apes", "Dawn of the Planet of the Apes is the 2014 sequel to the 2011 science fiction film Rise of the Planet of the Apes. Andy Serkis, returns as Caesar, the chimpanzee revolutionary while stuntman Terry Notary returns to reprise his role as Caesar's hairless chimpanzee best friend, Rocket.",
                               "https://upload.wikimedia.org/wikipedia/en/thumb/7/77/Dawn_of_the_Planet_of_the_Apes.jpg/220px-Dawn_of_the_Planet_of_the_Apes.jpg", "https://www.youtube.com/watch?v=3sHMCRaS3ao")

interstellar = media.Movie("Interstellar", "Interstellar is a 2014 science fiction film directed by Christopher Nolan. Starring Matthew McConaughey, Anne Hathaway, Jessica Chastain, Mackenzie Foy and Michael Caine, the film features a team of astronauts who travel through a wormhole in search of a new habitable planet for the survival of humanity.",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/b/bc/Interstellar_film_poster.jpg/220px-Interstellar_film_poster.jpg", "https://www.youtube.com/watch?v=zSWdZVtXT7E")

lucy = media.Movie("Lucy", "Lucy is a 24-year-old American woman living and studying in Taipei, Taiwan. She is tricked into working as a drug mule by her new boyfriend, whose employer, Mr. Jang, is a Korean mob boss and drug lord. Lucy delivers a briefcase to Mr. Jang containing a highly valuable synthetic drug called CPH4.",
                   "https://upload.wikimedia.org/wikipedia/en/thumb/1/14/Lucy_%282014_film%29_poster.jpg/220px-Lucy_%282014_film%29_poster.jpg", "https://www.youtube.com/watch?v=MVt32qoyhi0")

star_wars_force_awkens = media.Movie("Star Wars: The Force Awakens", "30 years after the defeat of Darth Vader and the Empire, Rey, a scavenger from the planet Jakku, finds a BB-8 droid that knows the whereabouts of the long lost Luke Skywalker. Rey, as well as a rogue stormtrooper and two smugglers, are thrown into the middle of a battle between the Resistance and the daunting legions of the First Order.",
                                     "https://upload.wikimedia.org/wikipedia/en/thumb/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg/220px-Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg", "https://www.youtube.com/watch?v=sGbxmsDFVnE")

batman_v_superman = media.Movie("Batman v Superman: Dawn of Justice", "The General public is controversial over having superman on their planet and letting the dark knight pursue the streets of Gotham. And while this is happening, a power-phobic batman tries to attack superman, meanwhile, superman tries to settle on a decision, and Lex Luther, a millionaire, tries to use his own advantages to fight the man of steel.",
                                "https://upload.wikimedia.org/wikipedia/en/thumb/2/20/Batman_v_Superman_poster.jpg/220px-Batman_v_Superman_poster.jpg", "https://www.youtube.com/watch?v=fis-9Zqu2Ro")

# Combine movies into a list to be rendered into HTML output
movies = [the_dark_knight, dawn_planet_apes, interstellar,
          lucy, star_wars_force_awkens, batman_v_superman]

fresh_tomatoes.open_movies_page(movies)
