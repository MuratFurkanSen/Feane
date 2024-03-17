const search = document.querySelector(".search-wrapper");
const input = search.querySelector("input");

search.addEventListener("mouseenter", () => {
    if (!input.matches(":focus")) {
        search.classList.add("search-active");
    }
});

search.addEventListener("mouseleave", () => {
    if (!input.matches(":focus") && !input.value.trim()) {
        search.classList.remove("search-active");
    }
});

search.addEventListener("mouseleave", () => {
    search.classList.remove("search-active");

});