// user takes photo
// user uploads photo
// app compares photo to database
// app returns a) info on plant b) plant not in db

class Photos {
  constructor(photo) {
    this.photo = photo;
    this.matches = false;
    this.database = new DatabaseConnection("plantCatalogue")
    this.photoTranslator = new PhotoTranslator()
  }

  comparePhoto(photo) {
    // this will give you name of plant from photo
    const plantName = this.photoTranslator.translate(photo)
    
    if (plantName === "not found") {
      return "Sorry, this plant couldn't be found. Try another photo."
    }  
    
    return this.database.findPlantByName(plantName)
  }
}

class DatabaseConnection {
  constructor(databaseName) {
    this.databaseName = databaseName;
  }

  findPlantByName(plantName) {
    //searches databaseName for plant with that name
    // returns the plantInfo
    // or returns not found
  }
}

class PhotoTranslator {
  translate(photo) {
    // "facial recognition" for plant
    // returns name of the found plant
    // or returns not found
  }
}