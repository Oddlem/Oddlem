# makin' a quiz
# plan: there will be TEN questions. And it'll be about how tough you are. Each question has 4 possible answers. Depending on how many TOUGH questions you get right, you get a TOUGH score. 
# 0 - 10 toughness, 11 - 40 toughness, 41 - 69 toughness, 70 - 90 toughness, 91 - 100 toughness
# total points: 10; each correct answer counts as 1 point

quizanswers = ["1", "2", "3", "4"]
userscore = 0
rightanswer1 = "1"
rightanswer2 = "2"
rightanswer3 = "3"
rightanswer4 = "4"
quizstart = "Start"


while True:
    userinput = input("~~~~~~~~~~~~~~~~~~~~~~~~~~~~     Welcome to the TOUGHNESS quiz!! SHOW ME HOW TOUGH YOU ARE.      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n(Type 'Start' to begin)\n\n\n")
    if not userinput == quizstart:
        print("JUST SAY START!!!!!!")
    else:
        print("It's... BEGUN!!!!!")
        break
while True:
    print("========= Question 1 =========")
    print("What do you eat for BREAKFAST in the MORNING\n")
    print("1. I eat NAILS for breakfast.\n")
    print("2. I eat cereal... :) LIKE A WIMP!!!\n")
    print("3. raw eggs.\n")
    print("4. I don't eat anything...\n")
    userinput = input("\nSelect your ANSWER!!!! SCUM\n\n")
    if not userinput in quizanswers:
        print("THAT'S... NOT!!! A VALID... ANSWER!!!!!!!!!!!!!!!!!!!!!!!!! twy again! :)")
        continue
    if userinput == rightanswer1:
        userscore += 1
    break
while True:
    print("========= Question 2 =========")
    print("What song do you LIKE the BEST?\n")
    print("1. ERmmm ermmmm... I don't listen to music.\n")
    print("2. My enemies' bones snapping.\n")
    print("3. Pop!\n")
    print("4. Game soundtrack.\n")
    userinput = input("\nSelect your ANSWER!!!! SCUM\n\n")
    if not userinput in quizanswers:
        print("THAT'S... NOT!!! A VALID... ANSWER!!!!!!!!!!!!!!!!!!!!!!!!! twy again! :)")
        continue
    if userinput == rightanswer2:
        userscore += 1
    break
while True:
    print("========= Question 3 =========")
    print("Do you like quizzes?\n")
    print("1. I LOVEEEE quizzessss!\n")
    print("2. I HATE QUIZZES.\n")
    print("3. I'm neutral about quizzes.\n")
    print("4. raw eggs\n")
    userinput = input("\nSelect your ANSWER!!!! SCUM\n\n")
    if not userinput in quizanswers:
        print("THAT'S... NOT!!! A VALID... ANSWER!!!!!!!!!!!!!!!!!!!!!!!!! twy again! :)")
        continue
    if userinput == rightanswer2:
        userscore += 1
    break
while True:
    print("========= Question 4 =========")
    print("What car do you drive?\n")
    print("1. A TANK.\n")
    print("2. A normal car.\n")
    print("3. I don't drive... :(\n")
    print("4. I break into other peoples' cars.\n")
    userinput = input("\nSelect your ANSWER!!!! SCUM\n\n")
    if not userinput in quizanswers:
        print("THAT'S... NOT!!! A VALID... ANSWER!!!!!!!!!!!!!!!!!!!!!!!!! twy again! :)")
        continue
    if userinput == rightanswer1:
        userscore += 1
    break
while True:
    print("========= Question 5 =========")
    print("How many pushups can you do?\n")
    print("1. Zero, I'M WEAK!!!\n")
    print("2. Maybe 20?\n")
    print("3. 40! Confidently!\n")
    print("4. If I do a pushup... the WORLD will explode cause I'm so strong. \n")
    userinput = input("\nSelect your ANSWER!!!! SCUM\n\n")
    if not userinput in quizanswers:
        print("THAT'S... NOT!!! A VALID... ANSWER!!!!!!!!!!!!!!!!!!!!!!!!! twy again! :)")
        continue
    if userinput == rightanswer4:
        userscore += 1
    break
while True:
    print("========= Question 6 =========")
    print("What are your hobbies?\n")
    print("1. Rock climbing.\n")
    print("2. Shooting an RPG-28.\n")
    print("3. Doing jigsaw puzzles.\n")
    print("4. Jogging.\n")
    userinput = input("\nSelect your ANSWER!!!! SCUM\n\n")
    if not userinput in quizanswers:
        print("THAT'S... NOT!!! A VALID... ANSWER!!!!!!!!!!!!!!!!!!!!!!!!! twy again! :)")
        continue
    if userinput == rightanswer2:
        userscore += 1
    break
while True:
    print("========= Question 7 =========")
    print("What PETS do you own?\n")
    print("1. NONE!!!\n")
    print("2. Cat(s).\n")
    print("3. Dog(s).\n")
    print("4. My enemies.\n")
    userinput = input("\nSelect your ANSWER!!!! SCUM\n\n")
    if not userinput in quizanswers:
        print("THAT'S... NOT!!! A VALID... ANSWER!!!!!!!!!!!!!!!!!!!!!!!!! twy again! :)")
        continue
    if userinput == rightanswer4:
        userscore += 1
    break
while True:
    print("========= Question 8 =========")
    print("What's the meaning of life?\n")
    print("1. To have a happy and satisfying time on Earth.\n")
    print("2. WAR!!!!!\n")
    print("3. raw eggs.\n")
    print("4. Ermmm ummm never thought about it!!\n")
    userinput = input("\nSelect your ANSWER!!!! SCUM\n\n")
    if not userinput in quizanswers:
        print("THAT'S... NOT!!! A VALID... ANSWER!!!!!!!!!!!!!!!!!!!!!!!!! twy again! :)")
        continue
    if userinput == rightanswer2:
        userscore += 1
    break
while True:
    print("========= Question 9 =========")
    print("Hmmm\n")
    print("1. Excuse me?\n")
    print("2. Hmmmm?\n")
    print("3. SPEAK UP I CAN'T HEAR YOU!!!!!!\n")
    print("4. ...What?\n")
    userinput = input("\nSelect your ANSWER!!!! SCUM\n\n")
    if not userinput in quizanswers:
        print("THAT'S... NOT!!! A VALID... ANSWER!!!!!!!!!!!!!!!!!!!!!!!!! twy again! :)")
        continue
    if userinput == rightanswer3:
        userscore += 1
    break
while True:
    print("========= Question 10 =========")
    print("Do you like meeeee? :)\n")
    print("1. NO. I HATE YOU.\n")
    print("2. Yea!\n")
    print("3. Sorry I was distracted what did you say?\n")
    print("4. -stare longingly into the scary sargent's eyes and twirl your hair around like a schoolgirl-\n")
    userinput = input("\nSelect your ANSWER!!!! SCUM\n\n")
    if not userinput in quizanswers:
        print("THAT'S... NOT!!! A VALID... ANSWER!!!!!!!!!!!!!!!!!!!!!!!!! twy again! :)")
        continue
    if userinput == rightanswer1:
        userscore += 1
    break

print("Very good!!! Um.. s-sSARGENT. Here's your score!!! :)")
print("======================================================")

percentage = 100 * userscore/10
print(percentage)
if percentage <= 10:
    print("Absolutely disgusting. You might as well be A SLUG.")
elif percentage <= 25:
    print("You're actually REALLY weak... REALLY weak!! MADE OF GLASS!!!!!")
elif percentage <= 50:
    print("Decent... maybe drink more milk and you can get buff like ME.")
elif percentage <= 75:
    print("...Yes very good. You're clearly pretty tough, but there's room for improvement.")
elif percentage <= 85:
    print("EXCELENT!! You, sir, are tough.")
elif percentage <= 100:
    print("You're the peak of human evolution, incredible.")

    # else:
    #     print("LAST QUESTION!!!!")
    #     print("Do you like meee? :)")
    #     print("1. Yeaaaa!\n")
    #     print("2. Noooo.....\n")
    #     print("3. Stare and smile but say nothing\n")
    #     print("4. RIP the general's head off\n")
    #     if userinput == rightanswer4:
    #         userscore += 1
    #         break