from esercizio.Validator import Validator
from esercizio.Richiesta import Richiesta
from esercizio.Pipeline import Pipeline


pipeline_1 = Pipeline(Validator(), Richiesta())
pipeline_2 = Pipeline(GPTModel(), LocalEmbedding())

result_1=pipeline_1.esegui("Lista finale")
