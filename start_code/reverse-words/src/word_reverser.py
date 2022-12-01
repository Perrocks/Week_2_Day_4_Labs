class WordReverser:
    def __init__(self, string):
        self.string = string

    def reverse_string(self, word_reverser):
        new_list=[]
        list=word_reverser.string.split(" ")

        words=""

        for word in list:
            if len(word)>=5:
                reverse=word[::-1]
                new_list.append(reverse)
            elif len(word)<5:
                new_list.append(word)

        for word in new_list:
            words+=f"{word} "
        return words
