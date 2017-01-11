class NGram:
    def normal(self, gram_num, corpus):
        grams = []
        if type(gram_num) is not int and type(corpus) is not list:
            message = "First variable must be a number," \
                      " second variable must be a list."
            return message
        else:
            for i in range(len(corpus)):
                temp = ["Null_Word"]
                if i + 1 < gram_num:
                    temp *= (gram_num - (i + 1))

                while len(temp) < gram_num:
                    temp.append(corpus[i])
                grams.append(corpus)
        return grams
