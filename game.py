import random

class Game: 
    def __init__(game):
        game.num_of_players = 0
        game.players = []
        game.scores = {}
        game.colours = [
    (1.0, 0.8, 0.8, 1), (0.8, 1.0, 0.8, 1), (0.8, 0.8, 1.0, 1),
    (1.0, 1.0, 0.8, 1), (1.0, 0.8, 1.0, 1), (0.8, 1.0, 1.0, 1),
    (1.0, 0.9, 0.8, 1), (0.9, 0.8, 1.0, 1), (0.8, 1.0, 0.9, 1),
    (1.0, 0.85, 0.85, 1)
]

        game.questions = [
    # 1. Animals - Strengths/Weaknesses
    [
        "What is the strongest animal you think you could take in a fight?",
        "Which animal is the sneakiest hunter?",
        "Which animal could survive longest in the wild alone?",
        "Which animal do you think is the fastest?",
        "Which animal would make the best guardian?",
        "Which animal would be the worst to encounter in the forest?",
        "Which animal has the most intimidating roar?"
    ],

    # 2. Superpowers - Morally Ambiguous
    [
        "Which superpower would you use to get rich fastest?",
        "Which superpower could help you get revenge without getting caught?",
        "Which superpower would you use to prank your friends?",
        "Which superpower would you use to avoid work?",
        "Which superpower would be the most fun at a party?",
        "Which superpower could cause the most chaos harmlessly?",
        "Which superpower would be useless in daily life but fun in a game?"
    ],

    # 4. Romantic / Flirty - Dating Behaviors
    [
        "Who would send a flirty text first?",
        "Who would ghost someone without explanation?",
        "Who would flirt with multiple people at the same time?",
        "Who would be most likely to get caught cheating?",
        "Who would fall in love too fast?",
        "Who would lie about their relationship status?",
        "Who would overthink a simple message too much?"
    ],

    # 5. Food / Weird Habits
    [
        "Which snack is the grossest to eat together with your hands?",
        "Which food would you secretly eat if no one else liked it?",
        "Which flavor is overrated but everyone pretends to like?",
        "Which food would you eat secretly at night?",
        "Which dessert would you finish first in a group?",
        "Which food would you never share with anyone?",
        "Which combination is weird but secretly delicious?"
    ],

    # 6. Childhood / Embarrassing Moments
    [
        "Which embarrassing habit did you have as a kid?",
        "Which toy did you take too seriously?",
        "Which imaginary friend was your favorite?",
        "Which childhood fear still makes you laugh?",
        "Which story from your childhood would you never admit?",
        "Which hobby did you secretly obsess over?",
        "Which nickname did you hate but everyone called you?"
    ],

    # 7. Travel / Adventure Choices
    [
        "Which city would you get lost in fastest?",
        "Which country would you survive least in?",
        "Which mode of transport scares you the most?",
        "Which extreme activity would you try once?",
        "Which vacation would end in disaster?",
        "Which location is overrated but everyone pretends to love?",
        "Which place would you run from if alone?"
    ],

    # 8. Adult / Naughty Humor
    [
        "Who would send the naughtiest meme first?",
        "Who would prank text someone in a flirty way?",
        "Who would accidentally text the wrong person?",
        "Who would try something risky on a dare?",
        "Who would laugh the hardest at a scandalous joke?",
        "Who would get away with flirting the most?",
        "Who would make the most awkward sexual joke?"
    ],

    # 9. Movies / TV Shows Opinions
    [
        "Which movie would you watch on repeat without shame?",
        "Which TV villain do you secretly root for?",
        "Which movie character would you date if possible?",
        "Which plot twist did you pretend to understand but didn’t?",
        "Which movie ending makes you cry every time?",
        "Which character death hit you the hardest?",
        "Which film scene would you reenact in real life?"
    ],

    # 10. Survival / Skills
    [
        "Who would last longest in the wild without tools?",
        "Who would build the best shelter?",
        "Who would find water first?",
        "Who would light a fire fastest?",
        "Who would make the weirdest survival tool from random items?",
        "Who would survive a zombie apocalypse best?",
        "Who would panic first but still somehow survive?"
    ],

    # 12. Music / Concerts
    [
        "Which genre would you secretly listen to but deny?",
        "Which concert would you sneak into?",
        "Which artist would you scream at if you met them?",
        "Which song would you blast at full volume?",
        "Which music trend do you actually like but find embarrassing?",
        "Which band would you fight over tickets for?",
        "Which song would you dance embarrassingly to?"
    ],

    # 14. Embarrassing Texts / Social Media
    [
        "Who would accidentally like an old photo?",
        "Who would reply too aggressively to a comment?",
        "Who would send a text to the wrong person?",
        "Who would overreact to a typo?",
        "Who would post something they immediately regret?",
        "Who would screenshot messages secretly?",
        "Who would slide into DMs awkwardly?"
    ],

    # 15. Fears / Phobias
    [
        "Who would scream first in a haunted house?",
        "Who would avoid spiders at all costs?",
        "Who would panic in the dark alone?",
        "Who would freak out at small insects?",
        "Who would refuse to watch horror movies?",
        "Who would cry during a scary game?",
        "Who would jump at the smallest noise?"
    ]
    ]
        game.playersQ = {}
        game.playerAns = []
        game.current_turn = 0
        game.current_question = ''
        game.current_liarQ = ''
        game.turn = []
        game.liar = 0

    def set_up(self):
        for x in self.players:
            self.scores[x] = 0
        turn_order = game.players[:]
        random.shuffle(turn_order)
        self.turn = turn_order
        
    
    def Qsort(self):
        liar = random.randint(0,game.num_of_players - 1)
        game.liar = liar
        qtopic = random.randint(0,11)
        qglobal = random.randint(0,6)
        qliar = random.randint(0,6)
        while qliar == qglobal:
            qliar = random.randint(0,6)
        for x in self.players:
            if x == self.players[liar]:
                self.playersQ[x] = self.questions[qtopic][qliar]
            else:
                self.playersQ[x] = self.questions[qtopic][qglobal]
        chaos = random.randint(0,100)
        if chaos == 1:
            game.current_question = self.questions[qtopic][qliar]
            game.current_liarQ = self.questions[qtopic][qglobal]
        else:
            game.current_question = self.questions[qtopic][qglobal]
            game.current_liarQ = self.questions[qtopic][qliar]




game = Game()