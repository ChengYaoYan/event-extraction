var express = require('express');
var router = express.Router();

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

router.get('/:event', function(req, res, next) {
    res.setHeader("Access-Control-Allow-Origin", "http://127.0.0.1:5500");

    const eventName = req.params.event;

    connectToDb()
        .then(() => {
            console.log("successfully connected to the server");
            const db = client.db("eventExtraction");
            return db;
        })
        .then((db) => {
            const collection = db.collection("events");
            return collection;
        })
        .then((collection) => {
            const docs = collection.find({ $or: [ { reason: eventName }, { result: eventName } ] }, { _id: 0 }).toArray();
            return docs;
        })
        .then((docs) => {
            docs.map((doc) => {
                delete doc._id;
                return doc;
            })
            res.json({ data: docs });
        });
})

module.exports = router;
