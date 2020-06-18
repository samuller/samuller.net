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
