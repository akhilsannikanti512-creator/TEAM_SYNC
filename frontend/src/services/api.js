import axios from "axios";

const api = axios.create({
  baseURL: "https://teamsync-backend-rdr1.onrender.com",
});

export default api;