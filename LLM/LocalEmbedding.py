from LLM.EmbeddingModel import EmbeddingModel


class LocalEmbedding(EmbeddingModel):

    def genera_embedding(self, testo):
        return [0.8, 0.3, 0.1]