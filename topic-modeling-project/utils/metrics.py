# metrics.py

from sklearn.metrics import silhouette_score
from gensim.models import CoherenceModel

def calculate_silhouette_score(X, labels):
    return silhouette_score(X, labels)

def calculate_coherence_score(model, texts):
    coherence_model = CoherenceModel(model=model, texts=texts, dictionary=model.dictionary)
    return coherence_model.get_coherence()
