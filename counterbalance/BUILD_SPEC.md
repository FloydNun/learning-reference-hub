# 🛸 COUNTERBALANCE - Build Specification

**Version:** 1.0.0  
**Status:** Foundation Phase  
**Owner:** FloydNun  
**Architecture:** Self-Healing Modular Workspace

---

## 🎯 SYSTEM PHILOSOPHY

### Core Principles
- ✅ **No Hard-Coded Paths** - Everything discovered dynamically
- ✅ **Portable Modules** - Each module is self-contained, can be promoted to root
- ✅ **Self-Healing** - Failures trigger bootstrap rebuilds, never bother user
- ✅ **Self-Documenting** - Functions auto-documented in Footer comments
- ✅ **AI-Assisted** - Complex failures escalate to AI safety rails (Qwen/Gemini)
- ✅ **Three Ways** - At least 3 ways to accomplish any task
- ✅ **Alien-Friendly** - Visual tracking via naming conventions (CAPS, underscores)

### Safety Rails
- Access rights enforcement
- Command level authority
- Validation before execution
- Escalation hierarchy (Module → Root → AI)

---

## 📁 REPOSITORY STRUCTURE

```
counterbalance/                           ROOT PROJECT
│
├── BUILD_SPEC.md                         This file - system blueprint
├── README.md                             User-facing documentation
├── BOOTSTRAP. py                          One-command setup script
├── . gitignore                            Ignore rules (see below)
├── requirements.txt                      Root-level dependencies
├── . env. template                         Environment template (self-healing)
├── .venv/                                Root virtual environment
│
├── Import_Header_Include.py              Standard header for all scripts
├── Import_Footer_Include.py              Standard footer for all scripts
├── Import_Globals_Include.py             Root-level globals (no hard paths)
│
├── Root_Processor. py                     Prepares files for modules
├── Overwatch_Processor.py                File watcher, triggers processors
├── auto_function_doc.py                  Auto-documents functions (from Colab)
│
├── INBOX/                                Landing zone for all new files
│   ├── INBOX_Processor.py
│   └── README.md
│
├── System_Logs/                          Centralized logging
│   ├── header.log
│   ├── console. log
│   ├── error.log
│   ├── footer.log
│   └── README.md
│
├── AI_CHATS/                             AI-assisted healing (safety rails)
│   ├── AI_CHATS_Processor. py
│   ├── Qwen_cli.msg
│   ├── Gemini_cli.msg
│   ├── Qwen_cli.log
│   ├── Gemini_cli. log
│   └── README. md
│
├── __Scrap_Pile/                         Personal junk sorting (GIT IGNORED)
│   └── README.md
│
├── CODE_REFINERY/                        Analysis staging before integration
│   ├── CODE_REFINERY_Processor.py
│   └── README.md
│
└── MODULES/                              Portable, self-contained modules
    │
    ├── CHATS/
    │   ├── CHATS_Processor.py
    │   ├── requirements.txt
    │   ├── .venv/
    │   └── README.md
    │
    ├── SNIPPETS/
    │   ├── SNIPPETS_Processor.py
    │   ├── requirements.txt
    │   ├── .venv/
    │   └── README.md
    │
    ├── CODE_PLAYGROUND/
    │   ├── CODE_PLAYGROUND_Processor.py
    │   ├── CODE_PLAYGROUND_Globals_Include. py  (only if needed)
    │   ├── requirements.txt
    │   ├── .venv/
    │   └── README.md
    │
    └── NOTEBOOKS/
        ├── NOTEBOOKS_Processor.py
        ├── requirements.txt
        ├── . venv/
        └── README.md
```

---

## 🚫 GIT IGNORE RULES

### Folders Starting with `__`
- `__Scrap_Pile/` contents ignored (README kept)
- `__*/` pattern for any future double-underscore folders

### Standard Ignores
- Virtual environments (`.venv/`, `venv/`, `env/`)
- Python cache (`__pycache__/`, `*.pyc`)
- Environment files (`.env`, NOT `.env.template`)
- IDE files (`.vscode/`, `.idea/`)
- OS files (`.DS_Store`, `Thumbs.db`)
- Large dumps, temp files

### Exceptions (Always Tracked)
- `README.md` in ALL folders (even ignored ones)
- `.gitkeep` files for empty folders
- `requirements.txt` in all modules
- `.env.template` (but NOT `.env`)

---

## 🔧 MODULE SPECIFICATIONS

### Module Requirements (Every Module Must Have):
1. **`MODULE_Processor.py`** - Validates, processes files
2. **`requirements.txt`** - Dependencies (cannot run without this)
3. **`.venv/`** - Isolated virtual environment
4. **`README.md`** - Module documentation

### Optional (Only If Needed):
- **`MODULE_Globals_Include.py`** - Overrides root globals (rare)

### Module Independence:
- Each module can be:
  - Extracted and run standalone
  - Promoted to ROOT of new project
  - Mixed/matched with other modules
- No dependencies on sibling modules
- All paths discovered dynamically

---

## 📝 NAMING CONVENTIONS (Alien Tracking System)

### Capitalization Rules:
- **ALL CAPS** - Main folders (`INBOX`, `MODULES`, `AI_CHATS`)
- **Title_Case** - System scripts (`Root_Processor.py`)
- **lowercase** - User files (`chat.md`, `snippet.js`)

### Underscore Usage:
- `Folder_Processor. py` - Folder name + Processor
- `Import_Header_Include.py` - Import prefix for includes
- `MODULE_Globals_Include.py` - Module-specific overrides

### Special Prefixes:
- `__FolderName/` - Git ignored contents (except README)
- `Import_` - System includes
- `_Processor` - Processing scripts
- `_Include` - Importable components

**These conventions are CRITICAL for alien visual tracking!**

---

## 🔄 PROCESSING FLOW

### File Ingestion: 
```
1. File lands in INBOX/
2. INBOX_Processor detects type via naming/content
3. Routes to Root_Processor if needs preparation
4. Root_Processor:
   - Checks for Header/Footer/Globals imports
   - Adds if missing (makes backup first)
   - Runs auto_function_doc.py (documents functions)
   - Validates structure
5. Routes to appropriate MODULE
6. MODULE_Processor validates and executes
```

### Self-Healing Flow:
```
1. Script execution fails → logs to System_Logs/error.log
2. MODULE_Processor detects failure
3. Attempts local healing: 
   - Missing .venv? → Rebuild
   - Missing dependency? → Install
   - Missing globals? → Use root
4. If can't heal → Escalates to AI_CHATS
5. AI_CHATS_Processor: 
   - Simple?  → Qwen_cli.msg
   - Complex? → Gemini_cli.msg
6. Waits for . log response
7. Applies fix with validation
8. Logs result
```

### Bootstrap Rebuild: 
```
- Climbs back toward ROOT looking for missing pieces
- Rebuilds . venv from requirements.txt
- Restores standard imports
- Never reports to user (silent healing)
```

---

## 📊 LOGGING SYSTEM

### Log Files (All in System_Logs/):
1. **header.log** - System initialization, timestamps, origin tracking
2. **console.log** - Actions performed, process flow, info
3. **error.log** - Failures, exceptions, healing triggers
4. **footer.log** - Close-out, escalation, summaries

### Log Entry Format:
```
[TIMESTAMP] [LEVEL] [ORIGIN] Message
2026-01-19 02:30:15 | ERROR | CHATS_Processor. py | Missing dependency:  pandas
2026-01-19 02:30:16 | CONSOLE | CHATS_Processor. py | Attempting venv rebuild
2026-01-19 02:30:20 | CONSOLE | CHATS_Processor.py | Dependency installed
2026-01-19 02:30:21 | FOOTER | CHATS_Processor. py | Healing successful, execution resumed
```

---

## 🤖 AI SAFETY RAILS

### Access Levels:
- **Level 1:** Module Processor (can modify module files)
- **Level 2:** Root Processor (can modify root files, NOT globals)
- **Level 3:** AI Assistants (read-only analysis, suggest fixes)

### AI Chat Protocol:
1. Error occurs beyond auto-healing
2. Processor creates `.msg` file with:
   - Error details
   - Code context
   - Attempted fixes
3. Routes to: 
   - **Qwen** - Syntax, logic, simple fixes
   - **Gemini** - Advanced reasoning, architecture questions
4. AI responds via `.log` file
5. Processor validates suggestion
6. Tests in isolated environment
7. If safe → applies fix
8. If unsafe → logs and escalates to user

---

## 🚀 BOOTSTRAP PROCESS

### One-Command Setup:
```bash
python BOOTSTRAP.py
```

### Bootstrap Actions:
1. Validates Python version (3.8+)
2. Creates folder structure
3. Creates root . venv
4. Installs root requirements
5. Creates . env from template
6. Creates placeholder READMEs
7. Creates .gitkeep in empty folders
8. Initializes git (if not exists)
9. Creates . gitignore
10. Runs validation checks
11. Reports status

### Bootstrap Output:
```
🛸 COUNTERBALANCE BOOTSTRAP
━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Python 3.11.5 detected
✅ Creating folder structure... 
✅ Creating root .venv...
✅ Installing dependencies...
✅ Setting up modules...
   ├── CHATS module ready
   ├── SNIPPETS module ready
   ├── CODE_PLAYGROUND module ready
   └── NOTEBOOKS module ready
✅ System validated
━━━━━━━━━━━━━━━━━━━━━━━━━━
🎉 COUNTERBALANCE READY! 

Next steps:
1. Review . env.template and create .env
2. Drop files in INBOX/ to test
3. Run: python Overwatch_Processor.py
```

---

## 📦 DEPENDENCIES

### Root Level (requirements.txt):
```
watchdog>=3.0.0          # File watching for Overwatch
python-dotenv>=1.0.0     # Environment management
GitPython>=3.1.40        # Git operations
```

### Module Level (varies by module):
- **CHATS:** `markdown`, `beautifulsoup4`
- **SNIPPETS:** `pygments`, `jinja2`
- **CODE_PLAYGROUND:** `monaco-editor-wrapper`
- **NOTEBOOKS:** `jupyter`, `nbconvert`

---

## 🧪 TESTING PROTOCOL

### Validation Checks:
1. Structure validation (folders exist)
2. Import validation (Header/Footer/Globals accessible)
3. Processor validation (each can run)
4. Healing validation (break something, watch it fix)
5. Portability validation (extract module, run standalone)

### Test Files (Included):
- `test_ingestion.py` - Tests INBOX → MODULE flow
- `test_healing.py` - Tests self-healing mechanisms
- `test_portability.py` - Tests module extraction

---

## 📚 DOCUMENTATION SYSTEM

### Auto-Generated Docs:
- Footer comments parsed by doc renderer
- Generates markdown in `DOCS/` folder
- Linked to user dashboards

### Manual Docs:
- This BUILD_SPEC.md
- README.md in each folder
- MODULE-specific guides

---

## 🎯 PHASES

### Phase 1: Foundation (Current)
- [ ] Create folder structure
- [ ] Create Include files
- [ ] Create INBOX_Processor
- [ ] Create Root_Processor
- [ ] Test file ingestion

### Phase 2: Self-Healing
- [ ] Add error detection
- [ ] Add . venv rebuild logic
- [ ] Add bootstrap climbing
- [ ] Test healing mechanisms

### Phase 3: AI Safety Rails
- [ ] Create AI_CHATS structure
- [ ] Implement Qwen/Gemini routing
- [ ] Add validation checks
- [ ] Test AI-assisted healing

### Phase 4: Automation
- [ ] Create Overwatch_Processor
- [ ] Implement file watching
- [ ] Add trigger logic
- [ ] Test full automation

### Phase 5: User Interface
- [ ] Dashboard for monitoring
- [ ] Drag-and-drop file upload
- [ ] Log viewer
- [ ] Module manager

---

## 🔐 SECURITY

### Environment Variables:
- API keys stored in `.env` (git ignored)
- Template provided as `.env.template`
- Self-healing if . env missing (prompts user once)

### Access Control:
- Processors run with limited permissions
- AI assistants read-only by default
- File operations logged and validated
- Escalation required for root modifications

---

## 📞 SUPPORT

### If System Fails:
1. Check System_Logs/error.log
2. Check AI_CHATS/ for healing attempts
3. Run:  `python BOOTSTRAP.py --repair`
4. Join discussion:  [GitHub Issues]

### Contributing:
- This is Floyd's personal system
- Will be open-sourced when stable
- Designed for other "aliens" who need structure

---

**Built for brains that need counterbalance.  🛸**