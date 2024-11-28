import React from "react";
import { AppBar, Toolbar, Typography, Button } from "@mui/material";
import { Link } from "react-router-dom";

function Navbar() {
  return (
    <AppBar position="static">
      <Toolbar>
        <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
          Sistema de Gestão
        </Typography>
        <Button color="inherit" component={Link} to="/">
          Login
        </Button>
        <Button color="inherit" component={Link} to="/dashboard">
          Dashboard
        </Button>
        <Button color="inherit" component={Link} to="/events">
          Eventos
        </Button>
        <Button color="inherit" component={Link} to="/resources">
          Recursos
        </Button>
      </Toolbar>
    </AppBar>
  );
}

export default Navbar;
