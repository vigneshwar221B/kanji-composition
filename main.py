import json
import requests

with open('./data/kanjiapi.json', 'r', encoding='utf-8') as f:
    kanji_data = json.load(f)

def get_kanji_meanings(word):
    meanings = []
    for char in word:
        if char in kanji_data['kanjis']:
            char_info = kanji_data['kanjis'][char]
            # Limit meanings to a maximum of 3
            limited_meanings = char_info['meanings'][:3]
            meanings.append(f"{char} - {', '.join(limited_meanings)}")
    return "<br>".join(meanings)

def update_anki_cards(deck_name, note_type):
    response = requests.post('http://localhost:8765', json={
        'action': 'findNotes',
        'version': 6,
        'params': {
            'query': f'deck:{deck_name}'
        }
    })
    
    note_ids = response.json()['result']
    total_notes = len(note_ids)

    for index, note_id in enumerate(note_ids):
        response = requests.post('http://localhost:8765', json={
            'action': 'notesInfo',
            'version': 6,
            'params': {
                'notes': [note_id]
            }
        })
        
        notes_info = response.json()['result']
        for note in notes_info:
            word = note['fields']['Word']['value']
            kanji_meanings = get_kanji_meanings(word)

            response = requests.post('http://localhost:8765', json={
                'action': 'updateNoteFields',
                'version': 6,
                'params': {
                    'note': {
                        'id': note['noteId'],
                        'fields': {
                            'Info': kanji_meanings
                        }
                    }
                }
            })

            if response.status_code == 200:
                result = response.json()
                if result.get('error') is None:
                    print(f"{index + 1}/{total_notes} done")

if __name__ == '__main__':
    update_anki_cards('Japanese', 'Basic')
