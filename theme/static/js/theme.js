---
---

/**
 * Iterate between possible themes.
 */
function switchTheme(){
    let themes = ['light', 'dark', 'white'];
    let currTheme = document.documentElement.getAttribute('data-theme');
    let currIdx = Math.max(themes.indexOf(currTheme), 0);
    let newTheme = themes[(currIdx + 1) % themes.length];
    document.documentElement.setAttribute('data-theme', newTheme);
}

/**
 * Hide/show elements with 'ref-link' class.
 */
function toggleRefLinks() {
    for (let el of document.querySelectorAll('.ref-link')) {
        if (['', 'none'].includes(el.style.display)) {
            el.style.display = 'initial';
        } else if (el.style.display == 'initial') {
            el.style.display = 'none';
        }
    }
}
