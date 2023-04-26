const menus=['치킨', '피자']
const preCooking = function(item) {
    return new Promise((resolve, reject) => {
        console.log(`${item} 재료 준비`)
        setTimeout(() => {
            resolve()
        }, 1000)
    })
}

const realCooking = function(item) {
    return new Promise((resolve, reject) => {
        console.log(`${item} 요리중`)
        setTimeout(() => {
            resolve()
        },3000)
    })
}

const afterCooking = function(item) {
    return new Promise((resolve, reject) => {
        console.log(`${item} 요리 완료, 청소중`)
        setTimeout(() => {
            resolve()
        }, 2000)
    })
    
}

/*
const cooking = function(item, callback) {
    preCooking(item).then(() => {
        console.log(`${item} 재료 준비 완료`)
        realCooking(item).then(() => {
            console.log(`${item} 요리 완료`)
            afterCooking(item).then(() => {
                console.log(`${item} 청소 완료`)
                callback()
            })
        })
    }).catch((error) => {
        console.log(error)
    })
}
*/

//1. 앱으로 치킨 주문
const orderDelivery = function(item){
    if (menus.includes(item)){
        console.log(`${item} 주문 들어옴. 식당에게 전달`)
        order(item, function(){
            console.log(`${item} 배달 완료`)
        })
    }
    else{
        console.log('메뉴가 존재하지 않음')
    }

}


//2. 앱 -> 식당으로 전달
const order = function(item, callback){
    console.log(`${item} 식당에서 메뉴 전달받음`)
    cooking(item, function(){
        console.log(`조리완료 배달시작`)
    })
    callback()
}


// 요리하는 함수
const cooking = function(item, callback) {
    preCooking(item).then(() => {
        console.log(`${item} 재료 준비 완료`)
        realCooking(item)
    }).then(() => {
        console.log(`${item} 요리 완료`)
        afterCooking(item)
    }).then(() => {
        console.log(`${item} 청소 완료`)
        callback()
    }).catch((error) => {
        console.log(error)
    })
}

orderDelivery('치킨')
orderDelivery('피자')