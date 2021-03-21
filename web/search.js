import renderGraph from "./renderGraph.js";

const searchBtn = document.getElementById("search-btn");

const handleSearchEvent = () => {
    const inputBox = document.getElementById("input-box");
    const event = inputBox.value;
    // api fetch event relative reasons and results
    const reasons = ["reason1", "reason2", "reason3"];
    const results = ["result1", "result2", "result3"];
    const payload = {
        event,
        reasons,
        results
    };
    renderGraph(payload);
};

searchBtn.addEventListener("click", handleSearchEvent);
