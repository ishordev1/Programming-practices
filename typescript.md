## Setup  typescript
install node js
run command in terminal: npm install -g typescript
check version: tsc -v


# how to run code
tsc filename.extension
run that generated js file: node filename.js


# Setup when save ts file it give output in browser
1. compile the ts code
2. create one html page
3. link that compiled js in that html code with script tag
4. Run with live server
5. now it will show output in browser console direct when compile ts file
6. tsc filename.ts --watch <-- It auto compile ts file when save

now when save ts file, it auto-compiles that ts file and that js is linked with html and html is running live server, it give output

# typeof
`
if (typeof value == "string") {
console.log(value.toUpperCase);
} else {
console.log(value.toFixed(2));
});
`

# Null Undefine Any
## null value   <-- obsese of value
eg:  let userName=null
log(typeof userName);
log(userName)

## undefine <-- when a variable is initialized, but not value given or not variable
eg: let userName;
log(userName)

# null and undefine is falsey value
it alway trigger false statement
if(username) log("true)
else log("false")

output: false


## any <--- any value 
let product:any={
productName:"book"
price:324,
}
log(product.productName)
log(product.isActive)




# Array
let arrayName: type[];
eg: let mynumber:number[]=[2,4,6,7,3,6,7]
let friendsName:string[]=["kumar","ram","shyam"]
mynumber.push(5)
friendsName.push("lala")

number.forEach(val)=>{
log(val)
}


let uppercaseName = friendsName.map((name)=>{
log(name);
return name.toUpperCase();
});
log(uppercaseName)


let uppercaseName = friendsName.map((name,index)=>{
log(index , name);
return name.toUpperCase();
});
log(uppercaseName)

# Object
//only store can't access
let student:object={
name:'ram',
address:'india',
}
 log(student)
 log(student.name) // error

 let student:
 {
name:string;
address:string;
}={
name:'ram',
address:'india',
}
log(student)
 log(student.name) 



# function
function funName(variable:datatype):returnType{
//statement
}

ex:
function test(name:String,age:number):number{
return age;
}




















# Union

let mixed: (string | number) [ ] ;
mixed = ["one", "two", "three", 23, 35];
mixed.forEach((value) => {
if (typeof value == "string") {
console.log(value.toUpperCase);
} else {
console.log(value.toFixed(2));
});
console.log(mixed);


// store user id
let userId: string | number = "q5fsdgfafaf";
userId = 23523562;
userId = "sdgsagsagsgas";
userId = 2352521356;
display user id and return
function displayUserId(userId: string | number): string |
console.log("user id is " + userId);
if (typeof userId === "string") {
console.log(userId.toUpperCase);
}
return userId;
}
displayUserId(userId);




