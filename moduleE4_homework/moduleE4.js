// Задание 1

// function showKeyValue(obj) {
//     for ( let key in obj) {
//         if (obj.hasOwnProperty(key)) {
//             console.log(`${key}: ${obj[key]}`)
//         }
//     }
// }
//
// const user = {
//     city: 'Novokuznetsk'
// }
//
// const userDima = Object.create(user)
//
// userDima.name = 'Dima'
// userDima.age = 28
//
// showKeyValue(userDima)

// Задание 2

// const isKey = (string, obj) => string in obj
//
// console.log(isKey('name', userDima))

// Здание 3

// const createObj = () => Object.create(null)
//
// console.log(createObj())

// Задание 4

// function ElectricDevice () {
//     this.feeds = 'power grid'
//     this.isTurnOn = false
// }
//
// ElectricDevice.prototype.turnOn = function () {
//     this.isTurnOn = true
// }
//
// ElectricDevice.prototype.turnOff = function () {
//     this.isTurnOn = false
// }
//
// function LightingDevice (name, wattage) {
//     this.name = name;
//     this.wattage = wattage;
// }
//
// LightingDevice.prototype = new ElectricDevice();
//
// LightingDevice.prototype.powerConsumption = function (time) {
//     return this.wattage * time
// }
//
// function SmartPhone (model, os, version, batteryMax, batteryNow, chargingSpeedPerMinute) {
//     this.model = model;
//     this.os = os;
//     this.version = version;
//     this.batteryMax = batteryMax;
//     this.batteryNow = batteryNow;
//     this.chargingSpeedPerMinute = chargingSpeedPerMinute;
// }
//
// SmartPhone.prototype = new ElectricDevice();
//
// SmartPhone.prototype.updateVersion = function (newVersion) {
//     this.version = newVersion;
// }
//
// SmartPhone.prototype.charge = function (timeCharge) {
//     if (this.isTurnOn) {
//         this.batteryNow += this.chargingSpeedPerMinute * timeCharge
//         this.turnOff()
//     } else {
//         console.log('Подключите смартфон к сети')
//     }
// }
//
// SmartPhone.prototype.getBattery = function () {
//     return `Заряд аккумулятора составляет ${this.batteryNow / this.batteryMax * 100} %`
// }
//
// const tableLamp = new LightingDevice('Настольная лампа', 8);
//
// console.log(tableLamp)
// console.log(tableLamp.powerConsumption(2))
//
// const realmeXT = new SmartPhone('RMX1921', 'Android', '11',
//     4000, 1000, 50);
//
// console.log(realmeXT)
// console.log(realmeXT.getBattery())
// realmeXT.turnOn()
// console.log(realmeXT.isTurnOn)
// realmeXT.charge(15)
// console.log(realmeXT.getBattery())
// console.log(realmeXT.isTurnOn)
// realmeXT.updateVersion(12)
// console.log(realmeXT)

// Задание 5

class ElectricDevice {
    constructor() {
        this.feeds = 'power grid'
        this.isTurnOn = false
    }

    turnOn() {
        this.isTurnOn = true
    }

    turnOff() {
        this.isTurnOn = false
    }
}

class LightingDevice extends ElectricDevice{
    constructor(name, wattage) {
        super(ElectricDevice);
        this.name = name;
        this.wattage = wattage;
    }
    powerConsumption(time) {
        return this.wattage * time
    }
}

class SmartPhone extends ElectricDevice{
    constructor(model, os, version, batteryMax, batteryNow, chargingSpeedPerMinute) {
        super(ElectricDevice);
        this.model = model;
        this.os = os;
        this.version = version;
        this.batteryMax = batteryMax;
        this.batteryNow = batteryNow;
        this.chargingSpeedPerMinute = chargingSpeedPerMinute;
    }

    updateVersion(newVersion) {
        this.version = newVersion;
    }

    charge(timeCharge) {
        if (this.isTurnOn) {
            this.batteryNow += this.chargingSpeedPerMinute * timeCharge
            this.turnOff()
        } else {
            console.log('Подключите смартфон к сети')
        }
    }

    getBattery() {
        return `Заряд аккумулятора составляет ${this.batteryNow / this.batteryMax * 100} %`
    }
}

const tableLamp = new LightingDevice('Настольная лампа', 8);

console.log(tableLamp)
console.log(tableLamp.powerConsumption(2))

const realmeXT = new SmartPhone('RMX1921', 'Android', '11',
    4000, 1000, 50);

console.log(realmeXT)
console.log(realmeXT.getBattery())
realmeXT.turnOn()
console.log(realmeXT.isTurnOn)
realmeXT.charge(15)
console.log(realmeXT.getBattery())
console.log(realmeXT.isTurnOn)
realmeXT.updateVersion(12)
console.log(realmeXT)


