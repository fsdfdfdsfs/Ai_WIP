Isprocessing = False
SeeThoughtProcess = False
while True:
    if not Isprocessing:
        UserInput = input("Type here ")
        UserInputSplit = UserInput.split()
        with open('Data.txt', 'r+', encoding='utf-8') as file:
            BestMatchingPrompt = ""
            BestMatchingPromptNumOfUsableWords = 0

            CurrentPromptNumOfUsableWords = 0

            CurrentPromptSplit = None

            CurrentLine = file.readline()
            while CurrentLine != '': #loop through every line
                CurrentLine = file.readline()
                CurrentLineSplit = CurrentLine.split()
                for i in range(len(CurrentLineSplit)):
                    if CurrentLineSplit[i] == "|":# if its add the middle then set the current prompt to everything before that
                        CurrentPrompt = CurrentLineSplit[i-1]
                        CurrentAnswer = CurrentLineSplit[i+1]

                        CurrentPromptSplit = CurrentPrompt.split()

                    if CurrentPromptSplit != None:
                        for i in range(len(CurrentPromptSplit)):
                            if UserInputSplit[i] == CurrentPromptSplit[i]:#maybe add more in depth searching in the future
                                CurrentPromptNumOfUsableWords += 1

                        if CurrentPromptNumOfUsableWords >= BestMatchingPromptNumOfUsableWords or BestMatchingPromptNumOfUsableWords == 0 or BestMatchingPrompt == "":
                            BestMatchingPrompt = CurrentPrompt
                            BestMatchingPromptNumOfUsableWords = CurrentPromptNumOfUsableWords
        if BestMatchingPrompt == "":
            print("Sorry i couldnt answer that.")
        else:
            print(BestMatchingPrompt)
        Isprocessing = False