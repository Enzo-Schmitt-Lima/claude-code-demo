# Demonstração: delegação a subagentes (Agent tool)

Este arquivo é o **relatório real**, gerado por um subagente `Explore` que foi
despachado para investigar a própria pasta deste projeto de demonstração —
sem que o agente principal (esta conversa) precisasse ler cada arquivo
manualmente. Isso mostra como o Claude Code pode paralelizar/isolar tarefas
de exploração em subagentes especializados, preservando o contexto da
conversa principal.

## Tarefa dada ao subagente
"Liste todos os arquivos do projeto de demo e diga, em uma linha por pasta,
qual capacidade cada uma demonstra."

## Resposta do subagente (Explore)

### Arquivos encontrados
- `01-arquivos-e-codigo/`: task_manager.py, test_task_manager.py, resultado_dos_testes.txt
- `02-terminal-bash/`: sysinfo.txt
- `03-busca-e-exploracao/`: busca_exemplo.txt
- `04-git-versionamento/`: git_demo.txt
- `05-pesquisa-web/`: pesquisa_claude_code.md
- `06-subagentes/`: (vazia no momento da varredura)
- `07-navegador/`: (vazia no momento da varredura)
- Raiz: `.gitignore`

### Capacidade por pasta
- **01-arquivos-e-codigo**: criação de arquivos/código — módulo Python `TaskManager`
  baseado em dataclass, suíte de testes unittest e resultado da execução salvo.
- **02-terminal-bash**: execução de terminal/bash — roda comandos de shell
  (date, df, free, ps) e registra info do sistema em arquivo.
- **03-busca-e-exploracao**: busca/exploração — usa grep/find para localizar
  definições de função/classe e listar todos os arquivos do projeto.
- **04-git-versionamento**: controle de versão git — mostra histórico de
  commits (git log) e status criados durante a sessão.
- **05-pesquisa-web**: pesquisa web — usa WebSearch para buscar
  "Claude Code CLI Anthropic features 2026" e resume com fontes.
- **06-subagentes / 07-navegador**: pastas existiam mas ainda vazias no
  momento em que o subagente rodou (preenchidas logo depois).
