# 📄 Sistema de Gerenciamento e Emissão de Relatórios Pedagógicos

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-blueviolet)](https://github.com/TomSchimansky/CustomTkinter)
[![SQLite3](https://img.shields.io/badge/Database-SQLite3-003B57?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Google Drive API](https://img.shields.io/badge/Cloud-Google%20Drive%20API%20v3-4285F4?logo=googledrive&logoColor=white)](https://developers.google.com/drive)
[![python-docx](https://img.shields.io/badge/Docx%20Engine-python--docx-2B579A?logo=microsoftword&logoColor=white)](https://python-docx.readthedocs.io/)

Aplicação desktop corporativa de alta performance desenvolvida em **Python** para automatizar o ciclo completo de planejamento de aulas, geração de relatórios pedagógicos em arquivos Microsoft Word (`.docx`) com formatação institucional e upload automatizado para pastas compartilhadas do **Google Drive**.

---

## 🎯 Contexto e Problema de Negócio

Em instituições de ensino e projetos sociais que atendem múltiplos polos e programas pedagógicos (como *Projeto Crescendo com Música*, *Juventude*, entre outros), o preenchimento manual de relatórios mensais gera:
* **Perda de tempo:** Professores gastando horas formatando tabelas repetitivas no Word.
* **Erros de padronização:** Desalinhamento de templates institucionais, fontes divergentes e perda de cabeçalhos/rodapés.
* **Falta de controle de entrega:** Relatórios espalhados por e-mails ou pendrives sem centralização em nuvem.

Este sistema resolve esse gargalo através de um ecossistema integrado: desde a interface de cadastro de aulas diárias até a entrega do relatório assinado e organizado na hierarquia de pastas da instituição no Google Drive.

---

## ✨ Principais Funcionalidades

### 🔐 1. Autenticação e Controle de Acesso
* Sistema de login com validação de credenciais contra banco de dados relacional **SQLite**.
* Sessão persistente por professor com carregamento automático das disciplinas e templates vinculados.
* Campo de senha com alternância de visibilidade e estilização refinada.

### 👩‍🏫 2. Gestão de Professores e Disciplinas
* Visualização moderna em cards com anéis de destaque em cores neon.
* Cadastro dinâmico de professores com criação automatizada de estrutura física de pastas.
* Cadastro de novas disciplinas por professor com **auto-refresh reativo** na interface gráfica.

### 📝 3. Cadastro Inteligente de Conteúdos
* Seleção intuitiva de modelos pedagógicos com carregamento reativo de turmas vinculadas.
* Opção de preenchimento por data atual ou seleção retroativa de datas.
* Armazenamento estruturado no banco de dados com integridade referencial.

### 📑 4. Engenharia de Documentos Word (`.docx`)
* Preenchimento automatizado de templates Word preservando 100% da identidade visual institucional.
* Injeção dinâmica de linhas e dados em tabelas conforme a quantidade de turmas/aulas cadastradas.
* Inserção de assinatura digital preservando dimensões e proporção original.
* Sistema de backup local versionado por professor, modelo e data (`Professores/<Nome>/<Disciplina>/backup<Modelo>/`).

### ☁️ 5. Integração com Google Drive API v3 (OAuth 2.0)
* **Fluxo OAuth 2.0 Desktop:** Autenticação segura com geração de `token.json` e renovação silenciosa em segundo plano via `refresh_token`.
* **Navegação Recursiva em Árvore:** Criação automática e sem duplicações da hierarquia institucional:
  ```text
  📁 Pasta Compartilhada (ID Raiz)
  └── 📁 2026 (Ano Vigente)
      └── 📁 Crescendo com Música (Projeto)
          └── 📁 Matheus (Professor)
              └── 📁 Outubro (Mês do Relatório)
                  └── 📄 RelatorioPCMVioloncelo06-10-2026.docx
  ```
* **Mapeamento Institucional (De-Para):** Tradução automática de códigos internos de modelo (ex: `PCM` ➔ `"Crescendo com Música"`).
* **Upload Multipart com Suporte Corporativo:** Suporte a Drives Compartilhados do Google Workspace (`supportsAllDrives=True`).
* **Proteção de UX:** Botão com trava anti-clique duplo, status visual de carregamento e pop-up informando a pasta exata de destino.

---

## 🏗️ Arquitetura do Software

O projeto segue princípios de **separação de responsabilidades (SoC)**, mantendo interface gráfica, regras de negócio, acesso a dados e serviços de nuvem totalmente desacoplados:

```text
SistemaRelatorios/
│
├── componentes/                     # Componentes e contêineres visuais da interface
│   ├── botoes.py                    # Fábrica de botões padronizados e navegação
│   ├── conteinersTelaCadastro.py    # Widgets da tela de cadastro de conteúdos
│   ├── conteinersTelaLogin.py       # Widgets e campos da tela de login
│   ├── conteiners_visualizarRelatorio.py # Tabela rolável, filtros e botão de upload
│   └── objetosConteiner.py          # Estrutura mestra dos frames (lateral e central)
│
├── funcoes_docx/                    # Módulos de engenharia de documentos
│   ├── funcoes_cadastro.py          # Leitura/escrita de templates .docx e turmas
│   └── funcoes_leitura.py           # Consultas e buscas de datas cadastradas
│
├── imagens/                         # Ícones e identidades visuais da aplicação
│
├── Professores/                     # Estrutura local de armazenamento e backups
│
├── caminhos.py                      # Centralização e resolução dinâmica de paths locais
├── config.py                        # Configurações globais e diretório base (BASE_DIR)
├── constantes.py                    # Constantes de modelos e ID raiz da pasta do Drive
├── database.py                      # Camada de persistência relacional (SQLite3)
├── funcoes_cadastro_visual.py       # Modais e diálogos de cadastro de usuários e disciplinas
├── menuPrincipal.py                 # Orquestrador do menu lateral e rotas entre telas
├── servico_drive.py                 # Integração completa com Google Drive API v3
├── telaLogin.py                     # Controlador da tela de login
├── tela_cadastro.py                 # Controlador da tela de cadastro de conteúdos
├── tela_professores.py              # Controlador da tela de gestão de professores
├── tela_visualizacao.py             # Controlador da tela de visualização e envio ao Drive
└── main.py                          # Ponto de entrada (Entrypoint) da aplicação
```

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Finalidade |
| :--- | :--- |
| **Python 3.12+** | Linguagem de programação principal |
| **CustomTkinter** | Interface gráfica moderna com suporte nativo a Dark Theme e componentes customizados |
| **Pillow (PIL)** | Manipulação e renderização de imagens, ícones e assinaturas digitais |
| **SQLite3** | Banco de dados relacional embarcado para usuários, disciplinas, modelos e aulas |
| **python-docx** | Manipulação e preenchimento dinâmico de arquivos do Microsoft Word |
| **Google Drive API v3** | Conexão com a nuvem, busca de diretórios e upload multipart de relatórios |
| **Google Auth & OAuthlib** | Fluxo de autenticação OAuth 2.0 seguro com renovação automática de credenciais |

---

## 🚀 Como Executar o Projeto

### 1. Pré-requisitos
* **Python 3.12** ou superior instalado.
* Conta Google com permissão de acesso à pasta institucional do Google Drive.
* Arquivo `credentials.json` gerado no [Google Cloud Console](https://console.cloud.google.com/) com a Google Drive API ativada.

### 2. Clonar o Repositório
```bash
git clone https://github.com/Matt-96/SistemaRelatorios.git
cd SistemaRelatorios
```

### 3. Configurar o Ambiente Virtual
```bash
# Criar o ambiente virtual
python -m venv .venv

# Ativar no Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Ativar no Linux/macOS
source .venv/bin/activate
```

### 4. Instalar as Dependências
```bash
pip install customtkinter pillow python-docx google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

### 5. Configurar as Credenciais do Google Drive
1. Coloque o arquivo `credentials.json` (OAuth Client ID para Desktop App) na raiz do projeto.
2. Defina o ID da pasta institucional compartilhada no arquivo `constantes.py`:
   ```python
   ID_PASTA_COMPARTILHADA = "SEU_ID_DA_PASTA_DO_DRIVE_AQUI"
   ```

### 6. Executar a Aplicação
```bash
python main.py
```
*(No primeiro envio para o Google Drive, o navegador abrirá automaticamente para autorização das permissões. O acesso será persistido com segurança no arquivo local `token.json` para os próximos acessos).*

---

## 🔒 Boas Práticas e Segurança

* **Segurança de Segredos:** Arquivos de credenciais (`credentials.json`), tokens de acesso (`token.json`) e imagens de assinaturas digitais (`**/assinatura.png`) estão estritamente ignorados no `.gitignore`.
* **Histórico Limpo:** Histórico do Git auditado e expurgado contra vazamento acidental de chaves corporativas.
* **Resiliência a Erros:** Bloqueios com `try/except` em todas as rotas de E/S de arquivos e requisições HTTP da API para evitar congelamento de interface.

---

## 👨‍💻 Autor

Desenvolvido por **Matheus** ([@Matt-96](https://github.com/Matt-96)).  
Projeto desenvolvido com foco em automação corporativa, arquitetura limpa e integração de sistemas em nuvem.
