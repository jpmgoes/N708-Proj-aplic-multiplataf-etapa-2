import React, { useState, useEffect } from "react";
import { Box, Typography, TextField, Button, List, ListItem, ListItemText } from "@mui/material";
import api from "../api";

function Events() {
  const [events, setEvents] = useState([]);
  const [eventTitle, setEventTitle] = useState("");
  const [error, setError] = useState("");

  const fetchEvents = async () => {
    try {
      const response = await api.get("/events");
      setEvents(response.data);
    } catch (err) {
      setError("Erro ao carregar eventos.");
    }
  };

  const addEvent = async () => {
    if (!eventTitle) {
      setError("O título do evento não pode ser vazio.");
      return;
    }

    try {
      const response = await api.post("/events", { title: eventTitle });
      setEvents([...events, response.data]);
      setEventTitle("");
      setError(""); // Limpa o erro após o sucesso
    } catch (err) {
      setError("Erro ao adicionar evento.");
    }
  };

  useEffect(() => {
    fetchEvents();
  }, []);

  return (
    <Box mt={3} mx={2}>
      <Typography variant="h4" gutterBottom>
        Gerenciamento de Eventos
      </Typography>
      {error && <Typography color="error">{error}</Typography>}
      <TextField
        label="Título do Evento"
        variant="outlined"
        fullWidth
        margin="normal"
        value={eventTitle}
        onChange={(e) => setEventTitle(e.target.value)}
        error={!!error}
        helperText={error && "O título do evento é obrigatório."}
      />
      <Button variant="contained" color="primary" onClick={addEvent}>
        Adicionar Evento
      </Button>
      <List>
        {events.map((event, index) => (
          <ListItem key={index}>
            <ListItemText primary={event.title} />
          </ListItem>
        ))}
      </List>
    </Box>
  );
}

export default Events;
