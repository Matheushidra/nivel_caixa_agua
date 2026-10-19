"""
Sistema de Monitoramento de Reservatório de Água
Disciplina: Desenvolvimento de Sistemas / Algoritmos e Programação
Descrição: Simulação de monitoramento de níveis de água com alertas coloridos via terminal utilizando Colorama.
"""

import time
from colorama import init, Fore, Style

# Inicializa o colorama. 
# autoreset=True garante que a formatação padrão seja restaurada automaticamente após cada print.
init(autoreset=True)

# 1. Estrutura de dados contendo as configurações de cada nível
NIVEIS_RESERVATORIO = [
    {
        "nivel": 1,
        "situacao": "Muito baixo (crítico)",
        "cor": Fore.RED,
        "descricao": "Nível de emergência: risco de esgotamento total."
    },
    {
        "nivel": 2,
        "situacao": "Baixo",
        "cor": Fore.YELLOW,
        "descricao": "Atenção: capacidade reduzida, evitar desperdícios."
    },
    {
        "nivel": 3,
        "situacao": "Médio",
        "cor": Fore.GREEN,
        "descricao": "Operação normal: volume adequado para consumo regular."
    },
    {
        "nivel": 4,
        "situacao": "Alto",
        "cor": Fore.CYAN,
        "descricao": "Volume elevado: monitorar para evitar transbordamento."
    },
    {
        "nivel": 5,
        "situacao": "Muito alto (alerta)",
        "cor": Fore.BLUE,
        "descricao": "Nível máximo atingido: acionar comportas ou escoamento."
    }
]


def formatar_alerta_nivel(dados_nivel: dict) -> str:
    """
    Formata e retorna a mensagem de alerta com a respectiva cor e estilos aplicados.
    Restaura explicitamente o padrão ao final da string via Style.RESET_ALL.
    """
    cor = dados_nivel["cor"]
    nivel = dados_nivel["nivel"]
    situacao = dados_nivel["situacao"]
    descricao = dados_nivel["descricao"]

    mensagem = (
        f"{Style.BRIGHT}{cor}[NÍVEL {nivel}] {situacao.upper()}\n"
        f"  └─ Status: {descricao}{Style.RESET_ALL}"
    )
    return mensagem


def simular_monitoramento():
    """
    Executa uma simulação visual de monitoramento do reservatório,
    percorrendo todos os níveis pré-definidos.
    """
    print(f"{Style.BRIGHT}{Fore.WHITE}{'='*60}")
    print("   SISTEMA DE MONITORAMENTO EM TEMPO REAL - RESERVATÓRIO")
    print(f"{'='*60}{Style.RESET_ALL}\n")

    for item in NIVEIS_RESERVATORIO:
        alerta = formatar_alerta_nivel(item)
        print(alerta)
        print("-" * 60)
        time.sleep(1)  # Intervalo de 1 segundo entre leituras simuladas

    print(f"\n{Fore.LIGHTBLACK_EX}[Fim da simulação de monitoramento. Sistema em espera.]{Style.RESET_ALL}\n")


if __name__ == "__main__":
    simular_monitoramento()
