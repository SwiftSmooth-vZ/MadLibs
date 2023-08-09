print("Hello and Welcome to MadLibs")
print("Please go through the lists of MadLibs from  \'MadLibs-List.txt'")
MadLibs_text = ""
condition = True

while condition == True:
    madlibs_choice = int(input("Please enter the number of the MadLibs you selected, for e.g. Type \'1' for MadLibs Number 1 ==> "))
    if madlibs_choice == 1:
        MadLibs_text += "In the land of [adjective], a [noun] named [name] set off on a daring quest to find the fabled [adjective2] [noun2]. Armed with a [adjective3] [noun3] and guided by a talking [animal], they ventured through [place] where [verb ending in -ed] [plural noun] roamed. Along their journey, they encountered a wise [noun4] who shared [number] riddles, leading them closer to their destiny."
        print(MadLibs_text)
        print("\nHere\'s your MadLibs text, please follow the instructions below to see the end results")
        adjective = input("Enter an adjective: ")
        noun = input("Enter a noun: ")
        name = input("Enter a name: ")
        adjective2 = input("Enter another adjective: ")
        noun2 = input("Enter another noun: ")
        adjective3 = input("Enter one more adjective: ")
        noun3 = input("Enter one more noun: ")
        animal = input("Enter an animal: ")
        place = input("Enter a place: ")
        verb_ed = input("Enter a verb ending in -ed: ")
        plural_noun = input("Enter a plural noun: ")
        noun4 = input("Enter another noun: ")
        number = input("Enter a number: ")
        print(
            f"\nIn the land of {adjective}, a {noun} named {name} set off on a daring quest to find the fabled {adjective2} {noun2}. Armed with a {adjective3} {noun3} and guided by a talking {animal}, they ventured through {place} where {verb_ed} {plural_noun} roamed. Along their journey, they encountered a wise {noun4} who shared {number} riddles, leading them closer to their destiny.")
        condition = False

    elif madlibs_choice == 2:
        MadLibs_text += "In the bustling city of [city], the annual [adjective] Food Festival was in full swing. Chefs from around the world showcased their [adjective2] dishes, from [color] [noun] to [adjective3] [plural noun]. The highlight of the event was the Great [noun2] Cook-Off, where [celebrity chef] amazed everyone with their secret ingredient: [ingredient]. The crowd cheered as the judges devoured each creation with [adjective4] delight."
        print(MadLibs_text)
        print("\nHere\'s your MadLibs text, please follow the instructions below to see the end results")
        city = input("Enter a city: ")
        adjective = input("Enter an adjective: ")
        adjective2 = input("Enter another adjective: ")
        color = input("Enter a color: ")
        noun = input("Enter a noun: ")
        adjective3 = input("Enter one more adjective: ")
        plural_noun = input("Enter a plural noun: ")
        noun2 = input("Enter another noun: ")
        celebrity_chef = input("Enter a celebrity chef's name: ")
        ingredient = input("Enter an ingredient: ")
        adjective4 = input("Enter one more adjective: ")
        print(
            f"\nIn the bustling city of {city}, the annual {adjective} Food Festival was in full swing. Chefs from around the world showcased their {adjective2} dishes, from {color} {noun} to {adjective3} {plural_noun}. The highlight of the event was the Great {noun2} Cook-Off, where {celebrity_chef} amazed everyone with their secret ingredient: {ingredient}. The crowd cheered as the judges devoured each creation with {adjective4} delight.")
        condition = False

    elif madlibs_choice == 3:
        MadLibs_text += "When [name] activated the experimental [noun], they never expected to be transported to [year]. In this [adjective] era, they encountered [number] [adjective2] [plural noun] who mistook them for a [profession]. To return home, they needed to locate the elusive [adjective3] [noun2] guarded by a [adjective4] [creature]. Along the way, they formed an unlikely friendship with [historical figure] and uncovered the true meaning of [concept]."
        print(MadLibs_text)
        print("\nHere\'s your MadLibs text, please follow the instructions below to see the end results")
        name = input("Enter a name: ")
        noun = input("Enter a noun: ")
        year = input("Enter a year: ")
        adjective = input("Enter an adjective: ")
        number = input("Enter a number: ")
        adjective2 = input("Enter another adjective: ")
        plural_noun = input("Enter a plural noun: ")
        profession = input("Enter a profession: ")
        adjective3 = input("Enter one more adjective: ")
        noun2 = input("Enter another noun: ")
        adjective4 = input("Enter one more adjective: ")
        creature = input("Enter a creature: ")
        historical_figure = input("Enter a historical figure: ")
        concept = input("Enter a concept: ")
        print(
            f"\nWhen {name} activated the experimental {noun}, they never expected to be transported to {year}. In this {adjective} era, they encountered {number} {adjective2} {plural_noun} who mistook them for a {profession}. To return home, they needed to locate the elusive {adjective3} {noun2} guarded by a {adjective4} {creature}. Along the way, they formed an unlikely friendship with {historical_figure} and uncovered the true meaning of {concept}.")
        condition = False

    elif madlibs_choice == 4:
        MadLibs_text += "In the distant galaxy of [galaxy name], a crew of [number] [adjective] [noun] embarked on a mission to explore [adjective2] planets. Their spaceship, the [ship name], used [color] [noun2] to navigate through [adjective3] asteroid fields. During their voyage, they discovered a [adjective4] anomaly that led them to a parallel [dimension]. There, they met [alien species] and exchanged [adjective5] stories about their worlds."
        print(MadLibs_text)
        print("\nHere\'s your MadLibs text, please follow the instructions below to see the end results")
        galaxy_name = input("Enter a galaxy name: ")
        number = input("Enter a number: ")
        adjective = input("Enter an adjective: ")
        noun = input("Enter a noun: ")
        adjective2 = input("Enter another adjective: ")
        ship_name = input("Enter a ship name: ")
        color = input("Enter a color: ")
        noun2 = input("Enter another noun: ")
        adjective3 = input("Enter one more adjective: ")
        adjective4 = input("Enter one more adjective: ")
        dimension = input("Enter a dimension: ")
        alien_species = input("Enter an alien species: ")
        adjective5 = input("Enter one more adjective: ")
        print(
            f"\nIn the distant galaxy of {galaxy_name}, a crew of {number} {adjective} {noun} embarked on a mission to explore {adjective2} planets. Their spaceship, the {ship_name}, used {color} {noun2} to navigate through {adjective3} asteroid fields. During their voyage, they discovered a {adjective4} anomaly that led them to a parallel {dimension}. There, they met {alien_species} and exchanged {adjective5} stories about their worlds.")
        condition = False

    elif madlibs_choice == 5:
        MadLibs_text += "As the city slept, [superhero name] leaped into action, their [adjective] cape billowing in the wind. Armed with [color] [noun] and [adjective2] powers, they thwarted [adjective3] villains and rescued [number] [plural noun]. In their secret hideout, a [adjective4] [noun2], they analyzed clues with their trusty sidekick, [sidekick name]. With their teamwork, they always managed to save the day."
        print(MadLibs_text)
        print("\nHere\'s your MadLibs text, please follow the instructions below to see the end results")
        superhero_name = input("Enter a superhero name: ")
        adjective = input("Enter an adjective: ")
        color = input("Enter a color: ")
        noun = input("Enter a noun: ")
        adjective2 = input("Enter another adjective: ")
        adjective3 = input("Enter one more adjective: ")
        number = input("Enter a number: ")
        plural_noun = input("Enter a plural noun: ")
        adjective4 = input("Enter one more adjective: ")
        noun2 = input("Enter another noun: ")
        sidekick_name = input("Enter a sidekick name: ")
        print(
            f"\nAs the city slept, {superhero_name} leaped into action, their {adjective} cape billowing in the wind. Armed with {color} {noun} and {adjective2} powers, they thwarted {adjective3} villains and rescued {number} {plural_noun}. In their secret hideout, a {adjective4} {noun2}, they analyzed clues with their trusty sidekick, {sidekick_name}. With their teamwork, they always managed to save the day.")
        condition = False

    elif madlibs_choice == 6:
        MadLibs_text += "Deep in the [adjective] ocean, [name] discovered the entrance to an [adjective2] underwater kingdom. Among the vibrant [color] coral reefs and [adjective3] sea creatures, they befriended a playful [noun] who showed them the way to the [adjective4] palace. There, they met the [adjective5] mermaid queen, who entrusted them with a [magical item] to restore balance to the [adjective6] sea."
        print(MadLibs_text)
        print("\nHere\'s your MadLibs text, please follow the instructions below to see the end results")
        adjective = input("Enter an adjective: ")
        name = input("Enter a name: ")
        adjective2 = input("Enter another adjective: ")
        color = input("Enter a color: ")
        adjective3 = input("Enter one more adjective: ")
        noun = input("Enter a noun: ")
        adjective4 = input("Enter one more adjective: ")
        adjective5 = input("Enter one more adjective: ")
        magical_item = input("Enter a magical item: ")
        adjective6 = input("Enter one more adjective: ")
        print(
            f"\nDeep in the {adjective} ocean, [name] discovered the entrance to an {adjective2} underwater kingdom. Among the vibrant {color} coral reefs and {adjective3} sea creatures, they befriended a playful {noun} who showed them the way to the {adjective4} palace. There, they met the {adjective5} mermaid queen, who entrusted them with a {magical_item} to restore balance to the {adjective6} sea.")
        condition = False

    elif madlibs_choice == 7:
        MadLibs_text += "In the eccentric inventor's workshop, a [adjective] contraption hummed and whirred. The inventor, [name], aimed to create a [adjective2] device that could [verb]. However, their invention kept producing [adjective3] [noun] instead. Undeterred, they enlisted the help of a [adjective4] robot and a mischievous [noun2] for a brainstorming session that led to unexpected [adjective5] solutions."
        print(MadLibs_text)
        print("\nHere\'s your MadLibs text, please follow the instructions below to see the end results")
        adjective = input("Enter an adjective: ")
        name = input("Enter a name: ")
        adjective2 = input("Enter another adjective: ")
        verb = input("Enter a verb: ")
        adjective3 = input("Enter one more adjective: ")
        noun = input("Enter a noun: ")
        adjective4 = input("Enter one more adjective: ")
        noun2 = input("Enter another noun: ")
        adjective5 = input("Enter one more adjective: ")
        print(
            f"\nIn the eccentric inventor's workshop, a {adjective} contraption hummed and whirred. The inventor, {name}, aimed to create a {adjective2} device that could {verb}. However, their invention kept producing {adjective3} {noun} instead. Undeterred, they enlisted the help of a {adjective4} robot and a mischievous {noun2} for a brainstorming session that led to unexpected {adjective5} solutions.")
        condition = False

    elif madlibs_choice == 8:
        MadLibs_text += "Deep within the [adjective] forest, a hidden [noun] guarded the entrance to a [adjective2] realm. Those who entered encountered talking [plural noun] and mischievous [adjective3] fairies. At the heart of the forest stood a [adjective4] tree that granted wishes when one placed a [color] [noun2] beneath its branches. One day, a [name] stumbled upon the tree and made a wish that changed their [adjective5] life."
        print(MadLibs_text)
        print("\nHere\'s your MadLibs text, please follow the instructions below to see the end results")
        adjective = input("Enter an adjective: ")
        noun = input("Enter a noun: ")
        adjective2 = input("Enter another adjective: ")
        plural_noun = input("Enter a plural noun: ")
        adjective3 = input("Enter one more adjective: ")
        adjective4 = input("Enter one more adjective: ")
        color = input("Enter a color: ")
        noun2 = input("Enter another noun: ")
        name = input("Enter a name: ")
        adjective5 = input("Enter one more adjective: ")
        print(
            f"\nDeep within the {adjective} forest, a hidden {noun} guarded the entrance to a {adjective2} realm. Those who entered encountered talking {plural_noun} and mischievous {adjective3} fairies. At the heart of the forest stood a {adjective4} tree that granted wishes when one placed a {color} {noun2} beneath its branches. One day, a {name} stumbled upon the tree and made a wish that changed their {adjective5} life.")
        condition = False

    elif madlibs_choice == 9:
        MadLibs_text += "When [name] activated their grandfather's [adjective] time machine, their [plural noun] were accidentally transported to [era]. Amidst [adjective2] fashion and [adjective3] music, the pets found themselves in hilarious situations. The [adjective4] dog became a royal guard, the [adjective5] cat joined a [profession] club, and the [adjective6] parrot taught locals [slang term]. With each escapade, they brought laughter to the past."
        print(MadLibs_text)
        print("\nHere\'s your MadLibs text, please follow the instructions below to see the end results")
        name = input("Enter a name: ")
        adjective = input("Enter an adjective: ")
        plural_noun = input("Enter plural noun: ")
        era = input("Enter an era: ")
        adjective2 = input("Enter an adjective: ")
        adjective3 = input("Enter another adjective: ")
        adjective4 = input("Enter one more adjective: ")
        adjective5 = input("Enter another adjective: ")
        profession = input("Enter a profession: ")
        adjective6 = input("Enter one more adjective: ")
        slang_term = input("Enter a slang term: ")
        print(
            f"\nWhen {name} activated their grandfather's {adjective} time machine, their {plural_noun} were accidentally transported to {era}. Amidst {adjective2} fashion and {adjective3} music, the pets found themselves in hilarious situations. The {adjective4} dog became a royal guard, the {adjective5} cat joined a {profession}\'s club, and the {adjective6} parrot taught locals {slang_term}. With each escapade, they brought laughter to the past.")
        condition = False

    elif madlibs_choice == 10:
        MadLibs_text += "In the bustling intergalactic market of [planet name], traders bartered for [adjective] artifacts from distant galaxies. A [adjective2] merchant sold sparkling [color] [noun], while an [adjective3] alien offered jars of [adjective4] space jelly. Among the stalls, [name] found a mysterious [adjective5] amulet that whispered [verb] in [language]. Little did they know, it held the key to unlocking [adjective6] cosmic secrets."
        print(MadLibs_text)
        print("\nHere\'s your MadLibs text, please follow the instructions below to see the end results")
        planet_name = input("Enter a planet name: ")
        adjective = input("Enter an adjective: ")
        adjective2 = input("Enter another adjective: ")
        color = input("Enter a color: ")
        noun = input("Enter a noun: ")
        adjective3 = input("Enter one more adjective: ")
        adjective4 = input("Enter another adjective: ")
        name = input("Enter a name: ")
        adjective5 = input("Enter one more adjective: ")
        verb = input("Enter a verb: ")
        language = input("Enter a language: ")
        adjective6 = input("Enter one more adjective: ")
        print(
            f"\nIn the bustling intergalactic market of {planet_name}, traders bartered for {adjective} artifacts from distant galaxies. A {adjective2} merchant sold sparkling {color} {noun}, while an {adjective3} alien offered jars of {adjective4} space jelly. Among the stalls, {name} found a mysterious {adjective5} amulet that whispered {verb} in {language}. Little did they know, it held the key to unlocking {adjective6} cosmic secrets.")
        condition = False

    else:
        print("Incorrect Selection. Please type in a number between 1 and 10")
