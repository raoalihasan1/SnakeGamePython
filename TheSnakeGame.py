# The Screen Resolution For My Game Is 1366x768
from tkinter import *
from tkinter import messagebox
import os
import random

LightMode = True
GameEnd = False
GameIsPaused = False
BossHere = False
TempScore = 0
GameDifficulty = "Medium"
KeyControls = "Arrow Keys"
CheatCodeScore = False
CheatCodeSpeed = False
CheatCodeSpike = False
NewGame = True
X = 0

# This Function Is Used To Change The Colours And Design of The Layout
# When the User Toggles The Button To Change Between Light And Dark Mode


def DarkLightMode():
    global LightMode
    if LightMode:
        Theme.config(text="Dark Mode: ON", bg="#F5F5F5",
                     activebackground="#C4C4C4", activeforeground="#181818",
                     highlightbackground="#EBECF0", fg="#313131",
                     highlightthickness=2)
        MainScreen.itemconfig(BackgroundImage, image=BackgroundNight)
        MainScreen.itemconfig(Heading, fill="#EBECF0")
        PlayButton.config(bg="#0492C2", activebackground="#0047AB",
                          activeforeground="#FFFEF2",
                          highlightbackground="#EBECF0",
                          fg="#EBECF0", highlightthickness=3)
        LoadButton.config(bg="#0492C2", activebackground="#0047AB",
                          activeforeground="#FFFEF2",
                          highlightbackground="#EBECF0",
                          fg="#EBECF0", highlightthickness=3)
        LeaderBoard.config(bg="#0492C2", activebackground="#0047AB",
                           activeforeground="#FFFEF2",
                           highlightbackground="#EBECF0",
                           fg="#EBECF0", highlightthickness=3)
        ExitGame.config(bg="#D1350D", activebackground="#BF0000",
                        activeforeground="#FFFEF2",
                        highlightbackground="#EBECF0",
                        fg="#EBECF0", highlightthickness=3)
        PauseButton.config(bg="#D1350D", activebackground="#BF0000",
                           activeforeground="#FFFEF2",
                           highlightbackground="#EBECF0",
                           fg="#EBECF0", highlightthickness=3)
        ExitButton.config(bg="#D1350D", activebackground="#BF0000",
                          activeforeground="#FFFEF2",
                          highlightbackground="#EBECF0", fg="#EBECF0")
        ResumeButton.config(bg="#0096FF", activebackground="#0047AB",
                            activeforeground="#FFFEF2",
                            highlightbackground="#EBECF0", fg="#EBECF0")
        SaveGame.config(bg="#0096FF", activebackground="#0047AB",
                        activeforeground="#FFFEF2",
                        highlightbackground="#EBECF0", fg="#EBECF0")
        MainMenuButton.config(bg="#0096FF", activebackground="#0047AB",
                              activeforeground="#FFFEF2",
                              highlightbackground="#EBECF0", fg="#EBECF0")
        GameCanvas.itemconfig(HighScore, fill="#18A558")
        GameTimer.config(bg="#020408")
        PauseFrame.config(bg="#020408")
        Countdown.config(bg="#020408", fg="#EBECF0")
        GameCanvas.config(bg="#020408")
        CurrentScore.config(bg="#020408", fg="#EBECF0")
        GameCanvas.itemconfig(PrintScore, fill="#EBECF0")
        PauseButton.config(bg="#D1350D", activebackground="#BF0000",
                           activeforeground="#FFFEF2",
                           highlightbackground="#EBECF0", fg="#EBECF0")
        LightMode = False
    else:
        Theme.config(text="Dark Mode: OFF", bg="#313131",
                     activebackground="#181818", fg="#F5F5F5",
                     activeforeground="#C4C4C4", highlightthickness=2,
                     highlightbackground="#181818")
        MainScreen.itemconfig(BackgroundImage, image=BackgroundDay)
        MainScreen.itemconfig(Heading, fill="#020408")
        PlayButton.config(bg="#C5C5C5", activebackground="#AEAEAE",
                          activeforeground="#000000",
                          highlightbackground="#2B2B2B", fg="#2B2B2B")
        LoadButton.config(bg="#C5C5C5", activebackground="#AEAEAE",
                          activeforeground="#000000",
                          highlightbackground="#2B2B2B", fg="#2B2B2B")
        LeaderBoard.config(bg="#C5C5C5", activebackground="#AEAEAE",
                           activeforeground="#000000",
                           highlightbackground="#2B2B2B", fg="#2B2B2B")
        ExitGame.config(bg="#C5C5C5", activebackground="#AEAEAE",
                        activeforeground="#000000",
                        highlightbackground="#2B2B2B", fg="#2B2B2B")
        PauseButton.config(bg="#C5C5C5", activebackground="#AEAEAE",
                           activeforeground="#000000",
                           highlightbackground="#2B2B2B", fg="#2B2B2B")
        ResumeButton.config(bg="#3DED97", activebackground="#345414",
                            activeforeground="#000000",
                            highlightbackground="#2B2B2B", fg="#2B2B2B")
        SaveGame.config(bg="#3DED97", activebackground="#345414",
                        activeforeground="#000000",
                        highlightbackground="#2B2B2B", fg="#2B2B2B")
        ExitButton.config(bg="#fe612c", activebackground="#fd3a2d",
                          activeforeground="#000000",
                          highlightbackground="#2B2B2B", fg="#2B2B2B")
        MainMenuButton.config(bg="#3DED97", activebackground="#345414",
                              activeforeground="#000000",
                              highlightbackground="#2B2B2B", fg="#2B2B2B")
        GameCanvas.itemconfig(HighScore, fill="#21B6A8")
        GameTimer.config(bg="#EBECF0")
        PauseFrame.config(bg="#EBECF0")
        Countdown.config(bg="#EBECF0", fg="#020408")
        GameCanvas.config(bg="#EBECF0")
        GameCanvas.itemconfig(PrintScore, fill="#020408")
        CurrentScore.config(bg="#EBECF0", fg="#020408")
        PauseButton.config(bg="#C5C5C5", activebackground="#AEAEAE",
                           activeforeground="#000000",
                           highlightbackground="#2B2B2B", fg="#2B2B2B")
        LightMode = True

# Loads The File Where The Saved Game Is Stored And Assigns The Values
# To The Variables From The Text File Which Contains The Saved Game


def LoadSavedGame():
    global NewGame, Score, GameDifficulty, KeyControls, SnakeSize
    if not os.path.isfile("SnakeGameSaved.txt"):
        messagebox.showerror("No Saved Games", "No Games Have Been Saved!")
    else:
        with open("SnakeGameSaved.txt", "r") as SavedGameFile:
            for Line in SavedGameFile:
                if Line != "":
                    NewGame = False
                    Score, GameDifficulty, KeyControls, SnakeSize = Line.split("|")
                    SnakeSize = int(SnakeSize)
        ChangeToTimer()

# Function Used To Place A Poison That Kills The Snake 
# If It Collides With The Snake (Only Placed In Hard Mode)


def PlacePoison():
    global Poison, PoisonX, PoisonY
    Poison = GameCanvas.create_oval(0, 0, SnakeSize, SnakeSize, fill="#F00", outline="#F00")
    PoisonX = random.randint(125, (GAMECANVASWIDTH-75)-SnakeSize)
    PoisonY = random.randint(100, (GAMECANVASHEIGHT-75)-SnakeSize)
    GameCanvas.move(Poison, PoisonX, PoisonY)


# Function Used To Place The Snakes Food On The Canvas


def PlaceOrange():
    global Orange, OrangeX, OrangeY
    if GameDifficulty == "Hard":
        global Poison, PoisonX, PoisonY
        Orange = GameCanvas.create_oval(0, 0, SnakeSize, SnakeSize, fill="#FF8000", outline="#FF8000")
        OrangeX = random.randint(125, (GAMECANVASWIDTH-75)-SnakeSize)
        OrangeY = random.randint(100, (GAMECANVASHEIGHT-75)-SnakeSize)
        if PoisonX == OrangeX or PoisonY == OrangeY or PoisonX == (OrangeX + 50) or PoisonX == (OrangeX - 50) or PoisonY == (OrangeY + 50) or PoisonY == (OrangeY - 50):
            PlaceOrange()
        else:
            GameCanvas.move(Orange, OrangeX, OrangeY)
    else:
        Orange = GameCanvas.create_oval(0, 0, SnakeSize, SnakeSize, fill="#FF8000", outline="#FF8000")
        OrangeX = random.randint(125, (GAMECANVASWIDTH-75)-SnakeSize)
        OrangeY = random.randint(100, (GAMECANVASHEIGHT-75)-SnakeSize)
        GameCanvas.move(Orange, OrangeX, OrangeY)

# Binds Left Key To The Left Direction For Snake To Move


def Left(Event):
    global ChangeDirection, KeyControls
    if KeyControls == "Arrow Keys":
        ChangeDirection = "left"
    else:
        ChangeDirection = "a"

# Binds Right Key To The Right Direction For Snake To Move


def Right(Event):
    global ChangeDirection, KeyControls
    if KeyControls == "Arrow Keys":
        ChangeDirection = "right"
    else:
        ChangeDirection = "d"

# Binds Up Key To The Up Direction For Snake To Move


def Up(Event):
    global ChangeDirection, KeyControls
    if KeyControls == "Arrow Keys":
        ChangeDirection = "up"
    else:
        ChangeDirection = "w"

# Binds Down Key To The Down Direction For Snake To Move


def Down(Event):
    global ChangeDirection, KeyControls
    if KeyControls == "Arrow Keys":
        ChangeDirection = "down"
    else:
        ChangeDirection = "s"

# Used To Grow The Size Of The Snake When The Snake Eats An Orange
# And Gives A Colour Scheme To The Snake As It Grows To Give It A Good Look


def GrowSnakeSize():
    global Score, HighScore, Highest, TempScore, CheatCodeScore
    LastElement = len(Snake)-1
    LastElementPosition = GameCanvas.coords(Snake[LastElement])
    if LightMode:
        if LastElement < 4:
            Snake.append(GameCanvas.create_rectangle
                         (0, 0, SnakeSize, SnakeSize,
                          fill="#2AF598", outline="#2AF598"))
        elif LastElement >= 4 and LastElement < 8:
            Snake.append(GameCanvas.create_rectangle
                         (0, 0, SnakeSize, SnakeSize,
                          fill="#22E4AC", outline="#22E4AC"))
        elif LastElement >= 8 and LastElement < 12:
            Snake.append(GameCanvas.create_rectangle
                         (0, 0, SnakeSize, SnakeSize,
                          fill="#1BD7BB", outline="#1BD7BB"))
        elif LastElement >= 12 and LastElement < 16:
            Snake.append(GameCanvas.create_rectangle
                         (0, 0, SnakeSize, SnakeSize,
                          fill="#14C9CB", outline="#14C9CB"))
        elif LastElement >= 16 and LastElement < 20:
            Snake.append(GameCanvas.create_rectangle
                         (0, 0, SnakeSize, SnakeSize,
                          fill="#0FBED8", outline="#0FBED8"))
        elif LastElement >= 20 and LastElement < 24:
            Snake.append(GameCanvas.create_rectangle
                         (0, 0, SnakeSize, SnakeSize,
                          fill="#08B4E5", outline="#08B4E5"))
        elif LastElement >= 24 and LastElement < 28:
            Snake.append(GameCanvas.create_rectangle
                         (0, 0, SnakeSize, SnakeSize,
                          fill="#0FBED8", outline="#0FBED8"))
        elif LastElement >= 28 and LastElement < 32:
            Snake.append(GameCanvas.create_rectangle
                         (0, 0, SnakeSize, SnakeSize,
                          fill="#14C9CB", outline="#14C9CB"))
        elif LastElement >= 32 and LastElement < 36:
            Snake.append(GameCanvas.create_rectangle
                         (0, 0, SnakeSize, SnakeSize,
                          fill="#1BD7BB", outline="#1BD7BB"))
        elif LastElement >= 36 and LastElement < 40:
            Snake.append(GameCanvas.create_rectangle
                         (0, 0, SnakeSize, SnakeSize,
                          fill="#22E4AC", outline="#22E4AC"))
        else:
            Snake.append(GameCanvas.create_rectangle
                         (0, 0, SnakeSize, SnakeSize,
                          fill="#2AF598", outline="#2AF598"))
    else:
        if LastElement < 4:
            Snake.append(GameCanvas.create_rectangle
                         (0, 0, SnakeSize, SnakeSize,
                          fill="#C13126", outline="#C13126"))
        elif LastElement >= 4 and LastElement < 8:
            Snake.append(GameCanvas.create_rectangle
                         (0, 0, SnakeSize, SnakeSize,
                          fill="#CE3B2B", outline="#CE3B2B"))
        elif LastElement >= 8 and LastElement < 12:
            Snake.append(GameCanvas.create_rectangle
                         (0, 0, SnakeSize, SnakeSize,
                          fill="#ED3F36", outline="#ED3F36"))
        elif LastElement >= 12 and LastElement < 16:
            Snake.append(GameCanvas.create_rectangle
                         (0, 0, SnakeSize, SnakeSize,
                          fill="#EF4C3B", outline="#EF4C3B"))
        elif LastElement >= 16 and LastElement < 20:
            Snake.append(GameCanvas.create_rectangle
                         (0, 0, SnakeSize, SnakeSize,
                          fill="#F15D43", outline="#F15D43"))
        elif LastElement >= 20 and LastElement < 24:
            Snake.append(GameCanvas.create_rectangle
                         (0, 0, SnakeSize, SnakeSize,
                          fill="#E07765", outline="#E07765"))
        elif LastElement >= 24 and LastElement < 28:
            Snake.append(GameCanvas.create_rectangle
                         (0, 0, SnakeSize, SnakeSize,
                          fill="#F15D43", outline="#F15D43"))
        elif LastElement >= 28 and LastElement < 32:
            Snake.append(GameCanvas.create_rectangle
                         (0, 0, SnakeSize, SnakeSize,
                          fill="#EF4C3B", outline="#EF4C3B"))
        elif LastElement >= 32 and LastElement < 36:
            Snake.append(GameCanvas.create_rectangle
                         (0, 0, SnakeSize, SnakeSize,
                          fill="#ED3F36", outline="#ED3F36"))
        elif LastElement >= 36 and LastElement < 40:
            Snake.append(GameCanvas.create_rectangle
                         (0, 0, SnakeSize, SnakeSize,
                          fill="#CE3B2B", outline="#CE3B2B"))
        else:
            Snake.append(GameCanvas.create_rectangle
                         (0, 0, SnakeSize, SnakeSize,
                          fill="#C13126", outline="#C13126"))

    if(ChangeDirection == "left"):
        GameCanvas.coords(Snake[LastElement+1],
                          LastElementPosition[0]+SnakeSize,
                          LastElementPosition[1],
                          LastElementPosition[2]+SnakeSize,
                          LastElementPosition[3])
    elif(ChangeDirection == "right"):
        GameCanvas.coords(Snake[LastElement+1],
                          LastElementPosition[0]-SnakeSize,
                          LastElementPosition[1],
                          LastElementPosition[2]-SnakeSize,
                          LastElementPosition[3])
    elif(ChangeDirection == "up"):
        GameCanvas.coords(Snake[LastElement+1],
                          LastElementPosition[0],
                          LastElementPosition[1]+SnakeSize,
                          LastElementPosition[2],
                          LastElementPosition[3]+SnakeSize)
    else:
        GameCanvas.coords(Snake[LastElement+1],
                          LastElementPosition[0],
                          LastElementPosition[1]-SnakeSize,
                          LastElementPosition[2],
                          LastElementPosition[3]-SnakeSize)

    Score = int(Score)

    if CheatCodeScore:
        Score += 3
    else:
        Score += 1
    TempScore = Score

    ScoreRecorder = "Score: " + str(Score)
    GameCanvas.itemconfig(PrintScore, text=ScoreRecorder)

    if "Highest" in globals():
        Highest = int(Highest)
    else:
        Highest = 0

    if Score > Highest:
        GameCanvas.itemconfig(PrintScore, text="")
        NewHighScore = "New High Score: " + str(Score)
        GameCanvas.itemconfig(HighScore, text=NewHighScore)

# Used To Move The Orange On The Canvas After It Is Eaten By The Snake


def MoveOrange():
    global Orange, OrangeX, OrangeY
    if GameDifficulty == "Hard":
        global Poison, PoisonX, PoisonY
        GameCanvas.move(Orange, (OrangeX*(-1)), (OrangeY*(-1)))
        OrangeX = random.randint(125, (GAMECANVASWIDTH-75)-SnakeSize)
        OrangeY = random.randint(100, (GAMECANVASHEIGHT-75)-SnakeSize)
        if PoisonX == OrangeX or PoisonY == OrangeY or PoisonX == (OrangeX + 50) or PoisonX == (OrangeX - 50) or PoisonY == (OrangeY + 50) or PoisonY == (OrangeY - 50):
            MoveOrange()
        else:
            GameCanvas.move(Orange, OrangeX, OrangeY)
    else:
        GameCanvas.move(Orange, (OrangeX*(-1)), (OrangeY*(-1)))
        OrangeX = random.randint(125, (GAMECANVASWIDTH-75)-SnakeSize)
        OrangeY = random.randint(100, (GAMECANVASHEIGHT-75)-SnakeSize)
        GameCanvas.move(Orange, OrangeX, OrangeY)

# Checks If There Is A Collision Between The Snake
# And Another Object e.g. The Orange Or The Screen Edge


def CollisionDetection(CoordinateA, CoordinateB):
    if (CoordinateA[0] < CoordinateB[2] and
        CoordinateA[2] > CoordinateB[0] and
        CoordinateA[1] < CoordinateB[3] and
        CoordinateA[3] > CoordinateB[1]):
        return True
    return False

# Used To Move The Snake Around The Canvas As The User Changes
# Directions And End The Game If There Is A Collision Between
# The Snake And The Screen Edge Or Eat The Orange And Increment The Score


def MoveSnake():
    global GameIsPaused, GameEnd, ChangeDirection, LightMode
    global GameDifficulty, KeyControls, BossHere, CheatCodeSpeed
    global Poison, NewGame, X

    if NewGame:
        if ((len(Snake) == 0) and (LightMode is False)):
            Snake.append(GameCanvas.create_rectangle
                         (SnakeSize, SnakeSize, SnakeSize * 2,
                          SnakeSize * 2, fill="#C13126",
                          outline="#C13126"))
        elif ((len(Snake) == 0) and LightMode):
            Snake.append(GameCanvas.create_rectangle
                         (SnakeSize, SnakeSize, SnakeSize * 2,
                          SnakeSize * 2, fill="#2AF598",
                          outline="#2AF598"))
    else:
        GameScore = int(Score)
        GameCanvas.itemconfig(PrintScore, text="Score: " + str(GameScore))
        while X != GameScore:
            if LightMode:
                if X < 4:
                    Snake.append(GameCanvas.create_rectangle
                                 (SnakeSize, SnakeSize, SnakeSize * 2,
                                  SnakeSize * 2, fill="#2AF598",
                                  outline="#2AF598"))
                elif X >= 4 and X < 8:
                    Snake.append(GameCanvas.create_rectangle
                                 (SnakeSize, SnakeSize, SnakeSize * 2,
                                  SnakeSize * 2, fill="#22E4AC",
                                  outline="#22E4AC"))
                elif X >= 8 and X < 12:
                    Snake.append(GameCanvas.create_rectangle
                                 (SnakeSize, SnakeSize, SnakeSize * 2,
                                  SnakeSize * 2, fill="#1BD7BB",
                                  outline="#1BD7BB"))
                elif X >= 12 and X < 16:
                    Snake.append(GameCanvas.create_rectangle
                                 (SnakeSize, SnakeSize, SnakeSize * 2,
                                  SnakeSize * 2, fill="#14C9CB",
                                  outline="#14C9CB"))
                elif X >= 16 and X < 20:
                    Snake.append(GameCanvas.create_rectangle
                                 (SnakeSize, SnakeSize, SnakeSize * 2,
                                  SnakeSize * 2, fill="#0FBED8",
                                  outline="#0FBED8"))
                elif X >= 20 and X < 24:
                    Snake.append(GameCanvas.create_rectangle
                                 (SnakeSize, SnakeSize, SnakeSize * 2,
                                  SnakeSize * 2, fill="#08B4E5",
                                  outline="#08B4E5"))
                elif X >= 24 and X < 28:
                    Snake.append(GameCanvas.create_rectangle
                                 (SnakeSize, SnakeSize, SnakeSize * 2,
                                  SnakeSize * 2, fill="#0FBED8",
                                  outline="#0FBED8"))
                elif X >= 28 and X < 32:
                    Snake.append(GameCanvas.create_rectangle
                                 (SnakeSize, SnakeSize, SnakeSize * 2,
                                  SnakeSize * 2, fill="#14C9CB",
                                  outline="#14C9CB"))
                elif X >= 32 and X < 36:
                    Snake.append(GameCanvas.create_rectangle
                                 (SnakeSize, SnakeSize, SnakeSize * 2,
                                  SnakeSize * 2, fill="#1BD7BB",
                                  outline="#1BD7BB"))
                elif X >= 36 and X < 40:
                    Snake.append(GameCanvas.create_rectangle
                                 (SnakeSize, SnakeSize, SnakeSize * 2,
                                  SnakeSize * 2, fill="#22E4AC",
                                  outline="#22E4AC"))
                else:
                    Snake.append(GameCanvas.create_rectangle
                                 (SnakeSize, SnakeSize, SnakeSize * 2,
                                  SnakeSize * 2, fill="#2AF598",
                                  outline="#2AF598"))
            else:
                if X < 4:
                    Snake.append(GameCanvas.create_rectangle
                                 (SnakeSize, SnakeSize, SnakeSize * 2,
                                  SnakeSize * 2, fill="#C13126",
                                  outline="#C13126"))
                elif X >= 4 and X < 8:
                    Snake.append(GameCanvas.create_rectangle
                                 (SnakeSize, SnakeSize, SnakeSize * 2,
                                  SnakeSize * 2, fill="#CE3B2B",
                                  outline="#CE3B2B"))
                elif X >= 8 and X < 12:
                    Snake.append(GameCanvas.create_rectangle
                                 (SnakeSize, SnakeSize, SnakeSize * 2,
                                  SnakeSize * 2, fill="#ED3F36",
                                  outline="#ED3F36"))
                elif X >= 12 and X < 16:
                    Snake.append(GameCanvas.create_rectangle
                                 (SnakeSize, SnakeSize, SnakeSize * 2,
                                  SnakeSize * 2, fill="#EF4C3B",
                                  outline="#EF4C3B"))
                elif X >= 16 and X < 20:
                    Snake.append(GameCanvas.create_rectangle
                                 (SnakeSize, SnakeSize, SnakeSize * 2,
                                  SnakeSize * 2, fill="#F15D43",
                                  outline="#F15D43"))
                elif X >= 20 and X < 24:
                    Snake.append(GameCanvas.create_rectangle
                                 (SnakeSize, SnakeSize, SnakeSize * 2,
                                  SnakeSize * 2, fill="#E07765",
                                  outline="#E07765"))
                elif X >= 24 and X < 28:
                    Snake.append(GameCanvas.create_rectangle
                                 (SnakeSize, SnakeSize, SnakeSize * 2,
                                  SnakeSize * 2, fill="#F15D43",
                                  outline="#F15D43"))
                elif X >= 28 and X < 32:
                    Snake.append(GameCanvas.create_rectangle
                                 (SnakeSize, SnakeSize, SnakeSize * 2,
                                  SnakeSize * 2, fill="#EF4C3B",
                                  outline="#EF4C3B"))
                elif X >= 32 and X < 36:
                    Snake.append(GameCanvas.create_rectangle
                                 (SnakeSize, SnakeSize, SnakeSize * 2,
                                  SnakeSize * 2, fill="#ED3F36",
                                  outline="#ED3F36"))
                elif X >= 36 and X < 40:
                    Snake.append(GameCanvas.create_rectangle
                                 (SnakeSize, SnakeSize, SnakeSize * 2,
                                  SnakeSize * 2, fill="#CE3B2B",
                                  outline="#CE3B2B"))
                else:
                    Snake.append(GameCanvas.create_rectangle
                                 (SnakeSize, SnakeSize, SnakeSize * 2,
                                  SnakeSize * 2, fill="#C13126",
                                  outline="#C13126"))
            X += 1
        if KeyControls == "Arrow Keys":
            ChangeDirection = "down"
        else:
            ChangeDirection = "s"
        NewGame = True

    GameCanvas.pack()
    Position = []
    Position.append(GameCanvas.coords(Snake[0]))

    if GameDifficulty == "Easy":
        if Position[0][0] < 0:
            GameCanvas.coords(Snake[0], GAMECANVASWIDTH, Position[0][1],
                              GAMECANVASWIDTH-SnakeSize, Position[0][3])
        elif Position[0][2] > GAMECANVASWIDTH:
            GameCanvas.coords(Snake[0], 0-SnakeSize,
                              Position[0][1], 0, Position[0][3])
        elif Position[0][3] > GAMECANVASHEIGHT:
            GameCanvas.coords(Snake[0], Position[0][0],
                              0-SnakeSize, Position[0][2], 0)
        elif Position[0][1] < 0:
            GameCanvas.coords(Snake[0], Position[0][0],
                              GAMECANVASHEIGHT, Position[0][2],
                              GAMECANVASHEIGHT-SnakeSize)
    else:
        if (Position[0][0] < 0 or
            Position[0][2] > GAMECANVASWIDTH or
            Position[0][3] > GAMECANVASHEIGHT or
            Position[0][1] < 0):
            GameEnd = True

    Position.clear()
    Position.append(GameCanvas.coords(Snake[0]))

    if BossHere:
            BossFrame.pack(expand=1, fill="both")
            GameFrame.forget()
            HideGameCanvas = Canvas(BossFrame, width=GAMECANVASWIDTH,
                                    height=GAMECANVASHEIGHT)
            HideGameCanvas.pack()
            HideGameCanvas.create_image(0, 0, image=BossImage, anchor="nw")

    if not GameIsPaused and not BossHere:
        if KeyControls == "Arrow Keys":
            GameCanvas.bind("<Left>", Left)
            GameCanvas.bind("<Right>", Right)
            GameCanvas.bind("<Up>", Up)
            GameCanvas.bind("<Down>", Down)
            if ChangeDirection == "left":
                GameCanvas.move(Snake[0], -SnakeSize, 0)
            elif ChangeDirection == "right":
                GameCanvas.move(Snake[0], SnakeSize, 0)
            elif ChangeDirection == "up":
                GameCanvas.move(Snake[0], 0, -SnakeSize)
            elif ChangeDirection == "down":
                GameCanvas.move(Snake[0], 0, SnakeSize)
        else:
            GameCanvas.bind("<a>", Left)
            GameCanvas.bind("<d>", Right)
            GameCanvas.bind("<w>", Up)
            GameCanvas.bind("<s>", Down)
            if ChangeDirection == "a":
                GameCanvas.move(Snake[0], -SnakeSize, 0)
            elif ChangeDirection == "d":
                GameCanvas.move(Snake[0], SnakeSize, 0)
            elif ChangeDirection == "w":
                GameCanvas.move(Snake[0], 0, -SnakeSize)
            elif ChangeDirection == "s":
                GameCanvas.move(Snake[0], 0, SnakeSize)

        HeadPosition = GameCanvas.coords(Snake[0])
        OrangePosition = GameCanvas.coords(Orange)

        if GameDifficulty == "Hard":
            if CheatCodeSpike:
                pass
            else:
                PoisonPosition = GameCanvas.coords(Poison)
                if CollisionDetection(HeadPosition, PoisonPosition):
                    GameEnd = True

        if CollisionDetection(HeadPosition, OrangePosition):
            MoveOrange()
            GrowSnakeSize()

        for i in range(1, len(Snake)):
            if CollisionDetection(HeadPosition, GameCanvas.coords(Snake[i])):
                GameEnd = True

        for i in range(1, len(Snake)):
            Position.append(GameCanvas.coords(Snake[i]))

        for i in range(len(Snake)-1):
            GameCanvas.coords(Snake[i+1], Position[i][0],
                              Position[i][1], Position[i][2], Position[i][3])

    if GameEnd:
        if LightMode:
            GameCanvas.config(bg="#8B0000")
            GameCanvas.itemconfig(PrintScore, fill="#FFF")
            GameCanvas.create_text((GAMECANVASWIDTH/2)-52.5,
                                   (GAMECANVASHEIGHT/2)-22.5, fill="white",
                                   font="Consolas 120 bold",
                                   text=("GAME OVER"))
            GameTimer.after(1250, ChangeToEnd)
        else:
            GameCanvas.config(bg="#2A2D43")
            GameCanvas.create_text((GAMECANVASWIDTH/2)-52.5,
                                   (GAMECANVASHEIGHT/2)-22.5, fill="white",
                                   font="Consolas 120 bold",
                                   text=("GAME OVER"))
            GameTimer.after(1250, ChangeToEnd)
    else:
        if not CheatCodeSpeed:
            if GameDifficulty == "Easy":
                if ((len(Snake)-1) < 4):
                    GameFrame.after(70, MoveSnake)
                elif ((len(Snake)-1) >= 4 and (len(Snake)-1) < 8):
                    GameFrame.after(65, MoveSnake)
                elif ((len(Snake)-1) >= 8 and (len(Snake)-1) < 12):
                    GameFrame.after(60, MoveSnake)
                elif ((len(Snake)-1) >= 12 and (len(Snake)-1) < 16):
                    GameFrame.after(55, MoveSnake)
                elif ((len(Snake)-1) >= 16 and (len(Snake)-1) < 20):
                    GameFrame.after(50, MoveSnake)
                elif ((len(Snake)-1) >= 20 and (len(Snake)-1) < 24):
                    GameFrame.after(45, MoveSnake)
                else:
                    GameFrame.after(42, MoveSnake)
            elif GameDifficulty == "Medium":
                if ((len(Snake)-1) < 4):
                    GameFrame.after(65, MoveSnake)
                elif ((len(Snake)-1) >= 4 and (len(Snake)-1) < 8):
                    GameFrame.after(60, MoveSnake)
                elif ((len(Snake)-1) >= 8 and (len(Snake)-1) < 12):
                    GameFrame.after(55, MoveSnake)
                elif ((len(Snake)-1) >= 12 and (len(Snake)-1) < 16):
                    GameFrame.after(50, MoveSnake)
                elif ((len(Snake)-1) >= 16 and (len(Snake)-1) < 20):
                    GameFrame.after(45, MoveSnake)
                elif ((len(Snake)-1) >= 20 and (len(Snake)-1) < 24):
                    GameFrame.after(40, MoveSnake)
                else:
                    GameFrame.after(35, MoveSnake)
            else:
                if ((len(Snake)-1) < 4):
                    GameFrame.after(50, MoveSnake)
                elif ((len(Snake)-1) >= 4 and (len(Snake)-1) < 8):
                    GameFrame.after(47, MoveSnake)
                elif ((len(Snake)-1) >= 8 and (len(Snake)-1) < 12):
                    GameFrame.after(42, MoveSnake)
                elif ((len(Snake)-1) >= 12 and (len(Snake)-1) < 16):
                    GameFrame.after(37, MoveSnake)
                elif ((len(Snake)-1) >= 16 and (len(Snake)-1) < 20):
                    GameFrame.after(31, MoveSnake)
                elif ((len(Snake)-1) >= 20 and (len(Snake)-1) < 24):
                    GameFrame.after(24, MoveSnake)
                else:
                    GameFrame.after(16, MoveSnake)
        else:
            GameFrame.after(70, MoveSnake)

# Used To Start The Snake Game


def PlayGame():
    if GameDifficulty == "Hard":
        PlacePoison()
        PlaceOrange()
        MoveSnake()
    else:
        PlaceOrange()
        MoveSnake()

# A Cheat Code Function That Increases The Score By 3 Instead Of 1


def CheatCode1(Event):
    global CheatCodeScore
    CheatCodeScore = True

# A Cheat Code Function That Increases The Score By 3 Instead Of 1


def CheatCode2(Event):
    global CheatCodeSpeed
    if CheatCodeSpeed:
        CheatCodeSpeed = False
    else:
        CheatCodeSpeed = True
        
# A Cheat Code Function That Increases The Score By 3 Instead Of 1


def CheatCode3(Event):
    global CheatCodeSpike
    CheatCodeSpike = True

# Resumes The Game If The Resume Button Is Clicked


def ResumeBackGame():
    global GameIsPaused
    GameIsPaused = False
    GameFrame.pack(fill="both", expand=1)
    PauseFrame.forget()

# Changes To The Pause Game Frame When The Pause Button Is Pressed


def ResumeGame():
    global GameIsPaused, CurrentScore, Score
    CurrentScore.config(text="Score: " + str(Score))
    GameIsPaused = True
    if GameEnd:
        ChangeToEnd()
    else:
        GameFrame.forget()
        PauseFrame.pack(fill="both", expand=1)

# Used To Pause The Game When the Enter Button Is Pressed While Playing


def PauseGameWithEnter(Event):
    global GameIsPaused, CurrentScore, Score
    CurrentScore.config(text="Score: " + str(Score))
    if GameEnd:
        ChangeToEnd()
    else:
        GameFrame.forget()
        PauseFrame.pack(fill="both", expand=1)
        if GameIsPaused:
            GameIsPaused = False
            PauseFrame.forget()
            GameFrame.pack(expand=1, fill="both")
        else:
            GameIsPaused = True

# Saves The Score And The Players Name To The Text File
# After The Game Is Over And The Add To Leaderboard Button Is Pressed


def AddScore():
    global Score, InputName, GameDifficulty
    Name = InputName.get("1.0", END)
    Score = int(Score)
    if Score < 10:
        Score = "0" + str(Score)
    else:
        pass
    if Name == "" or Name == "\n":
        messagebox.showerror("Invalid Name", "Please Enter Your Name To Add Your Score To The Leaderboard")
    else:
        TextFile = open("SnakeGameScores.txt", "a+")
        TextFile.write(str(Score)+"|"+Name+"\n")
        TextFile.close()
        messagebox.showinfo("Leaderboard Updated",
                            "Your Score Has Been Added To The Leaderboard")
        ChangeToMainMenu()

# Changes To The Leaderboard Frame When THe Leaderboard Button Is Pressed


def ChangeToLeaderBoard():
    global LightMode
    LBHeading = LeaderBoardPage.create_text(
        (GAMECANVASWIDTH/2)-25, 40,
        text="The Snake Game Leaderboard:",
        font=("Consolas 30 bold"))
    Padding = 125
    TextFile = open("SnakeGameScores.txt", "r")
    ReadTextFile = TextFile.readlines()
    SortScores = sorted(ReadTextFile, reverse=1)
    ReturnToMM = Button(LeaderBoardPage, borderwidth=3,
                        text="Return", font=("Consolas 24 bold"),
                        cursor="plus", width=20,
                        command=MainMenu)
    LeaderBoardPage.create_window(277.5, 690, window=ReturnToMM)
    PlayGame = Button(LeaderBoardPage, borderwidth=3,
                      text="Play Game", font=("Consolas 24 bold"),
                      cursor="plus", width=20,
                      command=GameRulesDisplay)
    LeaderBoardPage.create_window(1032, 690, window=PlayGame)
    LeaderBoardPage.create_image(730, 60, image=Trophy, anchor="nw")
    LeaderBoardPage.create_image(-20, 60, image=Trophy2, anchor="nw")

    if len(SortScores) < 10 and len(SortScores) > 0:
        for X in range(len(SortScores)):
            Scores = SortScores[X]
            PlayerScore, Name = Scores.split("|")
            PrintedScores = LeaderBoardPage.create_text(
                (GAMECANVASWIDTH/2)-30, Padding,
                text=(str(X+1) + ". " + str(PlayerScore) + " - " + str(Name)),
                font=("Consolas 20 bold"), fill="#020408")
            Padding += 50
            if not LightMode:
                LeaderBoardPage.config(bg="#020408")
                LeaderBoardPage.itemconfig(LBHeading, fill="#EBECF0")
                if X == 0:
                    LeaderBoardPage.itemconfig(PrintedScores, fill="#FFBF00")
                elif X == 1:
                    LeaderBoardPage.itemconfig(PrintedScores, fill="#A8A9AD")
                elif X == 2:
                    LeaderBoardPage.itemconfig(PrintedScores, fill="#B08D57")
                else:
                    LeaderBoardPage.itemconfig(PrintedScores, fill="#BF0000")
                PlayGame.config(bg="#D1350D", activebackground="#BF0000",
                                activeforeground="#FFFEF2",
                                highlightbackground="#EBECF0", fg="#EBECF0",
                                highlightthickness=3)
                ReturnToMM.config(bg="#0096FF", activebackground="#0047AB",
                                  activeforeground="#FFFEF2",
                                  highlightbackground="#EBECF0",
                                  fg="#EBECF0", highlightthickness=3)
            else:
                LeaderBoardPage.config(bg="#EBECF0")
                LeaderBoardPage.itemconfig(LBHeading, fill="#020408")
                if X == 0:
                    LeaderBoardPage.itemconfig(PrintedScores, fill="#FFBF00")
                elif X == 1:
                    LeaderBoardPage.itemconfig(PrintedScores, fill="#A8A9AD")
                elif X == 2:
                    LeaderBoardPage.itemconfig(PrintedScores, fill="#B08D57")
                else:
                    LeaderBoardPage.itemconfig(PrintedScores, fill="#020408")
                PlayGame.config(bg="#82EEFD", activebackground="#1F456E",
                                foreground="#FFFFFF",
                                activeforeground="#FFFAFA",
                                highlightbackground="#2B2B2B",
                                highlightthickness=3)
                ReturnToMM.config(bg="#3DED97", activebackground="#345414",
                                  foreground="#FFFFFF",
                                  activeforeground="#FFFAFA",
                                  highlightbackground="#2B2B2B",
                                  highlightthickness=3)
    else:
        for X in range(10):
            Scores = SortScores[X]
            Scores = Scores.strip('\n')
            PlayerScore, Name = Scores.split("|")
            PrintedScores = LeaderBoardPage.create_text(
                (GAMECANVASWIDTH/2)-30, Padding,
                text=(str(X+1) + ". " + str(PlayerScore) + " - " + str(Name)),
                font=("Consolas 20 bold"), fill="#020408")
            Padding += 50
            if not LightMode:
                LeaderBoardPage.config(bg="#020408")
                LeaderBoardPage.itemconfig(LBHeading, fill="#EBECF0")
                if X == 0:
                    LeaderBoardPage.itemconfig(PrintedScores, fill="#FFBF00")
                elif X == 1:
                    LeaderBoardPage.itemconfig(PrintedScores, fill="#A8A9AD")
                elif X == 2:
                    LeaderBoardPage.itemconfig(PrintedScores, fill="#B08D57")
                else:
                    LeaderBoardPage.itemconfig(PrintedScores, fill="#D21404")
                PlayGame.config(bg="#D1350D", activebackground="#BF0000",
                                activeforeground="#FFFEF2",
                                highlightbackground="#EBECF0",
                                fg="#EBECF0", highlightthickness=3)
                ReturnToMM.config(bg="#0096FF", activebackground="#0047AB",
                                  activeforeground="#FFFEF2",
                                  highlightbackground="#EBECF0",
                                  fg="#EBECF0", highlightthickness=3)
            else:
                LeaderBoardPage.create_image(730, 60,
                                             image=Trophy, anchor="nw")
                LeaderBoardPage.create_image(-20, 60,
                                             image=Trophy2, anchor="nw")
                LeaderBoardPage.config(bg="#EBECF0")
                LeaderBoardPage.itemconfig(LBHeading, fill="#020408")
                if X == 0:
                    LeaderBoardPage.itemconfig(PrintedScores, fill="#FFBF00")
                elif X == 1:
                    LeaderBoardPage.itemconfig(PrintedScores, fill="#A8A9AD")
                elif X == 2:
                    LeaderBoardPage.itemconfig(PrintedScores, fill="#B08D57")
                else:
                    LeaderBoardPage.itemconfig(PrintedScores, fill="#020408")
                PlayGame.config(bg="#C5C5C5", activebackground="#AEAEAE",
                                activeforeground="#000000",
                                highlightthickness=3,
                                highlightbackground="#2B2B2B",
                                fg="#2B2B2B")
                ReturnToMM.config(bg="#C5C5C5", activebackground="#AEAEAE",
                                  activeforeground="#000000",
                                  highlightthickness=3,
                                  highlightbackground="#2B2B2B",
                                  fg="#2B2B2B")

    LeaderBoardFrame.pack(fill="both", expand=1)
    MainFrame.forget()

# Returns Back To The Main Menu


def MainMenu():
    MainFrame.pack(fill="both", expand=1)
    SettingsFrame.forget()
    LeaderBoardFrame.forget()

# Changes To The Game End Frame After The Snake
# Dies And Displays Final Score And Other Options


def ChangeToEnd():
    global HighestScore, Score
    GameFrame.forget()
    EndFrame.pack(fill="both", expand=1)
    FinalScore = Label(EndFrame, text=("Final Score:   " + str(Score)),
                       font=("Consolas 31 bold"))
    FinalScore.place(x=443.5, y=170)

    NameLabel = Label(EndFrame, text="Enter Name:", font=("Consolas 20 bold"))
    NameLabel.place(x=413, y=265)

    SubmitScoreAndName = Button(EndFrame, text="Add Score To Leaderboard",
                                font=("Consolas 18 bold"), width=32,
                                borderwidth=5, command=AddScore,
                                cursor="plus", highlightthickness=3)
    SubmitScoreAndName.place(x=413, y=325, height=65)

    ExitGame = Button(EndFrame, text="Exit Game", font=("Consolas 18 bold"),
                      width=32, borderwidth=5, command=SnakeGame.destroy,
                      cursor="plus", highlightthickness=3)
    ExitGame.place(x=413, y=475, height=65)

    MainMenu = Button(EndFrame, text="Main Menu", font=("Consolas 18 bold"),
                      width=32, borderwidth=5, command=ChangeToMainMenu,
                      cursor="plus", highlightthickness=3)
    MainMenu.place(x=413, y=400, height=65)

    GameScore = int(Score)
    if GameScore > Highest:
        NewHighScore = Label(EndFrame,
                             text="Congratulations! You Have Broken The Previous High Score",
                             font=("Consolas 29 bold"))
        NewHighScore.place(x=17.5, y=660)

        if LightMode:
            NewHighScore.config(bg="#EBECF0", fg="#03C04A")
        else:
            NewHighScore.config(fg="#0492C2", bg="#020408")

    if LightMode:
        EndFrame.config(bg="#EBECF0")
        FinalScore.config(bg="#EBECF0", fg="#020408")
        NameLabel.config(bg="#EBECF0", fg="#020408")
        SubmitScoreAndName.config(bg="#0FBED8",
                                  activebackground="#0096FF", fg="#FFF",
                                  activeforeground="#EBECF0",
                                  highlightbackground="#2B2B2B")
        ExitGame.config(bg="#FF2C05", activebackground="#F00505",
                        fg="#FFF", activeforeground="#EBECF0",
                        highlightbackground="#2B2B2B")
        MainMenu.config(bg="#0FBED8", activebackground="#0096FF",
                        fg="#FFF", activeforeground="#EBECF0",
                        highlightbackground="#2B2B2B")
    else:
        EndFrame.config(bg="#020408")
        FinalScore.config(fg="#EBECF0", bg="#020408")
        NameLabel.config(fg="#EBECF0", bg="#020408")
        SubmitScoreAndName.config(bg="#0096FF", activebackground="#0047AB",
                                  activeforeground="#FFFEF2",
                                  highlightbackground="#EBECF0", fg="#EBECF0")
        ExitGame.config(bg="#D1350D", activebackground="#BF0000",
                        activeforeground="#FFFEF2",
                        highlightbackground="#EBECF0", fg="#EBECF0")
        MainMenu.config(bg="#0096FF", activebackground="#0047AB",
                        activeforeground="#FFFEF2",
                        highlightbackground="#EBECF0", fg="#EBECF0")

# A Frame That Displays The Games Rules And The
# Option To Go To Game Settings Or To Play The Game


def GameRulesDisplay():
    global KeyControls
    RulesFrame.config(bg="#EBECF0")
    RulesTitle = Label(RulesFrame, text="The Snake Game Rules:",
                       font=("Consolas 30 bold"), foreground="#020408")
    Controls1 = Label(RulesFrame, font=("Consolas 20 bold"),
                      foreground="#020408")
    Controls2 = Label(RulesFrame, font=("Consolas 20 bold"),
                      foreground="#020408")
    Controls3 = Label(RulesFrame, font=("Consolas 20 bold"),
                      foreground="#020408")
    Controls4 = Label(RulesFrame, font=("Consolas 20 bold"),
                      foreground="#020408")
    Description1 = Label(RulesFrame, text="1. The Speed Of The Game \n   Increases As The Snake \n   Size Grows.",
                         font=("Consolas 20 bold"), anchor="e",
                         justify=LEFT, foreground="#020408")
    Description2 = Label(RulesFrame, text="2. The Aim Is For The Snake \n   To Eat The Oranges And \n   Beat The High Score.",
                         font=("Consolas 20 bold"), anchor="e",
                         justify=LEFT, foreground="#020408")
    Description3 = Label(RulesFrame, text="3. If The Head Of The Snake \n   Touches The Edge Of Screen\n   (Not In Easy Mode) Or The\n   Body, The Game Will End.", font=("Consolas 20 bold"), anchor="e", justify=LEFT, foreground="#020408")
    Description4 = Label(RulesFrame, text="4. Press The Space Key To Hide\n   The Game From Your Boss And\n   Space To Play Again.",
                         font=("Consolas 20 bold"), anchor="e",
                         justify=LEFT, foreground="#020408")
    SettingsButton = Button(RulesFrame, borderwidth=5,
                            text="Settings", width=28,
                            bg="#C5C5C5", activebackground="#AEAEAE",
                            activeforeground="#000000", highlightthickness=4,
                            highlightbackground="#2B2B2B",
                            font=("Consolas 18 bold"), fg="#2B2B2B",
                            cursor="plus", command=GameSettings)
    PlayGameButton = Button(RulesFrame, borderwidth=5,
                            text="Play Game", width=28,
                            bg="#C5C5C5", activebackground="#AEAEAE",
                            activeforeground="#000000", highlightthickness=4,
                            highlightbackground="#2B2B2B",
                            font=("Consolas 18 bold"), fg="#2B2B2B",
                            cursor="plus", command=ChangeToTimer)
    FullRules = Label(RulesFrame, font=("Consolas 19 bold"),
                      foreground="#020408",
                      text="READ THE RULES, FEATURES AND CHEAT CODES IN THE FILE SNAKEGAMERULES.TXT")

    RulesTitle.place(x=(GAMECANVASWIDTH/2)-300, y=35)
    Controls1.place(x=(GAMECANVASWIDTH/4)-225, y=150)
    Controls2.place(x=(GAMECANVASWIDTH/4)-225, y=210)
    Controls3.place(x=(GAMECANVASWIDTH/4)-225, y=270)
    Controls4.place(x=(GAMECANVASWIDTH/4)-225, y=330)
    Description1.place(x=(GAMECANVASWIDTH/2)+25, y=150)
    Description2.place(x=(GAMECANVASWIDTH/2)+25, y=270)
    Description3.place(x=(GAMECANVASWIDTH/2)+25, y=390)
    Description4.place(x=(GAMECANVASWIDTH/2)+25, y=545)
    SettingsButton.place(x=(GAMECANVASWIDTH/4)-225, y=430, height=95)
    PlayGameButton.place(x=(GAMECANVASWIDTH/4)-225, y=545, height=95)
    FullRules.place(x=(GAMECANVASWIDTH/4)-222.5, y=650, height=95)

    if KeyControls == "Arrow Keys":
        Controls1.config(text="← : Left Key To Move Left")
        Controls2.config(text="→ : Right Key To Move Right")
        Controls3.config(text="↓ : Down Key To Move Down")
        Controls4.config(text="↑ : Up Key To Move Up")
    else:
        Controls1.config(text="A : A Key To Move Left   ")
        Controls2.config(text="D : D Key To Move Right    ")
        Controls3.config(text="S : S Key To Move Down     ")
        Controls4.config(text="W : W Key To Move Up       ")

    if LightMode:
        SettingsButton.config(bg="#3DED97", activebackground="#03C04A",
                              activeforeground="#FFF",
                              highlightbackground="#2B2B2B",
                              fg="#DCD9CD")
        PlayGameButton.config(bg="#63C5DA", activebackground="#0492C2",
                              activeforeground="#FFF",
                              highlightbackground="#2B2B2B",
                              fg="#DCD9CD")
        RulesTitle.config(bg="#EBECF0", fg="#020408")
        Controls1.config(bg="#EBECF0", fg="#020408")
        Controls2.config(bg="#EBECF0", fg="#020408")
        Controls3.config(bg="#EBECF0", fg="#020408")
        Controls4.config(bg="#EBECF0", fg="#020408")
        Description1.config(bg="#EBECF0", fg="#020408")
        Description2.config(bg="#EBECF0", fg="#020408")
        Description3.config(bg="#EBECF0", fg="#020408")
        Description4.config(bg="#EBECF0", fg="#020408")
        FullRules.config(bg="#EBECF0", fg="#020408")
    else:
        RulesFrame.config(bg="#020408")
        SettingsButton.config(bg="#0096FF", activebackground="#0047AB",
                              activeforeground="#FFFEF2",
                              highlightbackground="#EBECF0", fg="#EBECF0")
        PlayGameButton.config(bg="#D1350D", activebackground="#BF0000",
                              activeforeground="#FFFEF2",
                              highlightbackground="#EBECF0",
                              fg="#EBECF0")
        RulesTitle.config(bg="#020408", fg="#EBECF0")
        Controls1.config(bg="#020408", fg="#EBECF0")
        Controls2.config(bg="#020408", fg="#EBECF0")
        Controls3.config(bg="#020408", fg="#EBECF0")
        Controls4.config(bg="#020408", fg="#EBECF0")
        Description1.config(bg="#020408", fg="#EBECF0")
        Description2.config(bg="#020408", fg="#EBECF0")
        Description3.config(bg="#020408", fg="#EBECF0")
        Description4.config(bg="#020408", fg="#EBECF0")
        FullRules.config(bg="#020408", fg="#EBECF0")

    MainFrame.forget()
    SettingsFrame.forget()
    LeaderBoardFrame.forget()
    RulesFrame.pack(fill="both", expand=1)

# Used To Change The Keyboard Buttons Used To
# Control The Movement Of The Snake On The Canvas


def ChangeKeyBinds():
    global KeyControls, ChangeDirection
    if KeyControls == "Arrow Keys":
        KeyControls = "W A S D Keys"
        ChangeDirection = "s"
        GameSettings()
    else:
        KeyControls = "Arrow Keys"
        GameSettings()

# Used To Change The Difficulty Of The Game
# When The Button Is Pressed In The Settings


def ChangeDifficulty():
    global GameDifficulty
    if GameDifficulty == "Medium":
        GameDifficulty = "Hard"
        GameSettings()
    elif GameDifficulty == "Hard":
        GameDifficulty = "Easy"
        GameSettings()
    else:
        GameDifficulty = "Medium"
        GameSettings()

# Used To Change The Size of The Snake And Canvas
# When The Button Is Pressed In The Settings


def ChangeSnakeCanvasSize():
    global SnakeSize
    if SnakeSize == 35:
        SnakeSize = 50
        GameSettings()
    elif SnakeSize == 50:
        SnakeSize = 20
        GameSettings()
    else:
        SnakeSize = 35
        GameSettings()

# Toggles Between light And Dark mode When
# Button Is Pressed in The Game Settings


def ChangeMode():
    DarkLightMode()
    GameSettings()

# A Frame That Displays The Settings Of The
# Game Which Can Be Configured To Preference


def GameSettings():
    global GameDifficulty, SnakeSize, KeyControls
    RulesFrame.forget()
    SettingsTitle = Label(SettingsFrame, text="Settings:",
                          font=("Consolas 30 bold"),
                          foreground="#020408")
    LMDM = Button(SettingsFrame, borderwidth=5,
                  text="", highlightthickness=4,
                  font=("Consolas 18 bold"), fg="#2B2B2B",
                  cursor="plus", command=ChangeMode,
                  width=85)
    Return = Button(SettingsFrame, borderwidth=5,
                    text="Return", highlightthickness=4,
                    font=("Consolas 18 bold"), fg="#2B2B2B",
                    cursor="plus", command=GameRulesDisplay,
                    width=40)
    MainMenuDisplay = Button(SettingsFrame, borderwidth=5,
                             text="Main Menu",
                             highlightthickness=4,
                             font=("Consolas 18 bold"),
                             fg="#2B2B2B", cursor="plus",
                             command=MainMenu, width=40)
    KeyControlsForGame = Button(SettingsFrame, borderwidth=5,
                                text=("Controls: " +
                                      str(KeyControls)),
                                highlightthickness=4,
                                font=("Consolas 18 bold"),
                                fg="#2B2B2B", cursor="plus",
                                command=ChangeKeyBinds, width=85)
    ChangeSnakeSize = Button(SettingsFrame, borderwidth=5,
                             text=("Snake Size: " +
                                   str(SnakeSize)),
                             highlightthickness=4,
                             font=("Consolas 18 bold"),
                             fg="#2B2B2B", cursor="plus",
                             command=ChangeSnakeCanvasSize,
                             width=85)
    Difficulty = Button(SettingsFrame, borderwidth=5,
                        text=("Difficulty: " +
                              str(GameDifficulty)),
                        highlightthickness=4,
                        font=("Consolas 18 bold"),
                        fg="#2B2B2B", cursor="plus",
                        command=ChangeDifficulty,
                        width=85)
    SettingsTitle.place(x=(GAMECANVASWIDTH/2)-130, y=35)
    LMDM.place(x=47.5, y=132.5, height=90)
    Return.place(x=47.5, y=620, height=90)
    MainMenuDisplay.place(x=680, y=620, height=90)
    KeyControlsForGame.place(x=47.5, y=255, height=90)
    ChangeSnakeSize.place(x=47.5, y=377.5, height=90)
    Difficulty.place(x=47.5, y=500, height=90)
    SettingsFrame.pack(fill="both", expand=1)

    if LightMode:
        SettingsFrame.config(bg="#EBECF0")
        SettingsTitle.config(bg="#EBECF0")
        LMDM.config(text="Dark Mode: OFF", bg="#313131",
                    activebackground="#181818", fg="#F5F5F5",
                    activeforeground="#C4C4C4",
                    highlightthickness=2, highlightbackground="#181818")
        Return.config(bg="#82EEFD", activebackground="#1F456E",
                      foreground="#FFFFFF",
                      activeforeground="#FFFAFA",
                      highlightbackground="#2B2B2B")
        MainMenuDisplay.config(bg="#3DED97", activebackground="#345414",
                               foreground="#FFFFFF",
                               activeforeground="#FFFAFA",
                               highlightbackground="#2B2B2B")

        if GameDifficulty == "Easy":
            Difficulty.config(bg="#FCE205",
                              activebackground="#FCD12A",
                              foreground="#FFFFFF",
                              activeforeground="#FFFAFA",
                              highlightbackground="#2B2B2B")
        elif GameDifficulty == "Medium":
            Difficulty.config(bg="#FF781F",
                              activebackground="#FF6600",
                              foreground="#FFFFFF",
                              activeforeground="#FFFAFA",
                              highlightbackground="#2B2B2B")
        else:
            Difficulty.config(bg="#E3242B",
                              activebackground="#990F02",
                              foreground="#FFFFFF",
                              activeforeground="#FFFAFA",
                              highlightbackground="#2B2B2B")

        if SnakeSize == 20:
            ChangeSnakeSize.config(bg="#FCE205",
                                   activebackground="#FCD12A",
                                   foreground="#FFFFFF",
                                   activeforeground="#FFFAFA",
                                   highlightbackground="#2B2B2B")
        elif SnakeSize == 35:
            ChangeSnakeSize.config(bg="#FF781F",
                                   activebackground="#FF6600",
                                   foreground="#FFFFFF",
                                   activeforeground="#FFFAFA",
                                   highlightbackground="#2B2B2B")
        else:
            ChangeSnakeSize.config(bg="#E3242B",
                                   activebackground="#990F02",
                                   foreground="#FFFFFF",
                                   activeforeground="#FFFAFA",
                                   highlightbackground="#2B2B2B")

        if KeyControls == "Arrow Keys":
            KeyControlsForGame.config(bg="#FF781F",
                                      activebackground="#FF6600",
                                      foreground="#FFFFFF",
                                      activeforeground="#FFFAFA",
                                      highlightbackground="#2B2B2B")
        else:
            KeyControlsForGame.config(bg="#E3242B",
                                      activebackground="#990F02",
                                      foreground="#FFFFFF",
                                      activeforeground="#FFFAFA",
                                      highlightbackground="#2B2B2B")

    else:
        SettingsFrame.config(bg="#020408")
        SettingsTitle.config(bg="#020408", fg="#EBECF0")
        LMDM.config(text="Dark Mode: ON", bg="#F5F5F5",
                    activebackground="#C4C4C4",
                    activeforeground="#181818",
                    highlightbackground="#EBECF0",
                    fg="#313131")
        Return.config(bg="#710193",
                      activebackground="#4D0F28",
                      foreground="#FFFFFF",
                      activeforeground="#FFFAFA",
                      highlightbackground="#2B2B2B")
        MainMenuDisplay.config(bg="#0096FF",
                               activebackground="#0047AB",
                               foreground="#FFFFFF",
                               activeforeground="#FFFAFA",
                               highlightbackground="#2B2B2B")

        if GameDifficulty == "Easy":
            Difficulty.config(bg="#AEF359",
                              activebackground="#3DED97",
                              foreground="#FFFFFF",
                              activeforeground="#FFFAFA",
                              highlightbackground="#2B2B2B")
        elif GameDifficulty == "Medium":
            Difficulty.config(bg="#5DBB63",
                              activebackground="#03C04A",
                              foreground="#FFFFFF",
                              activeforeground="#FFFAFA",
                              highlightbackground="#2B2B2B")
        else:
            Difficulty.config(bg="#03AC13",
                              activebackground="#32612D",
                              foreground="#FFFFFF",
                              activeforeground="#FFFAFA",
                              highlightbackground="#2B2B2B")

        if SnakeSize == 20:
            ChangeSnakeSize.config(bg="#AEF359",
                                   activebackground="#3DED97",
                                   foreground="#FFFFFF",
                                   activeforeground="#FFFAFA",
                                   highlightbackground="#2B2B2B")
        elif SnakeSize == 35:
            ChangeSnakeSize.config(bg="#5DBB63",
                                   activebackground="#03C04A",
                                   foreground="#FFFFFF",
                                   activeforeground="#FFFAFA",
                                   highlightbackground="#2B2B2B")
        else:
            ChangeSnakeSize.config(bg="#03AC13",
                                   activebackground="#32612D",
                                   foreground="#FFFFFF",
                                   activeforeground="#FFFAFA",
                                   highlightbackground="#2B2B2B")

        if KeyControls == "Arrow Keys":
            KeyControlsForGame.config(bg="#5DBB63",
                                      activebackground="#03C04A",
                                      foreground="#FFFFFF",
                                      activeforeground="#FFFAFA",
                                      highlightbackground="#2B2B2B")
        else:
            KeyControlsForGame.config(bg="#03AC13",
                                      activebackground="#32612D",
                                      foreground="#FFFFFF",
                                      activeforeground="#FFFAFA",
                                      highlightbackground="#2B2B2B")

# Decrements From 3 To 1 Before The Game Frame Is Displayed


def Timer(Count):
    GameTimer.after(1, lambda: GameTimer.focus_force())
    Countdown['text'] = Count
    if Count > 0:
        GameTimer.after(1000, Timer, Count-1)
    else:
        ChangeToGame()

# Returns To The Main Menu


def ChangeToMainMenu():
    global SnakeGame
    SnakeGame.destroy()
    os.system("python3 TheSnakeGame.py")

# Changed To The Game After The 3 Second Timer Ends


def ChangeToGame():
    GameFrame.pack(fill="both", expand=1)
    PlayGame()
    GameTimer.forget()

# Changes To The Frame To Dipslay The 3, 2, 1 Timer Before The Game Starts


def ChangeToTimer():
    GameTimer.pack(fill="both", expand=1)
    GameTimer.focus_force()
    RulesFrame.forget()
    PauseFrame.forget()
    LeaderBoardFrame.forget()
    MainFrame.forget()
    Timer(3)

# Returns To The Main Menu After The Game Ends


def RestartGame():
    global SnakeGame
    SnakeGame.destroy()
    os.system("python3 TheSnakeGame.py")

# Changes The Boolean Of BossHere When Space Is Pressed


def Boss(Event):
    global BossHere
    if not BossHere:
        BossHere = True
    else:
        BossHere = False
        BossFrame.forget()
        GameFrame.pack(expand=1, fill="both")

# Saves The Score, Difficulty And Keybinds Used For
# The Game To Restore The Previous State Of The Game


def SaveGameState():
    global TempScore, GameDifficulty, KeyControls
    global CheatCodeSpeed, CheatCodeScore, SnakeSize, CheatCodeSpike
    if not (CheatCodeScore or CheatCodeScore or CheatCodeSpike):
        Save = messagebox.askyesno("Confirm Save Game",
                                   "Saving The Game Will Return You To The Main Menu. Do You Want To Proceed?")
        if Save:
            SaveFile = open("SnakeGameSaved.txt", "w")
            SaveFile.write(str(TempScore) + "|" +
                           str(GameDifficulty) + "|" +
                           str(KeyControls) + "|" +
                           str(SnakeSize))
            SaveFile.close()
            ChangeToMainMenu()
        else:
            ResumeGame()
    else:
        messagebox.showerror("Cannot Save Game",
                             "You Cannot Save The Game As You Have Used Cheat Codes For This Game!")

# Initiate The Window For The Snake Game
SnakeGame = Tk()
SnakeGame.title("The Snake Game")
SnakeGame.geometry("1366x768")
SnakeGame.columnconfigure(0, weight=1)
SnakeGame.rowconfigure(0, weight=1)
os.system("cat SNAKEGAMERULES.txt")

# Create Frames For All The Displays In The Game
MainFrame = Frame(SnakeGame)
MainFrame.pack(fill="both", expand=1)
RulesFrame = Frame(SnakeGame)
SettingsFrame = Frame(SnakeGame)
GameTimer = Frame(SnakeGame)
GameFrame = Frame(SnakeGame)
BossFrame = Frame(SnakeGame)
PauseFrame = Frame(SnakeGame)
LeaderBoardFrame = Frame(SnakeGame)
EndFrame = Frame(SnakeGame)

# Create A List To Store The Snakes Body
Snake = []

# Define Constants And Variables For The
# Screen Resolution And The Size Of The Snake
GAMECANVASWIDTH,  GAMECANVASHEIGHT, SnakeSize = 1366, 768, 35

# Load The Files For The Images Used
# Free Image From vecteezy.com
# https://es.vecteezy.com/arte-vectorial/3222850-grupo-de-serpientes-en-bosque-durante-el-dia-escena-con-muchos-arboles
BackgroundDay = PhotoImage(file="DayImage.png")
# Free Image From freepik.com
# https://de.freepik.com/vektoren-kostenlos/natuerliche-dschungellandschaft_10248636.htm
BackgroundNight = PhotoImage(file="NightImage.png")
# Screenshot Of My Own Code For This Games
BossImage = PhotoImage(file="BossKeyImage.png")
# Free Image From lovepick.com
Trophy = PhotoImage(file="Trophy.png")
# Same Trophy Image Which Has Been Flipped
Trophy2 = PhotoImage(file="Trophy2.png")

# Create A Canvas For The Main Menu Display And Leaderboard Display
MainScreen = Canvas(MainFrame, width=GAMECANVASWIDTH, height=GAMECANVASHEIGHT)
MainScreen.pack()
LeaderBoardPage = Canvas(LeaderBoardFrame,
                         width=GAMECANVASWIDTH,
                         height=GAMECANVASHEIGHT)
LeaderBoardPage.pack()

# Buttons, Label And Images For The Main Menu Display
BackgroundImage = MainScreen.create_image(0, 0, image=BackgroundDay,
                                          anchor="nw")

Heading = MainScreen.create_text(GAMECANVASWIDTH/2, 180,
                                 text="The Snake Game",
                                 font=("Consolas 40 bold"),
                                 fill="#020408")

PlayButton = Button(MainFrame, borderwidth=5,
                    text="New Game", width=30,
                    bg="#C5C5C5", activebackground="#AEAEAE",
                    highlightthickness=4,
                    activeforeground="#000000",
                    highlightbackground="#2B2B2B",
                    font=("Consolas 17 bold"),
                    fg="#2B2B2B", cursor="plus",
                    command=GameRulesDisplay)

LoadButton = Button(MainFrame, borderwidth=5,
                    text="Load Last Saved Game",
                    width=30, bg="#C5C5C5",
                    activebackground="#AEAEAE",
                    highlightthickness=4,
                    activeforeground="#000000",
                    highlightbackground="#2B2B2B",
                    font=("Consolas 17 bold"), fg="#2B2B2B",
                    cursor="plus", command=LoadSavedGame)

LeaderBoard = Button(MainFrame, borderwidth=5,
                     text="Leaderboard", width=30,
                     bg="#C5C5C5", activebackground="#AEAEAE",
                     activeforeground="#000000",
                     highlightthickness=4, highlightbackground="#2B2B2B",
                     font=("Consolas 17 bold"), fg="#2B2B2B",
                     cursor="plus", command=ChangeToLeaderBoard)

ExitGame = Button(MainFrame, borderwidth=5, text="Exit Game",
                  width=30, bg="#C5C5C5", activebackground="#AEAEAE",
                  activeforeground="#000000", highlightthickness=4,
                  highlightbackground="#2B2B2B", font=("Consolas 17 bold"),
                  fg="#2B2B2B", cursor="plus", command=SnakeGame.destroy)

Theme = Button(MainFrame, borderwidth=4, text="Dark Mode: OFF",
               font=("Consolas 15 bold"), bg="#313131",
               activebackground="#181818", fg="#F5F5F5",
               activeforeground="#C4C4C4", highlightthickness=2,
               highlightbackground="#181818", command=DarkLightMode,
               cursor="plus", width=25)

MainScreen.create_window((GAMECANVASWIDTH/2)-2, 250, window=PlayButton)
MainScreen.create_window((GAMECANVASWIDTH/2)-2, 320, window=LoadButton)
MainScreen.create_window((GAMECANVASWIDTH/2)-2, 390, window=LeaderBoard)
MainScreen.create_window((GAMECANVASWIDTH/2)-2, 460, window=ExitGame)
MainScreen.create_window(1155, 33, window=Theme)

# Canvas And Button For The Snake Game Display
GameCanvas = Canvas(GameFrame, width=GAMECANVASWIDTH, height=GAMECANVASHEIGHT)
PauseButton = Button(GameFrame, borderwidth=5, text="Pause Game",
                     width=20, bg="#C5C5C5", activebackground="#AEAEAE",
                     activeforeground="#000000", highlightthickness=4,
                     highlightbackground="#2B2B2B", font=("Consolas 12 bold"),
                     fg="#2B2B2B", cursor="plus", command=ResumeGame)
GameCanvas.create_window(137.5, 32, window=PauseButton)

# 3, 2, 1 Countdown Label
Countdown = Label(GameTimer, font=("Consolas 300 bold"))
Countdown.place(x=550, y=110)

# Display For Current Score For The Pause Display Display
CurrentScore = Label(PauseFrame, font=("Consolas 35 bold"))
CurrentScore.place(x=545, y=75)

ResumeButton = Button(PauseFrame, text="Resume Game",
                      font=("Consolas 35 bold"), width=45,
                      borderwidth=5, cursor="plus", bg="#03C04A",
                      activebackground="#03AC13", activeforeground="#FFF",
                      highlightthickness=4, highlightbackground="#2B2B2B",
                      fg="#C5C5C5", command=ResumeBackGame)
ResumeButton.place(x=16.5, y=638, height=90)

SaveGame = Button(PauseFrame, text="Save Game", font=("Consolas 35 bold"),
                  width=45, borderwidth=5, cursor="plus", bg="#03C04A",
                  activebackground="#03AC13", activeforeground="#FFF",
                  highlightthickness=4, highlightbackground="#2B2B2B",
                  fg="#C5C5C5", command=SaveGameState)
SaveGame.place(x=16.5, y=530, height=90)

MainMenuButton = Button(PauseFrame, text="Main Menu",
                        font=("Consolas 35 bold"),
                        width=45, borderwidth=5,
                        cursor="plus", bg="#03C04A",
                        activebackground="#03AC13",
                        activeforeground="#FFF",
                        highlightthickness=4,
                        highlightbackground="#2B2B2B",
                        fg="#C5C5C5", command=ChangeToMainMenu)
MainMenuButton.place(x=16.5, y=422, height=90)

ExitButton = Button(PauseFrame, text="Exit Game",
                    font=("Consolas 35 bold"),
                    width=45, borderwidth=5,
                    cursor="plus", bg="#ED4D4D",
                    activebackground="#fd3a2d",
                    activeforeground="#FFF",
                    highlightthickness=4,
                    highlightbackground="#2B2B2B",
                    fg="#C5C5C5", command=SnakeGame.destroy)
ExitButton.place(x=16.5, y=314, height=90)

# Creates The Text File Where Scores Are Read From And Stored
# To If It Doesn't Already Exist In The Current Directory
if not os.path.isfile("SnakeGameScores.txt"):
    open("SnakeGameScores.txt", "w").close()

# Display The Current Score In The Snake Game And Calculate And
# Display The Highest Score From The Text File Where Scores Are Stored
Score = 0
ScoreRecorder = "Score: " + str(Score)
TextFile = open("SnakeGameScores.txt", "r")
ReadTextFile = TextFile.readlines()

if len(ReadTextFile) == 0:
    HighestScore = "Highest Score: None"
else:
    SortScores = sorted(ReadTextFile, reverse=1)
    Highest = SortScores[0]
    Highest = Highest.strip('\n')
    Highest, Name = Highest.split("|")
    Highest = int(Highest)
    HighestScore = "Highest Score: " + str(Highest)
TextFile.close()

PrintScore = GameCanvas.create_text((2*GAMECANVASWIDTH)/5, 32,
                                    font="Consolas 25 bold",
                                    text=ScoreRecorder)

HighScore = GameCanvas.create_text((4*GAMECANVASWIDTH)/5, 32,
                                   font="Consolas 25 bold",
                                   text=HighestScore, fill="#03C04A")

# Bind The Space Key As The Boss Key And The Enter Key To Pause Game
GameCanvas.bind("<space>", Boss)
GameCanvas.bind("<Return>", PauseGameWithEnter)
GameCanvas.bind("<Control-q>", CheatCode1)
GameCanvas.bind("<Control-f>", CheatCode2)
GameCanvas.bind("<Control-z>", CheatCode3)
GameCanvas.focus_set()
ChangeDirection = "down"

# Removes Any Blank Lines From The Scores Textfile
NewValues = ""
with open("SnakeGameScores.txt") as TxtFile:
    for Lines in TxtFile:
        if not Lines.isspace():
            NewValues += Lines

File = open("SnakeGameScores.txt", "w")
File.write(NewValues)
File.close()

InputName = Text(EndFrame, height=1, width=18,
                 font=("Consolas 20 bold"),
                 spacing1=1, selectborderwidth=3)
InputName.place(x=606.5, y=265)

SnakeGame.mainloop()
