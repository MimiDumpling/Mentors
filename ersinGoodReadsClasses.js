// user uploads a short review of book

class User {
  constructor (name, email) {
    this.name = name;
    this.email = email;
    this.reviews = {}
  }

  getUserReviews() {
    return this.reviews
  }

  writeUserReviews(title, review) {
    newReview = new Review(title, review)
    this.reviews[title] = review
  }
}

class Review {
  constructor (title, review) {
    this.title = title;
    this.review = review;
  }
}

class Application {
  constructor() {
    this.user = undefined;
  }

  createAccount(name, age, email) {
    // statefulness
    this.user = new User(name, email);
  }

  getUserInfo() {
    return {name: this.user.name, email: this.user.email, reviews: this.user.reviews}
  }
}