import React, { useState, useEffect } from "react";
import { Box, Typography, List, ListItem, ListItemText, TextField, Button } from "@mui/material";
import api from "../api";

function Notifications() {
  const [notifications, setNotifications] = useState([]);
  const [message, setMessage] = useState("");

  const fetchNotifications = async () => {
    try {
      const response = await api.get("/notifications");
      setNotifications(response.data);
    } catch (err) {
      console.error("Erro ao buscar notificações", err);
    }
  };

  const sendNotification = async () => {
    try {
      const response = await api.post("/notifications", { message });
      setNotifications([...notifications, response.data]);
      setMessage("");
    } catch (err) {
      console.error("Erro ao enviar notificação", err);
    }
  };

  useEffect(() => {
    fetchNotifications();
  }, []);

  return (
    <Box mt={3} mx={2}>
      <Typography variant="h4" gutterBottom>
        Notificações
      </Typography>
      <TextField
        label="Nova Notificação"
        variant="outlined"
        fullWidth
        margin="normal"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />
      <Button variant="contained" color="primary" onClick={sendNotification}>
        Enviar
      </Button>
      <List>
        {notifications.map((notification, index) => (
          <ListItem key={index}>
            <ListItemText primary={notification.message} />
          </ListItem>
        ))}
      </List>
    </Box>
  );
}

export default Notifications;
