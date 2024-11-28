import React from "react";
import ReactDOM from "react-dom";
import "./index.css"; // Você pode usar este arquivo para estilizações globais
import App from "./App";

// Renderiza o componente principal `App` dentro do elemento com id `root`
ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById("root")
);
