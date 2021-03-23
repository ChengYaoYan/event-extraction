import renderGraph from "./renderGraph.js";

const searchBtn = document.getElementById("search-btn");

const handleSearchEvent = () => {
    const inputBox = document.getElementById("input-box");
    const event = inputBox.value;
    
    fetch(`http://localhost:3000/search/${event}`)
        .then(response => response.json())
        .then(data => {
            let reasons = data.data.filter(item => item.result == event)
                                    .map(item => item.reason);
            let results = data.data.filter(item => item.reason == event)
                                    .map(item => item.result);

            let payload = {
                event,
                reasons,
                results,
            }
            renderGraph(payload);
        });
};

searchBtn.addEventListener("click", handleSearchEvent);
