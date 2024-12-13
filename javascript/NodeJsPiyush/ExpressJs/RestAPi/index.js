const express = require("express");
const users = require("./data.json");
const { json } = require("body-parser");
const fs = require("fs");
const status = require("statuses");
const app = express();
//send Html Data
app.get("/users", (req, res) => {
    const html =
        `<ul>
    ${users.map(user => `<li>${user.first_name}</li>`).join("")}
    </ul>`;
    res.send(html);

})

//Send Json Data
//getData
app.get("/api/user", (req, res) => {
    return res.json(users);
})

//Get user by Id
app.get("/api/users/:userId", (req, res) => {
    const id = Number(req.params.userId);
    const user = users.find(user => user.id === id);
    return res.json(user);
})



//express not know which types of data come from client so that use middle ware
app.use(express.urlencoded({ extended: false }));

//after allow then only work post,patch,delete
//update delete create also merge these there with once app. -----------also allow make one by one method.
app
    .route("/api/user/:id")
    .patch((req, res) => {
        //update
        return res.json({ status: "pending" });
    })
    .delete((req, res) => {
        //delete 
        return res.json({ status: "pending" })
        
    })



app.post("/api/user",(req, res)=> {
    //create
    const body = req.body;
    console.log(body);
    
    users.push({ ...body, id: users.length + 1 });
    fs.writeFile("./data.json", JSON.stringify(users), (error, data) => {
        return res.status(200).json({ status: "success", id: [users.length] })
    })
})





app.listen(3000, () => { console.log("Server is running on port 3000"); })