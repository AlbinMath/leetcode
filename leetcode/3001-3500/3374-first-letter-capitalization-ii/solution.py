import pandas as pd

def capitalize_content(user_content: pd.DataFrame) -> pd.DataFrame:
    def transform_word(word: str) -> str:
        if not word or not word[0].isalpha():
            return word
        
        parts = word.split('-')
        if len(parts) >= 2 and all(p.isalpha() for p in parts):
            return '-'.join(p.capitalize() for p in parts)
        
        return word[0].upper() + word[1:].lower()

    def transform_text(text: str) -> str:
        return ' '.join(transform_word(w) for w in text.split(' '))

    return pd.DataFrame({
        'content_id': user_content['content_id'],
        'original_text': user_content['content_text'],
        'converted_text': user_content['content_text'].apply(transform_text)
    })
