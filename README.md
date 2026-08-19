# Demo: capacidades do Claude Code

Este projeto foi criado pelo próprio Claude Code para demonstrar, com
**exemplos reais e executados**, o que ele consegue fazer. Cada pasta abaixo
contém a prova concreta de uma capacidade — não é só descrição, é o
resultado real de rodar cada coisa nesta máquina.

| Pasta | Capacidade demonstrada | O que tem lá |
|---|---|---|
| [`01-arquivos-e-codigo/`](01-arquivos-e-codigo/) | Escrever e editar código | Um módulo Python (`TaskManager`) + suíte de testes `unittest` + resultado da execução (`4 passed`) |
| [`02-terminal-bash/`](02-terminal-bash/) | Executar comandos no terminal | Info real do sistema (data, disco, memória, processos) coletada via `bash` |
| [`03-busca-e-exploracao/`](03-busca-e-exploracao/) | Buscar/explorar código | Resultado de `grep`/`find` localizando funções, classes e arquivos do projeto |
| [`04-git-versionamento/`](04-git-versionamento/) | Controle de versão (Git) | Repositório Git real, inicializado e com 3 commits incrementais |
| [`05-pesquisa-web/`](05-pesquisa-web/) | Pesquisar na web | Busca real sobre "Claude Code features 2026", resumida com fontes |
| [`06-subagentes/`](06-subagentes/) | Delegar tarefas a subagentes | Relatório escrito por um subagente `Explore` despachado para investigar este próprio projeto |
| [`07-navegador/`](07-navegador/) | Automação de navegador | Conteúdo extraído de uma navegação real até `code.claude.com` |

## Outras capacidades do Claude Code (não demonstradas em arquivo, mas disponíveis nesta sessão)

- **Artifacts**: publicar páginas HTML/Markdown interativas e compartilháveis
  — veja o guia visual publicado junto com esta resposta.
- **Integrações MCP conectadas** nesta conta: Google Calendar, Gmail, Google
  Drive, Notion, Figma, e um quadro visual (board/canvas). O Claude Code pode
  ler, criar e editar conteúdo nessas ferramentas quando autorizado.
- **Skills**: rotinas reutilizáveis pré-configuradas (ex.: gerar `.docx`,
  `.pptx`, `.xlsx`, `.pdf`, revisão de código, design de artifacts, etc.).
- **Agendamento**: criar tarefas recorrentes/agendadas (`schedule`, `loop`,
  cron).
- **Edição multi-arquivo em larga escala**, refatoração, debugging e revisão
  de segurança de código.

## Como reproduzir

```bash
cd 01-arquivos-e-codigo && python3 -m unittest test_task_manager -v
cat 02-terminal-bash/sysinfo.txt
cat 03-busca-e-exploracao/busca_exemplo.txt
git log --oneline --graph --decorate
cat 05-pesquisa-web/pesquisa_claude_code.md
cat 06-subagentes/relatorio_subagente.md
cat 07-navegador/navegacao_docs.md
```
