# split-waw-arabic
Separate the conjunction Waw from Arabic words

## Main Advantage
This program helps to normalize Arabic text and reduce word's variations. 

## Examples
1. وصديقاتها changed to و صديقاتها 
2. وتقوم changed to و تقوم
3. وتفعيل changed to و تفعيل


## Methods
The implementation incudes the following two methods: 
1. Get the root of the word, if the Waw و still in the root letters, then the Waw is original, else, split Waw and the word.
2. Use AySpell speller to check the word, if the word + Waw و is in the dictionary, then the Waw is original, else, split Waw and the word. 

## References
* The ISRI Arabic Stemmer https://www.nltk.org/_modules/nltk/stem/isri.html
* aspell-python - Python bindings for GNU aspell https://github.com/WojciechMula/aspell-python

## Usage
```python process_waw_rooting.py [-h] -i INFILE -o OUTFILE```

```python process_waw_ayspell.py [-h] -i INFILE -o OUTFILE```


## How to contribute
Your contributions to improve the code are welcomed. Please follow the steps below.
1. Fork the project.
2. Modify the code, test it, make sure that it works fine. 
3. Make a pull request.

Please consult [github help](https://help.github.com/) to get help.