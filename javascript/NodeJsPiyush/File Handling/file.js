const fs=require("fs");
fs.writeFileSync("./File Handling/test.txt","helllo")
// fs.writeFile("./test.txt","this is testing text",(error)=>{})


    //result return if error come then it throw error
// const result=fs.readFileSync("./File Handling/test.txt","utf-8")
// console.log(result);

//it assepect call back function to handle if error come
fs.readFile("./File Handling/test.txt","utf-8",(err,result)=>{
    if(err){
console.log(err);
    }
    else{
console.log(result);

    }
})

// fs.appendFileSync('./File Handling/test.txt',"this is added text.")


//copy all text from prev file and make file and put the data.
// fs.cpSync("./File Handling/test.txt","./File Handling/copy.txt")



//delete file
// fs.unlinkSync("./File Handling/copy.txt")

//get All details of files when it created
console.log(fs.statSync("./File Handling/copy.txt"))

//create folder
// fs.mkdirSync("new folder")

// create folder under folder
// fs.mkdirSync("folder/a/b",{recursive:true})



