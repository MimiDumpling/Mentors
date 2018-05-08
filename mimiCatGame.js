class User {
  constructor (catName) {
    this.catName = catName;
    this.score = 0;
  }

  updateScore () {

  }

  getCurrentScore () {

  }

  getHighScore () {

  }
}

class Scene {
  constructor (asciiImage, question) {
    this.asciiImage = asciiImage,
    this.question = question,
    this.answer = {}
  }

  mapAnswerToScene (answer, scene) {
    this.answers[answer] = scene,
  }
}

class Game {
  constructor () {
    this.user = undefined;
  }

  createAccount (catName) {
    this.user = new User(catName);
  }

  getUserInfo () {
    return {name: this.user.catName, score: this.score}
  }

  menuChoice () {
    
  }

  startGame () {

  }

  endGame () {

  }
}