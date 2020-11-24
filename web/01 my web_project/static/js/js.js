$(function () {
    setTimeout(se(), 1000);
    //-----------------------------------------------------
    function se(){
        const MongoClient = require(['mongodb']).MongoClient;
        const url = "mongodb://localhost/27017";
        MongoClient.connect(url, { useNewUrlParser: true }).then((conn) => {
            const test = conn.db("pingdb").collection("ping");
            // 增加
            test.then((res) => {
                // 查询
                var db1 = test.find().toArray().then((arr) => {});});});
        //-----------------------------------------------------
        if (db1 === imports.db3){
            setInterval(function () {
            $("#autore").load(location.href + " #autore");//注意后面DIV的ID前面的空格，很重要！没有空格的话，会出双眼皮！（也可以使用类名）
        }, 1500);//8秒自动刷新
            $("#block").empty();
        var txt;
            var name="name";
            txt = ''
            for (var key in arr) {
				txt = txt+'<p style="font-size: 7px;display: inline;word-break: normal;font-weight: bold">' + key + '</p>' +
                    '<p style="font-size: 7px;display: inline;word-break: normal">' + db1[key] + '</p>'
			}
            var reg = new RegExp('"',"g");
            txt = txt.replace(reg, "");
        $("#block").append(txt);
        //------------------------------------------------------
        $("#bloc").empty();
        var txt;
            var name="name";
            txt = ''
            var reg = new RegExp('"',"g");
            txt = txt.replace(reg, "");
        $("#bloc").append(txt);
    }

        else {
            var db3 = db1
            $("#block").empty();
        var txt;
            var name="name";
            txt = ''
            for (var key in arr) {
				txt = txt+'<p style="font-size: 7px;display: inline;word-break: normal;font-weight: bold">' + key + '</p>' +
                    '<p style="font-size: 7px;display: inline;word-break: normal">' + db1[key] + '</p>'
			}
            var reg = new RegExp('"',"g");
            txt = txt.replace(reg, "");
        $("#block").append(txt);
        //------------------------------------------------------
        $("#bloc").empty();
        var txt;
            var name="name";
            txt = ''
            var reg = new RegExp('"',"g");
            txt = txt.replace(reg, "");
        $("#bloc").append(txt);
        }}});