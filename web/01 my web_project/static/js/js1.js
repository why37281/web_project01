const MongoClient = require("mongodb").MongoClient;
        const url = "mongodb://localhost/";
        MongoClient.connect(url, { useNewUrlParser: true }).then((conn) => {
            const test = conn.db("testdb").collection("test");
            // 增加
            test.insertOne({"site": "runoob.com"}).then((res) => {
                // 查询
                return test.find().toArray().then((arr) => {
                    console.log(arr);
                });
            }).then(() => {
                // 更改
                return test.updateMany({"site": "runoob.com"},
                    {$set: {"site": "example.com"}});
            }).then((res) => {
                // 查询
                return test.find().toArray().then((arr) => {
                    console.log(arr);
                });
            }).then(() => {
                // 删除
                return test.deleteMany({"site": "example.com"});
            }).then((res) => {
                // 查询
                return test.find().toArray().then((arr) => {
                    console.log(arr);
                });
            });
        });
