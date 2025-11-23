/* =======================================================================
   Custom JavaScript for Generador de Constancias
   Bootstrap 5 + Custom Interactions
   ======================================================================= */

document.addEventListener('DOMContentLoaded', function() {
    
    // Initialize Bootstrap tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function(tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Initialize Bootstrap popovers
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    var popoverList = popoverTriggerList.map(function(popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    // Auto-hide alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert:not(.alert-permanent)');
    alerts.forEach(function(alert) {
        setTimeout(function() {
            const bsAlert = new bootstrap.Alert(alert);
            if (bsAlert) {
                bsAlert.close();
            }
        }, 5000);
    });

    // Form validation enhancement
    const forms = document.querySelectorAll('.needs-validation');
    forms.forEach(function(form) {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
                
                // Focus on first invalid field
                const firstInvalid = form.querySelector(':invalid');
                if (firstInvalid) {
                    firstInvalid.focus();
                }
            }
            form.classList.add('was-validated');
        });
    });

    // Smooth scrolling for anchor links
    const anchorLinks = document.querySelectorAll('a[href^="#"]');
    anchorLinks.forEach(function(link) {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href !== '#' && href !== '#!') {
                const target = document.querySelector(href);
                if (target) {
                    e.preventDefault();
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    });

    // Loading state for buttons
    function addLoadingState(button, text = 'Cargando...') {
        const originalText = button.innerHTML;
        button.innerHTML = `
            <span class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span>
            ${text}
        `;
        button.disabled = true;
        
        return function() {
            button.innerHTML = originalText;
            button.disabled = false;
        };
    }

    // Add loading state to form submission buttons
    const submitButtons = document.querySelectorAll('button[type="submit"]');
    submitButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            const form = button.closest('form');
            if (form && form.checkValidity()) {
                addLoadingState(button);
            }
        });
    });

    // File upload progress (if needed)
    const fileInputs = document.querySelectorAll('input[type="file"]');
    fileInputs.forEach(function(input) {
        input.addEventListener('change', function() {
            const fileName = this.files[0]?.name;
            const label = this.nextElementSibling;
            if (label && label.classList.contains('form-label')) {
                label.textContent = fileName || 'Seleccionar archivo';
            }
        });
    });

    // Table enhancements
    const tables = document.querySelectorAll('.table-sortable');
    tables.forEach(function(table) {
        const headers = table.querySelectorAll('th[data-sort]');
        headers.forEach(function(header) {
            header.style.cursor = 'pointer';
            header.addEventListener('click', function() {
                sortTable(table, this.dataset.sort);
            });
        });
    });

    // Simple table sorting function
    function sortTable(table, column) {
        const tbody = table.querySelector('tbody');
        const rows = Array.from(tbody.querySelectorAll('tr'));
        const isAscending = table.dataset.sortOrder !== 'asc';
        
        rows.sort(function(a, b) {
            const aValue = a.querySelector(`td:nth-child(${getColumnIndex(table, column)})`).textContent.trim();
            const bValue = b.querySelector(`td:nth-child(${getColumnIndex(table, column)})`).textContent.trim();
            
            if (isAscending) {
                return aValue.localeCompare(bValue, 'es', { numeric: true });
            } else {
                return bValue.localeCompare(aValue, 'es', { numeric: true });
            }
        });
        
        rows.forEach(function(row) {
            tbody.appendChild(row);
        });
        
        table.dataset.sortOrder = isAscending ? 'asc' : 'desc';
        
        // Update sort indicators
        const allHeaders = table.querySelectorAll('th[data-sort]');
        allHeaders.forEach(function(h) {
            h.classList.remove('sorted-asc', 'sorted-desc');
        });
        
        const currentHeader = table.querySelector(`th[data-sort="${column}"]`);
        currentHeader.classList.add(isAscending ? 'sorted-asc' : 'sorted-desc');
    }

    function getColumnIndex(table, column) {
        const headers = table.querySelectorAll('th');
        for (let i = 0; i < headers.length; i++) {
            if (headers[i].dataset.sort === column) {
                return i + 1;
            }
        }
        return 1;
    }

    // Search functionality
    const searchInputs = document.querySelectorAll('.table-search');
    searchInputs.forEach(function(input) {
        const targetTable = document.querySelector(input.dataset.target);
        if (targetTable) {
            input.addEventListener('input', function() {
                filterTable(targetTable, this.value);
            });
        }
    });

    function filterTable(table, searchTerm) {
        const rows = table.querySelectorAll('tbody tr');
        const term = searchTerm.toLowerCase();
        
        rows.forEach(function(row) {
            const text = row.textContent.toLowerCase();
            row.style.display = text.includes(term) ? '' : 'none';
        });
    }

    // Confirmation dialogs
    const confirmButtons = document.querySelectorAll('[data-confirm]');
    confirmButtons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            const message = this.dataset.confirm;
            if (!confirm(message)) {
                e.preventDefault();
                return false;
            }
        });
    });

    // Auto-resize textareas
    const textareas = document.querySelectorAll('textarea.auto-resize');
    textareas.forEach(function(textarea) {
        textarea.addEventListener('input', function() {
            this.style.height = 'auto';
            this.style.height = (this.scrollHeight) + 'px';
        });
    });

    // Copy to clipboard functionality
    const copyButtons = document.querySelectorAll('.copy-button');
    copyButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            const target = document.querySelector(this.dataset.target);
            if (target) {
                navigator.clipboard.writeText(target.textContent).then(function() {
                    // Show success feedback
                    const originalText = button.textContent;
                    button.textContent = '¡Copiado!';
                    setTimeout(function() {
                        button.textContent = originalText;
                    }, 2000);
                });
            }
        });
    });

    console.log('Generador de Constancias - JavaScript loaded successfully');
});