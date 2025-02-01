import pandas

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_data_frame = pandas.DataFrame(data)

dict = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}
print(dict)
def nato():
    try:
        word = (input("Word?: ")).upper()
        new_word = [dict[letter] for letter in word]

    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(new_word)
    finally:
        nato()

nato()



