window.addEventListener('load', () => {
    const filter = document.querySelector('#pixel-glitch feTurbulence');
    if (filter) {
        // Рандомізуємо частоту шуму при кожному завантаженні для унікальних смуг
        const seed = Math.random() * 100;
        filter.setAttribute('seed', seed);
    }
});