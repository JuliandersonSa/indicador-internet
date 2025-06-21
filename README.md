# Indicador de Qualidade da Conexão Residencial (IQCR)

Este projeto apresenta a construção de um indicador baseado em dados reais para avaliar a performance da internet contratada (200 Mbps).

## Objetivo

Avaliar a estabilidade e qualidade da conexão de internet residencial usando um índice percentual chamado **IQCR**.

## Fórmula

IQCR = (Velocidade média de download / Velocidade contratada) × 100

## Ferramentas utilizadas

- Python 3 + speedtest-cli
- Crontab (agendamento automático)
- CSV para registro de dados
- GitHub Pages para publicação

## Estrutura do projeto

- `dados/` → arquivos `.csv` com as coletas
- `scripts/` → script Python e gráfico `.png`
- `analise/` → análise final em PDF
- `index.html` → site publicado via GitHub Pages

## Site publicado

Acesse: [https://JuliandersonSa.github.io/indicador-internet](https://JuliandersonSa.github.io/indicador-internet)

---

> Trabalho acadêmico - Uninter - 2025

