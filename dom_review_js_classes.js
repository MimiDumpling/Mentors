class Being {
	isWarmBlooded() {
		return false
	}

	isAlive() {
		return true
	}
}

class Mammal extends Being {
	isWarmBlooded() {
		return true
	}
}

class Cat extends Mammal {
	constructor({name}) {
		super()
		this.name = name
	}

	meow() {
		console.log("Meow")
		console.log(`My name is ${this.name}`)
	}
}

const pan = new Cat({name:"Pancake"})
pan.meow()
console.log(pan.isWarmBlooded())
const maple = new Cat({name:"Maple"})
maple.meow()
maple.isWarmBlooded()

class Kat {}
const badKitty = new Kat('PanMaple', 1233, true, null, false, 1351135, 'test')
const badKitty2 = new Kat({
	name: 'PanMaple',
	age: 1233,
	isOld: true,
	isCute: false,
	height: 1351135,
	thing: 'test'
})


