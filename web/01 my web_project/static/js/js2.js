const MongoClient = require("mongodb").MongoClient;
        const url = "mongodb://localhost/27017";
        MongoClient.connect(url, { useNewUrlParser: true }).then((conn) => {
            const test = conn.db("testdb").collection("test");
            // 增加
            test.insertOne({ "site": "runoob.com" }).then((res));});
//---------------------------------------------------------
const MongoClient = require("mongodb").MongoClient;
        const url = "mongodb://localhost/27017";
        MongoClient.connect(url, { useNewUrlParser: true }).then((conn) => {
            const test = conn.db("testdb").collection("test");
            // 增加
            test.then((res) => {
                // 查询
                return test.find().toArray().then((arr) => {
                    console.log(arr);});});});