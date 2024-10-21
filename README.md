# Kanji Composition

## Overview

The **Kanji Composition** is an application that allows users to input Japanese text and retrieve the meanings of individual kanji characters. This tool is particularly useful for learners of Japanese, as it provides an easy way to understand kanji compositions and their meanings. This can also be used in your anki cards.

[Kanji Composition](https://vigneshwar221b.github.io/kanji-composition/)

## Anki usage

1. Install python
2. Clone the repo
```sh
git clone https://github.com/vigneshwar221B/kanji-composition.git
cd kanji-composition
```
3. Make changes to the fields in `main.py`
```python
    deck = "Japanese"

    word_field = "Word"
    info_field = "Info" # field to add the kanji meanings
```
4. run `python main.py`

Alternatively, You can also add the below code to your card template (Not recommended as it makes a http call for every card causing delay)

```html
<div id="kanji-composition"></div>
<script src="https://vigneshwar221b.github.io/kanji-composition/main.js"></script>

<script>
	(function() {
        const word = "{{Word}}";
        displayKanji(extractKanji(word));
    })();
</script>
```

## Acknowledgements

[Kanji API](https://kanjiapi.dev/) for providing kanji data.