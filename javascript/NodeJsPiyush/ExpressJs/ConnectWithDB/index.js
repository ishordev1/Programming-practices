const express = require("express")
const mongoose = require('mongoose')
const app = express();


//Connection
mongoose.connect('mongodb://127.0.0.1:27017/crudUser').then(()=>{
    console.log("connected");
    
}).catch((e)=>{
    console.log("error Occor:",e);
    
})

//schema create
const userSchema = new mongoose.Schema({
    firstName: {
        type: String,
        required: true,
    },
    lastName: {
        type: String
    },
    email: {
        type: String,
        required: true,
        unique: true
    },
    gender:{
        type:String,
    }

})

//create modal using schema
const User=mongoose.model("user",userSchema);






app.listen(3000, () => console.log(`Server started port: 3000`));
