from pathlib import Path
from agno.agent import Agent
from agno.models.openai import OpenAIResponses
from agno.skills import LocalSkills, Skills
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()
SKILLS_DIR = Path(__file__).parent / "skills"

class TriagemResponse(BaseModel):
    cor: str = Field(description="A cor da triagem: verde, amarelo, laranja, vermelho")

class TriagemAgent:

    @classmethod
    def build_agent(cls):
        return Agent(
            name="TriagemAgent",
            model=OpenAIResponses(id="gpt-5-mini"),
            description=(
                "Realiza a triagem de um paciente com base nos dados de entrada; "
                "use a skill triagem para realizar a triagem."
            ),
            instructions=["Use a skill triagem-veterinaria para realizar a triagem."],
            output_schema=TriagemResponse,
            skills=Skills(loaders=[LocalSkills(str(SKILLS_DIR))]),
        )

    @classmethod
    def mount_prompt(self, frequencia_cardiaca, frequencia_respiratoria, temperatura, peso, queixa, observacao):
        return f"""
            Frequencia Cardiaca: {frequencia_cardiaca} bpm
            Frequencia Respiratoria: {frequencia_respiratoria} mpm
            Temperatura: {temperatura} °C
            Peso: {peso} kg
            Queixa: {queixa}
            Observacao: {observacao}
        """