'''
Created on Nov 13, 2016

@author: oscar
'''
from src.store.domain.entities import Movie
from src.store.domain.validators import MovieValidatorException

#TODO cascada, daca stergi film sau asa sa stergi si rental.

class MovieController(object):
    """
    The class is the controller for the movies in the app
    """
    def __init__(self, movieRepository,undoController):
        """
        The function is only to set up.
        :param movieRepository: a class, in which are it is a set of operations visible for all controllers
        """
        self.__movieRepository = movieRepository
        self.__undoController = undoController

    def addMovie(self, movieId,title,genre,description):
        """
        The function add a movie into a controller
        :param movieId: is the key to the dictionary
        :param title: is a field of the movie
        :param genre: is another field of the movie
        :param description: another field of the movie
        :return: The function will return the list with the new movie in it
        """
        movie = Movie(movieId,title,genre,description)
        self.__movieRepository.save(movie)
        self.__undoController.registerOperation(self.addMovie,self.deleteMovie,movieId)


    def deleteMovie(self,movieId):
        """
        The function will delete the element with the movieId
        :param movieId: is the filed with which we will search
        :return: the list without an element in it
        """
        op = self.__movieRepository.findById(movieId)
        self.__movieRepository.delete(movieId)
        self.__undoController.registerOperation(self.deleteMovie,self.addMovie,movieId,op.title,op.genre,op.description)



    def getAll(self):
        """
        The function will return a list with all the movies in it
        """
        return self.__movieRepository.getAll()

    def updateMovie(self,movieId,command,new):
        """
        The function will update a field from a movie
        :param movieId: is the key in which we will update a value
        :param command: is the variable that will tell which field will be modified
        :param new: is the variable that is the update value
        :return: the list with the an element modified
        """
        op = self.__movieRepository.findById(movieId)
        if op == None:
            raise MovieValidatorException("Movie id not found")
        else:
            if command == 1:
                old = op.title
                op.title = new
                self.__undoController.registerOperation(self.updateMovie,self.updateMovieUndo,movieId,1,old)
            elif command == 2:
                old = op.genre
                op.genre = new
                self.__undoController.registerOperation(self.updateMovie, self.updateMovieUndo, movieId, 2, old)
            elif command == 3:
                old = op.description
                op.description = new
                self.__undoController.registerOperation(self.updateMovie, self.updateMovieUndo, movieId, 3, old)


    def updateMovieUndo(self,movieId,command,old):
        """
        This function does the same as the one above, but the only difference is that it is design for undo
        """
        op = self.__movieRepository.findById(movieId)
        if command == 1:
            op.title = old
        elif command ==2:
            op.genre = old
        elif command == 3:
            op.description = old


    def searchByTitle(self,title):
        """
        The function will search and return a list with the element that have at the field movie the value from the
            variable title
        """
        return (list(filter(lambda movies: title in movies.title.lower(), self.__movieRepository.getAll())))

    def searchByDescription(self,description):
        """
        The function will search and return a list with the element that have at the field description the value from the
            variable description
        """
        return (list(filter(lambda movies: description in movies.description.lower(), self.__movieRepository.getAll())))

    def searchByGenre(self,genre):
        """
        The function will search and return a list with the element that have at the field genre the value from the
            variable genre
        """
        return (list(filter(lambda movies: genre in movies.genre.lower(), self.__movieRepository.getAll())))

    def searchById(self,id):
        """
        The function will search and return a list with the element that have at the field entityId the value from the
            variable id
        """
        return (list(filter(lambda movies: id in str(movies.entityId) ,self.__movieRepository.getAll())))

    def startUp(self):
        """
        The function will give 100 elements into the controller for start up
        :return: the list with 100 elements in it
        """
        self.addMovie(1,"Ratatouille","Animation","A rat who can cook makes an unusual alliance with a young kitchen worker at a famous restaurant.")
        self.addMovie(2,"The incredibles", "Animation", "A family of undercover superheroes, while trying to live the quiet suburban life, are forced into action to save the world.")
        self.addMovie(3,"Shrek", "Animation", "After his swamp is filled with magical creatures, an ogre agrees to rescue a princess for a villainous lord in order to get his land back.")
        self.addMovie(4,"Madagascar", "Animation", "Spoiled by their upbringing with no idea what wild life is really like, four animals from New York Central Zoo escape, unwittingly assisted by four absconding penguins, and find themselves in Madagascar, among a bunch of merry lemurs")
        self.addMovie(5,"Ice Age", "Animation", "Set during the Ice Age, a sabertooth tiger, a sloth, and a wooly mammoth find a lost human infant, and they try to return him to his tribe.")
        self.addMovie(6,"Kung Fu Panda", "Animation", "The Dragon Warrior has to clash against the savage Tai Lung as China's fate hangs in the balance: However, the Dragon Warrior mantle is supposedly mistaken to be bestowed upon an obese panda who is a tyro in martial arts.")
        self.addMovie(7,"Cars", "Animation", "A hot-shot race-car named Lightning McQueen gets waylaid in Radiator Springs, where he finds the true meaning of friendship and family.")
        self.addMovie(8,"Despicable Me", "Animation", "When a criminal mastermind uses a trio of orphan girls as pawns for a grand scheme, he finds their love is profoundly changing him for the better.")
        self.addMovie(9,"Monster University", "Animation", "A look at the relationship between Mike and Sulley during their days at Monsters University -- when they weren't necessarily the best of friends.")
        self.addMovie(10,"Toy Story", "Animation", "When Woody is stolen by a toy collector, Buzz and his friends vow to rescue him, but Woody finds the idea of immortality in a museum tempting.")
        self.addMovie(11, "Ride Along", "Comedy", "Security guard Ben must prove himself to his girlfriend's brother, top police officer James. He rides along James on a 24-hour patrol of Atlanta.")
        self.addMovie(12, "Ride Along 2", "Comedy", "As his wedding day approaches, Ben heads to Miami with his soon-to-be brother-in-law James to bring down a drug dealer who's supplying the dealers of Atlanta with product.")
        self.addMovie(13, "Get Hard", "Comedy", "When millionaire James King is jailed for fraud and bound for San Quentin, he turns to Darnell Lewis to prep him to go behind bars.")
        self.addMovie(14, "Let's Be Cops", "Comedy", "Two struggling pals dress as police officers for a costume party and become neighborhood sensations. But when these newly-minted heroes get tangled in a real life web of mobsters and dirty detectives, they must put their fake badges on the line.")
        self.addMovie(15, "22 Jump Street", "Comedy", "After making their way through high school (twice), big changes are in store for officers Schmidt and Jenko when they go deep undercover at a local college.")
        self.addMovie(16, "Neighbors I", "Comedy", "After they are forced to live next to a fraternity house, a couple with a newborn baby do whatever they can to take them down.")
        self.addMovie(17, "Ted", "Comedy", "John Bennett, a man whose childhood wish of bringing his teddy bear to life came true, now must decide between keeping the relationship with the bear or his girlfriend, Lori.")
        self.addMovie(18, "Ted 2", "Comedy", "Newlywed couple Ted and Tami-Lynn want to have a baby, but in order to qualify to be a parent, Ted will have to prove he's a person in a court of law.")
        self.addMovie(19, "Horrible Bosses 2 ", "Comedy", "Dale, Kurt and Nick decide to start their own business but things don't go as planned because of a slick investor, prompting the trio to pull off a harebrained and misguided kidnapping scheme.")
        self.addMovie(20, "21 Jump Street", "Comedy", "A pair of underachieving cops are sent back to a local high school to blend in and bring down a synthetic drug ring.")
        self.addMovie(21, "The Godfather", "Action", "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son. (175 mins.)")
        self.addMovie(22, "The Shawshank Redemption", "Action", "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency. (142 mins.)")
        self.addMovie(23, "Schindler's List ", "Action", "In German-occupied Poland during World War II, Oskar Schindler gradually becomes concerned for his Jewish workforce after witnessing their persecution by the Nazi Germans. (195 mins.)")
        self.addMovie(24, "Raging Bull", "Action", "An emotionally self-destructive boxer's journey through life, as the violence and temper that leads him to the top in the ring destroys his life outside it. (129 mins.)")
        self.addMovie(25, "Casablanca", "Action", "In Casablanca, Morocco in December 1941, a cynical American expatriate meets a former lover, with unforeseen complications. (102 mins.)")
        self.addMovie(26, "Citizen Kane", "Action", "Following the death of a publishing tycoon, news reporters scramble to discover the meaning of his final utterance. (119 mins.)")
        self.addMovie(27, "Gone with the wind", "Action", "A manipulative Southern belle carries on a turbulent affair with a blockade runner during the American Civil War. (238 mins.)")
        self.addMovie(28, "The Wizard of oz", "Action", "Dorothy is a girl with magin shoes")
        self.addMovie(29, "Lawrence of Arabia", "Action", "The story of T.E. Lawrence, the English officer who successfully united and lead the diverse, often warring, Arab tribes during World War I in order to fight the Turks. (216 mins.)")
        self.addMovie(30, "Vertigo", "Action", "A San Francisco detective suffering from acrophobia investigates the strange activities of an old friend's wife, all the while becoming dangerously obsessed with her. (128 mins.)")
        self.addMovie(31, "Psycho", "Romance", "A Phoenix secretary embezzles $40,000 from her employer's client, goes on the run, and checks into a remote motel run by a young man under the domination of his mother. (109 mins.)")
        self.addMovie(32, "The Godfather part 2", "Romance", "The early life and career of Vito Corleone in 1920s New York is portrayed while his son, Michael, expands and tightens his grip on his crime syndicate stretching from Lake Tahoe, Nevada to pre-revolution 1958 Cuba. (202 mins.)")
        self.addMovie(33, "The Notebook", "Romance", "A poor yet passionate young man falls in love with a rich young woman, giving her a sense of freedom, but they are soon separated because of their social differences.")
        self.addMovie(34, "The Fault in our starts", "Romance", "Two teenage cancer patients begin a life-affirming journey to visit a reclusive author in Amsterdam.")
        self.addMovie(35, "The Vow", "Romance", "A car accident puts Paige in a coma, and when she wakes up with severe memory loss, her husband Leo works to win her heart again")
        self.addMovie(36, "A Walk to Remember", "Romance", "The story of two North Carolina teens, Landon Carter and Jamie Sullivan, who are thrown together after Landon gets into trouble and is made to do community service.")
        self.addMovie(37, "P.S. I Love You", "Romance", "A young widow discovers that her late husband has left her 10 messages intended to help ease her pain and start a new life.")
        self.addMovie(38, "Dear John", "Romance", "A romantic drama about a soldier who falls for a conservative college student while he's home on leave.")
        self.addMovie(39, "Friends with Benefits", "Romance", "A young man and woman decide to take their friendship to the next level without becoming a couple, but soon discover that adding sex only leads to complications.")
        self.addMovie(40, "The Lucky One", "Romance", "A Marine travels to Louisiana after serving three tours in Iraq and searches for the unknown woman he believes was his good luck charm during the war.")
        self.addMovie(41, "Titanic", "Drama", "A seventeen-year-old aristocrat falls in love with a kind but poor artist aboard the luxurious, ill-fated R.M.S. Titanic.")
        self.addMovie(42, "The Proposal", "Drama", "A pushy boss forces her young assistant to marry her in order to keep her visa status in the U.S. and avoid deportation to Canada.")
        self.addMovie(43, "The Longest Ride", "Drama", "The lives of a young couple intertwine with a much older man, as he reflects back on a past love.")
        self.addMovie(44, "The Best of Me", "Drama", "A pair of former high school sweethearts reunite after many years when they return to visit their small hometown.")
        self.addMovie(45, "Crazy, Stupid, Love", "Drama", "A middle-aged husband's life changes dramatically when his wife asks him for a divorce. He seeks to rediscover his manhood with the help of a newfound friend, Jacob, learning to pick up girls at bars.")
        self.addMovie(46, "Arrival", "Drama", "A linguist is recruited by the military to assist in translating alien communications.")
        self.addMovie(47, "Allied", "Drama", "In 1942, an intelligence officer in North Africa encounters a female French Resistance fighter on a deadly mission behind enemy lines. When they reunite in London, their relationship is tested by the pressures of war.")
        self.addMovie(48, "Silence", "Drama", "In the seventeenth century, two Jesuit priests face violence and persecution when they travel to Japan to locate their mentor and propagate Christianity.")
        self.addMovie(49, "Hacksaw Ridge", "Drama", "WWII American Army Medic Desmond T. Doss, who served during the Battle of Okinawa, refuses to kill people, and becomes the first man in American history to win the Medal of Honor without firing a shot.")
        self.addMovie(50, "Bad Santa 2", "Drama", "Fueled by cheap whiskey, greed and hatred, Willie teams up once again with his angry little sidekick, Marcus, to knock off a Chicago charity on Christmas Eve.")
        self.addMovie(51, "The Purge: Election Year", "Horror", "Expanding upon the explosive universe introduced in the sleeper hits that have earned $200 million at the worldwide box office, Universal Pictures’ The Purge 3 reveals the next terrifying chapter of 12 hours of anarchy that is sanctioned annually by the New Founders of America.")
        self.addMovie(52, "The Conjuring 2", "Horror", "Director James Wan brings this supernatural thriller to the screen with another real case from the files of renowned demonologists Ed and Lorraine Warren.. Reprising their roles, Oscar nominee Vera Farmiga and Patrick Wilson star as Lorraine and Ed Warren, who, in one of their most terrifying paranormal investigations, travel to north London to help a single mother raising four children alone in a house plagued by malicious spirits.")
        self.addMovie(53, "The Neon Demon", "Horror", "When aspiring model Jesse moves to Los Angeles, her youth and vitality are devoured by a group of beauty-obsessed women who will take any means necessary to get what she has.")
        self.addMovie(54, "10 Cloverfield Lane", "Horror", "Waking up from a car accident, a young woman finds herself in the basement of a man who says he's saved her life from a chemical attack that has left the outside uninhabitable.")
        self.addMovie(55, "Mr. Right", "Horror", "After a going through a painful break up, a woman meets a man who appears to be perfect for her. However, as their relationship develops, she learns that he is a former hit-man. Their new, but genuine relationship is tested even further as they try to save each other after his dark past comes back to haunt him.")
        self.addMovie(56, "Don't Breathe", "Horror", "A group of teens break into a blind man's home thinking they'll get away with the perfect crime. They're wrong.")
        self.addMovie(57, "Pride and Prejudice and Zombies", "Horror", "Jane Austin's classic tale of the tangled relationships between lovers from different social classes in 19th century England is faced with a new challenge -- an army of undead zombies.")
        self.addMovie(58, "Cabin Fever", "Horror", "Executive producer Eli Roth presents this reboot of his instant classic gorefest, which features all new characters and all new kills. This story is familiar: fresh out of college, a group of five friends retreat to a remote cabin in the woods for one last week of partying- only to become snacks for a gruesome, flesh-eating virus. What’s surprising are the ingenious new deaths, which offer a fresh spin on a horror-comedy milestone. With Gage Golightly (Teen Wolf) and Dustin Ingram (Paranormal Activity 3).")
        self.addMovie(59, "The Forest", "Horror", "The Forest, which is set in the Aokigahara forest at the base of Mt. Fuji, tells the story of a young American woman who goes in search of her twin sister, who has mysteriously disappeared.  Despite everyone’s warnings to “stay on the path,” Sara enters the forest determined to discover the truth about her sister’s fate, only to be confronted by the angry and tormented souls of the dead who prey on anyone who wanders into the forest.")
        self.addMovie(60, "ClownTown", "Horror", "A group of friends get stranded in a seemingly abandoned town and find themselves stalked by a gang of violent psychopaths dressed as clowns.")
        self.addMovie(61, "Carnage Park", "Thriller", "Part crime caper gone awry, part survival horror film, this 1970s set thriller depicts a harrowing fight for survival after a pair of wannabe crooks botch a bank heist and flee into the desert, where they inexplicably stumble upon Carnage Park, a remote stretch of wilderness occupied by a psychotic ex-military sniper.")
        self.addMovie(62, "Rogue One: A Star Wars Story", "Thriller", "From Lucasfilm comes the first of the Star Wars standalone films, “Rogue One: A Star Wars Story,” an all-new epic adventure. In a time of conflict, a group of unlikely heroes band together on a mission to steal the plans to the Death Star, the Empire’s ultimate weapon of destruction. This key event in the Star Wars timeline brings together ordinary people who choose to do extraordinary things, and in doing so, become part of something greater than themselves.")
        self.addMovie(63, "Assassin's Creed", "Thriller", "Through a revolutionary technology that unlocks his genetic memories, Callum Lynch (Michael Fassbender) experiences the adventures of his ancestor, Aguilar, in 15th Century Spain. Callum discovers he is descended from a mysterious secret society, the Assassins, and amasses incredible knowledge and skills to take on the oppressive and powerful Templar organization in the present day.")
        self.addMovie(64, "Passengers", "Thriller", "On a routine journey through space to a new home, two passengers, sleeping in suspended animation, are awakened 90 years too early when their ship malfunctions. As Jim (Chris Pratt) and Aurora (Jennifer Lawrence) face living the rest of their lives on board, with every luxury they could ever ask for, they begin to fall for each other, unable to deny their intense attraction... until they discover the ship is in grave danger. With the lives of 5000 sleeping passengers at stake, only Jim and Aurora can save them all.")
        self.addMovie(65, "A Monster Calls", "Thriller", "A Monster Calls is a visually spectacular drama about a young boy who attempts to deal with his mother’s illness and the bullying of his classmates by escaping into a fantastical world of monsters and fairy tales that deal with courage, loss and faith.")
        self.addMovie(66, "MallBrats", "Thriller", "Kevin Smith is planning a sequel to his 1995 comedy Mallrats. No further details have been announced.")
        self.addMovie(67, "The Raid", "Thriller", "A remake of the 2012 Gareth Evans action hit. A mobster and his thugs trap a SWAT team inside a building.")
        self.addMovie(68, "The New Mutants", "Thriller", "The New Mutants is a standalone spinoff that expands the X-Men movie universe. The series, already part of the X-Men Comics universe, introduces a new crop of mutant characters born with special powers. Boone will co-write with Knate Gwaltney. Simon Kinberg will produce with Lauren Shuler Donner.")
        self.addMovie(69, "Underworld: Blood Wars", "Thriller", "The epic struggle between the Lycan werewolf clan and the Vampire clan that has vowed to eradicate them continues in this stylish and moody fifth installment.")
        self.addMovie(70, "Fifty Shades Darker", "Thriller", "Director Sam Taylor-Johnson revealed during a fan screening in New York City, alongside cast members Jamie Dornan, Dakota Johnson and E.L. James that both Fifty Shades Darker and Fifty Shades Freed will be adapted for the big screen.")
        self.addMovie(71, "Star Wars 1", "Sf", "Come join the dark side")
        self.addMovie(72, "Star Wars 2", "Sf", "Come join the dark side")
        self.addMovie(73, "Star Wars 3", "Sf", "Come join the dark side")
        self.addMovie(74, "Star Wars 4", "Sf", "Come join the dark side")
        self.addMovie(75, "Star Wars 5", "Sf", "Come join the dark side")
        self.addMovie(76, "Star Wars 6", "Sf", "Come join the dark side")
        self.addMovie(77, "Star Wars 7", "Sf", "Come join the dark side")
        self.addMovie(78, "Star Wars 8", "Sf", "Not Released")
        self.addMovie(79, "Star Wars 9", "Sf", "Not Released")
        self.addMovie(80, "Divergent", "Sf", "It's about a girls with multimple abilities")
        self.addMovie(81, "The LEGO Batman Movie", "Musical", "Will Arnett's Batman will be the focus of the next LEGO movie, a spinoff of the 2014 hit animated feature.")
        self.addMovie(82, "John Wick: Chapter 2", "Musical", "Keanu Reeves returns in the sequel to the 2014 hit as legendary hitman John Wick who is forced to back out of retirement by a former associate plotting to seize control of a shadowy international assassins’ guild. Bound by a blood oath to help him, John travels to Rome where he squares off against some of the world’s deadliest killers.")
        self.addMovie(83, "The Legend of Conan", "Musical", "This sequel will pick-up where the original 1982 Conan the Barbarian left off.")
        self.addMovie(84, "Logan", "Musical", "Story details are under wraps. This will be the third solo outing for the popular mutant. It will be the 8th time Hugh Jackman as portrayed the character in a feature film.")
        self.addMovie(85, "Fast and Furious 8", "Musical", "The latest installment of the Fast & Furious franchise will take the action to New York. No further plot details have been revealed at this time.")
        self.addMovie(86, "Guardians of the Galaxy Vol. 2", "Musical", "In Guardians of the Galaxy 2, Peter Quill a.k.a. Star-Lord and his team of misfits continue their adventures as guardians of the galaxy against all-new threatens as their team grows and Peter learns about who his father really is.")
        self.addMovie(87, "Two unlikely prospective lifeguards vie for jobs alongside the buff bodies who patrol a beach in California.", "Musical", "Two unlikely prospective lifeguards vie for jobs alongside the buff bodies who patrol a beach in California.")
        self.addMovie(88, "Pirates of the Caribbean: Dead Men Tell No Tales", "Musical", "Thrust into an all-new adventure, a down-on-his-luck Captain Jack Sparrow finds the winds of ill-fortune blowing even more strongly when deadly ghost pirates led by his old nemesis, the terrifying Captain Salazar (Bardem), escape from the Devil's Triangle, determined to kill every pirate at sea...including him.")
        self.addMovie(89, "The Divergent Series: Ascendant", "Musical", "Beatrice Prior and Tobias Eaton fight to end the Bureau of Genetic Welfare's authoritarian reign over the United States.")
        self.addMovie(90, "Kingsman: The Golden Circle", "Musical", "A sequel to the hit action adventure Kingsman: The Secret Service.")
        self.addMovie(91, "Transformers: The Last Knight", "Others", "The Last Knight has Optimus Prime searching through the cosmos for the Quintessons, the beings believed to be responsible for the creation of the Transformers race. Meanwhile back at home, Wahlberg's Cade Yeager will be facing a new alien threat that brings Lennox (and possibly Epps) back into duty. ")
        self.addMovie(92, "Independence Day 3", "Others", "The new Independence Day Movie 2014")
        self.addMovie(93, "Spider-Man: Homecoming", "Others", "Marvel's Spiderman movie is set to reboot the franchise and bring the iconic Marvel character into The Avengers team. We will see the first appearance of Spider-man in Captain America: Civil War and he'll be wearing two suits.")
        self.addMovie(94, "The Fantastic Four 2", "Others", "The second installment of the rebooted franchise.")
        self.addMovie(95, "War for the Planet of the Apes", "Others", "No plot details have been revealed for this third installment of the rebooted franchise, which includes Rise of the Planet of the Apes and Dawn of the Planet of the Apes.")
        self.addMovie(96, "Valerian and the City of a Thousand Planets", "Others", "Valerian (Dane DeHaan) and Laureline (Cara Delevingne) are special operatives for the government of the human territories charged with maintaining order throughout the universe. ")
        self.addMovie(97, "Dunkirk", "Others", "The story is set during the legendary evacuation of the northern French city during WWII.")
        self.addMovie(98, "The Dark Tower", "Others", "Stephen King, Imagine Entertainment and Weed Road are in talks to create a movie trilogy and TV series based on King's The Dark Tower series.")
        self.addMovie(99, "IT", "Others", "IT centers on seven children in a small Maine town who confront the source of a series of murders in 1958 and again in 1985, when the cycle begins again. The Stephen King novel was previously adapted into a 1990 ABC miniseries.")
        self.addMovie(100, "AS","a","S")