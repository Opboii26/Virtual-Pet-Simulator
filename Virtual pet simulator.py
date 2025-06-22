import random
import sys
import os


class Pet:
    def __init__(self):
        self.name = "Dennis"
        self.type = "Dog"
        self.hunger = 10
        self.health = 10
        self.energy = 10
        self.moods = ["Happy", "Sad", "Angry", "Annoyed", "Sick", "Hurt", "Sleepy", "Bored", "Hungry"]
        self.currentMood = ["Happy"]

    def feed(self):
        chance = random.random()
        if self.currentMood[0] == "Hungry":
            if chance < 0.7 and chance > 0.3:
                if self.hunger < 9:
                    self.hunger += 2
                    print(f"{self.name} is feeded! 😁")

                elif self.hunger == 9:
                    self.hunger += 1
                    print(f"{self.name} is feeded! 😁")

                else:
                    print(f"{self.name}'s belly is full!")

            elif chance <= 0.3:
                if self.hunger < 10:
                    self.hunger += 1
                    self.currentMood[0] = "Sick"
                    self.health -= 1
                    print(f"{self.name} gets sick by eating this food! 😢 Maybe it is expired!")

                else:
                    print(f"{self.name}'s belly is full!")

        else:
            print(f"{self.name} is not hungry! 😃")

        if self.currentMood[0] in ["Sick", "Hurt"]:
            response = input(f"{self.name} is {self.currentMood[0]}. Do you want to give medicine? (Yes/No): ").capitalize()
            if response == "Yes":
                if chance < 0.5:
                    self.currentMood[0] = "Happy"
                    print(f"{self.name} is cured! 😁")
                else:
                    print(f"{self.name} is still {self.currentMood[0]} 😢 Please try again.")

            elif response == "No":
                print(f"What! Don't you want to cure your {self.name}?")
            else:
                print("Please enter Yes or No!")

    def play(self):
        chance = random.random()
        if self.currentMood[0] not in ["Sick", "Hurt"]:
            self.currentMood[0] = "Happy"
            self.energy -= 2
            self.hunger -= 1
            print(f"{self.name} is very happy after playing with you! 😁")

        if chance < 0.2:
            self.health -= 3
            self.currentMood[0] = "Hurt"
            print(f"Oh no! {self.name} gets hurt! 😢")

    def sleep(self):
        if len(self.currentMood) > 1 and self.currentMood[1] == "Sleepy":
            if self.energy <= 5:
                self.energy = 10
            else:
                self.energy += 5

            if self.health < 10:
                self.health = 10

            self.currentMood.pop(1)
            print(f"{self.name} slept peacefully 😴")
        else:
            print(f"{self.name} does not want to sleep!")

    def status(self):
        print(f"Name: {self.name}\nType: {self.type}\nHealth: {self.health}\nEnergy: {self.energy}\nHunger: {self.hunger}")
        if len(self.currentMood) > 1:
            print(f"Mood: {self.currentMood[0]} and {self.name} is also {self.currentMood[1]}")
        else:
            print(f"Mood: {self.currentMood[0]}")


class GameManager:
    def __init__(self):
        self.pet = Pet()
        self.firstTimeSetup()
        # if os.path.exists("save_file.txt"):
        #     self.loadGame()
        # else:
        #     self.firstTimeSetup()

    def firstTimeSetup(self):
        print("Welcome to Virtual Pet Simulator!\n")
        ask = input("Start with Defualt / Custom / Load?\n: ").capitalize()

        if ask == "Default":
            print("Using default pet settings...")

        elif ask == "Custom":
            self.pet.name = input("Enter the name of your pet: ")
            self.pet.type = input("Enter the type of your pet: ")

        elif ask == "Load":
            if os.path.exists("save_file.txt"):
                self.loadGame()

            else:
                print("\nSave file not found!\n")
                self.firstTimeSetup()

        else:
            print("Invalid input. Starting with default pet.")

    def menu(self):
        while True:
            if self.pet.energy < 3 and "Sleepy" not in self.pet.currentMood:
                self.pet.currentMood.append("Sleepy")
                print(f"{self.pet.name} wants to sleep! 😴")

            if self.pet.hunger <= 3 and self.pet.currentMood[0] != "Hungry":
                self.pet.currentMood[0] = "Hungry"

            action = input("\nWhat do you want to do? (Feed / Play / Sleep / Status / Quit): ").capitalize()

            if action == "Feed":
                self.pet.feed()

            elif action == "Play":
                self.pet.play()

            elif action == "Sleep":
                self.pet.sleep()

            elif action == "Status":
                self.pet.status()

            elif action == "Quit":
                self.saveGame()
                print("Game Saved. Bye Bye! 🐾")
                sys.exit()
            else:
                print("Invalid option! Choose: Feed / Play / Sleep / Status / Quit")
            
            self.saveGame()

    def saveGame(self):
        with open("save_file.txt", "w") as save:
            save.write(f"{self.pet.name}\n")
            save.write(f"{self.pet.type}\n")
            save.write(f"{self.pet.hunger}\n")
            save.write(f"{self.pet.health}\n")
            save.write(f"{self.pet.energy}\n")
            save.write(",".join(self.pet.currentMood))

    def loadGame(self):
        with open("save_file.txt", "r") as save:
            data = save.readlines()
            self.pet.name = data[0].strip()
            self.pet.type = data[1].strip()
            self.pet.hunger = int(data[2].strip())
            self.pet.health = int(data[3].strip())
            self.pet.energy = int(data[4].strip())
            self.pet.currentMood = data[5].strip().split(",")
        print(f"\nSave file loaded! Welcome back, {self.pet.name} the {self.pet.type}!\n")


# 🚀 Let's run the game!
manager = GameManager()
manager.menu()