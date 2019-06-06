
var mongodb = require("mongodb");

var client = mongodb.MongoClient;



///////////////////////////////////////////////////////////

// var MongoClient = require('mongodb').MongoClient;


///////////////////////////////////////////////////////////


var url = "mongodb://localhost:27017/";

client.connect(url, { useNewUrlParser: true },  function (err, client)  {
    
    var db = client.db("ProyectoBD");
    var collection = db.collection("clientes");
    
    var query = {primer_nombre:/^T/};
    
    var cursor = collection.find(query);
    
    cursor.forEach(
        function(doc) {
            console.log(doc.primer_nombre);
        }, 
        function(err) {
            client.close();
        }
    );
    
});



///////////////////////////////////////////////////////////



// MongoClient.connect(url, function(err, db) {
//   if (err) throw err;
//   var dbo = db.db("ProyectoBD");
//   dbo.collection("clientes").findOne({}, function(err, result) {
//     if (err) throw err;
//     console.log(result.primer_nombre);
//     db.close();
//   });
// });

