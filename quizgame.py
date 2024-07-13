print("Welcome to my computer Quiz")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play: ")
score = 0

answer = input("what does CPU stands for? ")
if answer.lower() == "central processing unit":
    print('correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("what does mern stack stands for? ")
if answer.lower() == "mongoDb,express,react,nodejs":
    print('correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("what does AI and Ml stands for? ")
if answer.lower() == "Artifical Intelligence and Machine learning":
    print('correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does jvm stands for? ")
if answer.lower() == "java virtual machine":
    print('correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + "questions correct!")
print("You got " + str(((score)/4) * 100) + "%")


























