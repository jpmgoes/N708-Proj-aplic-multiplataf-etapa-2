import React, { useState, useEffect } from "react";
import { Box, Typography, List, ListItem, ListItemText, TextField, Button } from "@mui/material";
import api from "../api";

function Users() {
  const [users, setUsers] = useState([]);
  const [user, setUser] = useState({ name: "", email: "" });

  const fetchUsers = async () => {
    try {
      const response = await api.get("/users");
      setUsers(response.data);
    } catch (err) {
      console.error("Erro ao buscar usuários", err);
    }
  };

  const addUser = async () => {
    try {
      const response = await api.post("/users", user);
      setUsers([...users, response.data]);
      setUser({ name: "", email: "" });
    } catch (err) {
      console.error("Erro ao adicionar usuário", err);
    }
  };

  useEffect(() => {
    fetchUsers();
  }, []);

  return (
    <Box mt={3} mx={2}>
      <Typography variant="h4" gutterBottom>
        Gerenciamento de Usuários
      </Typography>
      <TextField
        label="Nome"
        variant="outlined"
        fullWidth
        margin="normal"
        value={user.name}
        onChange={(e) => setUser({ ...user, name: e.target.value })}
      />
      <TextField
        label="Email"
        variant="outlined"
        fullWidth
        margin="normal"
        value={user.email}
        onChange={(e) => setUser({ ...user, email: e.target.value })}
      />
      <Button variant="contained" color="primary" onClick={addUser}>
        Adicionar Usuário
      </Button>
      <List>
        {users.map((user, index) => (
          <ListItem key={index}>
            <ListItemText primary={`${user.name} - ${user.email}`} />
          </ListItem>
        ))}
      </List>
    </Box>
  );
}

export default Users;
