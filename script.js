document.querySelectorAll('.drop-area').forEach(area => {
    area.addEventListener('drop', function(e) {
        e.preventDefault();
        // Logique pour manipuler les colonnes
    });

    area.addEventListener('dragover', function(e) {
        e.preventDefault();
    });
});

function updateTable(groupingRows, groupingCols) {
    // Fonction pour mettre à jour le tableau après regroupement
}
