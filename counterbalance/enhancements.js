// 🚀 Global Enhancements for Learning Reference Hub
// Adds interactive features WITHOUT breaking the simple design! 
// Author: Floyd + Copilot  |  Date: Jan 2026

(function() {
    'use strict';
    
    console.log('🚀 Enhancements loaded! ');
    
    // Track current file for notes
    window.currentMarkdownFile = 'README.md';
    
    // ===== FEATURE 1: COPY BUTTONS ON CODE BLOCKS =====
    function addCopyButtons() {
        const codeBlocks = document.querySelectorAll('pre code');
        
        codeBlocks.forEach((codeBlock) => {
            const pre = codeBlock.parentElement;
            
            // Don't add button if already exists
            if (pre.querySelector('. copy-btn')) return;
            
            // Create copy button
            const copyBtn = document.createElement('button');
            copyBtn.className = 'copy-btn';
            copyBtn. innerHTML = '📋 Copy';
            copyBtn.title = 'Copy code to clipboard';
            
            // Style the button
            Object.assign(copyBtn. style, {
                position: 'absolute',
                top: '8px',
                right: '8px',
                padding: '4px 10px',
                fontSize: '12px',
                fontWeight: '600',
                cursor: 'pointer',
                border: 'none',
                borderRadius: '5px',
                backgroundColor: '#667eea',
                color: 'white',
                zIndex:  '10',
                transition: 'all 0.3s',
                boxShadow: '0 2px 5px rgba(0,0,0,0.2)'
            });
            
            // Hover effect
            copyBtn.onmouseenter = () => {
                copyBtn.style.backgroundColor = '#5568d3';
                copyBtn.style. transform = 'scale(1.05)';
            };
            copyBtn.onmouseleave = () => {
                copyBtn. style.backgroundColor = '#667eea';
                copyBtn.style. transform = 'scale(1)';
            };
            
            // Click handler
            copyBtn.addEventListener('click', async () => {
                try {
                    await navigator.clipboard.writeText(codeBlock.textContent);
                    copyBtn.innerHTML = '✅ Copied!';
                    copyBtn.style.backgroundColor = '#28a745';
                    setTimeout(() => {
                        copyBtn.innerHTML = '📋 Copy';
                        copyBtn.style.backgroundColor = '#667eea';
                    }, 2000);
                } catch (err) {
                    copyBtn.innerHTML = '❌ Failed';
                    copyBtn.style.backgroundColor = '#dc3545';
                    setTimeout(() => {
                        copyBtn.innerHTML = '📋 Copy';
                        copyBtn.style.backgroundColor = '#667eea';
                    }, 2000);
                }
            });
            
            // Position pre element
            pre.style.position = 'relative';
            pre.appendChild(copyBtn);
        });
        
        console.log(`✅ Added copy buttons to ${codeBlocks.length} code blocks`);
    }
    
    // ===== FEATURE 2: NOTES AREA AT BOTTOM =====
    function addNotesArea() {
        const content = document.getElementById('markdown-content');
        if (!content) return;
        
        // Remove old notes if they exist
        const oldNotes = document.querySelector('.notes-area');
        if (oldNotes) oldNotes.remove();
        
        // Create notes section
        const notesSection = document.createElement('div');
        notesSection.className = 'notes-area';
        notesSection.innerHTML = `
            <hr style="margin:  40px 0; border: none; border-top: 2px solid #e0e0e0;">
            <div style="background: #f8f9fa; padding: 20px; border-radius: 8px; border:  1px solid #dee2e6;">
                <h3 style="margin-top: 0;">📝 My Personal Notes</h3>
                <p style="color: #666; font-size: 14px; margin-bottom: 15px;">
                    Private notes for this page - saved locally in your browser
                </p>
                <textarea 
                    id="page-notes" 
                    placeholder="Add your personal notes, code snippets, questions, or reminders here..."
                    style="width: 100%; min-height: 150px; padding: 12px; 
                           font-family: 'Courier New', monospace; font-size: 14px;
                           border: 2px solid #ccc; border-radius: 6px; 
                           resize: vertical; line-height: 1.5;">
                </textarea>
                <div style="margin-top:  12px; display: flex; gap: 10px; align-items: center;">
                    <button onclick="saveNotes()" 
                            style="padding: 10px 20px; background: #667eea; 
                                   color: white; border: none; border-radius: 5px; 
                                   cursor: pointer; font-weight: 600; transition: all 0.3s;">
                        💾 Save Notes
                    </button>
                    <button onclick="clearNotes()" 
                            style="padding: 10px 20px; background: #dc3545; 
                                   color: white; border: none; border-radius: 5px; 
                                   cursor: pointer; font-weight: 600; transition: all 0.3s;">
                        🗑️ Clear
                    </button>
                    <span id="notes-status" style="color: #28a745; font-weight: 600;"></span>
                </div>
            </div>
        `;
        
        content.appendChild(notesSection);
        loadNotes();
        console.log('✅ Notes area added');
    }
    
    // ===== NOTES FUNCTIONS =====
    window.saveNotes = function() {
        const currentFile = window.currentMarkdownFile || 'default';
        const notes = document.getElementById('page-notes').value;
        localStorage.setItem(`notes-${currentFile}`, notes);
        
        const status = document.getElementById('notes-status');
        status.textContent = '✅ Saved!';
        status.style.display = 'inline';
        setTimeout(() => {
            status.style.display = 'none';
        }, 2000);
    };
    
    window.loadNotes = function() {
        const currentFile = window.currentMarkdownFile || 'default';
        const notes = localStorage.getItem(`notes-${currentFile}`) || '';
        const textarea = document.getElementById('page-notes');
        if (textarea) {
            textarea.value = notes;
            console.log(`📝 Loaded notes for:  ${currentFile}`);
        }
    };
    
    window.clearNotes = function() {
        if (confirm('⚠️ Clear all notes for this page?  This cannot be undone! ')) {
            document.getElementById('page-notes').value = '';
            saveNotes();
        }
    };
    
    // ===== FEATURE 3: AUTO-SAVE NOTES =====
    function setupAutoSave() {
        let saveTimeout;
        const textarea = document.getElementById('page-notes');
        
        if (textarea) {
            textarea. addEventListener('input', () => {
                clearTimeout(saveTimeout);
                saveTimeout = setTimeout(() => {
                    saveNotes();
                    console.log('💾 Auto-saved notes');
                }, 2000); // Auto-save after 2 seconds of no typing
            });
        }
    }
    
    // ===== INITIALIZE ALL FEATURES =====
    function initEnhancements() {
        // Wait a bit for markdown to render
        setTimeout(() => {
            addCopyButtons();
            addNotesArea();
            setupAutoSave();
        }, 300);
    }
    
    // ===== HOOK INTO PAGE LOADS =====
    // Run when page first loads
    if (document.readyState === 'loading') {
        document. addEventListener('DOMContentLoaded', initEnhancements);
    } else {
        initEnhancements();
    }
    
    // Also run whenever content changes (watch for navigation clicks)
    const originalLoadMarkdown = window.loadMarkdown;
    if (originalLoadMarkdown) {
        window.loadMarkdown = async function(filename) {
            window.currentMarkdownFile = filename; // Track current file
            await originalLoadMarkdown(filename);
            initEnhancements(); // Re-init features after new content loads
        };
    }
    
    console.log('🎉 All enhancements initialized!');
})();