import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def gerar_documento_ia(tipo, cliente, empresa, valor, prazo, observacoes):
    """
    Gera um documento comercial usando a API OpenAI.
    Retorna o texto gerado ou uma mensagem de erro.
    """
    if not openai.api_key:
        return "Erro: Chave da API OpenAI não configurada."

    prompt = (
        f"Gere um documento do tipo {tipo} para o cliente {cliente}, da empresa {empresa}.\n"
        f"O serviço tem valor de {valor} e prazo de entrega de {prazo}.\n"
        f"Instruções adicionais: {observacoes}."
    )

    try:
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
    except Exception as e:
        return f"Erro ao gerar documento: {str(e)}"
