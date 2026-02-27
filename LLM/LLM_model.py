from abc import ABC, abstractmethod
class LLMModel(ABC):

    @abstractmethod #tutte le classi che vanno ad estendere questa classe qua devono generare qualcosa
    def genera(selfself, prompt):
        pass #ogni LLM che andremo a fare avrà "genera"
