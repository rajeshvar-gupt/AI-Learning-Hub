"""TF-IDF retrieval over original invented descriptions; not personalized."""
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

BOOKS = [
    {"id": "python", "title": "Python Workshop", "description": "python programming functions data files exercises"},
    {"id": "data", "title": "Tables and Questions", "description": "python data analysis tables statistics exercises"},
    {"id": "ml", "title": "Learning from Examples", "description": "machine learning data statistics models python"},
    {"id": "sql", "title": "Query Notebook", "description": "sql tables data analysis queries databases"},
    {"id": "garden", "title": "A Small Garden", "description": "soil flowers plants compost garden"},
    {"id": "space", "title": "Night Sky Notes", "description": "stars planets astronomy telescope space"},
]


def recommend(book_id, k=3, books=None):
    books = BOOKS if books is None else books
    if isinstance(k, bool) or not isinstance(k, int) or k < 1:
        raise ValueError("k must be a positive integer")
    ids = [book["id"] for book in books]
    if len(ids) != len(set(ids)):
        raise ValueError("book IDs must be unique")
    if book_id not in ids:
        raise ValueError("unknown book ID")
    descriptions = [book["description"] for book in books]
    try:
        matrix = TfidfVectorizer(stop_words="english").fit_transform(descriptions)
    except ValueError as error:
        raise ValueError("catalog must contain usable vocabulary") from error
    query = ids.index(book_id)
    scores = cosine_similarity(matrix[query], matrix).ravel()
    ranked = sorted((i for i in range(len(books)) if i != query and scores[i] > 0),
                    key=lambda i: (-scores[i], ids[i]))
    return [dict(id=ids[i], title=books[i]["title"], similarity=float(scores[i])) for i in ranked[:k]]


if __name__ == "__main__":
    print(json.dumps(recommend("python"), indent=2))
