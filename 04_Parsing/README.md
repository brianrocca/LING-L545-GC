# Results of UD Pipe Parsing

Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |    100.00 |    100.00 |    100.00 |    100.00
XPOS       |    100.00 |    100.00 |    100.00 |    100.00
Feats      |    100.00 |    100.00 |    100.00 |    100.00
AllTags    |    100.00 |    100.00 |    100.00 |    100.00
Lemmas     |    100.00 |    100.00 |    100.00 |    100.00
UAS        |     81.15 |     81.15 |     81.15 |     81.15
LAS        |     77.15 |     77.15 |     77.15 |     77.15

# Inspect 10 sentences: What errors were made?

## Sentence 1
![](sentence1.png)

    Baler adalah munisipalitas yang terletak di provinsi Aurora, Filipina.

*Gloss:*

    Baler is municipality that located in province Aurora, Philippines.

This tree is well-formed. “Munisipalitas” is the head of the predicate and should therefore be the root. The subject (Baler) and copula verb are governed by the root. “Terletak” is goverened by “municipalitas” and forms the head of a new clause.  

## Sentence 2
![](sentence2.png)

    Pencurian dan perampokan juga sangat jarang terjadi di wilayah ini.

*Gloss:*

    Theft and robbery also very rarely happen/occur in region this. 

“Terjadi” is the root of the tree because it’s the head of the predicate. The adverb phrase “...juga sangat jarang...” (also very rarely) is goverened by the root because the phrase is part of the predicate. Finally, there are two nouns in the subject joined by “dan” (and). The first noun takes the second one as a dependent, and the second noun takes the conjunction as its dependent.  

## Sentence 3
![](sentence3.png)

    Laut Sulawesi merupakan     tempat bagi banyak spesies ikan dan makhluk bawah air.

*Gloss:*

    Sea Sulawesi is-composed-of place for   many species fish and creature under water

One thing I question about this tree is the marking of the NP “makhluk bawah air”, which translates to "underwater creature". I’m not sure that “bawah” should be considered a noun. I thought it should be considered an adjective modifying “air” (water), but the Indonesian dictionary Indodict.com says that it is an adverb. Either way, I question calling it a noun.  


## Sentence 4
![](sentence4.png)

    Bahkan ia menolak telah menikah dan memiliki anak dari Sakuntala.

*Gloss:*

    In fact he  refused  has(pres.perf) marry and have child from Sakuntala. 

The only thing I questioned about this tree was “dari” (from) being called a “case” marker. This struck me because nouns aren’t modified for case in Indonesian. However, the CONLLU website says, “Case can also be a lexical feature of adpositions and describe the case meaning that the adposition contributes to the nominal in which it appears. (This usage of the feature is typical for languages that do not have case morphology on nouns….” Because of this, I would not disagree with the tree. 

## Sentence 5
![](sentence5.png)

    Ramanuja adalah seorang teolog, filsuf, dan juga penafsir kitab suci Hindu. 

*Gloss:*

    Ramanuja is  a theologian, philosopher, and interpreter (holy-)book holy Hundi. 

I agree with this tree. “Adalah” ("is") is the start of the predicate, but, because it’s a copula verb, the root is “teolog” ("theologian"). While “theologian, philosopher, and interpreter” is a noun phrase, “theologian is the root because it’s the first noun in the phrase. The other two nouns are dependents of “theologian," and the conjunction “dan” is a dependent of the final noun in the phrase. I agree with this interpretation. The only thing I disagree with is “kitab” being marked as a compound noun with “penafsir.” I believe “suci” is an adjective modifying “kitab," but “kitab” does not form a compound noun with “penafsir." 

## Sentence 6
![](sentence6.png)

    Kamila bertanya kenapa Eyang Tini menyuruhnya naik mobil?

*Gloss:*

    Kamila asked why Grandma Tini told her to get in the car? 

This tree looks appropriate. “Bertanya” is a verb meaning “to question”, and it should be the root of the tree. “kenapa” is an adverb modifying “menyuruhnya” (told him). So an arrow is drawn to “kenapa” because it depends on the verb.  “Eyang Tini” (Grandma Tini) is marked as “flat” because it is a NP without a head.  

## Sentence 7
![](sentence7.png)
Sementara itu, seorang pelawak merayu seorang pembantu rumah tangga.

*Gloss:*

While that, a comedian seduces a maid household. 

Even though this tree has a scary red line, it looks okay. It seems that a red line is used here because there is a comma after the adverb phrase “semantara itu” (translating to “meanwhile”). Punctuation usually always depends on the verb, but in this case, it depends on this adverb phrase. I would also disagree with calling “sementara itu” a conjunction + determiner. “Itu” is a determiner meaning “that”, but “sementara” should be labelled as an adverb. Then the arrow marking “sementara” as a dependent o “merayu” should be labelled “mark” instead of “cc” because it’s actually a subordinating conjunction instead of a coordinating conjunction. 

## Sentence 8
![](sentence8.png)
    Karakter utama di permainan ini bernama Claude Speed.

*Gloss:*

    Character main in game this named Calude Speed. 

The root is appropriate in this tree: “bernama” (“is named”). The NP “karakter utama” (“main character”) is governed by the root as well as the object “Clause Speed”. Because “Claude Speed” is a proper noun, it is headless and therefore marked as “flat”. 

## Sentence 9
![](sentence9.png)
Desa ini memiliki kodepos 86262.

    *Gloss:*

    Village this has postal code 86262.

This tree is beautiful. The main verb “memiliki” (“to possess”) is the root. It governs the subject “desa” (village”) and the object in the predicate (“postal code 86262”).  

## Sentence 10
![](sentence10.png)

    Dan bagaimanakah kamu lihat keadaannya sekarang?

*Gloss:*

    And  how you see his/her/its-circumstance now?

“Dan” marks the beginning of a subordinating clause, but I’m not sure that applies in this sentence unless it is seen as a continuation of a previous sentence or the previous speaker’s turn. Otherwise, the tree looks appropriate. 

