const MongoClient = require(['mongodb']).MongoClient;

const url = "mongodb://localhost/27017";
MongoClient.connect(url, { useNewUrlParser: true }).then((conn) => {
const test = conn.db("pingdb").collection("ping");
// 增加
test.then((res) => {
// 查询
var db3 = test.find().toArray().then((arr) => {});});});