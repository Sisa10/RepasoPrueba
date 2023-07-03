import string

import openai
from pydantic import BaseModel


class Document(BaseModel):
    prompt: str = ''



def inference(prompt: str) -> list:
    #openai.organization = 'org-PukKJ0lEU2b0jyEJplPr0m80'

    #openai.api_key = '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'
    openai.organization = 'org-spg5Kv9BlJGbfGznEb5AE93m'
    openai.api_key = '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'
    print('[PROCESANDO]'.center(40,'-'))
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """Eres un profesor de programación para niños, genera una explicación para el tema que se te proporcione"
            E.G: Programación
            -Es como armar un rompecabezas donde cada pieza forma el sistema completo"""},
            {"role": "user", "content": prompt}
        ]
    )
    content = completion.choices[0].message.content
    total_tokens = completion.usage.total_tokens

    print('[SE TERMINÓ DE PROCESAR]'.center(40, '-'))
    return [content, total_tokens]
