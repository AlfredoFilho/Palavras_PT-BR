// Wait for the DOM to be fully loaded before executing this code
document.addEventListener("DOMContentLoaded", function () {

    // Check if the browser supports WebAssembly
    if (typeof WebAssembly === 'object' && typeof WebAssembly.instantiate === 'function') {
        console.log("The browser supports WebAssembly.");
        start();
    } else {
        console.log("Your browser does NOT support WebAssembly.");
        showErrorModal("Your browser does NOT support WebAssembly.")
    }

    const input = document.getElementById("inputQuery");
    const button = document.getElementById("buttonExecute");

    input.focus();
    input.setSelectionRange(input.value.length, input.value.length);

    // Listen for keydown events in the input element
    input.addEventListener("keydown", function (event) {
        // If the Enter key (key code 13) is pressed, trigger a click on the execute button
        if (event.keyCode === 13) {
            button.click();
        }
    });
});


document.addEventListener("DOMContentLoaded", function () {

    const copyButtonLabel = "Copy";
    let blocks = document.querySelectorAll("pre");

    blocks.forEach((block) => {
        // only add button if browser supports Clipboard API
        if (navigator.clipboard) {
            let button = document.createElement("button");
            button.id = "bntCopy"

            button.innerText = copyButtonLabel;
            block.appendChild(button);

            button.addEventListener("click", async () => {
                await copyCode(block, button);
            });
        }
    });

});

async function copyCode(block, button) {
    let code = block.querySelector("code");
    let text = code.innerText;

    await navigator.clipboard.writeText(text);
    button.innerText = "Code Copied";

    setTimeout(() => {
        button.innerText = copyButtonLabel;
    }, 700);
}

let db = undefined;

async function start() {
    try {
        // Initialize SQL.js with the WebAssembly file
        const sqlPromise = initSqlJs({
            locateFile: (file) => `./assets/js/sql-wasm.wasm`,
        });

        // Fetch the database file
        const dataPromise = fetch("./Palavras_PT-BR.db").then((res) => res.arrayBuffer());

        // Wait for both promises to resolve
        const [SQL, buf] = await Promise.all([sqlPromise, dataPromise]);

        // Create a new database instance with the fetched data
        db = new SQL.Database(new Uint8Array(buf));

        // Get the total number of rows in the "words" table
        var totalRows = undefined
        const stmtSelectCount = db.prepare("SELECT COUNT(*) AS totalRows FROM words;");
        while (stmtSelectCount.step()) {
            const result = stmtSelectCount.getAsObject();
            totalRows = result.totalRows;
        }

        // Display the total number of rows in the HTML element with id "totalRows"
        document.getElementById("totalRows").textContent = `- ${totalRows.toLocaleString()} rows`;

    } catch (error) {
        // Handle any errors that occur during initialization
        console.error("Error initializing the database:", error);
    }
}

function showLoader() {
    document.getElementById("loader").style.display = "block";
}

function hideLoader() {
    document.getElementById("loader").style.display = "none";
}

function executeWithLoader() {
    showLoader();

    setTimeout(function () {
        const inputQuery = document.getElementById("inputQuery").value;
        executeQuery(inputQuery);

        hideLoader();
    }, 100);
}

function findDangerousKeyword(query) {
    const dangerousKeywords = ["DROP", "DELETE", "UPDATE", "ALTER", "TRUNCATE", "INSERT"];

    for (const keyword of dangerousKeywords) {
        if (query.toUpperCase().includes(keyword)) {
            return keyword;
        }
    }

    return null;
}

function executeQuery(inputQuery) {
    try {
        // Check if the input query is empty
        if (inputQuery.trim() === "") {
            // Display an alert if the query is empty
            setTimeout(function () {
                showErrorModal("Empty query!")
            }, 500);
        } else {
            // Check for dangerous keywords in the input query
            const dangerousKeyword = findDangerousKeyword(inputQuery);

            // If a dangerous keyword is found, show an error message
            if (dangerousKeyword !== null) {
                showError(`Query contains dangerous keyword: ${dangerousKeyword}`);
                return;
            }

            // Prepare and bind the input query
            const stmt = db.prepare(inputQuery);
            stmt.getAsObject({ $start: 1, $end: 1 });
            stmt.bind({ $start: 1, $end: 2 });

            const data = [];

            // Execute the query and fetch results
            while (stmt.step()) {
                const row = stmt.getAsObject();
                data.push(row);
            }

            // Display the query results in the HTML content
            const bodyContent = document.getElementById("content");
            bodyContent.innerHTML = JSON.stringify(data, null, 2);
            hljs.highlightAll();
            document.getElementById("preContent").style.display = "block";
        }
    } catch (error) {
        // Handle any errors that occur during query execution
        console.error("Query error:", error);
        showErrorModal("Query error: " + error.message);
    }
}


function showErrorModal(message) {
    const errorModal = document.getElementById("errorModal");
    const errorMessage = document.getElementById("errorMessage");

    errorMessage.textContent = message;
    errorModal.style.display = "block";
}

function closeErrorModal() {
    const errorModal = document.getElementById("errorModal");
    errorModal.style.display = "none";
}
