# 🛸 COUNTERBALANCE - Build Specification v2.0
## FLOYD'S COMPLETE LEARNING SYSTEM

---

## 📁 COMPLETE REPOSITORY STRUCTURE

```
counterbalance/                           ROOT PROJECT
│
├── BUILD_SPEC. md                         System blueprint (v2)
├── README.md                             User documentation
├── BOOTSTRAP.py                          One-command setup
├── . gitignore                            Ignore rules
├── requirements.txt                      Root dependencies
├── . env. template                         Environment template
├── .venv/                                Root virtual environment
│
├── Import_Header_Include.py              Standard header
├── Import_Footer_Include. py              Standard footer
├── Import_Globals_Include.py             Root globals
│
├── Root_Processor.py                     File preparation
├── Overwatch_Processor.py                File watcher
├── auto_function_doc.py                  Function documenter
│
├── INBOX/                                Main landing zone
│   ├── INBOX_Processor.py
│   └── README.md
│
├── DOCS_INBOX/                           Documentation sorting
│   ├── DOCS_INBOX_Processor.py
│   └── README.md
│
├── ZIP_INBOX/                            Unknown ZIPs
│   ├── ZIP_INBOX_Processor. py
│   └── README. md
│
├── MYSTERY_INBOX/                        Unknown file types
│   ├── MYSTERY_INBOX_Processor. py
│   └── README. md
│
├── System_Logs/                          Centralized logging
│   ├── header.log
│   ├── console.log
│   ├── error.log
│   ├── footer.log
│   └── README.md
│
├── AI_CHATS/                             AI-assisted healing
│   ├── AI_CHATS_Processor.py
│   ├── Qwen_cli. msg
│   ├── Gemini_cli.msg
│   ├── Qwen_cli.log
│   ├── Gemini_cli.log
│   └── README.md
│
├── __Scrap_Pile/                         Personal junk (GIT IGNORED)
│   └── README.md
│
├── CODE_REFINERY/                        Analysis staging
│   ├── CODE_REFINERY_Processor.py
│   └── README.md
│
└── MODULES/                              Portable modules
    │
    ├── CHATS/                            AI chat archives
    │   ├── CHATS_Processor.py
    │   ├── chat_indexer.py              Auto-index chats
    │   ├── requirements.txt
    │   ├── . venv/
    │   └── README.md
    │
    ├── CODE_SNIPPETS/                    Single scripts (Jupyter style)
    │   ├── CODE_SNIPPETS_Processor. py
    │   ├── snippet_renderer.py          Jupyter-style presentation
    │   ├── requirements.txt
    │   ├── .venv/
    │   └── README.md
    │
    ├── HTML_SHOWCASE/                    HTML files with previews
    │   ├── HTML_SHOWCASE_Processor.py
    │   ├── showcase_indexer.html        Auto-indexer with scroll previews
    │   ├── utilities/                   Floyd's utilities (polished)
    │   ├── requirements.txt
    │   ├── .venv/
    │   └── README.md
    │
    ├── ZIP_LABORATORY/                   ZIP extraction & comparison
    │   ├── ZIP_LABORATORY_Processor. py
    │   ├── zip_extractor.py             Parallel extraction
    │   ├── diff_tools/                  Crawler, diff, merge tools
    │   ├── gallery_viewer.html          Preview extracted contents
    │   ├── requirements.txt
    │   ├── .venv/
    │   └── README.md
    │
    ├── CODE_PLAYGROUND/                  Interactive testing
    │   ├── CODE_PLAYGROUND_Processor.py
    │   ├── playground. html              Monaco editor
    │   ├── requirements.txt
    │   ├── .venv/
    │   └── README.md
    │
    └── NOTEBOOKS/                        Jupyter notebooks
        ├── NOTEBOOKS_Processor.py
        ├── requirements.txt
        ├── . venv/
        └── README.md
```

---

## 🎨 MODULE SPECIFICATIONS

### **CHATS Module**
**Purpose:** Archive AI chat conversations  
**Inputs:** `.md` files with chat logs  
**Processing:**
- Index by date and topic
- Extract code blocks
- Link to related reference pages

**Presentation:**
- Timeline view
- Searchable
- Tagged by topic

---

### **CODE_SNIPPETS Module** ⭐ NEW
**Purpose:** Validated single scripts (Jupyter style)  
**Inputs:** `.py`, `.js`, `.sh`, etc.  (validated, working)  
**Processing:**
- Validate syntax
- Add syntax highlighting
- Extract function documentation
- Test if runnable

**Presentation:**  (JUPYTER NOTEBOOK STYLE)
```
┌─────────────────────────────────────────┐
│ Snippet:  data_processor.py              │
│ ─────────────────────────────────────── │
│                                         │
│ Description:                             │
│ Processes CSV data and generates        │
│ summary statistics                      │
│                                         │
│ Code:  [Syntax Highlighted]              │
│ [Copy Button] [Run Button]              │
│                                         │
│ Output:                                  │
│ [Results display here]                  │
│                                         │
│ Notes:                                  │
│ [Editable notes area]                   │
└─────────────────────────────────────────┘
```

---

### **HTML_SHOWCASE Module** ⭐ NEW  
**Purpose:** Display standalone HTML files with previews  
**Inputs:** Single HTML files (standalone, React, Firebase)  
**Processing:**
- Validate HTML
- Check for dependencies
- Extract metadata
- Generate thumbnail

**Presentation:** (AUTO-INDEXER WITH LEFT-RIGHT SCROLL)
```
┌──────────────────────────────────────────────────────────┐
│ HTML SHOWCASE                            [Filter] [Sort] │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  ◄ ────────────────────────────────────────────── ►     │
│                                                          │
│   ┌────────┐  ┌────────┐  ┌────────┐  ┌─��──────┐      │
│   │ [IMG]  │  │ [IMG]  │  │ [IMG]  │  │ [IMG]  │      │
│   │ App 1  │  │ App 2  │  │ App 3  │  │ App 4  │      │
│   │ React  │  │ Vanila │  │Firebase│  │ D3.js  │      │
│   └────────┘  └────────┘  └────────┘  └────────┘      │
│                                                          │
│  [Click to open full preview]                           │
└──────────────────────────────────────────────────────────┘
```

**Floyd's Utilities Integration:**
- Will polish and integrate your existing utilities
- Enhance with professional UX
- Add keyboard navigation

---

### **ZIP_LABORATORY Module** ⭐ NEW
**Purpose:** Extract, compare, and merge ZIP contents  
**Inputs:** `.zip` files from AI labs, Colabs, Firebase  
**Processing:**
- Extract to parallel subdirectory (NOT overwrite)
- Index contents
- Generate preview
- Enable diff/comparison

**Presentation:** (GALLERY + DIFF TOOLS)
```
┌──────────────��───────────────────────────────────────────┐
│ ZIP:  my_colab_project.zip                                │
├──────────────────────────────────────────────────────────┤
│ Extracted to:  ZIP_LABORATORY/my_colab_project_20260119/ │
│                                                          │
│ Contents:                                                │
│   📄 notebook.ipynb                                      │
│   📄 utils.py                                            │
│   📁 data/ (5 files)                                     │
│   📄 requirements.txt                                    │
│                                                          │
│ [Preview Gallery]  [Diff Tool]  [Merge Tool]            │
│                                                          │
│ Compare with:  [Select another ZIP] [Compare]           │
└──────────────────────────────────────────────────────────┘
```

**Diff Tools:**
- Crawler to find similar files
- Side-by-side comparison
- Merge selected parts
- Create new combined version

---

## 📥 INBOX SPECIFICATIONS

### **DOCS_INBOX** ⭐ NEW
**Purpose:** Staging for documentation files  
**Accepted:** `.md`, `.txt`, `.doc`, `.docx`, `.pdf`  
**Processing:**
- Sort manually later
- Preview available
- Can tag and categorize
- Eventually archive

---

### **ZIP_INBOX** ⭐ NEW
**Purpose:** Unknown/unsorted ZIPs  
**Accepted:** `.zip`, `.tar`, `.gz`, `.rar`, `.7z`  
**Processing:**
- Manual review first
- Preview contents without extraction
- Decide destination (ZIP_LABORATORY or __Scrap_Pile)

---

### **MYSTERY_INBOX** ⭐ NEW
**Purpose:** Unknown file types  
**Accepted:** Anything unrecognized  
**Processing:**
- Quarantine for safety
- Analyze with file command
- Eventually trigger Gemini:  "What is this file?  What should I do with it?"
- Gemini provides guidance
- User decides action

**AI Integration:**
```python
# When file lands in MYSTERY_INBOX: 
1. Get file metadata (size, magic bytes, etc.)
2. Create Gemini request: 
   "I have a file with extension .xyz
    Magic bytes:   [hex dump]
    Size:  [size]
    What is this file type? 
    Is it safe? 
    What should I do with it?"
3. Gemini analyzes and responds
4. Present options to user
```

---

## 🔄 ROUTING LOGIC (UPDATED)

```
File lands in INBOX
    ↓
INBOX_Processor detects type
    ↓
Route decision:
    │
    ├── . md (chat format) → MODULES/CHATS/
    ├── .md, .txt, .doc, .pdf → DOCS_INBOX/
    ├── .py, .js, .sh (single script) → MODULES/CODE_SNIPPETS/
    ├── .html (standalone) → MODULES/HTML_SHOWCASE/
    ├── .zip (known source) → MODULES/ZIP_LABORATORY/
    ├── .zip (unknown) → ZIP_INBOX/
    ├── .ipynb → MODULES/NOTEBOOKS/
    ├── Unknown extension → MYSTERY_INBOX/
    └── Needs processing → Root_Processor → appropriate MODULE
```

---

## 🎨 PRESENTATION STYLES

### Jupyter Notebook Style (CODE_SNIPPETS):
- Cell-based layout
- Syntax highlighting
- Inline execution
- Output display
- Notes area

### Gallery Style (HTML_SHOWCASE, ZIP_LABORATORY):
- Thumbnail previews
- Horizontal scroll
- Click to enlarge
- Filter and sort
- Quick actions

### Timeline Style (CHATS):
- Chronological order
- Expandable entries
- Search and filter
- Tag system

---

## 🛠️ TOOLS TO BUILD

### 1. **showcase_indexer.html** (HTML_SHOWCASE)
- Auto-generates preview gallery
- Horizontal scroll navigation
- Iframe previews
- Keyboard shortcuts
- Responsive design

### 2. **snippet_renderer.py** (CODE_SNIPPETS)
- Generates Jupyter-style HTML
- Syntax highlighting (Pygments)
- Runnable code cells
- Notes persistence

### 3. **zip_extractor.py** (ZIP_LABORATORY)
- Safe parallel extraction
- Prevents overwrites
- Generates manifest
- Creates preview index

### 4. **diff_tools/** (ZIP_LABORATORY)
- File crawler
- Side-by-side diff viewer
- Merge interface
- Export combined result

### 5. **mystery_analyzer.py** (MYSTERY_INBOX)
- File type detection
- Safety checks
- Gemini API integration
- User decision interface

---

## 📦 DEPENDENCIES (UPDATED)

### Root (requirements.txt):
```
watchdog>=3.0.0          # File watching
python-dotenv>=1.0.0     # Environment
GitPython>=3.1.40        # Git operations
```

### CODE_SNIPPETS: 
```
pygments>=2.17           # Syntax highlighting
jupyter>=1.0             # Notebook-style rendering
ipython>=8.0             # IPython kernel
```

### HTML_SHOWCASE:
```
beautifulsoup4>=4.12     # HTML parsing
pillow>=10.0             # Thumbnail generation
selenium>=4.15           # Screenshot capture (optional)
```

### ZIP_LABORATORY:
```
zipfile38>=0.0.3         # Better ZIP handling
rarfile>=4.1             # RAR support
py7zr>=0.20              # 7z support
difflib                  # Built-in diff
```

### MYSTERY_INBOX:
```
python-magic>=0.4.27     # File type detection
google-generativeai      # Gemini API (optional)
```

---

## 🚀 BUILD PHASES (REVISED)

### Phase 1:  Foundation ✅ (COMPLETE)
- [x] Folder structure
- [x] Include files
- [x] Basic processors
- [x] Logging system

### Phase 2: Core Modules (CURRENT)
- [ ] CHATS_Processor
- [ ] CODE_SNIPPETS_Processor + Jupyter-style renderer
- [ ] HTML_SHOWCASE_Processor + gallery indexer
- [ ] ZIP_LABORATORY_Processor + diff tools

### Phase 3: Inbox System
- [ ] DOCS_INBOX_Processor
- [ ] ZIP_INBOX_Processor
- [ ] MYSTERY_INBOX_Processor + Gemini integration

### Phase 4: Automation & Polish
- [ ] Overwatch full integration
- [ ] Self-healing complete
- [ ] AI safety rails active
- [ ] Floyd's utilities integration

### Phase 5: User Interface
- [ ] Dashboard
- [ ] Web interface
- [ ] Drag-and-drop
- [ ] Mobile responsive

---

**Floyd, THIS IS YOUR COMPLETE BUILD SPEC!** 🛸

**You have it ALL documented now!**

---

**Want me to continue building the MODULE processors?  Starting with:**
1. **CODE_SNIPPETS** (Jupyter-style renderer)
2. **HTML_SHOWCASE** (Gallery with left-right scroll)
3. **ZIP_LABORATORY** (Extraction + diff tools)

**Which one first?** 🚀💪