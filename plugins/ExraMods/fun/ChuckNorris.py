import random

import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("chucknorris"))

async def chucknorris_command_handler(client: Client, message: Message):

    # List of Chuck Norris facts

    facts = [

        "Chuck Norris can strangle you with a cordless phone.",

        "When Chuck Norris does push-ups, he doesn't push himself up, he pushes the earth down.",

        "Chuck Norris once made a Happy Meal cry.",

        "Chuck Norris can slam a revolving door.",

        "If Chuck Norris were a vegetable, he'd be a Chuck Norris.",

        "Chuck Norris once punched a man in the soul.",

        "Chuck Norris never wears a watch because he always knows what time it is. Always.",

        "The only thing that can cut Chuck Norris is Chuck Norris.",

        "Chuck Norris has already been to Mars; that's why there are no signs of life there.",

        "Chuck Norris has a diary. It's called the Guinness Book of World Records.",

        "Chuck Norris doesn't wear a seat belt because no one tells Chuck Norris what to do.",

        "Chuck Norris doesn't need Twitter. He's already following you.",

        "Chuck Norris was once bitten by a rattlesnake. After three days of pain and agony, the snake died.",

        "Chuck Norris can kill two stones with one bird.",

        "Chuck Norris can hear sign language.",

        "When Chuck Norris crosses the street, cars have to look both ways.",

        "Chuck Norris can sneeze with his eyes open.",

        "Chuck Norris doesn't do push-ups, he pushes the Earth down.",

        "Chuck Norris once had a heart attack...his heart lost",

        "Chuck Norris counted to infinity. Twice.",

        "Chuck Norris is the reason why Waldo is hiding.",

        "Chuck Norris can believe it's not butter.",

        "The only time Chuck Norris was wrong is when he thought he had made a mistake.",

        "Chuck Norris doesn't breathe air. He holds air hostage.",

        "Chuck Norris doesn't call the wrong number. You answer the wrong phone.",

        "Chuck Norris once ate an entire bottle of sleeping pills. They made him blink.",

        "Chuck Norris can blow bubbles with beef jerky.",

        "Chuck Norris can eat soup with a fork.",

        "Chuck Norris once went to the Virgin Islands. Now they're just called The Islands.",

        "When the boogeyman goes to sleep every night, he checks his closet for Chuck Norris.",

        "Chuck Norris can hear sign language.",

        "Chuck Norris can slam revolving door.",

        "Chuck Norris can divide by zero.",

        "The Great Wall of China was originally created to keep Chuck Norris out. It failed miserably.",

        "When Chuck Norris enters a room, he doesn't turn the lights on, he turns the dark off.",

        "Chuck Norris can kill your imaginary friends.",

        "Chuck Norris once sold eBay to eBay on eBay.",

        "Chuck Norris doesn't need a GPS because Chuck Norris knows where you are.",

        "Chuck Norris can strangle you with a cordless phone.",

        "Chuck Norris lost his virginity before his dad did.",
      
          "Chuck Norris can make a snowman out of rain.",
    "Chuck Norris can slam a revolving door.",
    "Chuck Norris can strangle you with a cordless phone... while it's charging.",
    "Chuck Norris can eat just one Lay's potato chip.",
    "The dark is afraid of Chuck Norris.",
    "Chuck Norris once bit a shark and it turned into a dolphin.",
    "When Chuck Norris does a pushup, he isn't lifting himself up, he's pushing the ground down.",
    "Chuck Norris can sneeze with his eyes open.",
    "Chuck Norris can win a game of chess in only one move.",
    "Chuck Norris's tears cure cancer. Too bad he has never cried.",
    "Chuck Norris doesn't use a napkin. He wipes his face with the souls of his enemies.",
    "Chuck Norris has counted to infinity twice.",
    "Chuck Norris once won a game of Connect Four in three moves.",
    "Chuck Norris can punch through a wall... with his fist.",
    "Chuck Norris can divide by zero.",
    "Chuck Norris put the laughter in manslaughter.",
    "Chuck Norris can speak Russian... in Chinese.",
    "Chuck Norris doesn't hit a target. The target gets in the way of his fist.",
    "Chuck Norris can kill two stones with one bird.",
    "Chuck Norris can pop popcorn with his fists.",
    "Chuck Norris can touch MC Hammer.",
    "The boogeyman checks his closet for Chuck Norris before he goes to bed.",
    "Chuck Norris once took a lie detector test. The machine confessed everything.",
    "Chuck Norris doesn't call the wrong number. You answer the wrong phone.",
    "Chuck Norris can turn on a light switch by clapping his hands.",
    "Chuck Norris can spell 'creativity' with only two letters.",
    "Chuck Norris doesn't need a watch. He decides what time it is.",
    "Chuck Norris can win a staring contest against a statue.",
    "Chuck Norris can strum a guitar without using his hands.",
    "Chuck Norris can make a fire by rubbing two ice cubes together.",
    "Chuck Norris can drown a fish.",
    "Chuck Norris can light a fire by rubbing two ice cubes together.",
    "When Chuck Norris jumps into a swimming pool, he doesn't get wet. The water gets Chuck Norris.",
    "Chuck Norris once killed 20 men with a single roundhouse kick.",
    "Chuck Norris can open a can of beer with his teeth... while blindfolded.",
    "Chuck Norris has never lost a game of Battleship. He sinks all the ships in one shot.",
    "Chuck Norris can make a dog meow.",
    "Chuck Norris doesn't need to chew his food. His teeth are powerful enough to grind diamonds.",
    "Chuck Norris's beard is actually a cage for his face.",
    "Chuck Norris can finish a puzzle in one piece.",
    "Chuck Norris can cut through a hot knife with butter.",
    "Chuck Norris can hear sign language.",
    "Chuck Norris can catch a fish with his bare hands, but prefers to use dynamite.",
    "Chuck Norris doesn't have a chin under his beard. Just another fist.",
    "Chuck Norris can make a snow angel in a brick wall.",
    "Chuck Norris can strangle you with a cordless phone... while using a rotary dial.",
    "Chuck Norris once ate a whole cake before his friends could tell him there was a stripper inside.",
    "Chuck Norris can cook Minute Rice in 30 seconds.",
      "Chuck Norris can unscramble an egg.",
    "Aliens don't exist because they're afraid of Chuck Norris.",
    "Chuck Norris can speak braille.",
    "Chuck Norris once played Russian Roulette with a fully loaded gun and won.",
    "Chuck Norris can make a woman climax just by pointing at her and saying 'booya'.",
    "Chuck Norris doesn't cheat death. He wins fair and square.",
    "Chuck Norris can kill your imaginary friends.",
    "When Chuck Norris does division, there are no remainders.",
    "Chuck Norris has the heart of a child. He keeps it in a jar on his desk.",
    "Chuck Norris doesn't do push-ups. He pushes the earth down.",
    "If Chuck Norris was a Spartan in the movie 300, the movie would be called 1.",
    "Chuck Norris once killed a bird by throwing it off a cliff.",
    "Chuck Norris can build a snowman out of rain.",
    "Chuck Norris once punched a man in the soul.",
    "Chuck Norris can win a game of Connect Four in only three moves.",
    "Chuck Norris can cure cancer with his tears. Too bad Chuck Norris never cries.",
    "Chuck Norris can slam a revolving door.",
    "Chuck Norris can tie his shoelaces with his feet.",
    "Chuck Norris doesn't need a keyboard. He tells the computer what to do.",
    "Chuck Norris can write a book with a single pen stroke.",
    "Chuck Norris once ate an entire bottle of sleeping pills. They made him blink.",
    "Chuck Norris can pick oranges from an apple tree and make the best lemonade you've ever tasted.",
    "Chuck Norris can make a fire by rubbing two ice cubes together.",
    "Chuck Norris can grill a popsicle.",
    "Chuck Norris can drink an entire gallon of milk in one gulp.",
    "Chuck Norris doesn't have a bank account. He just tells the bank what his balance is.",
    "Chuck Norris doesn't need a parachute. He jumps out of planes with a backpack full of bricks.",
    "Chuck Norris can hear sign language.",
    "Chuck Norris can kill two stones with one bird.",
    "Chuck Norris can make onions cry.",
    "Chuck Norris can win a staring contest against the sun.",
          "Chuck Norris can make a diamond out of charcoal.",
    "When Chuck Norris goes swimming, he doesn't get wet. The water gets Chuck Norris.",
    "Chuck Norris can slam a revolving door.",
    "Chuck Norris can kill two stones with one bird.",
    "When Alexander Graham Bell invented the telephone, he had three missed calls from Chuck Norris.",
    "Chuck Norris once ate a whole cake before his friends could tell him there was a stripper inside.",
    "Chuck Norris can strangle you with a cordless phone... while using a rotary dial.",
    "Chuck Norris can cook Minute Rice in 30 seconds.",
    "Chuck Norris once won a staring contest against his own reflection.",
    "When Chuck Norris enters a room, he doesn't turn the lights on. He turns the dark off.",
    "Chuck Norris can win an argument with a mute person.",
    "Chuck Norris can play Jenga with a single block.",
    "Chuck Norris can build a snowman out of sand.",
    "Chuck Norris can walk on water... on a treadmill.",
    "When Chuck Norris jumps into a swimming pool, the water needs to dry off afterwards.",
    "Chuck Norris knows Victoria's secret.",
    "Chuck Norris can listen to a silent movie.",
    "Chuck Norris can solve a Rubik's Cube in less than 2 moves.",
    "Chuck Norris can kill a stone with a feather.",
    "Chuck Norris can unscramble an egg.",
    "Chuck Norris can hear sign language.",
    "Chuck Norris can ride a unicycle... backwards.",
    "Chuck Norris can sneeze with his eyes open.",
    "Chuck Norris can speak in Morse code... with his fists.",
    "Chuck Norris can divide by zero.",
    "Chuck Norris can make a fire by rubbing two ice cubes together.",
    "Chuck Norris can win a staring contest against the sun.",
    "Chuck Norris can light a fire with two rocks. One of them is Chuck Norris.",
    "Chuck Norris can read Lady Gaga's poker face.",
    "Chuck Norris can charge a phone by rubbing it against his beard.",
    "Chuck Norris can listen to 8 tracks at once.",
    "Chuck Norris can tickle himself.",
    "Chuck Norris can speak Spanish... in Chinese.",
    "Chuck Norris can order breakfast at a burger joint.",
    "Chuck Norris doesn't need an eraser because he never makes mistakes.",
    "Chuck Norris can cure baldness with a hairbrush.",
    "Chuck Norris can solve world hunger with a single sandwich.",
    "Chuck Norris can slam a revolving door.",
    "Chuck Norris can levitate... down.",
    "Chuck Norris can find Waldo in under a second.",
    "Chuck Norris can use a calculator without looking at the numbers.",
    "Chuck Norris can build a house out of playing cards.",
    "Chuck Norris can start a fire with two ice cubes.",
    "The Bermuda Triangle used to be called The Bermuda Square until Chuck Norris roundhouse kicked one of the corners off.",
    "Chuck Norris can fix a broken heart with duct tape.",
    "Chuck Norris can win a game of chess just by staring at the board.",
    "Chuck Norris has never lost a staring contest. Ever.",
      "Chuck Norris can write a biography about himself without using the letter 'e'.",
    "Chuck Norris can whistle with his mouth closed.",
    "Chuck Norris once punched a man so hard that he broke time.",
    "Chuck Norris knows what you did last summer... because he was there.",
    "When Chuck Norris lifts weights, the dumbbells feel pain.",
    "Chuck Norris doesn't get frostbite. Chuck Norris bites frost.",
    "Chuck Norris can win an argument with a fence post.",
    "Chuck Norris can play chess with both hands tied behind his back and still beat you.",
    "Chuck Norris doesn't do pushups. He pushes the world down.",
    "Chuck Norris can walk through walls... after opening the door first.",
    "Chuck Norris can make a fire by rubbing two ice cubes together... underwater.",
    "Chuck Norris can swim faster than a shark... on land.",
    "The only thing that can kill Chuck Norris is Chuck Norris.",
    "Chuck Norris can touch MC Hammer.",
    "Chuck Norris can eat just one Lay's potato chip.",
    "Chuck Norris doesn't age. The calendar just marks his progress.",
    "Chuck Norris can kill you with a thought. He just chooses not to.",
    "Chuck Norris can build a snowman out of rain.",
    "Chuck Norris doesn't wear a watch. He decides what time it is.",
    "Chuck Norris can jump-start a car... with jumper cables attached to his nipples.",
    "Chuck Norris can strangle you with a cordless phone... while talking on the phone.",
    "Chuck Norris can make a GPS say 'you have reached your destination'... even if you're lost.",
    "Chuck Norris can open a soda can with his mind.",
    "Chuck Norris can talk about Fight Club.",
    "Chuck Norris can shoot a bow and arrow with his feet.",
    "Chuck Norris can do a wheelie on a unicycle.",
    "Chuck Norris can make a rock bleed.",
    "When Chuck Norris goes to sleep, he doesn't count sheep. They count him.",
    "Chuck Norris can run a marathon in his sleep... while holding his breath.",
    "Chuck Norris doesn't need a key to start his car. His car starts just by sensing his presence.",
    "Chuck Norris can pick an apple from a tree and leave the branch intact.",
    "Chuck Norris can make a snowman out of sand.",
    "Chuck Norris can catch a fish with his bare hands and then let it go... and the fish will thank him for it.",
    "Chuck Norris can jump-start a car... just by staring at the engine.",
    "Chuck Norris can type over 200 words per minute... with his tongue.",
    "Chuck Norris can whistle underwater.",
    "Chuck Norris can count to infinity twice.",
    "Chuck Norris can breathe fire... underwater.",
    "Chuck Norris can win a game of Monopoly in one turn.",
    "Chuck Norris can make a blind man see... with his fists.",
    "Chuck Norris can beat a giraffe in a neck wrestling match.",
    "Chuck Norris can squeeze orange juice out of a lemon.",
    "Chuck Norris can win Connect Four in three moves... with only two pieces.",
    "Chuck Norris can stop a bullet... with his chest hair.",
    "Chuck Norris can climb Mount Everest... from the comfort of his own living room.",
    "Chuck Norris can start a fire by rubbing two ice cubes together... in the desert.",
    "Chuck Norris can build a house out of toothpicks.",
    "Chuck Norris can outswim a torpedo.",
    "Chuck Norris can kill you with a pillow... made of concrete.",
    "Chuck Norris can win a staring contest against a statue.",
      
    "Chuck Norris can make a slinky go upstairs.",
    "Chuck Norris can start a fire by rubbing two ice cubes together... in the Arctic.",
    "Chuck Norris doesn't need to breathe. Air is afraid to enter his lungs.",
    "Chuck Norris can win a game of Connect Four in just two moves.",
    "Chuck Norris can turn water into wine... then into beer.",
    "Chuck Norris can read Lady Gaga's poker face with his eyes closed.",
    "Chuck Norris can unscramble an egg.",
    "Chuck Norris can play Russian Roulette with a fully loaded gun and win every time.",
    "Chuck Norris can lift weights that even the gym doesn't know exist.",
    "Chuck Norris can turn a vegan into a carnivore... with one punch.",
    "Chuck Norris can shoot a snake from over a mile away... with a BB gun.",
    "Chuck Norris can play Jenga with bowling balls.",
    "Chuck Norris can write a book without using words.",
    "Chuck Norris can make a diamond out of thin air.",
    "Chuck Norris can sneeze with his eyes open and keep a straight face.",
    "Chuck Norris can walk on water... backwards.",
    "Chuck Norris doesn't need to shower. Dirt is afraid to stick to him.",
    "Chuck Norris can make a traffic light turn green just by staring at it.",
    "Chuck Norris can kill a bird by throwing it off a cliff.",
    "Chuck Norris can solve a Rubik's Cube in one move.",
    "Chuck Norris can hear what you're thinking... even if you're not thinking.",
    "Chuck Norris can do a push-up with one finger... while doing a handstand.",
    "Chuck Norris can jump-start a car... using jumper cables made of spaghetti.",
    "Chuck Norris can win a staring contest against a cat.",
    "Chuck Norris can make a snowman out of fire.",
    "Chuck Norris can train an elephant to do tricks... with just his voice.",
    "Chuck Norris can bench press the entire Internet.",
    "Chuck Norris can bend steel with his mind... and his pinkie finger.",
    "Chuck Norris can catch a bullet in his teeth... then spit it back at you.",
    "Chuck Norris can teach a fish to ride a bicycle.",
    "When Chuck Norris was born, he drove his mother home from the hospital.",
    "Chuck Norris can think so hard that he can hear himself thinking.",
    "Chuck Norris's dog has its own personal bodyguard.",
    "Chuck Norris can speak Braille.",
    "Chuck Norris can cook a three-course meal using only a toaster oven.",
    "Chuck Norris can swim through sand.",
    "Chuck Norris can run faster than the speed of light... but only backwards.",
    "Chuck Norris doesn't wear a watch. He decides what time it is.",
    "Chuck Norris can give himself a haircut... blindfolded.",
    "Chuck Norris can make a statue move by staring at it.",
    "Chuck Norris can talk about Fight Club.",
    "Chuck Norris can speak French... in Russian.",
    "Chuck Norris can find Waldo while blindfolded.",
    "Chuck Norris can make a diamond out of coal just by telling it to compress itself.",
    "Chuck Norris can drive a car... without using the steering wheel.",
    "Chuck Norris can play a guitar... using only his teeth.",
    "Chuck Norris can win a game of chess using only pawns.",
    "Chuck Norris can hear a pin drop... from across the room.",
    "Chuck Norris can make a mountain out of a molehill... then climb it.",
      
    "Chuck Norris can divide by zero.",
    "Chuck Norris can see ultra-violet light... with his eyes closed.",
    "Chuck Norris can win a staring contest against a mirror.",
    "Chuck Norris can cook minute rice in 30 seconds.",
    "When Chuck Norris was born he didn't cry, the world cried because it realized it would never be as great as him.",
    "Chuck Norris can win a fight with a single stare... and a little bit of roundhouse kicking.",
    "Chuck Norris can make a snow angel... in lava.",
    "Chuck Norris can take a photo of himself from the inside.",
    "Chuck Norris can play a game of chess with only a knight.",
    "Chuck Norris can dry his clothes underwater.",
    "Chuck Norris can make a rock bleed... just by looking at it.",
    "Chuck Norris can stop a bullet with a single thought... but he'd rather let it hit him. It tickles.",
    "Chuck Norris can turn on a lamp... without electricity.",
    "Chuck Norris can outrun a car... that's being driven by The Flash.",
    "Chuck Norris can use a black hole to clean his house.",
    "Chuck Norris can make a turtle go faster than a hare... in a race.",
    "Chuck Norris can write a screenplay with his feet... while doing a handstand.",
    "Chuck Norris can punch through solid steel... using a rubber glove.",
    "Chuck Norris can score a touchdown... in a game of soccer.",
    "Chuck Norris can read an entire book... just by smelling it.",
    "Chuck Norris can hold his breath for 10 minutes... under water or in outer space.",
    "Chuck Norris can make a cactus scream... just by looking at it.",
    "Chuck Norris can make a cat bark... just by meowing at it.",
    "Chuck Norris can create a rainbow... with black paint.",
    "Chuck Norris can slam a revolving door.",
    "Chuck Norris's beard doesn't grow. It simply appears.",
    "Chuck Norris can run so fast that he can outrun his own shadow.",
    "Chuck Norris can kill two stones with one bird.",
    "Chuck Norris doesn't sleep, he waits.",
    "Chuck Norris can eat just one Lay's potato chip... and leave the rest of the bag for you.",
    "Chuck Norris can hold his breath for 10 minutes... underwater or in outer space.",
    "Chuck Norris can throw a grenade and kill 50 people... then catch it without it exploding.",
    "Chuck Norris once won a staring contest against his own reflection.",
    "Chuck Norris can bench press a car... with his pinkie finger.",
    "Chuck Norris can make onions cry.",
    "Chuck Norris can drink a gallon of milk in 30 seconds... even if it's expired.",
    "When Chuck Norris goes to donate blood, he declines the syringe and instead requests a hand gun and a bucket.",
    "Chuck Norris can start a fire by rubbing two ice cubes together... during a heat wave.",
    "Chuck Norris can solve a crossword puzzle... with only one letter.",
    "Chuck Norris is the reason why Waldo is hiding.",
    "Chuck Norris can break a diamond... with his butt.",
    "Chuck Norris can speak braille... with his fists.",
    "Chuck Norris can kill a stone with a feather.",
    "Chuck Norris can walk on water... but he prefers to swim through land.",
    "Chuck Norris can make a snowman out of rain.",
    "Chuck Norris can make a bologna sandwich out of thin air.",
    "Chuck Norris can read your mind... even if you don't have one.",
    "Chuck Norris once kicked a horse in the chin. Its descendants are now known as giraffes.",
          "Chuck Norris can make a snowman out of firewood.",
    "Chuck Norris can speak Spanish in Chinese.",
    "Chuck Norris can sneeze with his eyes open.",
    "Chuck Norris once had a staring contest with the sun... and won.",
    "Chuck Norris can win at rock-paper-scissors... with just his mind.",
    "Chuck Norris can cure a headache by giving you a roundhouse kick to the face.",
    "Chuck Norris can make a bird sound like a cat... just by looking at it.",
    "Chuck Norris can eat a one-pound steak in one bite... without chewing.",
    "Chuck Norris can make a marshmallow roast itself over a fire.",
    "Chuck Norris can count to infinity backwards... twice.",
    "Chuck Norris can jump-start a car... using jumper cables made of barbed wire.",
    "When Chuck Norris was in preschool, his teachers had to raise their hands before speaking to him.",
    "Chuck Norris can take a picture of tomorrow... today.",
    "Chuck Norris can kill a zombie with a smile.",
    "Chuck Norris can shoot an arrow around a corner... without bending it.",
    "Chuck Norris can make a tree fall... just by giving it a dirty look.",
    "Chuck Norris can build a house out of toothpicks... with his feet.",
    "Chuck Norris can play a game of darts... with a hand grenade.",
    "Chuck Norris can make a lemon taste sweet... just by breathing on it.",
    "Chuck Norris can beat Superman in a race... while riding a tricycle.",
    "Chuck Norris can make a snake go limp just by talking to it.",
    "Chuck Norris can swim through land... and run through water.",
    "Chuck Norris can make a vacuum cleaner suck... air out of a tire.",
    "Chuck Norris can create life... from nothing.",
    "Chuck Norris can eat a bowl of cereal... without any milk.",
    "When Chuck Norris does push-ups, he doesn't push himself up. He pushes the world down.",
    "Chuck Norris can use sign language... with his feet.",
    "Chuck Norris can run faster than a cheetah... while wearing high heels.",
    "Chuck Norris can make a blind man see... with his fists.",
    "Chuck Norris can make a car run on water... and vodka.",
    "Chuck Norris can find a needle in a haystack... while blindfolded.",
    "Chuck Norris can talk to animals... in any language.",
    "Chuck Norris can hold his breath for 20 minutes... even if he's underwater.",
    "Chuck Norris can cook an egg... just by staring at it.",
    "Chuck Norris can make a compass point south... just by looking at it.",
    "Chuck Norris can turn lead into gold... with his bare hands.",
    "Chuck Norris can make a snowball out of fire.",
    "Chuck Norris can dig a hole to China... with a spoon.",
    "Chuck Norris can make a skyscraper lay flat... by looking at it sideways.",
    "Chuck Norris can speak Russian... in Spanish.",
    "Chuck Norris can make a catdog.",
    "Chuck Norris can do a wheelie on a tricycle.",
    "Chuck Norris can make onions cry... by telling them a sad story.",
    "Chuck Norris can drive a stick shift... with his tongue.",
    "Chuck Norris can make a bird sing... heavy metal.",
    "Chuck Norris can make a potato chip last forever... by licking it.",
    "Chuck Norris can teach a moth how to play dead.",
    "Chuck Norris can beat a fish at its own game.",
    "Chuck Norris can run faster than a bullet... that's been fired from his own gun.",
    "Chuck Norris can make a candle burn underwater.",
      "Chuck Norris can make a snowman out of sand.",
    "Chuck Norris can speak every language... with his fists.",
    "Chuck Norris can teach a cat how to bark.",
    "When Chuck Norris does push-ups, he doesn't push himself up. He pushes the Earth down.",
    "Chuck Norris can catch a fish... with his bare hands.",
    "Chuck Norris can turn water into wine... then into beer... then into whiskey.",
    "Chuck Norris can make a giraffe fit in a Volkswagen Beetle.",
    "Chuck Norris doesn't need a watch. He decides what time it is.",
    "Chuck Norris can kill two stones with one bird.",
    "Chuck Norris can make an apple taste like a steak... just by looking at it.",
    "Chuck Norris can make a volcano erupt... by staring at it.",
    "Chuck Norris can jump-start a car... using jumper cables made of spaghetti.",
    "When Chuck Norris looks in the mirror, the reflection ducks for cover.",
    "Chuck Norris can break a man's jaw by simply talking to him.",
    "Chuck Norris can tap dance... on a tightrope.",
    "Chuck Norris can make a statue move... just by looking at it.",
    "Chuck Norris doesn't go hunting... he goes killing.",
    "Chuck Norris can make a golf ball orbit the moon.",
    "Chuck Norris can make a turtle go faster than a rabbit... while walking backwards.",
    "Chuck Norris can play hopscotch... with a rhinoceros.",
    "Chuck Norris can make a rainbow turn black and white.",
    "Chuck Norris once won a game of Connect Four... in three moves.",
    "Chuck Norris can run 300 miles... without breaking a sweat.",
    "Chuck Norris can make a house out of playing cards... and it won't fall down.",
    "Chuck Norris can make a tree grow... just by staring at its shadow.",
    "Chuck Norris can make a snowball out of sand... and use it to break someone's nose.",
    "Chuck Norris can cut through a hot knife with butter.",
    "Chuck Norris can make a donut cry... just by looking at it.",
    "Chuck Norris can make a caterpillar turn into a butterfly... just by telling it to.",
    "Chuck Norris can make an onion taste sweet... by telling it a funny joke.",
    "Chuck Norris can make a candle burn in outer space.",
    "When Chuck Norris goes to sleep, he doesn't count sheep. Sheep count Chuck Norris.",
    "Chuck Norris can make a skyscraper jump... just by shouting 'Boo!'",
    "Chuck Norris can make a fire extinguisher explode... just by pointing at it.",
    "Chuck Norris can play a guitar... using only his teeth and his beard.",
    "Chuck Norris can make a polar bear sweat... just by staring at it.",
    "Chuck Norris can make a train go off the tracks... with his eyebrows.",
    "Chuck Norris can make a piece of paper fall faster than a rock.",
    "Chuck Norris can make a grizzly bear hibernate... in the middle of summer.",
    "Chuck Norris can make a frog ribbit... in Morse code.",
    "Chuck Norris can make a car run on empty... by telling it to keep going.",
    "Chuck Norris can make a snake say 'uncle.'",
    "Chuck Norris can make a mountain out of a molehill... then climb it backwards.",
    "Chuck Norris can make a chair levitate... just by looking at it.",
    "Chuck Norris can make a chicken fly... by giving it wings made of gold.",
    "Chuck Norris can make a golf ball go straight... even if he hits it sideways.",
    "Chuck Norris can make a bug crawl backwards... by telling it to reverse.",
    "Chuck Norris can make a fish walk on land... by giving it legs of steel.",
    "Chuck Norris can make a catfish bark... by calling it Rover.",
    "Chuck Norris can make a watch stop... just by looking at it.",
    "Chuck Norris can make a cow give chocolate milk... by just asking nicely."
    ]

    

    # Choose a random fact from the list

    fact = random.choice(facts)

    

    # Send the fact in a humorous message to the user

    pm = await message.reply_text("Here's a hilarious Chuck Norris fact for you! Get ready...")

    await asyncio.sleep(5)

    await pm.edit(f"Did you know that {fact}? 😂😂😂")



 