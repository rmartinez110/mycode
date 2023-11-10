function moveDot() {
    const dot = document.getElementById("dot");

    // Generate random coordinates within the viewport
    const maxX = window.innerWidth - 20; // 20 is the dot's width
    const maxY = window.innerHeight - 20; // 20 is the dot's height
    const newX = Math.random() * maxX;
    const newY = Math.random() * maxY;

    // Set the dot's new position
    dot.style.left = newX + "px";
    dot.style.top = newY + "px";
}

// Get a reference to the result element
const resultElement = document.getElementById("result");

// Add a click event listener to the document
document.addEventListener("click", function (event) {
    // Get the mouse click coordinates
    const x = event.clientX;
    const y = event.clientY;

    // Display the coordinates in the result element
    resultElement.innerHTML = `Mouse clicked at X: ${x}, Y: ${y}`;
});
