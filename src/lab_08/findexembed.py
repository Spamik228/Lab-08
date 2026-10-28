import numpy as np
from sentence_transformers import SentenceTransformer


def build_embeddings(corpus_chunks, model_name="all-MiniLM-L6-v2", output_dir="data/"):
    model = SentenceTransformer(model_name)

    # Генерація ембеддингів з прогрес-баром (на CPU займає кілька хвилин для середніх корпусів)
    embeddings = model.encode(corpus_chunks, show_progress_bar=True, convert_to_numpy=True)

    # L2-нормалізація векторів для ефективного косинусного пошуку через скалярний добуток
    faiss_normalize = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)

    # Збереження у форматі float32 .npy
    np.save(f"{output_dir}/embeddings.npy", faiss_normalize.astype(np.float32))
    return embeddings