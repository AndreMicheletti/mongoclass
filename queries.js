
/* operators:

$ne - match se o valor do doc é diferente do passado

$in - match se o valor do doc aparece dentro da array
$nin - match se o valor do doc não aparece dentro da array

$gt - match se o valor for maior ao passado
$gte - match se o valor for maior ou igual ao passado
$lt - match se o valor for menor ao passado
$lte - match se o valor for menor ou igual ao passado

$exists - match se a field existe/ñ existe no documento
(existir é diferente de ter o valor nulo)


 */

// QUERY POR ID

db.timelog.find("5e60fbd330476ecc3faddfb3")
db.timelog.find(ObjectId("5e60fbd330476ecc3faddfb3"))


// QUERY COM OPERATORS

db.timelog.find({
    "employee": {
        "$in": [
            ObjectId("5e60fbd330476ecc3faddfb2"),
            ObjectId("5e60fbd330476ecc3faddfb2")
        ]
    },
    "kind": "entrada",
    "time": {
        "$gte": ISODate("2019-01-01"),
        "$lte": ISODate("2019-02-01")
    }
})

// timelogs entre os dias 22 e 25 de janeiro de 2020

// employees com routine 12x36 ou 5x2

// employees demitidos com initial day 1



// QUERY COM PROJECTION

/*
    dica monstra:

  uma query é mt mais rapida se o projection é exatamente igual a um indice
  que o collection tem

  por exemplo, se existir um indice na collection timelog q é exatamente

  { time: 1, employee: 1 }

  ele vai ser monstruosamente rapido
 */


db.timelog.find({
    "employee": ObjectId("5e60fbd330476ecc3faddfb2"),
    "kind": "entrada"
}, { time: 1, employee: 1 })


// QUERY COM SORT

// 1 = ascending
// 2 = descending

db.timelog.find({
    "employee": ObjectId("5e60fbd330476ecc3faddfb2"),
    "kind": "entrada"
}).sort({ time: 1 })



// QUERY COM LIMIT

db.timelog.find({
    "employee": ObjectId("5e60fbd330476ecc3faddfb2"),
    "kind": "entrada"
}).limit(1)

// fazer query de timelog com tipo entrada, no maximo 10 e ordenados por time descendente



// QUERY OPERATOR $or

db.employee.find({
    "routine": "5x2",
    "$or": [
        {"initial_day": 1},
        {"name": "funcionario 0"}
    ]
})