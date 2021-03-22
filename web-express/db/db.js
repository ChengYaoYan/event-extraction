const { MongoClient } = require("mongodb");
const assert = require("assert");

const url = "mongodb://localhost:27017?useUnifiedTopology=true";

const dbName = "eventExtraction";
const client = new MongoClient(url);

const connectToDb = function() {
    client.connect(function(err) {
        assert.equal(null, err);
        console.log("Connected successfully to server");

        const db = client.db(dbName);

        findDocuments(db, function() {
            client.close();
        });
    });
};

const insertDocuments = function(db, callback) {
    const collection = db.collection("events");

    collection.insertMany([{ a: 1 }, { a: 2 }, { a: 3 }], function(err, result) {
        assert.equal(err, null);
        assert.equal(3, result.result.n);
        assert.equal(3, result.ops.length);
        console.log('Inserted 3 documents into the collection');
        callback(result);
    });
};

const findDocuments = function(db, callback) {
    const collection = db.collection("events");
    collection.find({}).toArray(function(err, docs) {
        assert.equal(err, null);
        console.log("Found the following records");
        console.log(docs);
        callback(docs)

    });
};

const updateDocument = function(db, callback) {
    const collection = db.collection("events");

    collection.updateOne({ a: 2 }, { $set: { b: 1 }}, function(err, result) {
        assert.equal(err, null);
        assert.equal(1, result.result.n);
        console.log('Updated the document with the field a equal to 2');
        callback(result);
    });
};

const removeDocument = function(db, callback) {
    const collection = db.collection("events");
    collection.deleteOne({ a: 2, b: 1 }, function(err, result) {
        assert.equal(err, null);
        assert.equal(1, result.result.n);
        console.log("Removed the document with the field a equal to 3");
        callback(result);
    });
};

module.exports = connectToDb;
