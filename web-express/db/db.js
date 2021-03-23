const { MongoClient } = require("mongodb");

const url = "mongodb://localhost:27017?useUnifiedTopology=true";
const dbName = "eventExtraction";
const collectionName = "events";
const client = new MongoClient(url);

function connectToDb() {
    return new Promise((resolve, reject) => {
        client.connect(() => {
            resolve();
        });
    });
};

module.exports = connectToDb;