const myPromise = new Promise((resolve, reject) => {
    console.log('Promise 생성했음')
    resolve('성공')
    reject('실패')
})


myPromise.then((result) => {
    console.log('then하면', result)
}).catch((error) => {
    console.log('catch하면', error)
})