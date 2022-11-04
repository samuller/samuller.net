/**

To get text-to-speech working with Chromium on Ubuntu:
```
# Check that spd-say is installed and working
spd-say "some text"
# If not, check its list of languages
spd-say -L
# Once working, run chromium with parameter/flag
chromium --enable-speech-dispatcher
```

*/

/**
 * Countdown timer with voice alerts on state change.
 */

/* Text-to-speech support */
var speechSupported = false;
var voices = [];
var speech = null;

function checkVoices() {
    speechSupported = false
    speech = null;
    voices = window.speechSynthesis.getVoices();
    if(voices.length > 0) {
        speechSupported = true;
        speech = new SpeechSynthesisUtterance();
        // Update UI elements
        btnaudioicon.className = "";
        btnaudioicon.classList.add("fa-solid", "fa-volume-high");

        inp_voice.innerHTML = "";
        inp_voice.options.add(new Option("Default voice", ""));
        for (let i = 0; i < voices.length; i++) {
            let name = voices[i].name;
            let lang = voices[i].lang;
            inp_voice.options.add(new Option(`${name} [${lang}]`, i.toString()));
        }
        return true;
    } else {
        btnaudioicon.className = "";
        btnaudioicon.classList.add("fa-solid", "fa-volume-xmark");
        // and gray out button with "text: #666"
        return false;
    }
}

if ('speechSynthesis' in window) {
    checkVoices();
    // Support browsers that load voices after a delay (of checking remote servers)
    speechSynthesis.addEventListener("voiceschanged", () => {
        let supported = checkVoices();
        if (supported) {
            console.log("Text-to-speech voices found after delay!");
        }
    });
} else {
    console.log("Your browser doesn't support text to speech!");
}

// Centralise all spoken words
const _lang = {
    onStart: "Starting countdown",
    onEnd: "Countdown completed.",
    onPause: "Pause",
    onResume: "Continuing countdown",
    onEveryXSec: "10",
    onLastXSec: "5",
};

function speak(message) {
    if (!speechSupported) {
        return;
    }
    speech.lang = 'en';

    speech.text = message;
    window.speechSynthesis.cancel();
    window.speechSynthesis.speak(speech);
}

let alertList = document.getElementById("list-alerts-state");
for (const [key, value] of Object.entries(_lang)) {
    alertList.insertAdjacentHTML("beforeend",
        `<input type="checkbox" id="state_${key.toLowerCase()}_check" checked disabled />
        <label for="state_${key.toLowerCase()}_check">${key}:&nbsp;</label>
        <input type="text" id="state_${key.toLowerCase()}_text" value="${value}" style="flex: 1" oninput="_lang['${key}'] = this.value">`
    );
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
        // unobserved attributes: onstart, onpause, onresume, onreset, onend, onrender
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
            this.reset();
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
        eval(this.getAttribute('onstart'));
    }

    pause() {
        this.clearTimer();
        speak(_lang.onPause);
        eval(this.getAttribute('onpause'));
    }

    resume() {
        this.start(true);
        speak(_lang.onResume);
        eval(this.getAttribute('onresume'));
    }

    reset() {
        this.started = false;
        this.sec = this.initTime;
        this.active = false;
        this.forceNextUpdate = true;
        this.clearTimer();
        this.render();
        // TODO: move out into onreset attribute
        btnplayicon.classList.add("fa-play");
        btnplayicon.classList.remove("fa-pause");
        eval(this.getAttribute('onreset'));
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
        return this.active;
    }

    update() {
        let varUpdated = false;
        if (this.active) {
            if (this.sec > 0) {
                this.sec -= 1;
                varUpdated = true;
                if (this.sec == 0) {
                    speak(_lang.onEnd);
                    eval(this.getAttribute('onend'));
                } else if ((this.sec % parseInt(_lang.onEveryXSec) == 0) || (this.sec <= parseInt(_lang.onLastXSec))){
                    speak(`${this.sec}`);
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
        eval(this.getAttribute('onrender'));
    }

}

// Register our new web component
if ('customElements' in window) {
	customElements.define('app-countdown', CountdownTimer);
}

/**
 * Setup media control components.
 */

// Allow only keyboard events where numbers are typed.
function allowOnlyNumbers(evt) {
    evt = evt || window.event;
    var charCode = (typeof evt.which == "undefined") ? evt.keyCode : evt.which;
    var charStr = String.fromCharCode(charCode);
    if (!charStr.match(/^[0-9]+$/)) {
        evt.preventDefault();
    }
}

document.getElementById('inputsecs').addEventListener("keypress", allowOnlyNumbers);


class MediaControls {

    static setVoice(element) {
        speech.voice = voices[element.value];
    }

    static setVolume(element) {
        element.nextElementSibling.value = element.value;
        speech.volume = element.value / 100.0;
    }

    static setPitch(element) {
        element.nextElementSibling.value = element.value;
        speech.pitch = element.value / 100.0;
    }

    static setRate(element) {
        element.nextElementSibling.value = element.value;
        speech.rate = element.value / 100.0;
    }


    // Note that below we often take advantage of the fact that component id's get set directly on the "window" global,
    // and we can therefore use them directly as variables, e.g. an id of "component" becomes window["component"] or
    // window.component which can then be accessed directly as just "component", but only if the name is also a valid
    // parse-able variable name (i.e. no dashes which would parse to minuses).

    static clickSoundToggle() {
        formsound.hidden = !formsound.hidden;
        btnAudio.setAttribute('shadow_under', !formsound.hidden);
    }

    static updatePlayToggle(isPlaying) {
        if (isPlaying) {
            btnplayicon.classList.add("fa-pause");
            btnplayicon.classList.remove("fa-play");
        } else {
            btnplayicon.classList.add("fa-play");
            btnplayicon.classList.remove("fa-pause");
        }
    }

    static clickPlayToggle() {
        let active = countdown0.toggle();
        updatePlayToggle(active);
    }

    static clickReset() {
        countdown0.reset();
        btnplayicon.classList.add("fa-play");
        btnplayicon.classList.remove("fa-pause");
    }

    static clickSet() {
        // Toggle input section being shown (using the "hidden" boolean attribute)
        formsecs.hidden = !formsecs.hidden;
        // Toggle button shadow to make it look clickable (to indicate that clicking again does something)
        // btnset.setAttribute('shadow', !(btnset.getAttribute('shadow') === 'true'));
        btnset.setAttribute('shadow', !formsecs.hidden);
        // After closing input section
        if (formsecs.hidden) {
            // Set countdown attribute
            countdown0.setAttribute('secs', inputsecs.value);
        }
    }

}
