
# RhymeYomi





## Overview

RhymeYomi, named after a term used in the Japanese rap battle scene to refer to the act of predicting your opponent's next line, is an application designed to process a Japanese word and return other Japanese or English words that rhyme with it. It can do basic rhyme-searching using simple vowel parallels, but is also capable of recognizing double-vowel syllable pairs, like "a" and "i" creating "ai", or "e" and "i" creating "ei".

## Installation

I would like to create an installer for RhymeYomi very soon, but for now, it is simply a .zip file to be downloaded from the "releases" section. After downloading the .zip file, extract it. There are going to be a *lot* of files in the main directory, but just ignore these and look for rhymeyomi.exe. Run it, and it should work smoothly.
    
## Usage

The UI contains a search bar and a results field. In the search bar, enter the word you are wanting to find rhymes for, in kana (either hiragana or katakana). 

After you have entered your search, click the button next to the search bar and the program will return a list of words that rhyme with your query. The left-hand side of the results field will display the word in kanji, and the right-hand side will display the word in katakana.

It is *very* important that your search only be in kana, or else it will return an error by default, because the program is not made to handle input besides kana. The reason the application is set up this way is because kanji has different readings depending on context, and it would be not only extremely time-consuming to account for every reading of every individual kanji, but it would even still fail to consider words that are newly created/made-up, or uncommon names that are read differently from words.

## Error Guide
001 - You are feeding the program invalid characters. All kana, even obsoleted characters, are accounted for in RhymeYomi's character dictionary. If you are using obsoleted hiragana, try typing your query in katakana instead. 

## Acknowledgements

The word database currently being used, as of RhymeYomi Alpha 0.0.3, is the Vocab Database created by Matsushita Laboratory for Language Learning, which can be found [here](http://www17408ui.sakura.ne.jp/tatsum/database.html). It contains about 60,000 Japanese (and some English) words, and for the purpose of this program, the two most relevant columns of the main sheet have been extracted and moved to a smaller sheet, which is used as the program's dictionary.

There are lyrical examples in the assets folder compiled manually, but they are not functional yet, so they will not be elaborated on in the readme yet.

The font being used in the UI is UD-Digi Kyokasho, which can be downloaded [here](https://eng.m.fontke.com/font/24526460/download/).

The logo was created by my friend (genius) [kobeysucks](https://www.instagram.com/kobeysucks/), thank you so much for such a cool logo.

Huge special thanks to Takumi Saito/[Flo4ttt](https://soundcloud.com/flo4ttt) for giving me the inspiration to write Japanese rap for the first time after years of only listening and producing it. I wouldn't have ever needed to use a program like this if it weren't for his help, and I probably wouldn't have learned half as much about Python if I hadn't made this project. 

Also big special thanks to my friend [Nodrance](https://github.com/Nodrance) and my father [gaikman2015](https://github.com/gaikman2015) for looking over my code and helping me when I needed some assistance. Thank you as well to my best friend [theteamaker](https://github.com/theteamaker) for not only looking at my code, but being extremely encouraging and letting me know (in a way that frankly made me emotional) how proud she is of the progress I've made learning Python this year. 

Lastly, of course, a big thank you to my girlfriend Emma Taylor for supporting me all the time (even when I get mad at Python) and being a warm presence no matter what the situation.

