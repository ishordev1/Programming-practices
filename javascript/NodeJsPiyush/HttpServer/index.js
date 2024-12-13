const http = require("http");
const fs = require("fs")

/*
//-> Also create like this
//-> Express js write handler function manually.
function handler(req,res){
}
const myServer=http.createServer(handler);
*/


// const myServer = http.createServer((req, res) => {
//     //one time get request then in your log file it appere in two times besause browser call one extra to the fav icon so that.
//     if (req.url === '/favicon.ico') return res.end
//     const log = `${Date.now()}: ${req.url} new Request\n`
//     fs.appendFile("log.txt", log, (error, success) => {
//         res.end("new Request")
//     })
//     switch (req.url) {
//         case '/':
//             res.end("this is home page");
//             break;
//         case "/about": res.end("Jhon this side.");
//             break;
//         case "/signup":
//             if (req.method === "POST") {
//                 //MANUALLY handle post and get request, it is pain full so the express come.
//                 res.end("this is signup page.")
//             }
//             break;
//         default: res.end("404")
//             break;
//     }
//     // res.end("hello jhon")
// });

// myServer.listen(5000, () => {
//     console.log("server started..");

// })


/*
conclusion
first required http
to help of http, create server and pass callback function, function take 2argument request and response
listen the server port or allow the port.
*/





// -----------------------------Express solve problem--------
//--------------------------- install express: npm install express
const express = require("express")
const app = express();

app.get("/home", (req, res) => {
    return res.end("this is express home page.")
})
const myServer1 = http.createServer(app);
myServer1.listen(5000, () => {
    console.log("express server started..");
})


//-------------------------------------OR---------Direct----------------------

// const express = require("express")
// const app = express();
// app.get("/home", (req, res) => {
//     return req.end("this is express home page.")
// })
// app.listen(8000, () => console.log("server started...."));











