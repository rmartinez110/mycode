getOrders();

function getOrders() {
    url = "http://localhost:2224/database/getAllOrders";

    fetch(url)
        .then((response) => response.json())
        .then((data) => {
            createTableRows(data["body"]);
        })
        .catch((error) => console.log(error));
}

function createTableRows(data) {
    triggerSource = window.location.href;

    let tableBody = document.getElementById("confirmationTableBody");
    for (let i = 0; i < data.length; i++) {
        let tableRow = document.createElement("tr");
        tableRow.classList.add("tableRow");

        let rowOrderNumber = document.createElement("th");
        rowOrderNumber.textContent = data[i][0];

        let pizzaSize = document.createElement("td");
        pizzaSize.textContent = data[i][1];

        let pizzaCrust = document.createElement("td");
        pizzaCrust.textContent = data[i][2];

        let pizzaSauce = document.createElement("td");
        pizzaSauce.textContent = data[i][3];

        let pizzaToppings = document.createElement("td");
        pizzaToppings.textContent = JSON.parse(data[i][4]);

        tableRow.appendChild(rowOrderNumber);
        tableRow.appendChild(pizzaSize);
        tableRow.appendChild(pizzaCrust);
        tableRow.appendChild(pizzaSauce);
        tableRow.appendChild(pizzaToppings);

        if (triggerSource === "http://localhost:2224/") {
            let orderLink = document.createElement("td");
            let orderLinkButton = document.createElement("button");
            orderLinkButton.classList.add("btn");
            orderLinkButton.classList.add("btn-primary");
            orderLinkButton.textContent = "Reorder";
            orderLinkButton.value = data[i][0];
            orderLinkButton.onclick = function () {
                reorder(orderLinkButton.value);
            };
            orderLinkButton.style.paddingTop = "0px";
            orderLinkButton.style.paddingBottom = "0px";
            orderLink.appendChild(orderLinkButton);
            tableRow.appendChild(orderLink);
        }

        tableBody.appendChild(tableRow);
    }
}

function returnToMain() {
    window.location.href = "/";
}

function reorder(orderNumber) {
    url = "http://localhost:2224/database/getorder/" + orderNumber;

    fetch(url)
        .then((response) => response.json())
        .then((data) => {
            if (data["status"] === 200) {
                window.location.href = "confirmation";
            } else {
                window.location.href = "error";
            }
        })
        .catch((error) => console.log(error));
}
