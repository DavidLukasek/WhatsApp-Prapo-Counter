#   THIS FILE IS NOT INTENDED TO BE RUN BY CASUAL USERS

import prapo_file_reader as PrapoReader

replacements = {
    "+420 775 371 089" : "Sára Chrástová",
    "Sára 🖤" : "Sára Chrástová",
    "+420 732 549 516" : "Anna Buriánková",
    "Áňa" : "Anna Buriánková",
    "Anna Buriankova" : "Anna Buriánková",
    "+420 735 852 525" : "František Knitl",
    "Femda" : "František Knitl",
    "+420 733 617 629" : "Jan Roch",
    "Jan (H)Roch" : "Jan Roch",
    "+420 775 559 226" : "Lukáš Ptáčník",
    "Luky VŠE" : "Lukáš Ptáčník",
    "+420 602 284 723" : "Matylda Smolová",
    "Maty:" : "Matylda Smolová:",
    "Matylda Smolova" : "Matylda Smolová",
    "+420 601 365 884" : "Eliška Hrubošová",
    "Pæẞtę" : "Eliška Hrubošová",
    "+420 732 580 175" : "Kačka Buriánková",
    "Kačka Buriánková" : "Kačka Buriánková",
    "David DDI Lukášek" : "David DDI Lukášek",
    "+420 777 114 446" : "David DDI Lukášek",

    "+420 725 279 560" : "a",
    "+420 737 150 617" : "Anna K",
    "+420 739 128 455" : "Antonín Tesařík",
    "+420 775 246 822" : "barty",
    "+420 602 733 992" : "Daniela Poupová",
    "+420 721 551 848" : "Jakub Klazar",
    "+420 724 016 942" : "Jirka J",
    "+420 723 935 468" : "Klára Adamská",
    "+420 722 345 242" : "Magdaléna Dvořáková",
    "+420 705 400 298" : "Matěj Kándl",
    "+420 776 550 178" : "Ondra",
    "+420 702 076 603" : "T.A.",
    "+420 721 813 045" : "Vojta Kopecký",
    "+420 606 952 335" : "Dominik",
    "+420 732 180 588" : "Lada✨",
    "+420 774 968 544" : "Lukáš Hofman",
    "+420 608 110 939" : "Nari",

    "+420 739 479 544" : "Anet Špeldová",
    "+420 608 870 940" : "Matěj Damian",
    "+420 777 839 577" : "Eduard Tomas",
    "+420 605 939 682" : "Tadeáš Davídek",
    "+420 731 229 489" : "Martin Nejedlý",
    "+420 604 270 914" : "Filip Štambacher",
    "+420 730 627 116" : "Veronika Skopíková",
    "+420 776 236 361" : "Milan Pham",
    "+420 721 551 848" : "Kuba K.",
    "+420 731 148 264" : "Jiří Zlatuška",
    "+420 736 128 772" : "Bukai",
    "+420 607 789 995" : "Ondrej Ponechal",
    "+420 773 628 575" : "Antonín Bakoč",
    "+420 736 130 080" : "Kara",
    "+420 722 087 734" : "Jana",
    "+420 734 795 575" : "Kuba Luhan",
    "+420 731 406 871" : "Bára Listopadová",
    "+420 605 712 235" : "Marky Svobodová",
    "+420 774 063 751" : "Anička Mašlová",
    "+420 721 932 570" : "Marquetita 🔥",
    "+420 722 206 427" : "Adam P",
    "+420 775 960 789" : ":p",
    "+420 702 183 872" : "[any]",
    "+420 721 434 002" : "dave",
    "+420 776 459 991" : "Kája Novák",
    "+420 605 818 985" : "Lucie Šárová"
}

file_path = "prapo.txt"

messages = PrapoReader.read_file_lines(file_path)
new_messages = []

for message in messages:
    for old, new in replacements.items():
        message = message.replace(old, new)
    new_messages.append(message)

with open("prapotest.txt", "w", encoding="utf-8") as f:
    for message in new_messages:
        f.write(message + "\n")