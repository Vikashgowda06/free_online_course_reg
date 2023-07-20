document.addEventListener("DOMContentLoaded", function() {
            var paymentTypeSelect = document.getElementById("payment-type");
            var cardDetails = document.querySelectorAll(".card-details");
            var upiDetails = document.querySelector(".upi-details");

            paymentTypeSelect.addEventListener("change", function() {
                        if (paymentTypeSelect.value === "card") {
                            cardDetails.forEach(function(element) {
                                element.classList.remove("input-hidden");
                            });
                            upiDetails.classList.add("input-hidden");
                        } else {
                            cardDetails.forEach(function(element) {
                                        element.classList.add("input-hidden");