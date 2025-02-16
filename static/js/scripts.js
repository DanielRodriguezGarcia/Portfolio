// Animación al hacer clic en una habilidad
document.querySelectorAll('.skill-item').forEach(item => {
    item.addEventListener('click', () => {
        alert(`Has seleccionado: ${item.textContent}`);
    });
});

// Animación de desplazamiento suave
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});