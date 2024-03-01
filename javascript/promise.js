/*
Also use Async/Await but Promise is modern

promise has 3 part
1. then----------------------> is me return value milta hai
2. catch
3. finally
*/

//* Note:.......then and catch function leta hai parameter me

// ?????????????????????????       Note: Promise  <-it is keyword

//first promise created and execute
// const promiseOnce=new Promise (function (success,error){
//     setTimeout(function(){
//         console.log("asynsc task complete")
//         success()    //success is connect then function if not call success then then function not execute
//     },1000)
// })
//  promiseOnce.then(function(){
//     console.log("promise execute")
//  })


// -----------------2. Also creted like this second created------------------
// promise not need to store in other variable

// new Promise(function (resolve,reject){
//     setTimeout(function(){
//         console.log("successfuly execute")
//         resolve()
//     },1000)
// }).then(function(){
//     console.log("asyc 2 is resolved")
// })



// -----------------3. Also creted like this second created------------------
// const promiseThree=new Promise(function(resolve,reject){
//     setTimeout(function() {
//         resolve({name:"rajkumar",email:"raj@gmail.com"})
//     }, 1000);
// })
// promiseThree.then(function(user){
//     console.log(user)
// })

// -----------------4. Also creted like this second created------------------
// const promiseFour=new Promise(function(resolve,reject){
//     setTimeout(function() {
//         let error=true
//         if(!error){
//             resolve({name:"jhone",lastName:"kumar"})
//         }
//         else{
//             reject("ERROR is occor")
//         }
//     }, 1000);
// })
// promiseFour.then().catch()

//----------------------------------promise chaining or thanable ------------vvi concept----------------
//thanable means multiple then. first then value return karega o value dusra then me aaye ga.

// const promiseFour=new Promise(function(resolve,reject){
//     setTimeout(function() {
//         let error=true
//         if(!error){
//             resolve({name:"jhone",lastName:"kumar"})
//         }
//         else{
//             reject("ERROR is occor")
//         }
//     }, 1000);
// })
// promiseFour.then((user)=>{
//     console.log(user);
//     return user.name
// })
// //upar wala then return kar raha hai usko kaise le. iske liye dushra then laga lo usme o then ka return value mil jayega
// .then((username)=>{
// console.log(username);
// }).catch(function(error){
//     console.log(error);
// })


// const promiseFour=new Promise(function(resolve,reject){
//     setTimeout(function() {
//         let error=false
//         if(!error){
//             resolve({name:"jhone",lastName:"kumar"})
//         }
//         else{
//             reject("ERROR is occor")
//         }
//     }, 1000);
// })
// promiseFour
// .then((user)=>{
//     console.log(user);
//     return user.name
// })
// //upar wala then return kar raha hai usko kaise le. iske liye dushra then laga lo usme o then ka return value mil jayega
// .then((username)=>{
// console.log(username);
// }).catch(function(error){
//     console.log(error);
// }).finally(()=>{
//     console.log("Promise is executed  either is success or rejected but it executed")
// })


//***********/ Note: is function me aagar catch function nahi lagao ge aur error aagaya to exception aaye ga to error dega.


//5. -----------------------------Async and Await with Promise------------------------------
//Async and Await not directly handle the error

// const promiseFive =new Promise(function(resolve,reject){
//     setTimeout(function() {
//                 let error=true
//                 if(!error){
//                     resolve({name:"jhone",lastName:"kumar"})
//                 }
//                 else{
//                     reject("ERROR is occor")
//                 }
//             }, 1000);
// })

// //jaha jaha async function use karo uske andar await lagado
// async function consumePromiseFive (){
//     //jo vi promisefive se aaye ga o response me chalajaye ga. 
//     //*****************/ Note:....... promiseFive is object so dont need paranthisses in calling time
//     try{
//         const response=await promiseFive
//         //agar error aaye ga to try catch se handle karna padega kiuki async and await me direct error ko handle nahi karsakte
//         console.log(response);
//     }
//     catch(error){
//         console.log(error);
//     }
// }

// consumePromiseFive()





// 6 ------------------------fetch data with using async function---------------------------
// async function getAllUser(){
//     try{
//         // const response=await fetch("url to feach dummay data.  featch function to use to featch API")
//         const response=await fetch("https://jsonplaceholder.typicode.com/users")
//         const data=await response.json()// json me convert karne me time lagta hai to esi liye await lagana padta hai
//         console.log(data)
//     }
//     catch(error){
//         console.log(error);
//     }
// }
// getAllUser()

// 7.----------------------------featch data using then funtion and handle error and response time
//direct not need to rap in try catch block
    fetch("https://jsonplaceholder.typicode.com/users")
    .then((response)=>{
        return response.json()
    })
    .then((data)=>{
console.log(data);
    })
    .catch(()=>{
        console.log(error);
    })





    //our EBook project use like this 

    // export const loginUser=(loginDetail)=>{
    //     return myAxios
    //     .post('/auth/login',loginDetail)
    //     .then((response)=>response.data)
    // }

    // loginUser(loginDetails).then((jwtTokenData) => {
     
    // }).catch(error => {
    //     toast.error(error.response.data.message)
    //     console.log(error)
    //   })





