document.addEventListener("DOMContentLoaded", () => {
    const addToCartButtons = document.querySelectorAll(".product button");

    const cartCountElement = document.getElementById("cart-count");
    let cartCount = 0;

    addToCartButtons.forEach(button => {
        button.addEventListener("click", () => {
            cartCount++;
            cartCountElement.textContent = cartCount;
        });
    });
});
