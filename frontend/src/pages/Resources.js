import React, { useState, useEffect } from "react";
import { Box, Typography, List, ListItem, ListItemText, Button, TextField } from "@mui/material";
import api from "../api";

function Resources() {
  const [resources, setResources] = useState([]);
  const [resourceName, setResourceName] = useState("");
  const [error, setError] = useState("");

  const fetchResources = async () => {
    try {
      const response = await api.get("/resources");
      setResources(response.data);
    } catch (err) {
      setError("Erro ao carregar recursos.");
    }
  };

  const addResource = async () => {
    if (!resourceName) {
      setError("O nome do recurso não pode ser vazio.");
      return;
    }

    try {
      const response = await api.post("/resources", { name: resourceName });
      setResources([...resources, response.data]);
      setResourceName("");
      setError(""); // Limpa o erro após o sucesso
    } catch (err) {
      setError("Erro ao adicionar recurso.");
    }
  };

  useEffect(() => {
    fetchResources();
  }, []);

  return (
    <Box mt={3} mx={2}>
      <Typography variant="h4" gutterBottom>
        Recursos
      </Typography>
      {error && <Typography color="error">{error}</Typography>}
      <TextField
        label="Nome do Recurso"
        variant="outlined"
        fullWidth
        margin="normal"
        value={resourceName}
        onChange={(e) => setResourceName(e.target.value)}
        error={!!error}
        helperText={error && "O nome do recurso é obrigatório."}
      />
      <Button variant="contained" color="primary" onClick={addResource}>
        Adicionar Recurso
      </Button>
      <List>
        {resources.map((resource, index) => (
          <ListItem key={index}>
            <ListItemText primary={resource.name} />
          </ListItem>
        ))}
      </List>
    </Box>
  );
}

export default Resources;
