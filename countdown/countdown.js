/**
 * Countdown timer with voice alerts on state change.
 */

/* Text-to-speech support */
var speechSupported = false;
var speech = null;
if ('speechSynthesis' in window && window.speechSynthesis.getVoices().length > 0) {
    speechSupported = true;
    speech = new SpeechSynthesisUtterance();
} else {
    speechSupported = false;
    console.log("Your browser doesn't support text to speech!");
}

// Support browsers that load voices after a delay (of checking remote servers)
speechSynthesis.addEventListener("voiceschanged", () => {
    if(window.speechSynthesis.getVoices().length > 0) {
        speechSupported = true;
        speech = new SpeechSynthesisUtterance();
        console.log("Text-to-speech voices found after delay!");
    }
});

var voiceVolume = 1.0;

// Centralise all spoken words
const _lang = {
    onStart: "Starting countdown",
    onEnd: "Countdown completed.",
    onPause: "Pause",
    onResume: "Continuing countdown",
};

function speak(message) {
    if (!speechSupported) {
        return;
    }
    speech.volume = voiceVolume;
    speech.lang = 'en';

    speech.text = message;
    window.speechSynthesis.cancel();
    window.speechSynthesis.speak(speech);
}

/**
 * WebComponent/CustomElement class for countdown timer.
 */
class CountdownTimer extends HTMLElement {

    /**
     * Run when the element is created, but before its injected into the UI.
     */
    constructor () {
        super();

        // Whether countdown has been started since a countdown timer was set (used to differentiate
        // between pauses and full restarts).
        this.started = false;
        // Initial starting time of countdown timer
        this.initTime = 10;

        // If the countdown is currently active and counting down
        this.active = false;
        // Current countdown time counter (seconds)
        this.sec = this.initTime;

        // Need to force the next update to happen when we externally alter countdownSec
        // Start it with true to update on initial page load
        this.forceNextUpdate = true;

        this.timer = null;

        this.render();
    }

	/**
	 * Runs each time the element is appended to or moved in the DOM.
	 */
    connectedCallback () {
        this.addEventListener("click", this.handleClick);
    }

	/**
	 * Runs when the element is removed from the DOM.
	 */
	disconnectedCallback () {
        this.removeEventListener("click", this.handleClick);
        this.clearTimer();
    }

    /**
     * List all attributes to observe for changes.
     */
    static get observedAttributes () {
        return ["secs"];
    }

    /**
     * Runs when the value of an attribute is changed on the component.
     * @param  {String} name     The attribute name
     * @param  {String} oldValue The old attribute value
     * @param  {String} newValue The new attribute value
     */
    attributeChangedCallback (name, oldValue, newValue) {
        // console.log('changed', name, oldValue, newValue, this);
        if (name == "secs") {
            this.initTime = newValue;
        }
    }

    handleClick () {
        this.toggle();
    }

    clearTimer() {
        if (this.timer) {
            clearInterval(this.timer);
            this.timer = null;
        }
    }

    start(silent = false) {
        this.render();
        // Need bind() otherwise function can't access "this"
        this.timer = setInterval(this.update.bind(this), 1000);

        if(!silent) {
            speak(_lang.onStart);
        }
    }

    pause() {
        this.clearTimer();
        speak(_lang.onPause);
    }

    resume() {
        this.start(true);
        speak(_lang.onResume);
    }

    reset() {
        this.started = false;
        this.sec = this.initTime;
        this.active = false;
        this.forceNextUpdate = true;
        this.clearTimer();
        this.render();
    }

    startOrResume() {
        if (!this.started) {
            this.start();
        } else {
            this.resume()
        }
    }

    /**
     * Toggle state of countdown timer, e.g. active/started vs. paused/stopped.
     */
    toggle() {
        this.active = !this.active;
        if (this.active) {
            this.startOrResume();
        } else {
            this.pause();
        }
        this.started = true;
    }

    update() {
        let varUpdated = false;
        if (this.active) {
            if (this.sec > 0) {
                this.sec -= 1;
                varUpdated = true;
                if (this.sec == 0) {
                    speak(_lang.onEnd);
                }
            } else {
                // Stop countdown when it reaches zero
                this.reset();
            }
        }
        if (varUpdated || this.forceNextUpdate) {
            this.render();
            this.forceNextUpdate = false;
        }
    }

    static secToHHMMSS(seconds) {
        const hhmmss = new Date(seconds * 1000).toISOString().substring(11, 19);
        // British use 24-hour time strings and UTC needed to remove any time offset.
        // Thus, alternative: .toLocaleTimeString("en-GB", {timeZone: 'UTC'});
        return hhmmss;
    }

    render() {
        const hhmmss = CountdownTimer.secToHHMMSS(this.sec)
        const hms = [hhmmss.substr(0, 3), hhmmss.substr(3, 3), hhmmss.substr(6, 2)]
        this.innerHTML = `<span>${hms[0]}</span><span>${hms[1]}</span><span>${hms[2]}</span>`;
        // Show current timer in page/tab title (won't work for multiple timers on same page)
        document.title = hhmmss;
    }

}

// Register our new web component
if ('customElements' in window) {
	customElements.define('app-countdown', CountdownTimer);
}

/**
 * Setup media control components.
 */

document.getElementById('inputsecs').addEventListener("keypress", function (evt) {
    evt = evt || window.event;
    var charCode = (typeof evt.which == "undefined") ? evt.keyCode : evt.which;
    var charStr = String.fromCharCode(charCode);
    if (!charStr.match(/^[0-9]+$/)) {
        evt.preventDefault();
    }
});

// Note that below we often take advantage of the fact that component id's get set directly on the "window" global,
// and we can therefore use them directly as variables, e.g. an id of "component" becomes window["component"] or
// window.component which can then be accessed directly as just "component", but only if the name is also a valid
// parse-able variable name (i.e. no dashes which would parse to minuses).

function clickPlayToggle() {
    countdown0.toggle();
}

function clickReset() {
    countdown0.reset();
}

function clickSet() {
    // Toggle input section being shown (using the "hidden" boolean attribute)
    setsecs.hidden = !setsecs.hidden;
    // Toggle button shadow to make it look clickable (to indicate that clicking again does something)
    // btnset.setAttribute('shadow', !(btnset.getAttribute('shadow') === 'true'));
    btnset.setAttribute('shadow', !setsecs.hidden);
    // After closing input section
    if (setsecs.hidden) {
        // Set countdown attribute
        countdown0.setAttribute('secs', inputsecs.value);
    }
}
