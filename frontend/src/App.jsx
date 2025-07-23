import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  return (
    <>
    <div>
     <h1>Hello, word!</h1>
     <p>Ou devo dizer: Olá, mundo do frontend com React + Vite!</p>
    </div>
    </>
  );
}

useEffect(() => {
  fetch("http://127.0.0.1:8000/")
    .then(res => res.json())
    .then(data => console.log(data));
}, []);

export default App
