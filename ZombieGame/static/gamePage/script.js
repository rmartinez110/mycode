let playerInfo = {
    playerName: "Zombie Hunter",
    playerHealth: 100,
    playerLocation: "hall",
    playerInventory: {
        axe: { damage: 50, durability: 2 },
        hammer: { damage: 50, durability: 2 },
    },
    buildingLevel: 1,
};

let roomCoordinates;
let buildingRoom;
let weapons;

getGameData(1);
addPlayerInventoryButtons();
updatePlayerInfo();

// api call that gets the building layout and assigns it to the buildingRooms variable
async function getGameData(id) {
    url = "http://localhost:2224/game/map/1";
    await fetch(url)
        .then((response) => response.json())
        .then((data) => {
            parsedBuildingLayout = JSON.parse(data["body"][0]);
            buildingRoom = parsedBuildingLayout;
            parsedBuildingCoordinates = JSON.parse(data["body"][1]);
            roomCoordinates = parsedBuildingCoordinates;
            parsedWeapons = JSON.parse(data["body"][2]);
            weapons = parsedWeapons;
            deployWeapon();
        })
        .catch((error) => {
            console.error(error);
        });
}

// Get a reference to the result element
const resultElement = document.getElementById("result");

// Add a click event listener to the document
document.addEventListener("click", function (event) {
    // Get the mouse click coordinates
    const x = event.clientX - 10;
    const y = event.clientY - 10;

    // Display the coordinates in the result element
    resultElement.innerHTML = `Mouse clicked at X: ${x}, Y: ${y}`;

    if (x <= 600 && x >= 18 && y >= 65 && y <= 541) {
        moveDot(x, y);
    }
});

// Get the location of the mouse click
function getLocation(x, y) {
    for (let room in roomCoordinates[playerInfo["buildingLevel"]]) {
        if (
            x >=
                roomCoordinates[playerInfo["buildingLevel"]][room]["x"][
                    "min"
                ] &&
            x <= roomCoordinates[playerInfo["buildingLevel"]][room]["x"]["max"]
        ) {
            if (
                y >=
                    roomCoordinates[playerInfo["buildingLevel"]][room]["y"][
                        "min"
                    ] &&
                y <=
                    roomCoordinates[playerInfo["buildingLevel"]][room]["y"][
                        "max"
                    ]
            ) {
                return room;
            }
        }
    }
}
// Get a reference to the map element
function changeMap() {
    map = document.getElementById("gameMap");

    if (
        map.src === "http://localhost:2224/static/maps/floor1map.png" ||
        map.src === "/static/maps/floor1map.png"
    ) {
        map.src = "http://localhost:2224/static/maps/floor2map.png";
    } else {
        map.src = "http://localhost:2224/static/maps/floor1map.png";
    }
}

// Move the dot to the mouse click coordinates
function moveDot(newX, newY) {
    const dot = document.getElementById("dot");

    // new screen point
    const maxX = window.innerWidth - 20; // 20 is the dot's width
    const maxY = window.innerHeight - 20; // 20 is the dot's height

    // get the selected room by checking the coordinates
    selectedRoom = getLocation(newX, newY);

    // if the selected room is one of the traverable rooms for the players current room
    if (
        buildingRoom[playerInfo["buildingLevel"]][playerInfo["playerLocation"]][
            "traversable"
        ].includes(selectedRoom)
    ) {
        // if the selected room is stairs, change the map
        if (selectedRoom == "stairs") {
            // Set the dot's new position
            dot.style.left = newX + "px";
            dot.style.top = newY + "px";
            changeMap();
            if (playerInfo["playerLocation"] === "hall") {
                playerInfo["playerLocation"] = "gameroom";
                playerInfo["buildingLevel"] = 2;
                setTimeout(() => {
                    // Set the dot's new position
                    dot.style.left = 501 + "px";
                    dot.style.top = 138 + "px";
                }, "500");
            } else if (playerInfo["playerLocation"] === "gameroom") {
                playerInfo["playerLocation"] = "hall";
                playerInfo["buildingLevel"] = 1;
                setTimeout(() => {
                    // Set the dot's new position
                    dot.style.left = 295 + "px";
                    dot.style.top = 145 + "px";
                }, "500");
            }
        } else {
            playerInfo["playerLocation"] = selectedRoom;
            // Set the dot's new position
            dot.style.left = newX + "px";
            dot.style.top = newY + "px";
        }

        updatePlayerInfo();
        updateRoomInfo();
    }
}

function updatePlayerInfo() {
    document.getElementById("playerNameField").textContent =
        playerInfo["playerName"];
    document.getElementById("playerHealthField").textContent =
        playerInfo["playerHealth"];
    document.getElementById("playerLocationField").textContent =
        playerInfo["playerLocation"];
}

function updateRoomInfo() {
    document.getElementById("roomOccupants").textContent =
        buildingRoom[playerInfo["buildingLevel"]][playerInfo["playerLocation"]][
            "occupants"
        ];
    document.getElementById("roomInventory").textContent =
        buildingRoom[playerInfo["buildingLevel"]][playerInfo["playerLocation"]][
            "inventory"
        ];
    document.getElementById("roomTraversable").textContent =
        buildingRoom[playerInfo["buildingLevel"]][playerInfo["playerLocation"]][
            "traversable"
        ];
}

function loadPlayer() {
    // make a api call to get the player information
    // update the playerInfo
    // update the playerInfo in the game stats
}

function getRandomWeapon() {
    // make a api call to get a random weapon
}

function deployRandomZombie() {
    const zombieDeployer = new Worker("zombieWorker.js");
}

function addPlayerInventoryButtons() {
    let playerInventory = document.getElementById("playerInventory");
    for (let weapon in playerInfo["playerInventory"]) {
        let newInventoryButton = document.createElement("button");
        newInventoryButton.classList.add(
            "btn",
            "btn-primary",
            "inventoryButton"
        );
        newInventoryButton.style = "margin-left: 5px;";
        newInventoryButton.textContent = weapon;
        playerInventory.appendChild(newInventoryButton);
    }
}
function deployWeapon() {
    console.log(buildingRoom);
    console.log(
        buildingRoom[playerInfo["buildingLevel"]][playerInfo["playerLocation"]][
            "inventory"
        ]
    );
    buildingRoom[playerInfo["buildingLevel"]][playerInfo["playerLocation"]][
        "inventory"
    ] = {
        axe: { damage: 50, durability: 2 },
        hammer: { damage: 50, durability: 2 },
    };
    console.log(
        buildingRoom[playerInfo["buildingLevel"]][playerInfo["playerLocation"]][
            "inventory"
        ]
    );
}
