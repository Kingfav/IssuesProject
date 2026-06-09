const API = "/api/v1/issues";

function openModal() {
    document.getElementById("modal").style.display = "block";
}

function closeModal() {
    document.getElementById("modal").style.display = "none";
}

async function loadIssues() {
    const res = await fetch(API);
    const data = await res.json();

    document.getElementById("total").innerText = data.length;
    document.getElementById("open").innerText = data.filter(i => i.status === "open").length;
    document.getElementById("closed").innerText = data.filter(i => i.status === "closed").length;

    const container = document.getElementById("issues");
    container.innerHTML = "";

    data.forEach(issue => {
        container.innerHTML += `
            <div class="issue">
                <h3>${issue.title}</h3>
                <p>${issue.description}</p>
                <small>${issue.priority} | ${issue.status}</small>
                <br><br>
                <button onclick="deleteIssue('${issue.id}')">Delete</button>
            </div>
        `;
    });
}

async function createIssue() {
    const title = document.getElementById("title").value;
    const description = document.getElementById("description").value;
    const priority = document.getElementById("priority").value;

    await fetch(API, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title, description, priority })
    });

    closeModal();
    loadIssues();
}

async function deleteIssue(id) {
    await fetch(`${API}/${id}`, { method: "DELETE" });
    loadIssues();
}

loadIssues();