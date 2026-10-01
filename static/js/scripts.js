// scripts.js - Interactividad frontend para Mi Proyecto Django

document.addEventListener('DOMContentLoaded', () => {
    console.log('Django Static Scripts cargados correctamente.');

    // Funcionalidad de filtro de búsqueda para tablas de datos dinámicos
    const searchInputs = document.querySelectorAll('.search-input');
    searchInputs.forEach(input => {
        input.addEventListener('keyup', (e) => {
            const query = e.target.value.toLowerCase();
            const targetTableId = e.target.getAttribute('data-table-target');
            if (targetTableId) {
                const rows = document.querySelectorAll(`#${targetTableId} tbody tr`);
                rows.forEach(row => {
                    const text = row.textContent.toLowerCase();
                    row.style.display = text.includes(query) ? '' : 'none';
                });
            }

            // También filtrar listas simples si existen
            const targetListId = e.target.getAttribute('data-list-target');
            if (targetListId) {
                const items = document.querySelectorAll(`#${targetListId} li`);
                items.forEach(item => {
                    const text = item.textContent.toLowerCase();
                    item.style.display = text.includes(query) ? 'flex' : 'none';
                });
            }
        });
    });
});
