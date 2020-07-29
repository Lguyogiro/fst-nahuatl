import re


class VerbalStem(object):
    def __init__(self, stem, transitive=False, es=False):
        self.stem = stem
        self.vowels = ["ui", "ua", "a", "e", "i", "o", "u"]
        self.cons = ["p", "t", "c", "m", "n", "z", "x"]
        self.multi_char_cons = ["ch", "tl", "tz"]
        self.numVPattern = re.compile("|".join(self.vowels))
        self.n_syl = self.count_syllables()
        self.is_spanish = es
        self.trans = transitive

    def count_syllables(self):
        return len(re.sub(self.numVPattern, 'V', self.stem))

    @property
    def base1(self) -> str:
        return self.stem

    @property
    def base2(self) -> str:
        if self.n_syl == 1:
            if self.stem.endswith('a'):
                return "{}h".format(self.stem)

            else:
                #
                # for '-i' verbs, the vowel lengthens here, but since neither
                # IDIEZ orthography doesn't represent vowel length, this is
                # just an
                # identity.
                #
                return self.stem

        elif self.stem[-2:] in ('ia', 'oa'):
            return "{}h".format(self.stem[:-1])

        elif self.stem.endswith('hua'):
            if self.trans:
                if self.stem[-4] in self.vowels:
                    return "{}uh".format(self.stem[:-3])
                else:
                    return self.stem[:-3]
            else:
                return self.stem
        elif self.stem[-2:] in ('ma', 'mi'):
            return "{}n".format(self.stem[:-2])

        elif self.stem.endswith('ya'):
            return "{}x".format(self.stem[:-2])

        elif self.stem[-1] in ('a', 'i'):
            # check it is preceded by a single consonant
            if self.stem[-3:-1] in self.multi_char_cons:
                return self.stem[:-1]

            elif self.stem[-2] in self.cons and self.stem[-3] in self.vowels:
                return self.stem[:-1]

            else:
                return self.stem

        else:
            return self.stem

    @property
    def base3(self, stem):
        raise NotImplementedError

    @property
    def base4(self, stem):
        raise NotImplementedError