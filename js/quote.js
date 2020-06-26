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

function processURL(url) {
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
    return {quoteIdx: quoteIdx, category: category};
}

var quoteData = {{ site.data.quotes | jsonify }};
var categories = Object.keys(quoteData);
var data = processURL(new URL(location.href));

if (isVueLoaded()) {
    // delete filler div
    var el = document.querySelector('#inCase');
    el.parentNode.removeChild(el);
    // remove "display: hidden" inline style on app div
    el = document.querySelector('#quoteApp');
    el.style.removeProperty('display');
}

var app = new Vue({
    el: '#quoteApp',
    data: {
        quoteIdx: data.quoteIdx,
        category: data.category,
    },
    computed: {
        quoteNr: function () {
            return this.quoteIdx + 1;
        },
        prevQuoteNr: function () {
            return (this.quoteIdx == 0) ? this.categorySize : ((this.quoteIdx + 1) - 1);
        },
        nextQuoteNr: function () {
            return 1 + ((this.quoteIdx + 1) % this.categorySize);
        },
        currQuote: function () {
            return quoteData[this.category][this.quoteIdx];
        },
        categorySize: function () {
            return quoteData[this.category].length;
        },
    },
    watch: {
        quoteIdx: function (val) {
            if (history.state.quoteIdx != this.quoteIdx) {
                history.pushState(
                    {quoteIdx: this.quoteIdx, category: this.category}, '',
                    '?cat=' + this.category + '&nr=' + this.quoteNr);
            }
        },
        category: function (val) {
            if (history.state.category != this.category) {
                history.pushState(
                    {quoteIdx: this.quoteIdx, category: this.category}, '',
                    '?cat=' + this.category + '&nr=' + this.quoteNr);
            }
        }
    },
    methods: {
        prevQuote: function() {
            this.quoteIdx = (this.quoteIdx == 0) ? this.categorySize - 1 : (this.quoteIdx - 1);
        },
        nextQuote: function() {
            this.quoteIdx = ((this.quoteIdx + 1) % this.categorySize);
        },
        randomCategory: function() {
            this.category = categories[Math.floor(Math.random() * categories.length)];
            this.quoteIdx = Math.floor(Math.random() * quoteData[this.category].length);
        }
    }
});

// Set current state for to history to work
window.history.replaceState(data, '');
// When you press 'back' or 'forward' in history, update app state
window.onpopstate = function(event) {
    if (event.state) {
        app.quoteIdx = event.state.quoteIdx;
        app.category = event.state.category;
    }
};
