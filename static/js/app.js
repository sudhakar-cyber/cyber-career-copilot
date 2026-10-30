/**
 * AI Cybersecurity Career Copilot - Interactive Client Logic
 */

document.addEventListener('DOMContentLoaded', () => {
    // 1. Mobile Sidebar Toggle
    const mobileBtn = document.getElementById('mobileMenuBtn');
    const sidebar = document.getElementById('appSidebar');

    if (mobileBtn && sidebar) {
        mobileBtn.addEventListener('click', () => {
            sidebar.classList.toggle('open');
        });

        // Close sidebar on click outside on mobile
        document.addEventListener('click', (e) => {
            if (window.innerWidth <= 768 && sidebar.classList.contains('open')) {
                if (!sidebar.contains(e.target) && !mobileBtn.contains(e.target)) {
                    sidebar.classList.remove('open');
                }
            }
        });
    }

    // 2. Flash Alert Auto-Dismiss
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        const closeBtn = alert.querySelector('.alert-close');
        if (closeBtn) {
            closeBtn.addEventListener('click', () => {
                alert.style.opacity = '0';
                setTimeout(() => alert.remove(), 250);
            });
        }
        // Auto fade after 5 seconds
        setTimeout(() => {
            if (alert.parentNode) {
                alert.style.opacity = '0';
                setTimeout(() => alert.remove(), 250);
            }
        }, 5000);
    });

    // 3. Roadmap Task Completion Checkbox (AJAX)
    const taskCheckboxes = document.querySelectorAll('.task-toggle-btn');
    taskCheckboxes.forEach(btn => {
        btn.addEventListener('click', async (e) => {
            e.preventDefault();
            const taskId = btn.getAttribute('data-task-id');
            const taskItem = document.getElementById(`task-item-${taskId}`);
            const checkIcon = btn.querySelector('.task-checkbox-box');

            try {
                const response = await fetch('/api/toggle-task', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ task_id: taskId })
                });

                const result = await response.json();
                if (result.success) {
                    if (result.is_completed) {
                        taskItem.classList.add('completed');
                        checkIcon.classList.add('checked');
                        checkIcon.innerHTML = `<svg viewBox="0 0 24 24" width="14" height="14" stroke="currentColor" stroke-width="3" fill="none"><polyline points="20 6 9 17 4 12"></polyline></svg>`;
                    } else {
                        taskItem.classList.remove('completed');
                        checkIcon.classList.remove('checked');
                        checkIcon.innerHTML = '';
                    }

                    // Update progress display if elements exist
                    const progressFill = document.getElementById('roadmapProgressFill');
                    const progressText = document.getElementById('roadmapProgressText');
                    const completedCount = document.getElementById('completedTasksCount');

                    if (progressFill) progressFill.style.width = `${result.overall_progress}%`;
                    if (progressText) progressText.innerText = `${result.overall_progress}%`;
                    if (completedCount) completedCount.innerText = result.completed_tasks;
                }
            } catch (err) {
                console.error("Error toggling task:", err);
            }
        });
    });

    // 4. Project Status Selector Update (AJAX)
    const projectSelectors = document.querySelectorAll('.project-status-select');
    projectSelectors.forEach(select => {
        select.addEventListener('change', async (e) => {
            const projectId = select.getAttribute('data-project-id');
            const newStatus = select.value;
            const card = document.getElementById(`project-card-${projectId}`);

            try {
                const res = await fetch('/api/update-project-status', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ project_id: projectId, status: newStatus })
                });
                const data = await res.json();
                if (data.success && card) {
                    card.style.borderColor = newStatus === 'Completed' ? 'var(--cyber-green)' : (newStatus === 'In Progress' ? 'var(--cyber-blue)' : 'var(--border-subtle)');
                }
            } catch (err) {
                console.error("Error updating project status:", err);
            }
        });
    });

    // 5. Accessible Dialog / Modal Management (Modern Web Standards)
    const modalOpenTriggers = document.querySelectorAll('[data-open-modal]');
    modalOpenTriggers.forEach(btn => {
        btn.addEventListener('click', () => {
            const modalId = btn.getAttribute('data-open-modal');
            const dialog = document.getElementById(modalId);
            if (dialog && typeof dialog.showModal === 'function') {
                dialog.showModal();
            }
        });
    });

    const modalCloseTriggers = document.querySelectorAll('[data-close-modal]');
    modalCloseTriggers.forEach(btn => {
        btn.addEventListener('click', () => {
            const dialog = btn.closest('dialog');
            if (dialog && typeof dialog.close === 'function') {
                dialog.close();
            }
        });
    });

    // Light dismiss for dialog backdrops
    const allDialogs = document.querySelectorAll('dialog.cyber-modal');
    allDialogs.forEach(dialog => {
        dialog.addEventListener('click', (e) => {
            const rect = dialog.getBoundingClientRect();
            const isInDialog = (
                rect.top <= e.clientY && e.clientY <= rect.top + rect.height &&
                rect.left <= e.clientX && e.clientX <= rect.left + rect.width
            );
            if (!isInDialog) {
                dialog.close();
            }
        });
    });

    // 6. Cyber Copilot Chatbot Handler
    const chatForm = document.getElementById('chatForm');
    const chatInput = document.getElementById('chatInput');
    const chatMessages = document.getElementById('chatMessages');
    const clearChatBtn = document.getElementById('clearChatBtn');
    const suggestionChips = document.querySelectorAll('.suggestion-chip');

    if (chatForm && chatInput && chatMessages) {
        // Auto scroll to bottom
        chatMessages.scrollTop = chatMessages.scrollHeight;

        // Click suggestion chip
        suggestionChips.forEach(chip => {
            chip.addEventListener('click', () => {
                chatInput.value = chip.innerText.replace(/[✨🔥🛡️🚀📜]/g, '').trim();
                chatForm.dispatchEvent(new Event('submit'));
            });
        });

        // Submit message
        chatForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const message = chatInput.value.trim();
            if (!message) return;

            // Append user bubble
            appendChatBubble('user', escapeHtml(message));
            chatInput.value = '';

            // Typing indicator bubble
            const loadingBubble = appendChatBubble('copilot', '<span class="typing-indicator">Cyber Copilot is thinking...</span>');

            try {
                const response = await fetch('/api/chat', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ message: message })
                });

                const data = await response.json();
                if (data.success) {
                    loadingBubble.innerHTML = formatMarkdown(data.response);
                } else {
                    loadingBubble.innerHTML = `<span style="color:var(--cyber-red);">Error: ${data.error || 'Unable to connect to Copilot'}</span>`;
                }
            } catch (err) {
                loadingBubble.innerHTML = `<span style="color:var(--cyber-red);">Network connection failed. Please retry.</span>`;
            }

            chatMessages.scrollTop = chatMessages.scrollHeight;
        });

        // Clear Chat
        if (clearChatBtn) {
            clearChatBtn.addEventListener('click', async () => {
                if (!confirm("Are you sure you want to clear your conversation history?")) return;
                try {
                    await fetch('/api/clear-chat', { method: 'POST' });
                    chatMessages.innerHTML = `
                        <div class="chat-bubble copilot">
                            <blockquote>ℹ️ <strong>System Initialized</strong></blockquote>
                            Hello! I am your <strong>Cyber Copilot</strong>. Ask me anything about career paths, certifications, projects, or interview prep.
                        </div>
                    `;
                } catch (e) {
                    console.error("Error clearing chat", e);
                }
            });
        }
    }
});

// Helper: Append chat bubble
function appendChatBubble(sender, contentHtml) {
    const chatContainer = document.getElementById('chatMessages');
    if (!chatContainer) return null;
    const bubble = document.createElement('div');
    bubble.className = `chat-bubble ${sender}`;
    bubble.innerHTML = contentHtml;
    chatContainer.appendChild(bubble);
    chatContainer.scrollTop = chatContainer.scrollHeight;
    return bubble;
}

// Basic markdown formatter for Copilot responses
function formatMarkdown(text) {
    if (!text) return '';
    let parsed = text
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/^### (.*$)/gim, '<h4 style="margin:8px 0 4px; color:var(--cyber-cyan); font-weight:700;">$1</h4>')
        .replace(/^## (.*$)/gim, '<h3 style="margin:10px 0 6px; color:var(--text-bright);">$1</h3>')
        .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
        .replace(/\*(.*?)\*/g, '<em>$1</em>')
        .replace(/`([^`]+)`/g, '<code style="background:rgba(0,242,254,0.1); padding:2px 5px; border-radius:4px; color:var(--cyber-cyan); font-family:var(--font-mono); font-size:12px;">$1</code>')
        .replace(/^\> (.*$)/gim, '<blockquote style="border-left:3px solid var(--cyber-cyan); padding-left:10px; margin:6px 0; color:var(--text-muted);">$1</blockquote>')
        .replace(/\n/g, '<br>');
    return parsed;
}

function escapeHtml(str) {
    return str.replace(/[&<>"']/g, function(m) {
        return {
            '&': '&amp;',
            '<': '&lt;',
            '>': '&gt;',
            '"': '&quot;',
            "'": '&#039;'
        }[m];
    });
}
