#Segmenter.py Synopsis

Segmenter.py was created using a sentence tree logic adopted from *Jurafsky and Myers* to segment text written in Bahasa Banjar into sentences.  

The program tokenizes a while loop to tokenize words by splitting lines at each space. Then, if the word ends with a question mark or exclamation mark, the program interprets this as the end of the sentence and moves to a new line. 
If the word ends in a period, the program interprets this as the end of the sentence unless the word is an abbreviation (e.g., 'No.', 'Alm.', 'Ir.', '...', 'S.D.', 'V.R.', 'J.'  "No., Alm., Ir., S.D., V.R., J", an epllipses, an ordinal number (e.g., "1."), or a number that has a decimal (e.., "1.54").  
    
Running this program on my test data led to 100% accuracy. However, the program does not account for all possible abbreviations, and these should be added to the program as they are discovered. 
