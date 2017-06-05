"""
Requires:
    this module checks whether a mentioned phrase is in proper song
"""
import Parser
import SongText


# checks whether larger list contains smaller one
def contains(small, big):
    for i in range(len(big)-len(small)+1):
        for j in range(len(small)):
            if big[i+j] != small[j]:
                break
        else:
            return True
    return False


def checkCorrectness():
    phrase = Parser.getPhrase()
    text = SongText.getFullSong()

    # convert all the letters into lowercase
    # and then split them to get the list
    listOfWordsInPhrase = phrase.lower().split()
    # unfortunately had to made 2 methods in one line
    # in fact that otherwise it wouldn't be long-term change

    # do the same with text
    listOfWordsInText = text.lower().split()

    if contains(listOfWordsInPhrase, listOfWordsInText):
        print("Yes, it contains")
    else:
        print("No, it doesn't contain")


if __name__ == "__main__":
    checkCorrectness()
