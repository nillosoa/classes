
import React, { Component } from 'react';

import classes from './App.css';
import Aux from '../hoc/Auxiliary';
import WithClass from '../hoc/WithClass';
import Cockpit from '../components/Cockpit/Cockpit';
import Persons from '../components/Persons/Persons';
import AuthContext from '../context/auth-context';

class App extends Component {

  state = {
    appTitle: 'Person Manager',
    persons: [
      { id: 'asd1', name: 'Max', age: 28 },
      { id: 'fgh1', name: 'Manu', age: 29 },
      { id: 'jkl1', name: 'Stephanie', age: 26 }
    ],
    showPersons: false,
    showCockpit: true,
    changeCounter: 0,
    authenticated: false
  }

  static getDerivedStateFromProps(props, state) {
    console.log('[App.js] getDerivedStateFromProps', props);
    return state;
  }

  // componentWillMount() {
  //   console.log('[App.js] componentWillMount');
  // }

  componentDidMount() {
    console.log('[App.js] componentDidMount');
  }

  shouldComponentUpdate(nextProps, nextState) {
    console.log('[App.js] shouldComponentUpdate');
    return true;
  }

  componentDidUpdate() {
    console.log('[App.js] componentDidUpdate');
  }

  nameChangedHandler = (event, id) => {
    const personIndex = this.state.persons.findIndex(p => p.id === id);

    const person = {
      ...this.state.persons[personIndex]
    };

    person.name = event.target.value;

    const persons = [...this.state.persons];
    persons[personIndex] = person

    this.setState((prevState, props) => {
      return {
        persons,
        changeCounter: prevState.changeCounter + 1 };
    });
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

  loginHandler = () => {
    this.setState({ authenticated: true });
  }

  render() {

    let persons = null;

    if ( this.state.showPersons ) {
      persons = <Persons
            persons={this.state.persons}
            clicked={this.deletePersonHandler}
            changed={this.nameChangedHandler}
            isAuthenticated={this.state.authenticated} />;
    }

    return (
      <Aux>
        <button onClick={() => { this.setState({ showCockpit: !this.state.showCockpit }) }}>Remove Cockpit</button>
        <AuthContext.Provider
          value={{
            authenticated: this.state.authenticated, login: this.loginHandler }}>
          { this.state.showCockpit
            ? <Cockpit
            appTitle={this.state.appTitle}
            clicked={this.togglePersonsHandler}
            personsLength={this.state.persons.length}
            showPersons={this.state.showPersons}
            login={this.loginHandler} />
            : null }
          { persons }
        </AuthContext.Provider>
      </Aux>
    );
    // return (
    //   React.createElement('div', { className: 'App' },
    //     React.createElement('h1', null, 'Hi, I\'m a React App!!!')))
  }
}

export default WithClass(App, classes.App);
