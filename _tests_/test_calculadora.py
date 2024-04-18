# 1 - Bibliotecas, frameworks e referências externas
import pytest

# Funções que serão testadas
from calculadora.calculadora import somar_dois_numeros, subtrair_dois_numeros, multiplicar_dois_numeros, dividir_dois_numeros

# 2 - Testes

def test_somar_dois_numeros():
    
    # Padrão/ Standard AAA (se diz Triple A/ 3A) = Arrange/preparar os dados, Act/execute, Assert/validar
    
    # ARRANGE/ Prepara/Configura
    # Dados entrada e saída
    num1 = 5
    num2 = 7
    resultado_esperado = 12
    
    # ACT/ Executa 
    resultado_obtido = somar_dois_numeros(num1, num2)
    
    # ASSERT/ Valida
    
    assert resultado_esperado == resultado_obtido

