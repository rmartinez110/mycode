async function submitOrder() {
    event.preventDefault();
    const form = document.getElementById("orderForm");
    const checkboxes = form.querySelectorAll('input[name="topping"]:checked');
    const selectedValues = Array.from(checkboxes).map(
        (checkbox) => checkbox.value
    );

    const crustType = document.getElementById("crustField").value;
    const pizzaSize = document.getElementById("sizeField").value;
    const sauceType = document.getElementById("sauceField").value;

    const dataField = {
        size: pizzaSize,
        crust: crustType,
        sauce: sauceType,
        toppings: selectedValues,
    };

    try {
        const response = await fetch("/placeorder", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(dataField),
        });
        const result = await response.json();
        console.log("Insert successful. Inserted:", result);
        if (result["status"] === 200) {
            window.location.href = "confirmation";
        } else {
            alert(result["message"]);
        }
    } catch (error) {
        console.error("Error:", error);
    }
}
