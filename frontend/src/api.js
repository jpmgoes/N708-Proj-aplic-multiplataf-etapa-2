import axios from "axios";

// URL base do back-end
// const BASE_URL = "http://localhost:8000"; // Alterar
const BASE_URL = "http://212.56.32.194:8000"; // Alterar

// Criação do cliente Axios
const api = axios.create({
  baseURL: BASE_URL,
});

// Interceptor para adicionar token JWT
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem("token"); // Recupera o token JWT
    if (token) {
      config.headers.Authorization = `Bearer ${token}`; // Adiciona o token ao cabeçalho
    }
    return config;
  },
  (error) => Promise.reject(error)
);

export default api;
