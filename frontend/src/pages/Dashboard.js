import React, { useState, useEffect } from "react";
import { Box, Typography, Card, CardContent, Grid } from "@mui/material";
import api from "../api";

function Dashboard() {
  const [stats, setStats] = useState({
    totalEvents: 0,
    availableResources: 0,
  });

  const fetchStats = async () => {
    try {
      const [eventsResponse, resourcesResponse] = await Promise.all([
        api.get("/events"),
        api.get("/resources"),
      ]);

      setStats({
        totalEvents: eventsResponse.data.length,
        availableResources: resourcesResponse.data.filter((r) => r.availability).length,
      });
    } catch (err) {
      console.error("Erro ao buscar estatísticas", err);
    }
  };

  useEffect(() => {
    fetchStats();
  }, []);

  return (
    <Box mt={3} mx={2}>
      <Typography variant="h4" gutterBottom>
        Painel de Controle
      </Typography>
      <Grid container spacing={3}>
        <Grid item xs={12} sm={6} md={4}>
          <Card>
            <CardContent>
              <Typography variant="h6">Total de Eventos</Typography>
              <Typography>{stats.totalEvents}</Typography>
            </CardContent>
          </Card>
        </Grid>
        <Grid item xs={12} sm={6} md={4}>
          <Card>
            <CardContent>
              <Typography variant="h6">Recursos Disponíveis</Typography>
              <Typography>{stats.availableResources}</Typography>
            </CardContent>
          </Card>
        </Grid>
      </Grid>
    </Box>
  );
}

export default Dashboard;
