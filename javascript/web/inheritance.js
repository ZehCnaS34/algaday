var human = {
  species: "human",
  saySpecies: function () {
    console.log(this.species);
  },
  sayName: function () {
    console.log(this.name);
  }
};

var musician = Object.create(human);
musician.playInstrument = function () {
  console.log("Plays the " + this.instrument);
}

var alex = Object.create(musician);
alex.name = "Alex";
alex.instrument = "Sax";


function inherits(ctr, superCtr) {
  ctr.super_ = superCtr;
  ctr.prototype = Object.create(superCtr.prototype, {
    constructor: {
      value: superCtr,
      enumerable: false,
      writable: true,
      configurable: true
    }
  })
}

function Organism() {
  this.lifeTicks = 98123449;
}

Organism.prototype.kill = function () {
  this.lifeTicks = 0;
}

function Person(name) {
  Person.super_.call(this);
  this.name = name;
  this.sex = 'male';
}

inherits(Person, Organism);

Person.prototype.mate = function (person) {
  if (person.sex != this.sex) {
    let babyName = this.name.substr(0, this.name.length / 2) +
      person.name.substr(0, person.name.length / 2);
    return new Person(babyName);
  }
}