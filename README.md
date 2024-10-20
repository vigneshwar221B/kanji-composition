# Kanji Composition

## Overview

The **Kanji Composition** is a web application that allows users to input Japanese text and retrieve the meanings of individual kanji characters. This tool is particularly useful for learners of Japanese, as it provides an easy way to understand kanji compositions and their meanings. This can also be used in your anki cards.

[Kanji Composition](https://vigneshwar221b.github.io/kanji-composition/)

## Anki usage

Add the below code to your card template

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