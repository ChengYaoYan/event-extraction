var express = require('express');
var router = express.Router();
var connectToDb = require('../db/db.js');

router.get('/:event', function(req, res, next) {
    connectToDb();
    res.send("data");
})

module.exports = router;
