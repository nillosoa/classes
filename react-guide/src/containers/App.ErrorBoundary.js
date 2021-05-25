
import React, { Component } from 'react';

import classes from './App.css';

import Person from './Person/Person';
import ErrorBoundary from './ErrorBoundary/ErrorBoundary';


class App extends Component {

  state = {
    persons: [
      { id: 'asd1', name: 'Max', age: 28 },
      { id: 'fgh1', name: 'Manu', age: 29 },
      { id: 'jkl1', name: 'Stephanie', age: 26 }
    ],
    showPersons: false
  }

  nameChangedHandler = (event, id) => {
    const personIndex = this.state.persons.findIndex(p => p.id === id);

    const person = {
      ...this.state.persons[personIndex]
    };

    person.name = event.target.value;

    const persons = [...this.state.persons];
    persons[personIndex] = person

    this.setState({ persons });
  }

  togglePersonsHandler = () => {
    const doesShow = this.state.showPersons;
    this.setState({ showPersons: !doesShow });
  }

  deletePersonHandler = (personIndex) => {
    throw new Error('Error boundary check');

    // const persons = this.state.persons.slice();
    const persons = [...this.state.persons];
    persons.splice(personIndex, 1);
    this.setState({ persons });
  }

  render() {

    let persons = null;
    let btnClass = '';

    if ( this.state.showPersons ) {
      btnClass = classes.Red;
      persons = this.state.persons.map((person, index) => {
        return (
          <ErrorBoundary
            key={person.id}>
            <Person
              age={person.age}
              name={person.name}
              click={() => this.deletePersonHandler(index)}
              changed={(event) => this.nameChangedHandler(event, person.id)} />
          </ErrorBoundary> )
      });
    }

    const assignedClasses = [];
    if ( this.state.persons.length <= 2 ) {
      assignedClasses.push(classes.red);
    }

    if ( this.state.persons.length <= 1 ) {
      assignedClasses.push(classes.bold)
    }

    return (
      <div className={classes.App}>
        <header className="App-header">
          <h1>Hi, I'm a React App</h1>
          <p className={assignedClasses.join(' ')}>This is really working!</p>
        </header>
        <div>
          <button
            className={btnClass}
            onClick={this.togglePersonsHandler}>Switch name</button>
          { persons }
        </div>
      </div>
    );
    // return (
    //   React.createElement('div', { className: 'App' },
    //     React.createElement('h1', null, 'Hi, I\'m a React App!!!')))
  }
}

export default App;
