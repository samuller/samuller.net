/**
 * Countdown timer with voice alerts on state change.
 */

/* Text-to-speech support */
var speechSupported = false;
var speech = null;
if ('speechSynthesis' in window && window.speechSynthesis.getVoices().length > 0) {
    speechSupported = true;
    var speech = new SpeechSynthesisUtterance();
} else {
    speechSupported = false;
    console.log("Your browser doesn't support text to speech!");
}
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

/* Countdown timer */

// Whether countdown has been started since a countdown timer was set (used to differentiate
// between pauses and full restarts).
var countdownStarted = false;
// Initial starting time of countdown timer
var countdownTime = 5;

// If the countdown is currently active and counting down
var countdownActive = false;
// Current countdown time counter (seconds)
var countdownSec = countdownTime;

// Need to force the next update to happen when we externally alter countdownSec
// Start it with true to update on initial page load
var forceNextUpdate = true;

function resetCountdown() {
    countdownActive = false;
    countdownSec = countdownTime;
    forceNextUpdate = true;
}

function updateCountdownDisplay(seconds) {
    const hhmmss = new Date(seconds * 1000).toISOString().substring(11, 19);
    // British use 24-hour time strings and UTC needed to remove any time offset.
    // Thus, alternative: .toLocaleTimeString("en-GB", {timeZone: 'UTC'});
    document.getElementById("countdown").innerHTML = hhmmss;
    document.title = hhmmss;
}

function updateCountdown() {
    var varUpdated = false;
    if (countdownActive) {
        if (countdownSec > 0) {
            countdownSec -= 1;
            varUpdated = true;
        } else {
            // Stop countdown when it reaches zero
            resetCountdown();
            speak(_lang.onEnd);
        }
    }
    if (varUpdated || forceNextUpdate) {
        updateCountdownDisplay(countdownSec);
        forceNextUpdate = false;
    }
    setTimeout(updateCountdown, 1000);
}

/**
 * Toggle state of countdown timer, e.g. active/started vs. paused/stopped.
 */
function toggleCountdown() {
    countdownActive = !countdownActive;

    // Select a message to indicate the update in countdown state
    var updateMsg = _lang.onPause;
    if (countdownActive) {
        updateMsg = _lang.onResume;
        if (!countdownStarted) {
            updateMsg = _lang.onStart;
        }
    }
    speak(updateMsg);

    countdownStarted = true;
}

// Start updates on page load
updateCountdown();
