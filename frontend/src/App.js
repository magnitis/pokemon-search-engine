import React, { useState } from 'react';
import logo from './poke_ball.svg';
import './App.css';


function App() {
  
  const [PostData, setPostData] = useState({name: "", description:""});

  // GET functionality
  let search = (e) => {
    e.preventDefault();
    let keyword = e.target.elements.keyword.value;
    fetch('/pokemon/' + keyword, {
      method: 'GET',
      headers: { 'Content-Type': 'application/json' }
    })
      .then((response) => response.json())
     .then(data => { setPostData(data); })
      .then((data) => console.log(data));
  }
  
  // Static webpage setup
  return (
    
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />

      
      <fieldset className="App-fieldset">
        <legend>Pokemon Search Engine</legend>
        <form method="get"  onSubmit={search} >
          <input type="text" name="keyword" placeholder="Input Pokemon name" />
          <input type="submit" value="Search" /> 
        </form>
      </fieldset>

      <h3> Name: {PostData.name} </h3>
      <h3> Shakespearean description:</h3>
      <p>  {PostData.description} </p>
      </header>


    </div>
      
  );
}

export default App;