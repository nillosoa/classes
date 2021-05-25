
import React, { Component } from 'react';
import styled from 'styled-components';

import './App.css';
import Person from './Person/Person';


const StyledButton = styled.button`
  background-color: ${props => props.alt ? 'red' : 'green'};
  color: white;
  font: inherit;
  border: 1px solid blue;
  padding: 8px;
  cursor: pointer;

  &:hover {
    color: black;
    background-color: ${props => props.alt ? 'salmon' : 'lightgreen'};
  }
`;


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
    // const persons = this.state.persons.slice();
    const persons = [...this.state.persons];
    persons.splice(personIndex, 1);
    this.setState({ persons });
  }

  render() {

    // const style = {
    //   backgroundColor: 'green',
    //   color: 'white',
    //   font: 'inherit',
    //   border: '1px solid blue',
    //   padding: '8px',
    //   cursor: 'pointer',
    //   ':hover': {
    //     color: 'black',
    //     backgroundColor: 'lightgreen'
    //   }
    // };

    let persons = null;
    if ( this.state.showPersons ) {
      // style.backgroundColor = 'red';
      // style[':hover'] = {
      //   color: 'black', backgroundColor: 'salmon' };
      persons = this.state.persons.map((person, index) => {
        return <Person
          key={person.id}
          age={person.age}
          name={person.name}
          click={() => this.deletePersonHandler(index)}
          changed={(event) => this.nameChangedHandler(event, person.id)} /> });
    }

    const classes = [];
    if ( this.state.persons.length <= 2 ) {
      classes.push('red');
    }

    if ( this.state.persons.length <= 1 ) {
      classes.push('bold')
    }

    return (
      <div className="App">
        <header className="App-header">
          <h1>Hi, I'm a React App</h1>
          <p className={classes.join(' ')}>This is really working!</p>
        </header>
        <div>
          <StyledButton
            alt={this.state.showPersons}
            onClick={this.togglePersonsHandler}>Switch name</StyledButton>
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
