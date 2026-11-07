let scripturesAll = [];
let scripturesPool = [];
let scriptureCurrent;
let correctNum;
let totalGuessed;
let guess;
let correctAnswer;
let applicableBooks;
let enhancedBalance = false;
let scripturesByBook;
let history = document.getElementById('history');
fetch('./scriptures.json').then(response => response.json()).then(scriptures => scripturesAll = scriptures);

function startGame() {
    // Grab all the scriptures based off selected books
    scripturesPool = getSelectedScriptures()
    if (scripturesPool.length === 0) {
        alert('You must select at least one book of scripture to play the game!');
        return;
    };

    // Group scriptures by book (for enhanced mode)
    scripturesByBook = new Map();

    for (const verse of scripturesPool) {
        if (!scripturesByBook.has(verse.book_title)) {
            scripturesByBook.set(verse.book_title, []);
        }
        scripturesByBook.get(verse.book_title).push(verse);
    }

    // Get book titles into selectbox
    let answerBox = document.getElementById('scripture-books');
    answerBox.replaceChildren();
    applicableBooks = [...scripturesByBook.keys()]
    applicableBooks.forEach(bookTitle => {
        let option = document.createElement('option');
        option.value = bookTitle;
        option.textContent = bookTitle;
        answerBox.append(option);
    });

    // Initialize score, and first random scripture
    correctNum = 0;
    totalGuessed = 0;
    document.getElementById('score').textContent = ''
    getRandomScripture();

    // Initialize history
    history.replaceChildren();
    document.getElementById('history').hidden = true;
    document.getElementById('history-button').textContent = 'Show History';

    // Change visible screen
    document.getElementById('menu').hidden = true;
    document.getElementById('game').hidden = false;

    // Go back to top of page
    window.scrollTo({top: 0, behavior:"smooth"});
};

function returnToMenu() {
    document.getElementById('game').hidden = true;
    document.getElementById('menu').hidden = false;
    document.getElementById('settings').hidden = true;

    // Go back to top of page
    window.scrollTo({top: 0, behavior:"smooth"});
};

function goToSettings() {
    document.getElementById('game').hidden = true;
    document.getElementById('menu').hidden = true;
    document.getElementById('settings').hidden = false;

    // Go back to top of page
    window.scrollTo({top: 0, behavior:"smooth"});
};


function getSelectedScriptures() {
    const selectedVolumes = [...document.querySelectorAll('input[name~="book-select"]:checked')].map(checkbox => checkbox.value);
    return scripturesAll.filter(verse => selectedVolumes.includes(verse.book_title));
};

function getRandomScripture() {
    if (!enhancedBalance) {
        // Regular mode
        const randomIndex = Math.floor(Math.random() * scripturesPool.length);
        scriptureCurrent = scripturesPool[randomIndex];
    } else {
        // Enhanced balance mode
        const randomBook = applicableBooks[Math.floor(Math.random() * applicableBooks.length)];

        const versesFromBook = scripturesByBook.get(randomBook);
        const randomIndex = Math.floor(Math.random() * versesFromBook.length);

        scriptureCurrent = versesFromBook[randomIndex];
    }
    

    document.getElementById('random-scripture').textContent = scriptureCurrent.scripture_text;
    correctAnswer = scriptureCurrent.book_title;
};

function submitAnswer() {
    document.getElementById('submit-button').disabled = true;
    totalGuessed += 1;
    guess = document.getElementById('scripture-books').value;

    let historyEntry = document.createElement('p');
    historyEntry.textContent = scriptureCurrent.verse_title;
    if (guess == correctAnswer) {
        correctNum += 1;
        historyEntry.classList.add('correct');
    } else {
        historyEntry.classList.add('incorrect');
    };
    history.append(historyEntry);

    document.getElementById('score').textContent = `${correctNum} / ${totalGuessed} (${(correctNum / totalGuessed * 100).toFixed(2)}%)`;
    document.getElementById('correct-answer').textContent = scriptureCurrent.verse_title;

    setTimeout(() => {
        document.getElementById('correct-answer').textContent = '';
        getRandomScripture();
        document.getElementById('submit-button').disabled = false;
    },1000); 
};

function selectAll(book) {
    document.querySelectorAll(`input[name~="${book}"]`).forEach(checkbox => {
        checkbox.checked = true;
    });
};

function unselectAll(book) {
    document.querySelectorAll(`input[name~="${book}"]`).forEach(checkbox => {
        checkbox.checked = false;
    });
};

function toggleHistory() {
    let historyButton = document.getElementById('history-button');
    if (history.hidden == true) {
        history.hidden = false;
        historyButton.textContent = 'Hide History';
    } else {
        history.hidden = true;
        historyButton.textContent = 'Show History';
    };
};

function toggleDarkMode() {
    body = document.getElementById('body');
    darkModeButton = document.getElementById('dark-mode-button');
    if (!body.classList.contains('dark-mode')) {
        body.classList.add('dark-mode');
        darkModeButton.textContent = 'Disable Dark Mode';
    } else {
        body.classList.remove('dark-mode');
        darkModeButton.textContent = 'Enable Dark Mode';
    }
}

function toggleBalanceMode() {
    body = document.getElementById('body');
    balanceModeButton = document.getElementById('balance-mode-button');
    if (!enhancedBalance) {
        enhancedBalance = true;
        balanceModeButton.textContent = 'Disable Enhanced Balance Mode';
    } else {
        enhancedBalance = false;
        balanceModeButton.textContent = 'Enable Enhanced Balance Mode';
    }
}