import React, { useState } from "react";
import { TextField, Button, Box, Typography } from "@mui/material";
import api from "../api"; // Importando o cliente Axios

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleLogin = async () => {
    // Validação simples
    if (!email || !password) {
      setError("Por favor, preencha todos os campos.");
      return;
    }

    const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    if (!emailRegex.test(email)) {
      setError("Por favor, insira um email válido.");
      return;
    }

    try {
      const response = await api.post("/token", { username: email, password });
      localStorage.setItem("token", response.data.access_token); // Salva o token JWT
      window.location.href = "/dashboard"; // Redireciona após login
    } catch (err) {
      setError("Credenciais inválidas");
    }
  };

  return (
    <Box display="flex" flexDirection="column" alignItems="center" mt={5}>
      <Typography variant="h4" gutterBottom>
        Login
      </Typography>
      {error && <Typography color="error">{error}</Typography>}
      <TextField
        label="Email"
        variant="outlined"
        fullWidth
        margin="normal"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        error={!!error} // Destaca o campo com erro
        helperText={error && "Preencha um email válido."}
      />
      <TextField
        label="Senha"
        variant="outlined"
        type="password"
        fullWidth
        margin="normal"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        error={!!error} // Destaca o campo com erro
        helperText={error && "Por favor, insira sua senha."}
      />
      <Button variant="contained" color="primary" onClick={handleLogin}>
        Entrar
      </Button>
    </Box>
  );
}

export default Login;
