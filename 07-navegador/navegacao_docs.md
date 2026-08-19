# Demonstração: automação de navegador (Browser tool)

O Claude Code pode abrir um navegador real, navegar até uma página e extrair
o conteúdo renderizado (não apenas o HTML bruto). Abaixo, o resultado real de
uma navegação até a documentação oficial do Claude Code.

**URL visitada:** https://docs.claude.com/en/docs/claude-code/overview
(redirecionou para `code.claude.com`)

## Texto extraído da página

> Claude Code is an AI-powered coding assistant that helps you build
> features, fix bugs, and automate development tasks. It understands your
> entire codebase and can work across multiple files and tools to get things
> done.
>
> Claude Code runs on several surfaces: the terminal, IDE extensions, a
> desktop app, and the web.

Comando de instalação encontrado na página (macOS/Linux/WSL):

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Isso mostra que o Claude Code consegue: abrir páginas reais, ler o texto
visível (pós-JavaScript), navegar entre abas e — em outros cenários — clicar,
preencher formulários e interagir com páginas como um usuário faria.
