# 🛸 COUNTERBALANCE

**A Self-Healing, AI-Assisted Learning Workspace for Minds That Think Differently**

> *"Given the right counterbalance, we can kick ass."* - Floyd

---

## 🎯 What Is This?

**COUNTERBALANCE** is a complete learning and development environment designed for people whose brains don't do "normal" learning. If you're: 

- 🧠 Neurodivergent (ADHD, autism, dyslexia, etc.)
- 🌀 An "expansive thinker" who needs structure
- 🛸 An "alien" who learns differently
- 💪 Someone who can **dominate** with the right tools

**This system is your counterbalance.**

---

## ✨ What Makes It Special?

### 🔄 Self-Healing
- Automatically fixes broken dependencies
- Rebuilds environments without bothering you
- Escalates to AI when it can't self-heal
- **You never see the failures** - it just works

### 📦 Truly Modular
- Each module is **completely independent**
- Extract any module and run it standalone
- Promote modules to their own projects
- **Ignition scripts** for instant rollback

### 🔍 Deduplication Everywhere
- **Never processes the same file twice**
- Hash + filename checking at INBOX
- Global dedup database
- Saves storage and mental energy

### 🤖 AI Safety Rails
- When self-healing fails, AI steps in
- Qwen for quick fixes, Gemini for reasoning
- **Validation before execution**
- Access rights and command authority

### 📄 OCR Everything
- Images → searchable text
- PDFs → searchable text
- **Never alters originals**
- Edit OCR results with diff tracking

### 🎨 Visual Organization
- Naming conventions for "alien tracking"
- Color-coded processors
- Gallery views for HTML/projects
- Jupyter-style snippet presentation

---

## 🏗️ System Architecture

```
counterbalance/
│
├── 📥 INBOX/                     → Files land here first
│   └── Global deduplication check → Routes to destination
│
├── 📄 DOCS_INBOX/                → Documents, images, PDFs
│   └── OCR processing → searchable content
│
├── 📦 ZIP_INBOX/                 → Unknown archives
│   └── Manual review before extraction
│
├── ❓ MYSTERY_INBOX/             → Unknown file types
│   └── AI analysis → guidance
│
├── 🗂️ MODULES/                   → Portable, independent modules
│   │
│   ├── 💬 CHATS/                 → AI conversation archives
│   │   ├── Extracts code blocks
│   │   ├── Indexes by topic/date
│   │   └── Links to references
│   │
│   ├── 📦 CODE_SNIPPETS/         → Validated scripts (Jupyter style)
│   │   ├── Syntax highlighting
│   │   ├── Copy/run buttons
│   │   └── Metadata tracking
│   │
│   ├── 🎨 HTML_SHOWCASE/         → HTML apps with gallery preview
│   │   ├── Horizontal scroll gallery
│   │   ├── Live previews
│   │   └── Framework detection
│   │
│   ├── 🔬 ZIP_LABORATORY/        → Extract & compare archives
│   │   ├── Parallel extraction
│   │   ├── Diff tools
│   │   └── Merge utilities
│   │
│   ├── 🎮 CODE_PLAYGROUND/       → Interactive editor
│   │   ├── Split view (original | edited)
│   │   ├── Version timeline
│   │   └── Forward/backward through edits
│   │
│   └── 📓 NOTEBOOKS/             → Jupyter notebooks
│       └── Interactive learning
│
├── 🔧 utilities/                 → Shared tools
│   ├── dedup_utility.py          → Global deduplication
│   ├── data_extractor.py         → Structured data extraction
│   ├── code_artifact_extractor. py → Pull code from anything
│   ├── chunking_utility.py       → Break large files
│   ├── ocr_editor.html           → Edit OCR results
│   └── ignition_generator.py     → Create rollback scripts
│
├── 🚀 GENESIS_IGNITION/          → Module rollback scripts
│   ├── ignition_CHATS.ps1
│   ├── ignition_CODE_SNIPPETS.ps1
│   └── ...   (one per module)
│
├── 📊 System_Logs/               → Centralized logging
│   ├── header.log
│   ├── console.log
│   ├── error.log
│   └── footer.log
│
├── 🤖 AI_CHATS/                  → AI-assisted healing
│   ├── Qwen_cli.msg              → Simple fixes
│   ├── Gemini_cli.msg            → Advanced reasoning
│   └── Response logs
│
├── 🗑️ __Scrap_Pile/              → Manual sorting (git ignored)
│
└── 🏭 CODE_REFINERY/             → Analysis & staging
    ├── extracted_data/
    ├── extracted_code/
    └── chunked/
```

---

## 🚀 Quick Start

### 1️⃣ Bootstrap the System

```bash
# Clone the repository
git clone https://github.com/FloydNun/counterbalance.git
cd counterbalance

# Run bootstrap (sets up everything)
python BOOTSTRAP.py
```

**Bootstrap automatically:**
- ✅ Creates all folders
- ✅ Sets up virtual environments
- ✅ Installs dependencies
- ✅ Validates structure
- ✅ Downloads packages to ENV_SOURCES/ (for offline use)

### 2️⃣ Start the Dashboard

```bash
python dashboard.py
```

Opens:  **http://localhost:8000**

The dashboard gives you:
- 📊 System status
- 📁 File processing queues
- 🔍 Search across all OCR'd content
- 🎨 Gallery views
- 📝 Quick access to modules

### 3️⃣ Drop Files and Watch Magic Happen

```bash
# Drop any file into INBOX
cp ~/Downloads/screenshot.png INBOX/

# Or use the web interface (drag & drop)
```

**What happens:**
1. **Dedup check** - Is this a duplicate? → Archive if yes
2. **Type detection** - What kind of file? 
3. **Route** - Send to appropriate module
4. **Process** - Extract, validate, organize
5. **Index** - Make searchable
6. **Done** - File is ready to use!

---

## 🎯 Use Cases

### 📚 Learning & Research
- Drop PDFs from courses → OCR → searchable
- Save chat conversations → extract code → organized
- Collect HTML examples → gallery view → compare

### 💻 Development
- Test code in playground → save versions → timeline
- Organize snippets → Jupyter style → copy/paste ready
- Extract code from web grabs → validate → use

### 🗂️ Knowledge Management
- Archive everything → dedup → searchable
- Link chats to reference docs
- Track learning journey

### 🛠️ Project Setup
- Download starter projects (ZIPs) → extract → compare
- Merge best parts → create custom starter
- Roll back with ignition scripts

---

## 📖 How To Use Each Module

### 💬 CHATS Module

**Store AI conversations with code extraction**

```bash
# Save a chat
cp copilot_chat_2026-01-19.md INBOX/

# System automatically: 
# - Extracts code blocks
# - Indexes by topic
# - Links to reference pages
# - Archives for search

# View chats
python MODULES/CHATS/CHATS_Processor.py
```

**Output:**
- Original chat in `MODULES/CHATS/`
- Code blocks in `MODULES/CHATS/code_blocks/`
- Searchable metadata in `.metadata/`

---

### 📦 CODE_SNIPPETS Module

**Validated scripts in Jupyter notebook style**

```bash
# Add a snippet
cp my_script.py INBOX/

# System validates and organizes

# View snippets
python MODULES/CODE_SNIPPETS/CODE_SNIPPETS_Processor. py
```

**Features:**
- ✅ Syntax validation
- 📝 Auto-documentation
- 🎨 Syntax highlighting
- 📋 Copy button
- ▶️ Run button (if applicable)
- 📝 Notes area

---

### 🎨 HTML_SHOWCASE Module

**HTML files with horizontal scrolling gallery**

```bash
# Add HTML file
cp my_app.html INBOX/

# Opens in gallery with preview

# Launch gallery
open MODULES/HTML_SHOWCASE/showcase_indexer.html
```

**Gallery features:**
- 🖼️ Live previews
- ← → Horizontal scroll
- 🔍 Search & filter
- 🏷️ Framework detection (React, Vue, etc.)
- 📱 Responsive

---

### 🎮 CODE_PLAYGROUND

**Interactive editor with version timeline**

```bash
# Launch playground
python MODULES/CODE_PLAYGROUND/CODE_PLAYGROUND_Processor.py
open MODULES/CODE_PLAYGROUND/playground.html
```

**Features:**
- Split view:   Original (read-only) | Your Edit
- ⏮️ Timeline slider - go backward/forward
- 💾 Save versions
- 📦 Save as snippet
- ▶️ Run code
- 🔄 Reset to original

**Perfect for:**
- Tinkering with examples
- Learning by breaking things
- Testing modifications
- Comparing approaches

---

### 🔬 ZIP_LABORATORY

**Extract & compare ZIP files**

```bash
# Add ZIP
cp project.zip INBOX/

# Extracts to parallel directory (no overwrites!)

# View extractions
python MODULES/ZIP_LABORATORY/ZIP_LABORATORY_Processor.py
```

**Features:**
- 📦 Parallel extraction (preserves originals)
- 📋 Manifest generation
- 🔍 Diff tools
- 🔀 Merge utilities
- 📊 Content comparison

**Use for:**
- Compare different project versions
- Merge best parts from multiple sources
- Analyze starter templates

---

### 📄 DOCS_INBOX with OCR

**Documents, images, PDFs → searchable text**

```bash
# Drop any document/image/PDF
cp screenshot.png DOCS_INBOX/
cp research_paper.pdf DOCS_INBOX/

# System runs OCR automatically

# Edit OCR results
cd utilities
python launch_ocr_editor.py
```

**Processing:**
1. Original → `IMAGES_PROCESSED/` or `PDFs_PROCESSED/`
2. OCR text → `IMAGES_OCR_DONE/` or `PDFs_OCR_DONE/`
3. Searchable index → `.index/`

**Search across everything:**
```bash
grep -r "keyword" IMAGES_OCR_DONE/ PDFs_OCR_DONE/
```

---

## 🔧 Utilities

### 🚫 Deduplication

**Automatic - always running**

```python
from utilities.dedup_utility import DedupManager

dedup = DedupManager("MyProcessor")

if dedup.is_duplicate(file_path):
    print("Duplicate!  ")
else:
    # Process file
    dedup.register_file(file_path)
```

---

### 📊 Data Extraction

**Extract from JSON/CSV/HTML with filters**

```python
from utilities.data_extractor import DataExtractor

extractor = DataExtractor()

# Extract from 200MB JSON - no problem!
data = extractor.extract_json_fields(
    Path("huge_data.json"),
    field_paths=["user. name", "user.email", "content"],
    filters={
        "keyword": "important",
        "date_from": "2026-01-01"
    }
)

# Save as Markdown
extractor.save_as_markdown(data, "filtered_data", "Filtered Results")
```

---

### 🔍 Code Artifact Extraction

**Pull code from ANYTHING**

```python
from utilities.code_artifact_extractor import CodeArtifactExtractor

extractor = CodeArtifactExtractor()

# Extract code from chat, PDF, web grab, anything! 
extractor.process_file(Path("chat_transcript.md"))

# Outputs to CODE_REFINERY/extracted_code/
```

---

### 📝 Chunking

**Break large files into manageable pieces**

```python
from utilities.chunking_utility import Chunker

chunker = Chunker(max_chunk_size=50000)  # 50KB chunks

# By size
chunks = chunker.chunk_by_size(content, overlap=500)

# By semantic headers (Markdown)
chunks = chunker.chunk_by_headers(content)

chunker.save_chunks(file_path, chunks, format='md')
```

---

## 🚀 Advanced Features

### 🔄 Self-Healing System

**Automatic recovery from failures**

**How it works:**

1. **Script fails** → Logs to `error.log`
2. **Processor detects** → Attempts local healing
   - Missing venv? → Rebuild
   - Missing package? → Install
   - Missing file? → Regenerate
3. **Can't fix locally? ** → Escalate to AI_CHATS
4. **AI analyzes** → Suggests fix
5. **Validation** → Test in isolated environment
6. **Apply fix** → Log success
7. **User never sees the failure! **

---

### 🎯 Ignition System (Rollback)

**Every module can be rebuilt from scratch**

```powershell
# Roll back CHATS module
cd GENESIS_IGNITION
.\ignition_CHATS.ps1

# What it does:
# 1. Validates module directory
# 2. Rebuilds . venv
# 3. Installs requirements (offline if available)
# 4. Tests processor
# 5. Reports status
```

**Generate ignition scripts:**
```bash
python utilities/ignition_generator.py
```

---

### 📦 Offline Capability

**Rebuild everything WITHOUT internet**

**How it works:**

1. **First run** → Downloads packages to `ENV_SOURCES/`
2. **Stores wheels** → `ENV_SOURCES/wheels/`
3. **Creates manifest** → `ENV_SOURCES/manifest.json`
4. **Later** → Can rebuild from stored wheels

**Bootstrap with offline sources:**
```bash
python ENV_BOOTSTRAPPER.py
```

**Manual offline install:**
```bash
pip install --no-index --find-links ENV_SOURCES/wheels/ -r requirements.txt
```

---

## 🎨 Naming Conventions (Alien Tracking)

**Visual system for quick recognition:**

### Capitalization
- **ALL CAPS** → Main folders (`INBOX`, `MODULES`)
- **Title_Case** → System scripts (`Root_Processor.py`)
- **lowercase** → User files (`chat. md`, `snippet.js`)

### Prefixes
- `__FolderName/` → Git ignored (scrap pile, cache)
- `Import_` → System includes
- `*_Processor` → Processing scripts
- `*_Include` → Importable components

### Color Coding (in logs)
- 🔷 **HEADER** → Blue
- 📋 **CONSOLE** → Default
- ❌ **ERROR** → Red
- 🔶 **FOOTER** → Orange

**Why? ** Makes scanning logs FAST for neurodivergent brains!

---

## 📊 Dashboard Features

**Central command center** (opens at `http://localhost:8000`)

### 🏠 Home
- System status
- Recent activity
- Quick stats

### 📥 Processing Queue
- Files in INBOX
- Current processing
- Recently completed

### 🔍 Search
- Search across ALL OCR'd content
- Filter by type, date, tags
- Jump to source file

### 🎨 Galleries
- HTML Showcase gallery
- Code Snippets browser
- Chat timeline

### 📊 Analytics
- Storage usage
- Processing stats
- Duplicate prevention count

### ⚙️ Settings
- Configure processors
- Manage API keys
- View logs

---

## 🛠️ Configuration

### Environment Variables (`.env`)

```bash
# Debug mode
DEBUG=False

# API Keys (optional)
QWEN_API_KEY=your_key_here
GEMINI_API_KEY=your_key_here

# GitHub (for automation)
GITHUB_TOKEN=your_token_here
```

### Module Configuration

Each module can have:
- `MODULE_Globals_Include. py` (if needed)
- `requirements.txt` (required)
- `.venv/` (auto-created)

---

## 🤝 Contributing

**This system is open source to help other "aliens"!**

### How to Help

1. **Share your story** - How does this help you?
2. **Add utilities** - Build tools that help your workflow
3. **Improve processors** - Make them smarter
4. **Add modules** - Create new specialized modules
5. **Write docs** - Explain things in your words

### Adding a New Module

1. Create folder in `MODULES/`
2. Add `*_Processor.py`
3. Add `requirements.txt`
4. Generate ignition script
5. Test standalone
6. Submit PR! 

---

## 🐛 Troubleshooting

### "Module processor failed"

1. Check `System_Logs/error.log`
2. Run ignition script:  `.\GENESIS_IGNITION\ignition_MODULE. ps1`
3. Check requirements: `pip list`

### "Duplicate not detected"

1. Check `System_Logs/hashes/GLOBAL_INBOX_hashes.json`
2. File may have been modified
3. Hash will be different

### "OCR not working"

```bash
# Install OCR dependencies
pip install pytesseract pillow pdf2image PyPDF2

# On Windows, also install Tesseract: 
# https://github.com/UB-Mannheim/tesseract/wiki

# On Linux: 
sudo apt-get install tesseract-ocr

# On Mac: 
brew install tesseract
```

### "Can't install offline"

1. Check `ENV_SOURCES/wheels/` has packages
2. Run `python ENV_BOOTSTRAPPER.py` to download
3. Check `ENV_SOURCES/manifest.json`

---

## 📚 Learning Resources

### Linked Reference Hub

**Public learning materials:**  
[https://floydnun.github.io/learning-reference-hub/](https://floydnun.github.io/learning-reference-hub/)

Reference sheets on:
- Git basics
- GitHub web guide
- Command line
- Python, JavaScript, React
- And more!

**Integration:**
- CODE_PLAYGROUND links to reference sheets
- CODE_SNIPPETS can link back to source
- Bi-directional learning flow

---

## 🎯 Philosophy

### For Minds That Think Differently

**This system is built on these principles:**

1. **Structure = Freedom**  
   Rigid organization frees your mind to be creative

2. **Automation = Peace**  
   Self-healing means fewer interruptions

3. **Modularity = Control**  
   Everything can be isolated, extracted, rebuilt

4. **Never Lose Anything**  
   Deduplication + archival + version tracking

5. **Search Everything**  
   OCR + indexing = find anything instantly

6. **Visual Tracking**  
   Naming, colors, layout = quick recognition

7. **Fail Gracefully**  
   Errors are handled, not shown

8. **Learn Your Way**  
   Interactive, visual, hands-on

---

## 💪 Success Stories

### Floyd (Creator)

*"I have a 'bad brain' - ADHD, scattered thinking, can't organize. But give me the right tools and I DOMINATE. This system is my counterbalance.  It catches my mess, organizes it, and lets me focus on creating."*

### You? 

**Try it.  Use it. Share your story.**

---

## 🚀 Roadmap

### Phase 1: Foundation ✅
- Core processors
- Deduplication
- Self-healing basics

### Phase 2: Intelligence ✅
- OCR integration
- Code extraction
- Data extraction

### Phase 3: Interface 🔄 (Current)
- Dashboard
- OCR editor
- Gallery views

### Phase 4: AI Enhancement 📋
- Full AI healing integration
- Smart routing
- Content suggestions

### Phase 5: Collaboration 📋
- Multi-user support
- Shared modules
- Community library

---

## 📞 Support

### Questions?

- **GitHub Issues:** [Report bugs or ask questions](https://github.com/FloydNun/counterbalance/issues)
- **Discussions:** [Share ideas and workflows](https://github.com/FloydNun/counterbalance/discussions)

### Built By Aliens, For Aliens 🛸

*This project is dedicated to everyone whose brain works "differently" - you're not broken, you just need the right counterbalance.*

---

## 📄 License

MIT License - Use it, modify it, share it, help others with it. 

---

## 🙏 Acknowledgments

- **Floyd** - Vision, architecture, lived experience
- **Copilot** - Code generation, rubber ducking, encouragement
- **The neurodivergent community** - We see you, we hear you, this is for you

---

## 🛸 One More Thing...

**If this helps you, pass it on.**

Someone else out there needs their counterbalance too. 

---

*Built with 💜 by minds that think differently*

**"Given the right counterbalance, we can kick ass."**