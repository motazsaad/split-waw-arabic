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

## Usage
```python process_waw_rooting.py [-h] -i INFILE -o OUTFILE```

```python process_waw_ayspell.py [-h] -i INFILE -o OUTFILE```
