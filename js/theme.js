---
---

function toggleTheme(){
    let currTheme = document.documentElement.getAttribute('data-theme');
    let newTheme = currTheme == 'light' ? 'dark' : 'light';
    document.documentElement.setAttribute('data-theme', newTheme);
}
