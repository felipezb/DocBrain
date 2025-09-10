import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def gerar_documento_ia(tipo, cliente, empresa, valor, prazo, observacoes):
    prompt = f"""
    Gere um documento do tipo {tipo} para o cliente {cliente}, da empresa {empresa}.
    O serviço tem valor de {valor} e prazo de entrega de {prazo}.
    Instruções adicionais: {observacoes}.
    """

    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um assistente que gera documentos comerciais."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=800
    )

    return resposta.choices[0].message.content.strip()
