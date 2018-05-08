// Domain Models

class User {
  constructor(name, age, email) {
    this.name = name;
    this.age = age;
    this.email = email;
    this.steps = 0;
    this.geoLocator = new GeoLocator();
    this.start = this.geoLocator.getPosition();
    this.distanceMoved = {longitude:0, latitude:0}
  }

  getInfo() {
    return {name: this.name, age: this.age, email: this.email}
  }

  step() {
    this.steps++
  }

  // startStepping() {
  //     const start = this.geoLocator.getPosition()
  // }

  stopStepping() {
    const startLongitude = this.start.longitude;
    const startLatitude = this.start.latitude;
    const stop = this.geoLocator.getPosition();
    const stopLongitude = stop.longitude;
    const stopLatitude = stop.latitude;
    const result = {
      longitude: stopLongitude - startLongitude, 
      latitude: stopLatitude - startLatitude
    }
    const resultLongitude = this.distanceMoved.longitude + result.longitude
    const resultLatitude = this.distanceMoved.latitude + result.latitude

    this.distanceMoved = {resultLongitude, resultLatitude}
  }
}

class GeoLocator {
  constructor() {
    this.location = {longitude: 0, latitude: 0}
  }
  
  // pretend it gets the user's current location
  getPosition() {
    return this.location
  }
}

// Programmatic Models

class Application {
  constructor() {
    this.user = undefined;
  }

  createAccount(name, age, email) {
    // statefulness
    this.user = new User(name, age, email);
  }

  getUserInfo() {
    return {name: this.user.name, age: this.user.age, email: this.user.email}
  }
}