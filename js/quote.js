---
---

function isVueLoaded() {
    try {
        new Vue();
        return true;
    }
    catch (e) {
        if (e instanceof ReferenceError) {
            return false;
        }
    }
}

var quoteData = {{ site.data.quotes | jsonify }};
var categories = Object.keys(quoteData);

var url = new URL(location.href);
var category = url.searchParams.get("cat");
var quoteIdx = parseInt(url.searchParams.get("nr")) - 1;
var nextCategory = categories[Math.floor(Math.random() * categories.length)];

if (!quoteData.hasOwnProperty(category)) { category = null; }
if (category === null) {
    category = categories[Math.floor(Math.random() * categories.length)];
    quoteIdx = Math.floor(Math.random() * quoteData[category].length)
}
if (quoteIdx === null || isNaN(quoteIdx)) {
    quoteIdx = Math.floor(Math.random() * quoteData[category].length)
}

if (isVueLoaded()) {
    var el = document.querySelector('#inCase');
    el.parentNode.removeChild(el);
}

var categorySize = quoteData[category].length;
var app = new Vue({
    el: '#quoteApp',
    data: {
        quoteNr: quoteIdx + 1,
        prevQuoteNr: (quoteIdx == 0) ? categorySize : ((quoteIdx + 1) - 1),
        nextQuoteNr: 1 + ((quoteIdx + 1) % categorySize),
        category: category,
        categorySize: categorySize,
        currQuote: quoteData[category][quoteIdx],
        nextCategory: nextCategory
    }
});