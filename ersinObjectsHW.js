dogs = {
  Fido: "retriever",
  Pongo: "dalmation",
  Lassie: "collie",
  Mutt: "mutt"
}

console.log(dogs)
const Mutt = "*mutt*"
dogs = {
  Fido: "retriever",
  Pongo: "dalmation",
  Lassie: "collie",
  Mutt
}
dogs.Fido = "*corgi*"
dogs['Pongo'] = "*labrador*"
console.log(dogs)

console.log("++++++++++++++++++++++++++")

celebrities = {
  actresses: ['Elizabeth Taylor', 'Marilyn Monroe', 'Nicole Kidman'],
  actors: ['Humphrey Bogart', 'Marlon Brando', 'Leonardo DiCaprio'],
  directors: ['Steven Spielberg', 'Martin Scorcese', 'Michael Bay'],
  audience: 'audience'
}

console.log(celebrities)
const audience = "*audience*"
celebrities = {
  actresses: ['Elizabeth Taylor', 'Marilyn Monroe', 'Nicole Kidman'],
  actors: ['Humphrey Bogart', 'Marlon Brando', 'Leonardo DiCaprio'],
  directors: ['Guillermo del Toro', 'Ava DuVernay', 'Patty Jenkins'],
  audience
}
celebrities.actresses = ['*','Lupita Nyonga', 'Constance Wu', 'Gina Rodriguez']
celebrities['actors'] = ['*', 'Donald Glover', 'Diego Luna', 'BD Wong']
console.log(celebrities)

console.log("++++++++++++++++++++++++++")

family = {
  mom: { Mimi: "Lan", Dominic: "Judy"},
  dad: { Mimi: "Thai", Dominic: "Mario" },
  sister: { Mimi: "Kim", Dominic: "Andrea" },
  brother: { Mimi: "Chris", Dominic: " " }
}

console.log(family)
const kitties = "kitties"
family = {
  mom: { Mimi: "Lan", Dominic: "Judy"},
  dad: { Mimi: "Thai", Dominic: "Mario" },
  sister: { Mimi: "Kim", Dominic: "Andrea" },
  brother: { Mimi: "Chris", Dominic: " " },
  kitties
}
family.dad.Mimi = "*Dan*"
family['brother']['Dominic'] = "*Jason*"

console.log(family)