let locationData;

function getLocations() {
    url = "http://localhost:2224/database/getAllLocations";

    fetch(url)
        .then((response) => response.json())
        .then((data) => {
            updateStates(data.body);
            locationData = data.body;
        })
        .catch((err) => console.log(err));
}

getLocations();

function updateStates(states) {
    for (let i = 0; i < states.length; i++) {
        stateLocation.innerHTML += `<option value="${i}">${states[i][1]}</option>`;
    }
}

// Event listener for the state dropdown of the city field
const stateDropdown = document.getElementById("stateLocation");
stateDropdown.addEventListener("change", () => {
    let cityLocation = document.getElementById("cityLocation");
    let cityDiv = document.getElementById("cityDiv");
    let locationButton = document.getElementById("locationButton");

    while (cityLocation.firstChild) {
        cityLocation.removeChild(cityLocation.firstChild);
    }

    if (stateDropdown.value == "") {
        cityDiv.hidden = true;
        locationButton.disabled = true;
    } else {
        let selectedState = JSON.parse(locationData[stateDropdown.value][2]);
        cityDiv.hidden = false;
        locationButton.hidden = false;
        for (let i = 0; i < selectedState.length; i++) {
            let newOption = document.createElement("option");
            newOption.textContent = selectedState[i];
            cityLocation.appendChild(newOption);
        }
    }
});

const locationButton = document.getElementById("locationButton");
locationButton.addEventListener("click", () => {
    event.preventDefault();
    let cityLocation = document.getElementById("cityLocation").value;
    let stateLocation = document.getElementById("stateLocation").value;
    let location = cityLocation + ", " + locationData[stateLocation][1];
    orderMenu();
});

function orderMenu() {
    window.location.href = "order";
}
