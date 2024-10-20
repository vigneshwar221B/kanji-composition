async function processInput() {
    const jpText = document.querySelector('#jpInput').value;
    const outputDiv = document.querySelector('#kanji-composition');
    outputDiv.innerHTML = 'Loading...';

    if (!jpText.trim()) {
        outputDiv.innerHTML = 'Please enter some text.';
        return;
    }

    const kanjiArray = extractKanji(jpText);
    console.log(kanjiArray);

    if (kanjiArray.length === 0) {
        outputDiv.innerHTML = 'No kanji found.';
        return;
    }

    await displayKanji(kanjiArray);
}

function extractKanji(text) {
    return text.split('').filter(char => char.match(/[\u4E00-\u9FAF]/));
}

async function getKanjiData(kanji) {
    try {
        const response = await fetch(`https://kanjiapi.dev/v1/kanji/${kanji}`);
        return response.json();
    } catch (error) {
        return null;
    }
}

async function displayKanji(kanjiArray, selector="#kanji-composition") {
    const outputDiv = document.querySelector(selector);
    outputDiv.innerHTML = '';

    for (const kanji of kanjiArray) {
        const kanjiData = await getKanjiData(kanji);

        if (kanjiData) {
            const meanings = kanjiData.meanings.slice(0, 3).join(', ');
            outputDiv.innerHTML += `<p class="kanji">${kanjiData.kanji}: ${meanings}</p>`;
        } else {
            outputDiv.innerHTML += `<p class="kanji">${kanji}: Data not found</p>`;
        }
    }
}
