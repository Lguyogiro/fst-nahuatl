import re


class VerbalStem(object):
    def __init__(self, stem, transitive=False, es=False):
        self.stem = stem
        self.vowels = ["a", "e", "i", "o", "u"]
        self.cons = "bcdfghjklmnpqrstvwxz"
        self.multi_char_cons = ["ch", "tl", "tz"]
        self.numVPattern = re.compile("|".join(self.vowels))
        self.n_syl = self.count_syllables()
        self.is_spanish = es
        self.trans = transitive

    def count_syllables(self):
        num_syl = 0
        search_stem = self.stem

        def find_next_vowel(s):
            for i, ch in enumerate(s):
                next_ch = s[i + 1] if i+1 < len(s) else ''

                if ch in self.vowels:
                    vowlen = 1
                    if ch == 'u' and next_ch in 'iae':
                        vowlen += 1
                    char_incr = i + vowlen
                    if char_incr <= len(s):
                        return s[char_incr:]
                    else:
                        return ''
            else:
                return None

        while True:
            search_stem = find_next_vowel(search_stem)
            if search_stem is not None:
                num_syl += 1
            else:
                return max([1, num_syl])

    @property
    def present(self) -> str:
        return self.stem

    @property
    def imperfect(self):
        if self.stem.endswith('ia'):
            return self.stem[:-2] + "a"
        else:
            return self.present

    @property
    def base2(self) -> str:
        if self.n_syl == 1:
            if self.stem.endswith('a'):
                return "{}h".format(self.stem)

            else:
                #
                # for '-i' verbs, the vowel lengthens here, but since neither
                # IDIEZ nor SEP orthographies doesn't represent vowel length,
                # this is just an identity.
                #
                return self.stem

        elif self.stem.endswith('ia'):
            #
            # In Classical Nahuatl, this verbs' base 2 stem would end in 'ih'.
            # In nhi the preterite they go from "...ih#" -> "...e#". I use
            # the multichar symbols {i} and {H} in order to enable this
            # phonological process.
            #
            return format(self.stem[:-2]) + "%{i%}%{H%}"

        elif self.stem.endswith('oa'):
            return self.stem[:-1] + "h"

        elif self.stem.endswith('ca'):
            return self.stem

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
    def base3(self):
        if self.stem[-2:] in ('oa', 'ia'):
            return self.stem[:-1]
        else:
            return self.stem


def generate_stem_lexical_entries(canonical, transitivity='iv'):
    if transitivity not in ('iv', 'tv', 'tv2'):
        raise KeyError("`transitivity` must be either iv (intransitive), tv "
                       "(transitive), or tv2 (bitransitive)")

    stem = VerbalStem(canonical)
    all_stems = [stem.present, stem.imperfect, stem.base2, stem.base3]
    cont_lexicons = ["PresentTense", "Imperfect", "Base2Suffixes", "Base3Suffixes"]

    lexical_entries = [
        "{}%<v%>%<{}%>:{}%>  {};".format(canonical,
                                         transitivity,
                                         stem,
                                         cont_lexicons[i])
        for i, stem in enumerate(all_stems)
    ]
    return lexical_entries
