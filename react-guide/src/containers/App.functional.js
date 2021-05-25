
import React, { useState } from 'react';
import './App.css';
import Person from './Person/Person';

const app = props => {

  const [ personsState, setPersonsState ] = useState({
    persons: [
      { name: 'Max', age: 28 },
      { name: 'Manu', age: 29 },
      { name: 'Stephanie', age: 26 } ],
    otherState: 'Some other value' });

   const [ otherState, setOtherState ] = useState('Some other value');

  console.log(personsState, otherState);

  const switchNameHandler = () => {
    setPersonsState({
      persons: [
        { name: 'Maximilian', age: 28 },
        { name: 'Manu', age: 29 },
        { name: 'Stephanie', age: 27 }  ] });
  }

  return (
    <div className="App">
      <header className="App-header">
        <h1>Hi, I'm a React App</h1>
        <p>This is really working!</p>
      </header>
      <div>
        <button onClick={switchNameHandler}>Switch name</button>
        <Person name={state.persons[0].name} age={state.persons[0].age} />
        <Person name={state.persons[1].name} age={state.persons[1].age}>My Hobbies: Racing</Person>
        <Person name={state.persons[2].name} age={state.persons[2].age} />
      </div>
    </div>
  );
}

export default app;