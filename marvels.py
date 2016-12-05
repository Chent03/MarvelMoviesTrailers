import media
import fresh_tomatoes

ironman = media.Movie("Iron Man",
                      "After being held captive in an Afghan cave, billionaire engineer Tony Stark creates a unique weaponized suit of armor to fight evil.",
                      "https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG",
                      "https://www.youtube.com/watch?v=8hYlB38asDY")

captain_america = media.Movie("Captain America",
                              "Steve Rogers, a rejected military soldier transforms into Captain America after taking a dose of a 'Super-Soldier serum'. But being Captain America comes at a price as he attempts to take down a war monger and a terrorist organization.",
                              "https://upload.wikimedia.org/wikipedia/en/3/37/Captain_America_The_First_Avenger_poster.jpg",
                              "https://www.youtube.com/watch?v=JerVrbLldXw")

guardian = media.Movie("Guardians of the Galaxy",
                       "A group of intergalactic criminals are forced to work together to stop a fanatical warrior from taking control of the universe.",
                       "https://upload.wikimedia.org/wikipedia/en/8/8f/GOTG-poster.jpg",
                       "https://www.youtube.com/watch?v=2LIQ2-PZBC8")

spiderman = media.Movie("Spider-Man",
                        "When bitten by a genetically modified spider, a nerdy, shy, and awkward high school student gains spider-like abilities that he eventually must use to fight evil as a superhero after tragedy befalls his family.",
                        "https://upload.wikimedia.org/wikipedia/en/f/f3/Spider-Man2002Poster.jpg",
                        "https://www.youtube.com/watch?v=O7zvehDxttM")

antman = media.Movie("Ant-Man",
                     "Armed with a super-suit with the astonishing ability to shrink in scale but increase in strength, cat burglar Scott Lang must embrace his inner hero and help his mentor, Dr. Hank Pym, plan and pull off a heist that will save the world.",
                     "https://upload.wikimedia.org/wikipedia/en/7/75/Ant-Man_poster.jpg",
                     "https://www.youtube.com/watch?v=pWdKf3MneyI")

hulk = media.Movie("The Incredible Hulk",
                   "Bruce Banner, a scientist on the run from the U.S. Government, must find a cure for the monster he emerges whenever he loses his temper. However, Banner then must fight a soldier who unleashes himself as a threat stronger than he.",
                   "https://upload.wikimedia.org/wikipedia/en/8/88/The_Incredible_Hulk_poster.jpg",
                   "https://www.youtube.com/watch?v=xbqNb2PFKKA")

movies = [ironman, captain_america, guardian, spiderman, antman, hulk]

fresh_tomatoes.open_movies_page(movies)
