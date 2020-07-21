# fst-nahuatl
This project is focused on applying Finite-State Transducers to modeling the 
morphology and orthography of a contemporary Nahuatl dialect (Western Sierra Nahuatl, nhi). 
This dialect has some significant internal variation which I will also try to 
capture eventually. For now, the models are built to most closely resemble the 
Nahuatl of Omitlán, Tepetzintla.

The primary deliverables of this project are:
1. Morphological analyzer/accepter
2. Spell Checker (uses the morphological accepter from 1)
3. Orthographical Normalization (already implemented in pure Python in a different repo).

## Resources
The following is a list of resources (grammars, books/transcripts, papers, etc) I am consulting for this project:
* Tenango Nahuatl grammar: https://www.sil.org/system/files/reapdata/79/10/32/7910324529403884548589500092074462468/nhi_Grammar.pdf
* OLAC Resource list: http://www.language-archives.org/language/nhi
* Launey (2011) "Introduction to Classical Nahuatl" - Classical Nahuatl Grammar (this is where the "base1/base2/base3/etc" nomenclature comes from): https://www.worldcat.org/title/introduction-to-classical-nahuatl/oclc/705001680
* Descriptive work on the Nahuatl of the Sierra Poblana: see Mitsuya...

## Todos

#### General
- [ ] Adjectives
- [ ] Particles
- [ ] Stem Guesser

#### NNCs
- [x] Support -tl, -tli, -n, -lli, -l Noun stems
- [x] Absolutive and plural suffixes
- [x] Possessive prefixes
- [x] Possessive plural suffixes
- [x] Diminutive Suffixes
- [x] Noun Compounding
- [ ] Adj-Noun Compoundinig
- [ ] Subject prefixes ('n-', 't-', etc)

#### VNCs
- [x] Standard Subject Prefixes
- [x] Object Prefixes
- [ ] Prefix honorific vowel harmony
- [ ] Tenango stress-sensitive Subject/Object Prefixes (e.g. "in-" instead of "ni-")
- [ ] Alternative nhi subj prefix ('se-')
- [x] Present for some stems
- [x] Preterite for some stems
- [ ] Future
- [ ] Imperfect
- [x] Optative
- [ ] Passive
- [ ] Noun Object incorporation
- [ ] Subject/Object person-number restrictions
