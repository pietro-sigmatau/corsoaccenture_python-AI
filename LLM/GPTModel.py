from LLM.LLM_model import LLMModel


class GPTModel(LLMModel):

    def genera_risposta(self, prompt):
        return f"Risposta locale per {prompt}"