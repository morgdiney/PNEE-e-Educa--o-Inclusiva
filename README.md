# Projeção de Impacto da Nova PNEE: O "Boom" de Matrículas sem Laudo

##  O Problema de Negócio (Public Policy)
A nova Política Nacional de Educação Especial (PNEE) propõe a dispensa de laudo médico para o Atendimento Educacional Especializado (AEE). Historicamente, a exigência do laudo atuava como uma barreira de entrada, represando a demanda real.

**A pergunta central:** Se essa barreira cair, o sistema educacional atual suporta a demanda reprimida? O modelo linear histórico é suficiente para prever 2030?

##  A Hipótese (Data Science)
A análise histórica simples (Regressão Linear) subestima o impacto de mudanças legislativas estruturais.
Neste projeto, modelamos um cenário de **Quebra Estrutural**, onde a variável "Fim do Laudo" atua como um catalisador, transformando o crescimento linear em **crescimento exponencial** no curto prazo (Efeito de Demanda Reprimida).

## Resultados da Simulação
1.  **Migração de Matrículas:** O modelo prevê uma queda acentuada nas matrículas de escolas especializadas (segregadas) devido à nova diretriz de prioridade na rede regular.
2.  **O "Efeito Tesoura":** Enquanto a rede especializada encolhe, a rede regular sofre uma explosão de demanda.
3.  **Alerta de Gestão:** A projeção indica que, sem a barreira do laudo, o número de alunos PAEE pode dobrar mais rápido do que a infraestrutura (salas de recursos/professores) consegue crescer.

## Tecnologias e Métodos
* **Python (Pandas/Numpy):** Simulação de cenários e manipulação de dados.
* **Matplotlib:** Visualização de dados comparativa (Histórico vs. Projeção).
* **Modelagem:** Comparação entre crescimento Linear (Status Quo) e Exponencial (Nova PNEE).

---
*Projeto desenvolvido com foco em Análise de Dados para Políticas Públicas.*
