Isprocessing = False
SeeThoughtProcess = False
def ShowThoughtProcess(Message):
    if SeeThoughtProcess:
        print(Message)
while True:
    if not Isprocessing:
        UserInput = input("Type here ")
        UserInputSplit = UserInput.split()
        ShowThoughtProcess(f"Turned user input into: {UserInputSplit} so i can parse it.")
        with open('Data.txt', 'r+', encoding='utf-8') as file:
            CurrentLine = file.readline()
            while CurrentLine != '':
                BestMatchingPrompt = ""
                BestMatchingPromptNumOfUsableWords = 0
                CurrentPromptNumOfUsableWords = 0
                CurrentPromptSplit = None
                ShowThoughtProcess(f"Looking at line of data: {CurrentLine}")
                CurrentLineSplit = CurrentLine.split()
                ShowThoughtProcess(f"Turned current line into: {CurrentLineSplit} so i can parse it.")
                for i in range(len(CurrentLineSplit)):
                    ShowThoughtProcess(f"Looking at word {CurrentLineSplit[i]} to see if it is the start or end of a prompt or answer")
                    if CurrentLineSplit[i] == "|":
                        ShowThoughtProcess(f"Found the middle of a line finding the prompt and answer")

                        CurrentPromptSplit = []
                        for k in range(len(CurrentLineSplit)-i):#get the whole prompt
                            CurrentPromptSplit.append(CurrentLineSplit[k])
                        CurrentPrompt = " ".join(CurrentPromptSplit)
                        ShowThoughtProcess(f"Found Prompt: {CurrentPrompt} on line: {CurrentLine}")

                        CurrentAnswerSplit = []
                        for k in range(i+1,len(CurrentLineSplit)):#get the whole prompt
                            CurrentAnswerSplit.append(CurrentLineSplit[k])
                        CurrentAnswer = " ".join(CurrentAnswerSplit)

                        ShowThoughtProcess(f"Found Answer: {CurrentAnswer} on line: {CurrentLine}")
                        CurrentPromptSplit = CurrentPrompt.split()
                        ShowThoughtProcess(f"Turned current prompt into: {CurrentPromptSplit} so i can parse it.")
                    else:
                        ShowThoughtProcess(f"Word: {CurrentLineSplit[i]} was not '|'.")
                    
                    ShowThoughtProcess(f"Checking if a prompt was found.")
                    if CurrentPromptSplit != None:
                        ShowThoughtProcess(f"Prompt was found")
                        for i in range(len(UserInputSplit)):
                            for j in range(len(CurrentPromptSplit)):
                                ShowThoughtProcess(f"Looking at word: {UserInputSplit[i]} To see if it matches the word in: {CurrentPromptSplit[j]}")
                                if UserInputSplit[i] == CurrentPromptSplit[j]:
                                    ShowThoughtProcess(f"Word: {UserInputSplit[i]} does match {CurrentPromptSplit[j]}")
                                    CurrentPromptNumOfUsableWords += 1
                        if CurrentPromptNumOfUsableWords > BestMatchingPromptNumOfUsableWords or BestMatchingPromptNumOfUsableWords == 0:
                            BestMatchingPrompt = CurrentAnswer
                            BestMatchingPromptNumOfUsableWords = CurrentPromptNumOfUsableWords
                CurrentLine = file.readline()

        if BestMatchingPrompt == "":
            ShowThoughtProcess(f"Done with whole process best answer was: Sorry i couldnt answer that.")
            print("Sorry i couldnt answer that.")
        else:
            ShowThoughtProcess(f"Done with whole process best answer was: {BestMatchingPrompt}")
            print(BestMatchingPrompt)
        Isprocessing = False