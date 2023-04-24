/*
const a = 10
if(true){
    b = 20
    console.log(a)

}

if(true){
    console.log(b)
}
*/

// const myFunction = function(x){
//     function add(y){
//         console.log(x + y)
//     }
//     return add
// }

// let func = myFunction(10)
// func(20)
// func(30)

// func = myFunction(20)
// func(40)

// function myFunction(x, y){
//     console.log(x+y)
//     console.log(arguments)
// }

// myFunction(10,20)
// myFunction(10,20,30,40)
// myFunction(10)
const arr = [1, 2, 3, 4]
for (let i = 0; i < arr.length; i++){
    arr[i] = arr[i] ** 3
  }
  
  console.log(arr)